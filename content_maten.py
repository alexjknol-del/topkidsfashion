# -*- coding: utf-8 -*-
"""Maatinformatie. Maat is in Nederland gelijk aan de lichaamslengte in centimeters."""

# maat, gemiddelde leeftijd, lengte
KLEDING = [
 ("50", "pasgeboren", "tot 50 cm"),
 ("56", "0 tot 2 maanden", "50 tot 56 cm"),
 ("62", "2 tot 4 maanden", "56 tot 62 cm"),
 ("68", "4 tot 6 maanden", "62 tot 68 cm"),
 ("74", "6 tot 9 maanden", "68 tot 74 cm"),
 ("80", "9 tot 12 maanden", "74 tot 80 cm"),
 ("86", "12 tot 18 maanden", "80 tot 86 cm"),
 ("92", "circa 2 jaar", "86 tot 92 cm"),
 ("98", "circa 3 jaar", "92 tot 98 cm"),
 ("104", "circa 4 jaar", "98 tot 104 cm"),
 ("110", "circa 5 jaar", "104 tot 110 cm"),
 ("116", "circa 6 jaar", "110 tot 116 cm"),
 ("122", "circa 7 jaar", "116 tot 122 cm"),
 ("128", "circa 8 jaar", "122 tot 128 cm"),
 ("134", "circa 9 jaar", "128 tot 134 cm"),
 ("140", "circa 10 jaar", "134 tot 140 cm"),
 ("146", "circa 11 jaar", "140 tot 146 cm"),
 ("152", "circa 12 jaar", "146 tot 152 cm"),
 ("158", "circa 13 jaar", "152 tot 158 cm"),
 ("164", "circa 14 jaar", "158 tot 164 cm"),
]

# schoenmaat, voetlengte in cm, gemiddelde leeftijd
SCHOENEN = [
 ("17", "10,0", "0 tot 3 maanden"),
 ("18", "10,7", "3 tot 6 maanden"),
 ("19", "11,3", "6 tot 9 maanden"),
 ("20", "12,0", "9 tot 12 maanden"),
 ("21", "12,7", "circa 1 jaar"),
 ("22", "13,3", "1 tot 1,5 jaar"),
 ("23", "14,0", "1,5 jaar"),
 ("24", "14,7", "circa 2 jaar"),
 ("25", "15,3", "2 tot 2,5 jaar"),
 ("26", "16,0", "circa 3 jaar"),
 ("27", "16,7", "3 tot 3,5 jaar"),
 ("28", "17,3", "circa 4 jaar"),
 ("29", "18,0", "4 tot 5 jaar"),
 ("30", "18,7", "circa 5 jaar"),
 ("31", "19,3", "5 tot 6 jaar"),
 ("32", "20,0", "circa 6 jaar"),
 ("33", "20,7", "6 tot 7 jaar"),
 ("34", "21,3", "circa 8 jaar"),
 ("35", "22,0", "8 tot 9 jaar"),
 ("36", "22,7", "circa 10 jaar"),
 ("37", "23,3", "circa 11 jaar"),
 ("38", "24,0", "circa 12 jaar"),
]

MUTSEN = [
 ("39 tot 41 cm", "pasgeboren", "maat 44/46"),
 ("42 tot 44 cm", "3 tot 6 maanden", "maat 44/46"),
 ("45 tot 47 cm", "6 tot 18 maanden", "maat 47/49"),
 ("48 tot 50 cm", "2 tot 4 jaar", "maat 50/52"),
 ("51 tot 53 cm", "4 tot 8 jaar", "maat 53/55"),
 ("54 tot 56 cm", "vanaf 8 jaar", "maat 55/57"),
]


def tabel(kop, rijen):
    th = "".join("<th>%s</th>" % k for k in kop)
    tr = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rijen)
    return '<div class="tabelwrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (th, tr)


