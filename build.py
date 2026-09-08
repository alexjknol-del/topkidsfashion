# -*- coding: utf-8 -*-
"""Bouwt de statische site voor topkidsfashion.nl in dist/."""

import os, shutil, sys
import core, art, video
from collections import defaultdict
from core import pagina, esc
from content_merken import MERKEN, KORT
from content_stijl import STIJL
from content_maten import MATEN, KLEDING, tabel
from content_materialen import MATERIALEN
from content_seizoen import SEIZOEN

SHOPCOL = "https://www.hedgehoganddeer.nl/collections/"

_teller = defaultdict(int)
_index = {}
for _m in MERKEN:
    _index[_m["slug"]] = _teller[_m["icoon"]]
    _teller[_m["icoon"]] += 1

SHOPHOME = "https://www.hedgehoganddeer.nl/"

VARIANT = [
 "%(aanbod)s van %(naam)s liggen bij <a href=\"%(url)s\" rel=\"noopener\">%(naam)s</a> in de winkel aan de Deventerstraat in Apeldoorn en in de webwinkel van Hedgehog &amp; Deer.",
 "De lopende collectie van <a href=\"%(url)s\" rel=\"noopener\">%(naam)s</a> is te zien bij Hedgehog &amp; Deer in Apeldoorn, met %(aanbod)s.",
 "Bij Hedgehog &amp; Deer in Apeldoorn staat <a href=\"%(url)s\" rel=\"noopener\">%(naam)s</a> in de rekken: %(aanbod)s.",
 "Wie %(aanbod)s van dit merk wil zien, vindt <a href=\"%(url)s\" rel=\"noopener\">%(naam)s</a> bij Hedgehog &amp; Deer aan de Deventerstraat in Apeldoorn.",
]


def plaat(naam, bijschrift=""):
    fn = getattr(art, naam, None)
    if not fn:
        return ""
    cap = '<figcaption>%s</figcaption>' % bijschrift if bijschrift else ""
    return '<figure class="tekening">%s%s</figure>' % (fn(), cap)


def kaart(link, titel, tekst, icoon=None):
    p = '<div class="plaat">%s</div>' % art.icoon(icoon) if icoon else ""
    return ('<article class="kaart">%s<h3>%s</h3><p>%s</p>'
            '<a class="meer" href="%s">Lezen</a></article>' % (p, titel, tekst, link))


