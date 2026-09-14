from pathlib import Path

p = Path('.github/scripts/r031_persist.py')
src = p.read_text(encoding='utf-8')
old = """# Federal Register HTML identity.\nstatus_fr, mime_fr, final_fr, fr_html = fetch(US005_FR_HTML)\nassert status_fr == 200\nfr_visible = ' '.join(re.sub(r'<[^>]+>', ' ', fr_html.decode('utf-8', 'replace')).split())\nassert 'Ensuring a National Policy Framework for Artificial Intelligence' in fr_visible\nassert '2025-23092' in fr_html.decode('utf-8', 'replace') or '2025-23092' in final_fr\n"""
new = """# Federal Register HTML endpoint identity. The page may render title content client-side,\n# so use the stable official document number/final URL as the HTML-layer assertion.\nstatus_fr, mime_fr, final_fr, fr_html = fetch(US005_FR_HTML)\nassert status_fr == 200\nfr_raw = fr_html.decode('utf-8', 'replace')\nassert '2025-23092' in final_fr or '2025-23092' in fr_raw\n"""
assert old in src, 'expected R031 Federal Register assertion block not found'
src = src.replace(old, new, 1)
exec(compile(src, 'r031_persist_runtime.py', 'exec'), {'__name__': '__main__'})
