# -*- coding: utf-8 -*-
"""Kern van de generator voor topkidsfashion.nl: paginaschil, navigatie, opmaak."""

import os, re, html

SITE = "topkidsfashion.nl"
BASE = "https://topkidsfashion.nl"
TITEL = "Top Kids Fashion"
MAIL = "info@topkidsfashion.nl"

SHOP = "https://www.hedgehoganddeer.nl"
SHOPNAAM = "Hedgehog &amp; Deer"

NAV = [
    ("/merken/", "Merken"),
    ("/stijl/", "Stijl"),
    ("/maten/", "Maten"),
    ("/materialen/", "Materialen"),
    ("/seizoen/", "Seizoen"),
    ("/video/", "Video"),
]

PAGINAS = []   # (pad, titel, meta, html, prioriteit)


def voegtoe(pad, titel, meta, inhoud, prio="0.6"):
    PAGINAS.append((pad, titel, meta, inhoud, prio))


def esc(t):
    return html.escape(t, quote=False)


def shoplink(url, tekst=None):
    """Uitgaande link. Ankertekst is de merknaam of de volledige URL."""
    t = tekst if tekst else url
    return '<a href="%s" rel="noopener">%s</a>' % (url, t)


CSS = r"""
:root{
  --papier:#fbf7f2; --papier2:#f4ece2; --inkt:#241f1b; --grijs:#6d635a;
  --klei:#c2573f; --salie:#6f8b6a; --zon:#e3a63c; --lijn:#e6dbcd; --wit:#fffdfa;
  --radius:18px;
}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--papier);color:var(--inkt);
  font-family:ui-sans-serif,system-ui,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  font-size:17px;line-height:1.65}
h1,h2,h3,h4,.display{font-family:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  font-weight:600;line-height:1.15;letter-spacing:-.01em}
h1{font-size:clamp(2rem,1.3rem + 2.6vw,3.1rem);margin:.2em 0 .35em}
h2{font-size:clamp(1.45rem,1.1rem + 1.3vw,2.05rem);margin:2.2rem 0 .7rem;position:relative;padding-left:0}
h2:before{content:"";display:inline-block;width:10px;height:10px;border-radius:50%;background:var(--zon);margin-right:11px;vertical-align:middle}
h3{font-size:1.2rem;margin:1.6rem 0 .5rem}
p{margin:0 0 1.05em}
a{color:var(--klei);text-underline-offset:3px;text-decoration-thickness:1px}
a:hover{color:#9c422e}
img,svg{max-width:100%}
.wrap{max-width:1120px;margin:0 auto;padding:0 22px}
.smal{max-width:760px}

/* kop */
.balk{background:var(--wit);border-bottom:1px solid var(--lijn);position:sticky;top:0;z-index:20}
.balk .wrap{display:flex;align-items:center;gap:22px;min-height:70px;flex-wrap:wrap}
.merk{display:flex;align-items:center;gap:11px;text-decoration:none;color:var(--inkt);font-weight:600}
.merk .naam{font-family:"Iowan Old Style",Palatino,Georgia,serif;font-size:1.22rem;letter-spacing:-.01em}
.merk .naam b{color:var(--klei);font-weight:600}
.menu{display:flex;gap:20px;margin-left:auto;flex-wrap:wrap}
.menu a{color:var(--inkt);text-decoration:none;font-size:.95rem;padding:6px 0;border-bottom:2px solid transparent}
.menu a:hover,.menu a[aria-current]{border-color:var(--klei);color:var(--klei)}

/* kruimels */
.kruimel{font-size:.85rem;color:var(--grijs);padding:16px 0 0}
.kruimel a{color:var(--grijs)}

/* hero */
.hero{padding:34px 0 8px}
.hero .in{background:linear-gradient(180deg,var(--papier2),rgba(244,236,226,0));border-radius:26px;padding:30px 30px 34px}
.hero svg{border-radius:16px}
.hero .in{display:grid;grid-template-columns:1.15fr .85fr;gap:40px;align-items:center}
.hero p.lead{font-size:1.14rem;color:#4a4139;max-width:52ch}
@media(max-width:820px){.hero .in{grid-template-columns:1fr;gap:18px}}

.lint{display:flex;gap:8px;flex-wrap:wrap;margin:18px 0 0;padding:0;list-style:none}
.lint li a{display:inline-block;background:var(--wit);border:1px solid var(--lijn);border-radius:999px;
  padding:7px 14px;font-size:.9rem;text-decoration:none;color:var(--inkt)}
.lint li a:hover{border-color:var(--klei);color:var(--klei)}

/* rooster */
.rooster{display:grid;gap:18px;margin:22px 0}
.k2{grid-template-columns:repeat(2,1fr)}
.k3{grid-template-columns:repeat(3,1fr)}
.k4{grid-template-columns:repeat(4,1fr)}
@media(max-width:900px){.k3,.k4{grid-template-columns:repeat(2,1fr)}}
@media(max-width:600px){.k2,.k3,.k4{grid-template-columns:1fr}}

.kaart{background:var(--wit);border:1px solid var(--lijn);border-radius:var(--radius);padding:20px 20px 18px;
  display:flex;flex-direction:column;gap:6px}
.kaart h3{margin:.1rem 0 .2rem;font-size:1.08rem}
.kaart p{font-size:.95rem;color:#544a41;margin:0 0 .6em}
.kaart a.meer{margin-top:auto;font-size:.92rem;text-decoration:none;font-weight:600}
.kaart a.meer:after{content:" \2192"}
.kaart .plaat{margin:-4px 0 8px}
.kaart .plaat svg{display:block;width:100%;max-height:170px;height:auto}
.embleem{border-radius:12px;padding:10px}
.embleem svg{display:block;width:100%;height:auto;max-height:150px}
.embleem.rond{border-radius:50%;padding:14px}

/* rij-opsomming */
.rijen{list-style:none;margin:18px 0;padding:0;border-top:1px solid var(--lijn)}
.rijen li{border-bottom:1px solid var(--lijn);padding:14px 4px;display:grid;
  grid-template-columns:34px 1fr;gap:14px;align-items:baseline}
.rijen li .nr{color:var(--klei);font-family:"Iowan Old Style",Georgia,serif;font-size:1.05rem}
.rijen li b{display:block;font-weight:600}
.rijen li span.uitleg{color:#544a41;font-size:.95rem}

/* blokken */
.vlak{background:var(--papier2);border-radius:var(--radius);padding:22px 24px;margin:26px 0}
.vlak h2,.vlak h3{margin-top:0}
.lijn{border:0;border-top:1px solid var(--lijn);margin:34px 0}
.klein{font-size:.88rem;color:var(--grijs)}
.tag{display:inline-block;background:var(--papier2);border-radius:999px;padding:3px 11px;font-size:.8rem;color:#5c5147}

table{border-collapse:collapse;width:100%;margin:18px 0;font-size:.95rem;background:var(--wit)}
th,td{border:1px solid var(--lijn);padding:9px 12px;text-align:left}
th{background:var(--papier2);font-weight:600}
.tabelwrap{overflow-x:auto}

/* video */
.video{background:var(--wit);border:1px solid var(--lijn);border-radius:var(--radius);overflow:hidden}
.video .doek{position:relative;aspect-ratio:16/9;background:#241f1b;display:flex;align-items:center;
  justify-content:center;cursor:pointer;border:0;width:100%;padding:0}
.video .doek img{width:100%;height:100%;object-fit:cover;opacity:.72}
.video .doek .knop{position:absolute;width:64px;height:64px;border-radius:50%;background:rgba(255,253,250,.92);
  display:flex;align-items:center;justify-content:center}
.video .doek .knop:after{content:"";border-left:19px solid var(--klei);border-top:12px solid transparent;
  border-bottom:12px solid transparent;margin-left:5px}
.video .bij{padding:12px 16px 14px}
.video .bij b{display:block;font-size:.98rem}
.video .bij span{font-size:.85rem;color:var(--grijs)}
.video iframe{width:100%;aspect-ratio:16/9;border:0;display:block}

/* voet */
.voet{background:var(--wit);border-top:1px solid var(--lijn);margin-top:56px;padding:34px 0 42px}
.voet .kolommen{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:28px}
@media(max-width:760px){.voet .kolommen{grid-template-columns:1fr}}
.voet h4{margin:0 0 .5rem;font-size:1rem}
.voet ul{list-style:none;margin:0;padding:0}
.voet li{margin:0 0 6px}
.voet a{color:var(--inkt);text-decoration:none;font-size:.93rem}
.voet a:hover{color:var(--klei)}
.voet .slot{margin-top:26px;padding-top:16px;border-top:1px solid var(--lijn);font-size:.85rem;color:var(--grijs)}

.inhoud ul,.inhoud ol{margin:0 0 1.1em;padding-left:1.25em}
.inhoud li{margin:0 0 .45em}
.tekening{margin:26px 0;background:var(--papier2);border-radius:var(--radius);padding:20px;text-align:center}
.tekening svg{display:block;width:100%;max-width:520px;height:auto;margin:0 auto}
.tekening figcaption{text-align:left}
.tekening figcaption{font-size:.85rem;color:var(--grijs);margin-top:10px}
.merkkop{display:grid;grid-template-columns:120px 1fr;gap:22px;align-items:center;margin:6px 0 10px}
@media(max-width:600px){.merkkop{grid-template-columns:80px 1fr;gap:14px}}

"""