# ---------------------------------------------------------------- home
def home():
    merkkaarten = "".join(
        '<article class="kaart"><div class="plaat">%s</div><h3>%s</h3><p>%s</p>'
        '<a class="meer" href="/merken/%s/">Naar het merk</a></article>'
        % (art.embleem(_index[m["slug"]], m["icoon"]), m["naam"], m["kort"], m["slug"])
        for m in MERKEN[:8])
    rubriek = "".join([
        kaart("/merken/", "Merken", "Achtendertig merken uit de winkel, van Zweeds tot Portugees, met wat ze maken en hoe het draagt."),
        kaart("/stijl/", "Stijl en inspiratie", "Kleuren combineren, laagjes opbouwen en een kast die klein blijft maar alles kan."),
        kaart("/maten/", "Maten", "Kledingmaten, schoenmaten en hoofdomtrek, met de leeftijd en de lengte die erbij horen."),
        kaart("/materialen/", "Materialen", "Biologisch katoen, merinowol, linnen en de keurmerken die op het label staan."),
        kaart("/seizoen/", "Per seizoen", "Van de dunne lentejas tot regenkleding, wintersokken en zwemshirts met uv-werende stof."),
        kaart("/video/", "Merkvideo&rsquo;s", "Collectiefilms van de merken zelf, gebundeld en pas geladen zodra er geklikt wordt."),
    ])
    videos = "".join(video.speler(v[1], v[2], v[3]) for v in
                     [x for x in video.VIDEOS if x[1] in ("GiCuLK_9juQ", "6lFMbFr5dHg", "iAqwO1I5oMk", "XN5huNHhmb8")])
    inhoud = f"""
<section class="hero"><div class="in">
<div>
<h1>Kindermode die langer meegaat dan een seizoen</h1>
<p class="lead">Top Kids Fashion is een gids over kinderkleding: welke merken wat maken, welke maat bij welke lengte hoort, welke stof waarvoor bedoeld is en hoe een kast klein blijft zonder saai te worden.</p>
<ul class="lint">
<li><a href="/merken/">38 merken</a></li>
<li><a href="/maten/">Maattabellen</a></li>
<li><a href="/stijl/capsule-garderobe/">Een kleine kast</a></li>
<li><a href="/seizoen/regenkleding/">Regenkleding</a></li>
</ul>
</div>
<div>{art.rek()}</div>
</div></section>

<h2>Waar deze gids uit bestaat</h2>
<div class="rooster k3">{rubriek}</div>

<h2>Merken om mee te beginnen</h2>
<p>Elk merk heeft een eigen handschrift: het ene werkt met grote dierenprints, het andere met ongeverfde wol. Deze acht laten het verschil goed zien.</p>
<div class="rooster k4">{merkkaarten}</div>
<p><a href="/merken/">Alle merken op een rij</a></p>

<div class="vlak">
<h2>Waar de collecties te zien zijn</h2>
<p>De merken in deze gids komen uit het assortiment van <a href="{SHOPHOME}" rel="noopener">Hedgehog &amp; Deer</a>, een kinderkledingwinkel aan de Deventerstraat in Apeldoorn met een webwinkel daarnaast. In de winkel zijn de collecties naast elkaar te zien, wat helpt bij het vergelijken van pasvorm en stof.</p>
</div>

<h2>Beeld van de merken</h2>
<p>Veel merken maken bij elke collectie een korte film. Deze vier geven een goed beeld van hoe verschillend ze naar kindermode kijken. De video wordt pas geladen na een klik.</p>
<div class="rooster k2">{videos}</div>
<p><a href="/video/">Alle video&rsquo;s</a></p>
"""
    pagina("/", "Top Kids Fashion, gids over kindermode, merken en maten",
           "Gids over kindermode: 38 merken uitgelegd, maattabellen per leeftijd, materialen en keurmerken, en kleding kiezen per seizoen.",
           inhoud, "1.0", breed=True)


