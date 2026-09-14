from pathlib import Path
import csv, hashlib, re, subprocess, tempfile, os

OUT = Path('76_COMPETITION/source_acquisition/AI-LAWS-R016_SOURCE_ACQUISITION_RESULTS_2026-09-14.csv')
OUT.parent.mkdir(parents=True, exist_ok=True)

FIELDS = ['source_key','jurisdiction','authority_class','title','official_url','http_status','content_type','byte_size','sha256','pages','verification_state','repository_snapshot','notes']
rows = []

def fetch(url):
    with tempfile.NamedTemporaryFile(delete=False) as h, tempfile.NamedTemporaryFile(delete=False) as b:
        hp, bp = h.name, b.name
    try:
        cmd = ['curl','-L','--connect-timeout','20','--max-time','180','-sS','-A','Mozilla/5.0 AI-LAWS-source-verification','-D',hp,'-o',bp,'-w','%{http_code}',url]
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        status = (p.stdout or '').strip()[-3:] if p.stdout else '000'
        body = Path(bp).read_bytes() if Path(bp).exists() else b''
        headers = Path(hp).read_text(encoding='utf-8', errors='ignore') if Path(hp).exists() else ''
        cts = re.findall(r'(?im)^content-type:\s*([^\r\n]+)', headers)
        ctype = cts[-1].strip() if cts else ''
        return status, ctype, body, p.stderr.strip()
    finally:
        for x in (hp,bp):
            try: os.unlink(x)
            except FileNotFoundError: pass