JS = r"""
document.addEventListener('click',function(e){
  var b=e.target.closest('.doek'); if(!b) return;
  var id=b.getAttribute('data-id'); if(!id) return;
  var f=document.createElement('iframe');
  f.src='https://www.youtube-nocookie.com/embed/'+id+'?autoplay=1&rel=0';
  f.setAttribute('title', b.getAttribute('data-titel')||'video');
  f.setAttribute('allow','accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture');
  f.setAttribute('allowfullscreen','');
  b.parentNode.replaceChild(f,b);
});
"""


def kruimel(paden):
    """paden: lijst van (url, naam); laatste zonder link."""
    stukken = ['<a href="/">Home</a>']
    for i, (u, n) in enumerate(paden):
        if i == len(paden) - 1:
            stukken.append(esc(n))
        else:
            stukken.append('<a href="%s">%s</a>' % (u, esc(n)))
    return '<div class="kruimel wrap">%s</div>' % ' &rsaquo; '.join(stukken)


LOGO = ('<svg viewBox="0 0 44 44" width="34" height="34" aria-hidden="true">'
        '<circle cx="22" cy="22" r="21" fill="#f4ece2"/>'
        '<path d="M22 11v6" stroke="#c2573f" stroke-width="2" stroke-linecap="round"/>'
        '<path d="M22 17c-3 0-5 2-5 4l5 3 5-3c0-2-2-4-5-4z" fill="#6f8b6a"/>'
        '<path d="M8 26h28l-14 8-14-8z" fill="#c2573f" opacity=".9"/>'
        '<circle cx="22" cy="9.5" r="2.4" fill="#e3a63c"/></svg>')