# ---------------------------------------------------------------- merken
def merken():
    lijst = "".join(
        '<article class="kaart"><div class="plaat">%s</div><h3>%s</h3><p>%s</p>'
        '<a class="meer" href="/merken/%s/">Naar het merk</a></article>'
        % (art.embleem(_index[m["slug"]], m["icoon"]), m["naam"], m["kort"], m["slug"]) for m in MERKEN)
    kort = "".join('<li><span class="nr">&bull;</span><div><b>%s</b><span class="uitleg">%s '
                   '<a href="%s%s" rel="noopener">%s</a></span></div></li>'
                   % (n, t, SHOPCOL, c, n) for n, c, t in KORT)
    inhoud = f"""
<h1>Merken in kindermode</h1>
<p class="lead">Achtendertig merken met een eigen pagina, plus negen kleinere namen. Per merk staat er wat het maakt, hoe de pasvorm uitvalt en waar het zich mee laat combineren.</p>
{plaat("rek", "Elk merk heeft een eigen pasvorm; de maat op het label zegt daarover weinig.")}
<div class="rooster k3">{lijst}</div>

<h2>Kleinere namen in het assortiment</h2>
<p>Deze merken hebben een beperkte collectie, maar zijn wel het bekijken waard.</p>
<ul class="rijen">{kort}</ul>

<div class="vlak">
<h2>Merken naast elkaar zien</h2>
<p>Pasvorm verschilt sterk per merk. Een maat 116 van het ene merk zit als een 110 van het andere, en dat is geen fout maar een keuze in de snit. In een winkel waar de merken naast elkaar hangen, zoals bij <a href="{SHOPHOME}" rel="noopener">Hedgehog &amp; Deer</a> in Apeldoorn, is dat verschil in een paar minuten te zien.</p>
</div>
"""
    pagina("/merken/", "Merken in kindermode, 38 merken op een rij",
           "Overzicht van 38 kindermodemerken met per merk het aanbod, de pasvorm en waar de kleding zich mee laat combineren.",
           inhoud, "0.9", kruimelpad=[("/merken/", "Merken")], breed=True)

    for i, m in enumerate(MERKEN):
        alineas = "".join("<p>%s</p>" % t for t in m["tekst"])
        vid = video.voor(m["col"], 3)
        waar = VARIANT[i % len(VARIANT)] % dict(naam=m["naam"], url=SHOPCOL + m["col"], aanbod=m["aanbod"].capitalize() if i % 4 == 0 else m["aanbod"])
        ander = [x for x in MERKEN if x["icoon"] == m["icoon"] and x["slug"] != m["slug"]][:3]
        verder = "".join('<li><span class="nr">&rsaquo;</span><div><b><a href="/merken/%s/">%s</a></b>'
                         '<span class="uitleg">%s</span></div></li>' % (a["slug"], a["naam"], a["kort"]) for a in ander)
        inhoud = f"""
<div class="merkkop"><div>{art.embleem(_index[m["slug"]], m["icoon"], rond=True)}</div>
<div><h1>{m["naam"]}</h1><p class="klein">{m["kort"]}</p></div></div>
{alineas}
<h2>Wat er in de collectie zit</h2>
<p>{m["aanbod"].capitalize()}.</p>
<div class="vlak"><h3>Praktisch</h3><p>{m["tip"]}</p></div>
{vid}
<div class="vlak"><h2>Waar het te vinden is</h2><p>{waar}</p></div>
<h2>Verder kijken</h2>
<ul class="rijen">{verder}</ul>
"""
        pagina("/merken/%s/" % m["slug"], "%s: collectie, pasvorm en stijl" % m["naam"],
               "%s %s" % (m["kort"], "Wat het merk maakt, hoe de pasvorm uitvalt en waar het zich mee laat combineren."),
               inhoud, "0.7", kruimelpad=[("/merken/", "Merken"), ("", m["naam"])])


# ---------------------------------------------------------------- rubrieken
def rubriek(pad, kop, lead, items, tekening, hubmeta, prio="0.8", naam="Rubriek"):
    kaarten = "".join(kaart("%s%s/" % (pad, it["slug"]), it["titel"], it["meta"]) for it in items)
    inhoud = f"""
<h1>{kop}</h1>
<p class="lead">{lead}</p>
{plaat(tekening)}
<div class="rooster k2">{kaarten}</div>
"""
    pagina(pad, kop, hubmeta, inhoud, prio, kruimelpad=[(pad, naam)], breed=True)