def extract(body):
    sha = hashlib.sha256(body).hexdigest()
    size = len(body)
    pages = ''
    is_pdf = body.startswith(b'%PDF-')
    if is_pdf:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as f:
            f.write(body); pp = f.name
        tp = pp + '.txt'
        try:
            q = subprocess.run(['pdfinfo',pp], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            m = re.search(r'(?m)^Pages:\s*(\d+)', q.stdout or '')
            pages = m.group(1) if m else ''
            subprocess.run(['pdftotext','-layout',pp,tp], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            text = Path(tp).read_text(encoding='utf-8', errors='ignore') if Path(tp).exists() else ''
        finally:
            for x in (pp,tp):
                try: os.unlink(x)
                except FileNotFoundError: pass
    else:
        text = body.decode('utf-8', errors='ignore')
        text = re.sub(r'<script[\s\S]*?</script>|<style[\s\S]*?</style>', ' ', text, flags=re.I)
        text = re.sub(r'<[^>]+>', ' ', text)
        text = re.sub(r'\s+', ' ', text)
    return sha,size,pages,is_pdf,text

def add(key,jur,aclass,title,url,markers,expected='ANY',notes=''):
    status,ctype,body,err = fetch(url)
    sha,size,pages,is_pdf,text = extract(body)
    low = text.lower()
    matched = all(m.lower() in low for m in markers)
    if status != '200':
        state = f'ACCESS_HTTP_{status}'
    elif expected == 'PDF' and not is_pdf:
        state = 'HTTP_200_BODY_NOT_PDF'
    elif expected == 'HTML' and is_pdf:
        state = 'HTTP_200_UNEXPECTED_PDF'
    elif matched:
        state = 'OFFICIAL_SOURCE_BODY_AND_MARKERS_VERIFIED'
    else:
        state = 'HTTP_200_BODY_MARKERS_NOT_VERIFIED'
    if err:
        notes = (notes + '; curl=' + err[:240]).strip('; ')
    rows.append({
        'source_key':key,'jurisdiction':jur,'authority_class':aclass,'title':title,'official_url':url,
        'http_status':status,'content_type':ctype,'byte_size':size,'sha256':sha,'pages':pages,
        'verification_state':state,'repository_snapshot':'NOT_VENDORED__URL_MANIFEST_PRIMARY','notes':notes
    })
    print(key,status,ctype,size,pages,state)

# European Union: binding primary law + Commission guidance/staff analysis.
add('EU-COMP-001','EU','TREATY_PRIMARY','TFEU Article 101','https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:12016E101',['Article 101','incompatible with the internal market'],'PDF','Binding treaty competition rule; agreement/concerted-practice analysis remains fact-specific.')
add('EU-COMP-002','EU','TREATY_PRIMARY','TFEU Article 102','https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:12016E102',['Article 102','abuse by one or more undertakings'],'PDF','Binding treaty abuse-of-dominance rule; dominance and abuse require market/fact analysis.')
add('EU-COMP-003','EU','STATUTE_OR_REGULATION','Council Regulation (EC) No 139/2004 — EU Merger Regulation','https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32004R0139',['control of concentrations between undertakings','significantly impede effective competition'],'PDF','Binding EU merger-control framework; notification/control thresholds and jurisdiction are transaction-specific.')
add('EU-COMP-004','EU','STATUTE_OR_REGULATION','Regulation (EU) 2022/1925 — Digital Markets Act','https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32022R1925',['contestable and fair markets','gatekeeper'],'PDF','Binding only within DMA scope; not a universal AI competition rule.')
add('EU-COMP-005','EU','OFFICIAL_GUIDANCE','2023 Horizontal Cooperation Guidelines','https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=PI_COM:C(2023)4752',['horizontal co-operation agreements','standardisation agreements'],'PDF','Commission guidance for Article 101 self-assessment; standardisation/information-sharing analysis is contextual and non-statutory.')
add('EU-COMP-006','EU','OFFICIAL_STAFF_ANALYSIS','Competition Policy Brief — Competition in Generative AI and Virtual Worlds','https://competition-policy.ec.europa.eu/document/download/c86d461f-062e-4dde-a662-15228d6ca385_en',['Competition in Generative AI and Virtual Worlds','generative artificial intelligence'],'PDF','Commission staff policy analysis; market-structure concerns are not violation findings.')

# Cross-authority AI competition statement.
add('INT-COMP-001','EU/GB/US','OFFICIAL_JOINT_STATEMENT','Joint Statement on Competition in Generative AI Foundation Models and AI Products','https://www.justice.gov/atr/media/1361306/dl?inline=',['Joint Statement on Competition in Generative AI Foundation Models and AI Products','Sovereign decision-making'],'PDF','Nonbinding joint enforcement-policy statement; each authority retains sovereign decision-making.')

# United States: current statutory text.
add('US-COMP-001','US','STATUTE_OR_REGULATION','15 U.S.C. § 1 — Sherman Act restraint of trade','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title15-section1',['Trusts, etc., in restraint of trade illegal','Every contract, combination'],'HTML','Current Office of Law Revision Counsel preliminary text; agreement requirement must not be inferred from parallel public statements alone.')
add('US-COMP-002','US','STATUTE_OR_REGULATION','15 U.S.C. § 2 — Sherman Act monopolization','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title15-section2',['Monopolizing trade a felony','monopolize, or attempt to monopolize'],'HTML','Current Office of Law Revision Counsel preliminary text; market power and exclusionary conduct are fact-specific.')
add('US-COMP-003','US','STATUTE_OR_REGULATION','15 U.S.C. § 18 — Clayton Act Section 7','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title15-section18',['Acquisition by one corporation of stock of another','substantially to lessen competition'],'HTML','Current Office of Law Revision Counsel preliminary text; acquisition coverage and competitive effect are transaction-specific.')
add('US-COMP-004','US','STATUTE_OR_REGULATION','15 U.S.C. § 45 — FTC Act Section 5','https://uscode.house.gov/view.xhtml?edition=prelim&req=granuleid%3AUSC-prelim-title15-section45',['Unfair methods of competition unlawful','Unfair methods of competition in or affecting commerce'],'HTML','Current Office of Law Revision Counsel preliminary text; does not convert every AI market concern into a violation.')

# U.S. current guidance, studies and collaboration-status records.
add('US-COMP-005','US','OFFICIAL_GUIDANCE','DOJ/FTC 2023 Merger Guidelines','https://www.ftc.gov/system/files/ftc_gov/pdf/P234000-NEW-MERGER-GUIDELINES.pdf',['Merger Guidelines','Guideline 3'],'PDF','Nonbinding enforcement guidance; current DOJ page in 2026 continues to list 2023 Merger Guidelines.')
add('US-COMP-006','US','OFFICIAL_GUIDANCE','DOJ/FTC Antitrust Policy Statement on Sharing of Cybersecurity Information','https://www.ftc.gov/system/files/documents/public_statements/297681/140410ftcdojcyberthreatstmt.pdf',['cybersecurity information','antitrust'],'PDF','Current DOJ guidance list still includes this 2014 statement; cybersecurity analogy only, not an AI-safety safe harbor.')
add('US-COMP-007','US','OFFICIAL_STAFF_REPORT','FTC Staff Report on AI Partnerships & Investments 6(b) Study','https://www.ftc.gov/system/files/ftc_gov/pdf/p246201_aipartnerships6breport_redacted_0.pdf',['AI Partnerships','Areas to Watch'],'PDF','Staff study based on three partnerships; identifies areas to watch, not adjudicated violations.')
add('US-COMP-008','US','OFFICIAL_POLICY_STATUS','FTC/DOJ Withdrawal of Collaboration Guidelines','https://www.justice.gov/atr/media/1380001/dl?inline=',['Antitrust Guidelines','withdrawal'],'PDF','Records December 2024 withdrawal; withdrawn guidelines must not be treated as current safe harbor.')
add('US-COMP-009','US','OFFICIAL_POLICY_STATUS','DOJ/FTC 2026 public inquiry on business-collaboration guidance','https://www.justice.gov/opa/pr/justice-department-and-federal-trade-commission-seek-public-comment-guidance-business',['Seek Public Comment for Guidance on Business Collaborations','2000 Antitrust Guidelines for Collaborations Among Competitors'],'HTML','Public inquiry, not final replacement guidance. Comment period was later extended to May 21, 2026.')
add('US-COMP-010','US','OFFICIAL_POLICY_STATUS','DOJ/FTC extension of collaboration-guidance comment period','https://www.justice.gov/opa/pr/doj-and-ftc-extend-deadline-public-comment-guidance-business-collaborations',['extend','May 21, 2026'],'HTML','Confirms inquiry status and extended deadline; no final replacement guidance is inferred by R016.')

with OUT.open('w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n')
    w.writeheader(); w.writerows(rows)

print('R016_SOURCE_RECORDS=', len(rows))
print('R016_VERIFIED_MARKER_RECORDS=', sum(r['verification_state']=='OFFICIAL_SOURCE_BODY_AND_MARKERS_VERIFIED' for r in rows))
print('ZIP_OR_ARTIFACT_CREATED=NO')
print('NOTEBOOK_UPLOADS=0')
print('AUTO_ADVANCE=NO')