def pagina(pad, titel, meta, inhoud, prio="0.6", kruimelpad=None, breed=False):
    canon = BASE + pad
    menu = "".join(
        '<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if pad.startswith(u) and u != "/" else "", esc(n))
        for u, n in NAV)
    kr = kruimel(kruimelpad) if kruimelpad else ""
    doc = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(titel)s</title>
<meta name="description" content="%(meta)s">
<link rel="canonical" href="%(canon)s">
<meta property="og:title" content="%(titel)s">
<meta property="og:description" content="%(meta)s">
<meta property="og:type" content="website">
<meta property="og:url" content="%(canon)s">
<meta property="og:site_name" content="%(sitenaam)s">
<meta name="theme-color" content="#fbf7f2">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/stijl.css">
</head>
<body>
<header class="balk"><div class="wrap">
<a class="merk" href="/">%(logo)s<span class="naam">Top <b>Kids</b> Fashion</span></a>
<nav class="menu" aria-label="Hoofdmenu">%(menu)s</nav>
</div></header>
%(kruimel)s
<main class="wrap%(breed)s inhoud">
%(inhoud)s
</main>
<footer class="voet"><div class="wrap">
<div class="kolommen">
<div>
<h4>Top Kids Fashion</h4>
<p class="klein">Een gids over kindermode: merken, maten, materialen en manieren om kleding te combineren. Gemaakt voor ouders die een kast willen die lang meegaat.</p>
</div>
<div>
<h4>Rubrieken</h4>
<ul>
<li><a href="/merken/">Merken</a></li>
<li><a href="/stijl/">Stijl en inspiratie</a></li>
<li><a href="/maten/">Maten per leeftijd</a></li>
<li><a href="/materialen/">Materialen en onderhoud</a></li>
<li><a href="/seizoen/">Per seizoen</a></li>
<li><a href="/video/">Merkvideo&rsquo;s</a></li>
</ul>
</div>
<div>
<h4>Over deze site</h4>
<ul>
<li><a href="/winkel-apeldoorn/">De winkel in Apeldoorn</a></li>
<li><a href="/hulpbronnen/">Hulpbronnen</a></li>
<li><a href="/contact/">Contact</a></li>
<li><a href="/privacybeleid/">Privacybeleid</a></li>
<li><a href="/cookiebeleid/">Cookiebeleid</a></li>
</ul>
</div>
</div>
<div class="slot">%(jaar)s &middot; topkidsfashion.nl</div>
</div></footer>
<script src="/site.js" defer></script>
</body>
</html>
""" % dict(titel=esc(titel), meta=esc(meta), canon=canon, sitenaam=TITEL, logo=LOGO,
           menu=menu, kruimel=kr, inhoud=inhoud, jaar="2026", breed="" if breed else " smal")
    voegtoe(pad, titel, meta, doc, prio)
    return doc


def schrijf(dist="dist"):
    for pad, titel, meta, doc, prio in PAGINAS:
        map_ = os.path.join(dist, pad.strip("/"))
        os.makedirs(map_, exist_ok=True)
        with open(os.path.join(map_, "index.html"), "w", encoding="utf-8") as f:
            f.write(doc)
    # sitemap
    urls = "".join('<url><loc>%s%s</loc><priority>%s</priority></url>\n' % (BASE, p, pr)
                   for p, t, m, d, pr in PAGINAS if p != "/404/")
    with open(os.path.join(dist, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n%s</urlset>\n' % urls)
    with open(os.path.join(dist, "robots.txt"), "w", encoding="utf-8") as f:
        f.write("User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % BASE)
    with open(os.path.join(dist, "stijl.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    with open(os.path.join(dist, "site.js"), "w", encoding="utf-8") as f:
        f.write(JS)
