# -*- coding: utf-8 -*-
"""Controleert de gebouwde site op interne links, aanspreekvormen, kostenwoorden,
dubbele titels en ankerteksten."""
import os, re, sys, html

DIST = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
fouten = []

VERBODEN_AANSPREEK = r"\b(je|jij|jouw|jullie|uw|wij|we|ons|onze)\b"
KOSTEN = r"\b(euro|prijs|prijzen|tarief|tarieven|kosten|kostte|gratis|betaald|betalen|goedkoop|korting|aanbieding|sale)\b"
TOEGESTAAN_EXTERN = ("https://www.hedgehoganddeer.nl", "https://www.youtube-nocookie.com", "https://topkidsfashion.nl")

paginas = {}
for wortel, mappen, bestanden in os.walk(DIST):
    for b in bestanden:
        if b.endswith(".html"):
            p = os.path.join(wortel, b)
            paginas[p] = open(p, encoding="utf-8").read()

print("%d html-bestanden" % len(paginas))

titels, metas = {}, {}
for p, t in paginas.items():
    rel = p.replace(DIST, "") or "/"
    tekst = re.sub(r"<script.*?</script>", " ", t, flags=re.S)
    tekst = re.sub(r"<[^>]+>", " ", tekst)
    tekst = html.unescape(tekst)

    for m in re.finditer(VERBODEN_AANSPREEK, tekst, re.I):
        fouten.append("%s: aanspreekvorm '%s'" % (rel, m.group(0)))
    for m in re.finditer(KOSTEN, tekst, re.I):
        fouten.append("%s: kostenwoord '%s'" % (rel, m.group(0)))
    if "—" in tekst or "–" in tekst:
        fouten.append("%s: gedachtestreepje" % rel)
    for woord in ("lorem", "TODO", "XXX", "placeholder", "voorbeeldtekst"):
        if woord.lower() in tekst.lower():
            fouten.append("%s: opvulling '%s'" % (rel, woord))

    ti = re.search(r"<title>(.*?)</title>", t, re.S)
    me = re.search(r'<meta name="description" content="(.*?)"', t, re.S)
    if ti:
        titels.setdefault(ti.group(1), []).append(rel)
        if len(ti.group(1)) > 70:
            fouten.append("%s: titel te lang (%d)" % (rel, len(ti.group(1))))
    else:
        fouten.append("%s: geen title" % rel)
    if me:
        metas.setdefault(me.group(1), []).append(rel)
        if not (60 <= len(me.group(1)) <= 175):
            fouten.append("%s: metalengte %d" % (rel, len(me.group(1))))
    else:
        fouten.append("%s: geen meta description" % rel)

    for href in re.findall(r'href="([^"]+)"', t):
        if href.startswith("/"):
            doel = os.path.join(DIST, href.strip("/"), "index.html")
            if href in ("/stijl.css", "/site.js", "/favicon.svg"):
                doel = os.path.join(DIST, href.strip("/"))
            if not os.path.exists(doel):
                fouten.append("%s: dode interne link %s" % (rel, href))
        elif href.startswith("http"):
            if not href.startswith(TOEGESTAAN_EXTERN):
                fouten.append("%s: onbekende externe host %s" % (rel, href))
        elif href.startswith("mailto:"):
            if href != "mailto:info@topkidsfashion.nl":
                fouten.append("%s: onbekend mailadres %s" % (rel, href))

    for anker in re.findall(r'<a href="https://www\.hedgehoganddeer\.nl[^"]*"[^>]*>(.*?)</a>', t, re.S):
        a = html.unescape(re.sub(r"<[^>]+>", "", anker)).strip()
        if not (a.startswith("http") or len(a.split()) <= 4):
            fouten.append("%s: verdachte ankertekst '%s'" % (rel, a))

for t, ps in titels.items():
    if len(ps) > 1:
        fouten.append("dubbele titel %r op %s" % (t, ps))
for m, ps in metas.items():
    if len(ps) > 1:
        fouten.append("dubbele meta op %s" % ps)

# sitemap
sm = open(os.path.join(DIST, "sitemap.xml"), encoding="utf-8").read()
locs = re.findall(r"<loc>(.*?)</loc>", sm)
for l in locs:
    pad = l.replace("https://topkidsfashion.nl", "")
    if not os.path.exists(os.path.join(DIST, pad.strip("/"), "index.html")):
        fouten.append("sitemap verwijst naar ontbrekende pagina %s" % l)
print("%d url's in de sitemap" % len(locs))

if fouten:
    print("\n%d bevindingen:" % len(fouten))
    for f in fouten[:80]:
        print(" -", f)
    sys.exit(1)
print("geen bevindingen")