MATEN = [
 dict(slug="baby", plaat="cirkelkind",
  titel="Babymaten: 50 tot en met 86",
  meta="Babymaten van 50 tot 86 met de bijbehorende leeftijd en lengte, en hoe vaak een maat in het eerste jaar wisselt.",
  lead="In het eerste jaar wisselt de maat vijf tot zes keer. Kopen op leeftijd gaat daardoor vaak mis; kopen op lengte klopt vrijwel altijd.",
  blokken=[
   ("Maat en leeftijd", tabel(["Maat", "Gemiddelde leeftijd", "Lichaamslengte"], KLEDING[:7])),
   ("Hoe lang een maat meegaat", "<p>Maat 50 wordt vaak maar twee tot drie weken gedragen. Veel ouders slaan die over en beginnen bij 56. Vanaf maat 74 wordt het rustiger: die gaat gemiddeld twee tot drie maanden mee.</p><p>Rompers en boxpakjes mogen ruim zitten, want ze krimpen licht bij de eerste wasbeurten en een luier neemt ruimte in. Bij slaapzakken geldt het omgekeerde: die moeten juist niet te groot zijn.</p>"),
   ("Waar op te letten", "<ul><li>Drukknopen in het kruis, zodat verschonen kan zonder alles uit te trekken</li><li>Platte naden en labels aan de buitenkant</li><li>Omslagen aan de mouw die over de handjes vallen, tegen krabben</li><li>Halsopening met een overslag, zodat een romper over de schouders uit kan als er iets misgaat</li></ul>"),
  ]),

 dict(slug="peuter", plaat="tuinbroek",
  titel="Peutermaten: 86 tot en met 104",
  meta="Maten 86 tot 104 voor dreumesen en peuters, met leeftijd, lengte en aandachtspunten bij zindelijkheid en zelf aankleden.",
  lead="Tussen de anderhalf en vier jaar groeit een kind ongeveer een maat per half jaar. In dezelfde periode begint zelf aankleden, en dat stelt eigen eisen aan de kleding.",
  blokken=[
   ("Maat en leeftijd", tabel(["Maat", "Gemiddelde leeftijd", "Lichaamslengte"], KLEDING[6:10])),
   ("Zindelijk worden", "<p>Broeken met een enkele elastische band werken in deze fase het best. Tuinbroeken, riemen en dubbele knopen vragen tijd die er op dat moment niet is.</p><p>Een reservebroek in de tas is geen overbodige luxe, ook enkele maanden nadat het goed gaat.</p>"),
   ("Pasvorm", "<p>Peuters hebben nog een rondere buik dan oudere kinderen. Een broek die in de lengte past, kan in de taille te ruim zijn; een verstelbaar elastiek in de band lost dat op.</p><p>Bij mouwen en pijpen geldt: liever iets te lang en omslaan, dan te kort na twee wasbeurten.</p>"),
  ]),

 dict(slug="kleuter", plaat="hanger",
  titel="Kleutermaten: 104 tot en met 116",
  meta="Maten 104 tot 116 voor kleuters, met leeftijd en lengte en wat er verandert zodra een kind naar school gaat.",
  lead="Vanaf vier jaar vertraagt de groei tot ongeveer een maat per jaar. Kleding gaat daardoor langer mee, maar slijt ook zichtbaarder omdat er harder mee gespeeld wordt.",
  blokken=[
   ("Maat en leeftijd", tabel(["Maat", "Gemiddelde leeftijd", "Lichaamslengte"], KLEDING[9:12])),
   ("Slijtplekken", "<p>Knieen en ellebogen gaan als eerste. Broeken met een dubbele stoflaag op de knie houden het een schooljaar vol waar een gewone broek halverwege doorslijt.</p><p>Mouwuiteinden en boorden rekken uit door aan de mouw te trekken; een geribde boord blijft langer strak dan een gestikte zoom.</p>"),
   ("Zelf regelen", "<p>In deze fase kan een kind een rits en een grote knoop aan. Wat nog niet lukt is een rits inzetten en veters strikken. Klittenband blijft daarom praktisch tot een jaar of zes.</p>"),
  ]),

 dict(slug="basisschool", plaat="rek",
  titel="Maten 116 tot en met 140",
  meta="Kledingmaten voor kinderen op de basisschool met leeftijd en lengte, en waarom pasvorm belangrijker wordt dan maat.",
  lead="Vanaf een jaar of zes lopen kinderen van dezelfde leeftijd sterk uiteen in lengte. De maat op het label zegt vanaf dat moment minder dan de lengte van het kind.",
  blokken=[
   ("Maat en leeftijd", tabel(["Maat", "Gemiddelde leeftijd", "Lichaamslengte"], KLEDING[11:16])),
   ("Meten in plaats van gokken", "<p>Meten gaat het eenvoudigst tegen een deurpost, op blote voeten, met een boek plat op het hoofd. Wie het eens per half jaar noteert, ziet ook wanneer een groeispurt begint.</p><p>Merken wijken onderling af. Een maat 128 van het ene merk kan zitten als een 122 van het andere; dat is geen fout maar een verschil in snit.</p>"),
   ("Voorkeuren", "<p>Rond deze leeftijd ontstaat een uitgesproken mening over kleding. Meepraten over de aankoop verkleint de kans dat een kledingstuk blijft hangen.</p><p>Comfort weegt in deze fase zwaarder dan model: labels die kriebelen, naden die schuren en stoffen die niet rekken zijn de meest genoemde bezwaren.</p>"),
  ]),

 dict(slug="tiener", plaat="trui",
  titel="Maten 140 tot en met 164",
  meta="Tienermaten van 140 tot 164 met leeftijd en lengte, en de overgang van kindermaten naar volwassen maten.",
  lead="Rond maat 140 begint de overgang naar volwassen maten. Sommige merken lopen door tot 176, andere stoppen bij 152 en gaan verder in XS.",
  blokken=[
   ("Maat en leeftijd", tabel(["Maat", "Gemiddelde leeftijd", "Lichaamslengte"], KLEDING[15:])),
   ("Kindermaat of volwassen maat", "<p>Kindermaten zijn gesneden op een rechte lichaamsbouw. Vanaf een jaar of twaalf klopt dat vaak niet meer, waardoor een damesmaat XS of een herenmaat S beter valt dan een 164.</p><p>Bij jassen en truien werkt de overstap meestal eerder dan bij broeken, omdat de lengte van de pijp bij volwassen maten anders is opgebouwd.</p>"),
   ("Groeispurt", "<p>In een groeispurt kan een kind in een half jaar twee maten opschuiven. Kleding met een omslagzoom of een verstelbare band overbrugt dat zonder dat alles tegelijk vervangen hoeft te worden.</p>"),
  ]),

 dict(slug="schoenmaten", plaat="laarsjes",
  titel="Schoenmaten en voetlengte",
  meta="Schoenmaten voor kinderen met de bijbehorende voetlengte in centimeters, plus hoe vaak de voet gemeten moet worden.",
  lead="Een schoenmaat volgt uit de voetlengte plus wat ruimte. Meten is nauwkeuriger dan passen, omdat een kind bij het passen de tenen intrekt.",
  blokken=[
   ("Meten", "<p>Zet het kind met de hiel tegen een muur op een vel papier en zet een streep bij de langste teen, die niet altijd de grote teen is. Meet beide voeten en houd de langste aan.</p><p>Bij de gemeten lengte komt ongeveer 1,2 centimeter ruimte. De maten in de tabel hieronder gaan uit van de voetlengte zelf, niet van de binnenzool.</p>"),
   ("Maat en voetlengte", tabel(["Schoenmaat", "Voetlengte", "Gemiddelde leeftijd"], SCHOENEN)),
   ("Hoe vaak controleren", "<p>Tot drie jaar groeit een voet ongeveer een maat per drie tot vier maanden. Daarna vertraagt dat naar een maat per half jaar. Een controle per kwartaal tot vier jaar is voldoende.</p><p>Te kleine schoenen zijn te herkennen aan een rode plek op de teen, een opgekrulde teennagel of sokken die aan de voorkant slijten.</p>"),
   ("Mutsen en petten", "<p>Voor mutsen telt de omtrek van het hoofd, gemeten net boven de oren en de wenkbrauwen.</p>" + tabel(["Hoofdomtrek", "Gemiddelde leeftijd", "Gangbare maat"], MUTSEN)),
  ]),
]