def artikelen():
    rubriek("/stijl/", "Stijl en inspiratie",
            "Combineren, opbouwen en kiezen. Tien stukken over hoe kinderkleding samenwerkt in plaats van los in de kast te hangen.",
            STIJL, "kleurenwaaier",
            "Tien artikelen over het combineren van kinderkleding: kleuren, prints, laagjes, een kleine kast en kleding die doorgaat naar een volgend kind.",
            naam="Stijl")
    for it in STIJL:
        secties = "".join("<h2>%s</h2>%s" % (k, "".join(p if p.startswith("<") else "<p>%s</p>" % p for p in ps))
                          for k, ps in it["secties"])
        inhoud = f"""<h1>{it["titel"]}</h1><p class="lead">{it["lead"]}</p>{plaat(it["plaat"])}{secties}"""
        pagina("/stijl/%s/" % it["slug"], it["titel"], it["meta"], inhoud, "0.6",
               kruimelpad=[("/stijl/", "Stijl"), ("", it["titel"])])

    rubriek("/maten/", "Maten voor kinderkleding",
            "Kledingmaat is in Nederland gelijk aan de lichaamslengte in centimeters. Deze zes pagina's zetten maat, leeftijd en lengte naast elkaar, inclusief schoenen en mutsen.",
            MATEN, "maatladder",
            "Maattabellen voor kinderkleding per leeftijd, van maat 50 tot 164, plus schoenmaten met voetlengte en maten voor mutsen.",
            "0.9", naam="Maten")
    for it in MATEN:
        blok = "".join("<h2>%s</h2>%s" % (k, v if v.startswith("<") else "<p>%s</p>" % v) for k, v in it["blokken"])
        inhoud = f"""<h1>{it["titel"]}</h1><p class="lead">{it["lead"]}</p>{plaat(it["plaat"])}{blok}
<div class="vlak"><h3>Kort samengevat</h3><p>De maat op het label staat voor de lichaamslengte in centimeters. Meten is nauwkeuriger dan rekenen met de leeftijd, zeker vanaf een jaar of zes.</p></div>"""
        pagina("/maten/%s/" % it["slug"], it["titel"], it["meta"], inhoud, "0.7",
               kruimelpad=[("/maten/", "Maten"), ("", it["titel"])])

    rubriek("/materialen/", "Materialen en onderhoud",
            "Waar kinderkleding van gemaakt is bepaalt hoe hij draagt, hoe lang hij meegaat en hoe hij gewassen moet worden.",
            MATERIALEN, "wolvezel",
            "Materialen in kinderkleding: biologisch katoen, merinowol, linnen, viscose en tencel, met keurmerken en wasadvies.",
            naam="Materialen")
    for it in MATERIALEN:
        blok = "".join("<h2>%s</h2>%s" % (k, v) for k, v in it["blokken"])
        inhoud = f"""<h1>{it["titel"]}</h1><p class="lead">{it["lead"]}</p>{plaat(it["plaat"])}{blok}"""
        pagina("/materialen/%s/" % it["slug"], it["titel"], it["meta"], inhoud, "0.6",
               kruimelpad=[("/materialen/", "Materialen"), ("", it["titel"])])

    rubriek("/seizoen/", "Kleding per seizoen",
            "Vier seizoenen, en twee categorieen die hun eigen regels hebben: regenkleding en zwemkleding.",
            SEIZOEN, "seizoenen",
            "Kinderkleding per seizoen: lente, zomer, herfst en winter, plus regenkleding met waterkolom en zwemkleding met uv-werende stof.",
            naam="Seizoen")
    for it in SEIZOEN:
        blok = "".join("<h2>%s</h2>%s" % (k, v) for k, v in it["blokken"])
        inhoud = f"""<h1>{it["titel"]}</h1><p class="lead">{it["lead"]}</p>{plaat(it["plaat"])}{blok}"""
        pagina("/seizoen/%s/" % it["slug"], it["titel"], it["meta"], inhoud, "0.6",
               kruimelpad=[("/seizoen/", "Seizoen"), ("", it["titel"])])


# ---------------------------------------------------------------- video
def videopagina():
    op_merk = {}
    for slug, vid, tekst, kanaal in video.VIDEOS:
        op_merk.setdefault(slug, []).append((vid, tekst, kanaal))
    naam = {m["col"]: (m["naam"], m["slug"]) for m in MERKEN}
    blokken = []
    for col, rij in op_merk.items():
        mnaam, mslug = naam.get(col, (col, None))
        kop = '<h2>%s</h2>' % mnaam
        if mslug:
            kop += '<p class="klein"><a href="/merken/%s/">Over %s</a></p>' % (mslug, mnaam)
        blokken.append(kop + '<div class="rooster k2">%s</div>' %
                       "".join(video.speler(v, t, k) for v, t, k in rij))
    inhoud = f"""
<h1>Merkvideo&rsquo;s</h1>
<p class="lead">Kindermodemerken maken bij elke collectie een korte film: soms een animatie, soms een portret van de werkplaats. Hieronder staan er {len(video.VIDEOS)}, gesorteerd per merk.</p>
<p>De video&rsquo;s worden pas geladen zodra er op het beeld geklikt wordt. Tot dat moment gaat er geen verzoek naar YouTube.</p>
{plaat("sterren")}
{''.join(blokken)}
"""
    pagina("/video/", "Merkvideo&rsquo;s van kindermodemerken",
           "Collectiefilms en animaties van kindermodemerken, gebundeld per merk. De video wordt pas geladen na een klik.",
           inhoud, "0.7", kruimelpad=[("/video/", "Video")], breed=True)


