from pathlib import Path

p = Path('.github/scripts/r031_persist.py')
src = p.read_text(encoding='utf-8')
old = """# Federal Register HTML identity.\nstatus_fr, mime_fr, final_fr, fr_html = fetch(US005_FR_HTML)\nassert status_fr == 200\nfr_visible = ' '.join(re.sub(r'<[^>]+>', ' ', fr_html.decode('utf-8', 'replace')).split())\nassert 'Ensuring a National Policy Framework for Artificial Intelligence' in fr_visible\nassert '2025-23092' in fr_html.decode('utf-8', 'replace') or '2025-23092' in final_fr\n"""
new = """# Federal Register structured identity. Use the official JSON document record\n# because the public HTML page may render title content client-side.\nFR_JSON = 'https://www.federalregister.gov/api/v1/documents/2025-23092.json'\nstatus_fr, mime_fr, final_fr, fr_json = fetch(FR_JSON)\nassert status_fr == 200\nfr_data = json.loads(fr_json.decode('utf-8'))\nassert fr_data.get('document_number') == '2025-23092'\nassert fr_data.get('title') == 'Ensuring a National Policy Framework for Artificial Intelligence'\nassert fr_data.get('publication_date') == '2025-12-16'\nassert fr_data.get('pdf_url') == US005_PDF\n"""
assert old in src, 'expected R031 Federal Register assertion block not found'
src = src.replace(old, new, 1)
exec(compile(src, 'r031_persist_runtime_v3.py', 'exec'), {'__name__': '__main__'})