# ---------------------------------------------------------------- overige
def overig():
    inhoud = f"""
<h1>De winkel in Apeldoorn</h1>
<p class="lead">De merken in deze gids komen uit het assortiment van Hedgehog &amp; Deer, een kinderkledingwinkel aan de Deventerstraat 1b in Apeldoorn.</p>
{plaat("kast")}
<p>De winkel voert kleding voor kinderen van nul tot ongeveer veertien jaar, aangevuld met speelgoed, kinderkamerartikelen en cadeaus. Naast de winkel is er een webwinkel: <a href="{SHOPHOME}" rel="noopener">{SHOPHOME}</a>.</p>
<h2>Wat er te vinden is</h2>
<ul>
<li>Kleding voor baby, peuter, kleuter en oudere kinderen, van maat 50 tot en met 164</li>
<li>Schoenen, laarzen en slofjes</li>
<li>Tassen, petten, haaraccessoires en sieraden</li>
<li>Speelgoed, knuffels en artikelen voor de kinderkamer</li>
</ul>
<h2>Openingstijden</h2>
<div class="tabelwrap"><table><tbody>
<tr><th>Maandag</th><td>gesloten</td></tr>
<tr><th>Dinsdag tot en met vrijdag</th><td>10.00 tot 17.00 uur</td></tr>
<tr><th>Zaterdag</th><td>10.00 tot 17.00 uur</td></tr>
<tr><th>Zondag</th><td>gesloten, behalve de eerste zondag van de maand</td></tr>
</tbody></table></div>
<p class="klein">Openingstijden kunnen rond feestdagen afwijken; de actuele tijden staan op <a href="{SHOPHOME}pages/contact" rel="noopener">{SHOPHOME}pages/contact</a>.</p>
<h2>Adres</h2>
<p>Deventerstraat 1b, 7311 BH Apeldoorn.</p>
"""
    pagina("/winkel-apeldoorn/", "Kinderkledingwinkel aan de Deventerstraat in Apeldoorn",
           "De winkel achter de merken uit deze gids: adres, openingstijden en wat er te vinden is in Apeldoorn.",
           inhoud, "0.7", kruimelpad=[("", "De winkel in Apeldoorn")])

    inhoud = """
<h1>Contact</h1>
<p class="lead">Top Kids Fashion is een gids over kindermode. Vragen, aanvullingen of een correctie op een van de pagina&rsquo;s zijn welkom per e-mail.</p>
<p>E-mail: <a href="mailto:info@topkidsfashion.nl">info@topkidsfashion.nl</a></p>
<h2>Waar deze site wel en niet over gaat</h2>
<p>Deze site beschrijft merken, maten en materialen. Er wordt niets verkocht en er worden geen bestellingen verwerkt. Vragen over een bestelling of over de voorraad van een merk horen bij de winkel zelf thuis.</p>
<h2>Correcties</h2>
<p>Merken wijzigen hun collecties, hun maatvoering en soms hun naam. Wie een onjuistheid tegenkomt, mag die melden; de pagina wordt dan aangepast.</p>
"""
    pagina("/contact/", "Contact", "Contactgegevens van Top Kids Fashion, een gids over kindermode.",
           inhoud, "0.4", kruimelpad=[("", "Contact")])

    inhoud = """
<h1>Privacybeleid</h1>
<p>Top Kids Fashion is een informatieve site. Er worden geen accounts aangemaakt, er is geen webwinkel en er worden geen bestellingen verwerkt.</p>
<h2>Gegevens die worden verwerkt</h2>
<p>Bij het bezoeken van deze site worden geen persoonsgegevens opgeslagen door de site zelf. De hostingpartij houdt technische logbestanden bij, waaronder ip-adressen, om storingen en misbruik te kunnen opsporen. Die gegevens worden niet gebruikt om bezoekers te volgen.</p>
<h2>E-mail</h2>
<p>Wie een bericht stuurt naar info@topkidsfashion.nl, deelt daarmee een e-mailadres en de inhoud van het bericht. Die gegevens worden alleen gebruikt om te antwoorden en niet doorgegeven aan derden.</p>
<h2>Video&rsquo;s</h2>
<p>Op deze site staan video&rsquo;s van YouTube. Die worden pas geladen nadat een bezoeker op het beeld klikt. Zolang er niet geklikt wordt, gaat er geen verzoek naar YouTube en worden er dus ook geen gegevens met YouTube gedeeld. Na een klik gelden de voorwaarden en het privacybeleid van YouTube, onderdeel van Google.</p>
<h2>Links naar andere sites</h2>
<p>Deze site verwijst naar sites van derden. Op die sites gelden de privacyvoorwaarden van de betreffende partij.</p>
<h2>Rechten</h2>
<p>Wie wil weten welke gegevens er zijn vastgelegd, of wil dat een e-mailwisseling wordt verwijderd, kan dat opvragen via info@topkidsfashion.nl.</p>
"""
    pagina("/privacybeleid/", "Privacybeleid", "Hoe Top Kids Fashion omgaat met gegevens van bezoekers: logbestanden, e-mail, video van YouTube en links naar andere sites.",
           inhoud, "0.3", kruimelpad=[("", "Privacybeleid")])

    inhoud = """
<h1>Cookiebeleid</h1>
<p>Deze site plaatst zelf geen cookies. Er is geen bezoekersstatistiek, geen advertentienetwerk en geen volgsysteem actief.</p>
<h2>Video&rsquo;s</h2>
<p>De video&rsquo;s op deze site staan op YouTube en worden pas geladen na een klik op het beeld. Wie klikt, laadt daarmee een venster van youtube-nocookie.com. Ook in die variant kan YouTube gegevens vastleggen zodra een video wordt afgespeeld.</p>
<h2>Cookies verwijderen</h2>
<p>Cookies die door andere sites zijn geplaatst, zijn te verwijderen via de instellingen van de browser. In Chrome, Firefox, Safari en Edge staat die optie onder privacy en beveiliging.</p>
"""
    pagina("/cookiebeleid/", "Cookiebeleid", "Welke cookies deze site plaatst en wat er gebeurt bij het afspelen van een video.",
           inhoud, "0.3", kruimelpad=[("", "Cookiebeleid")])


def foutpagina(dist):
    doc = core.PAGINAS
    inhoud = """
<h1>Deze pagina bestaat niet</h1>
<p class="lead">Het adres klopt niet meer of is verkeerd overgenomen. Onderstaande rubrieken zijn een goed beginpunt.</p>
<ul>
<li><a href="/merken/">Alle merken</a></li>
<li><a href="/maten/">Maattabellen</a></li>
<li><a href="/stijl/">Stijl en inspiratie</a></li>
<li><a href="/materialen/">Materialen en onderhoud</a></li>
<li><a href="/seizoen/">Kleding per seizoen</a></li>
</ul>
"""
    html = pagina("/404/", "Pagina niet gevonden", "Deze pagina bestaat niet meer of het adres is verkeerd overgenomen. Via de rubrieken hieronder zijn merken, maten en materialen terug te vinden.", inhoud, "0.1")
    with open(os.path.join(dist, "404.html"), "w", encoding="utf-8") as f:
        f.write(html)


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44">
<rect width="44" height="44" rx="10" fill="#fbf7f2"/>
<path d="M22 11v6" stroke="#c2573f" stroke-width="2" stroke-linecap="round"/>
<path d="M22 17c-3 0-5 2-5 4l5 3 5-3c0-2-2-4-5-4z" fill="#6f8b6a"/>
<path d="M8 26h28l-14 8-14-8z" fill="#c2573f"/>
<circle cx="22" cy="9.5" r="2.4" fill="#e3a63c"/></svg>"""


def main():
    dist = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist")
    if os.path.isdir(dist):
        shutil.rmtree(dist)
    os.makedirs(dist)
    home()
    merken()
    artikelen()
    videopagina()
    overig()
    core.schrijf(dist)
    foutpagina(dist)
    with open(os.path.join(dist, "favicon.svg"), "w", encoding="utf-8") as f:
        f.write(FAVICON)
    print("%d pagina's gebouwd in %s" % (len(core.PAGINAS), dist))


if __name__ == "__main__":
    main()
