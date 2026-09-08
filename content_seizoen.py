# -*- coding: utf-8 -*-
"""Per seizoen: wat er nodig is en waarop te letten."""

SEIZOEN = [
 dict(slug="lente", plaat="seizoenen",
  titel="Lente: het seizoen van de dunne jas",
  meta="Kinderkleding voor de lente: laagjes voor wisselend weer, de dunne winddichte jas en wat er na de winter uit de kast kan.",
  lead="Lente is het lastigste seizoen om voor te kleden. Een ochtend van zeven graden gaat over in een middag van zeventien, en dat gebeurt op een schooldag waarin niemand tussendoor thuiskomt.",
  blokken=[
   ("De dunne jas doet het werk", "<p>Een dunne winddichte jas over een sweater is warmer dan een gevoerde jas zonder winddichte buitenlaag. Bovendien past hij in een tas zodra het opklaart.</p><p>Modellen met een capuchon die opgerold in de kraag zit, zijn het praktischst; een losse capuchon raakt kwijt.</p>"),
   ("Wat mee moet in de tas", "<ul><li>Een dunne trui of vest dat opgevouwen weinig ruimte inneemt</li><li>Een regenjas of poncho, ook als de ochtend droog is</li><li>Bij fietsen: dunne handschoenen tot in april</li></ul>"),
   ("Opruimen na de winter", "<p>Wanten, dikke mutsen en gevoerde laarzen kunnen weg zodra de nachtvorst voorbij is. Ze gaan schoon de doos in, met de maat erop.</p><p>De winterjas hoort daar pas bij als hij gewassen of gereinigd is; opgeborgen vuil trekt motten aan bij wollen jassen.</p>"),
  ]),

 dict(slug="zomer", plaat="seizoenen",
  titel="Zomer: bescherming boven zo min mogelijk stof",
  meta="Zomerkleding voor kinderen: welke stoffen koelen, waarom lange mouwen soms verstandiger zijn en waar op te letten bij zon.",
  lead="Bij hitte is de eerste ingeving om zo min mogelijk aan te trekken. Voor een kind dat de hele dag buiten is, werkt dun en bedekkend vaak beter.",
  blokken=[
   ("Stoffen die koelen", "<p>Linnen en dun katoen laten lucht door en houden de stof van de huid af. Synthetische stoffen sluiten juist aan, waardoor warmte blijft hangen. Voor een dag in de zon is een dun linnen overhemd koeler dan een strak t-shirt van polyester.</p><p>Lichte kleuren weerkaatsen meer licht, maar het weefsel telt zwaarder: een dicht geweven donkere stof houdt zonlicht beter tegen dan een losjes geweven lichte.</p>"),
   ("Zon", "<ul><li>Een hoed of pet met een klep beschermt neus en oren, waar verbranding het vaakst begint</li><li>Zwemkleding met lange mouwen scheelt insmeren en blijft de hele dag werken</li><li>Tussen twaalf en drie uur is schaduw effectiever dan welke kleding ook</li></ul>"),
   ("Schoenen", "<p>Sandalen met een hielband houden de voet vast en zijn geschikt om in te rennen; modellen zonder hielband zijn dat niet. Blote voeten in gesloten schoenen leiden tot blaren, dus dunne sokken blijven ook in de zomer verstandig.</p>"),
  ]),

 dict(slug="herfst", plaat="regen",
  titel="Herfst: regen, plassen en modder",
  meta="Kinderkleding in de herfst: regenpak, laarzen, waterkolom en hoe kleding weer droog wordt voor de volgende dag.",
  lead="In de herfst gaat het minder om warmte dan om droog blijven. Een kind dat nat wordt, koelt snel af, ook bij tien graden.",
  blokken=[
   ("Regenkleding die werkt", "<p>Bij regenkleding staat vaak een waterkolom in millimeters vermeld. Alles vanaf ongeveer 5.000 millimeter is bruikbaar voor dagelijkse regen; vanaf 10.000 blijft het ook droog bij zitten in nat gras.</p><p>Belangrijker dan het getal zijn de naden. Gelaste of getapete naden houden water tegen; gewoon doorgestikte naden lekken op termijn.</p>"),
   ("Laarzen", "<p>Laarzen mogen een maat ruim zijn zodat er een dikke sok in past. Een lus aan de schacht maakt zelf aantrekken mogelijk.</p><p>Natte laarzen drogen van binnen het snelst met een prop krantenpapier erin, niet op de verwarming; dat maakt rubber bros.</p>"),
   ("Twee sets", "<p>Op natte dagen is een tweede set kleding op school of opvang geen luxe. Regenkleding die 's avonds nat blijft, is de volgende ochtend niet bruikbaar.</p><p>Regenkleding hoort niet in de droger en niet in de was met wasverzachter; beide tasten de waterafstotende laag aan.</p>"),
  ]),

 dict(slug="winter", plaat="seizoenen",
  titel="Winter: warm blijven zonder te zweten",
  meta="Winterkleding voor kinderen: lagen, jassen, handschoenen en het verschil tussen stilstaan en bewegen bij kou.",
  lead="Winterkleding wordt vaak gekozen op dikte. Wat meer uitmaakt, is de combinatie van lagen en de vraag of een kind stilstaat of beweegt.",
  blokken=[
   ("Stilstaan of bewegen", "<p>Een kind op de fiets achterop staat stil in de wind en heeft een winddichte, gevoerde jas nodig. Een kind dat op het schoolplein rent, heeft aan hetzelfde pak binnen tien minuten te warm.</p><p>De oplossing is een jas die open kan en een tussenlaag die uit kan, in plaats van een dikkere jas.</p>"),
   ("Handen, hoofd en voeten", "<ul><li>Wanten houden warmer dan handschoenen, omdat de vingers elkaar verwarmen</li><li>Een muts die de oren bedekt scheelt meer dan een dikkere jas</li><li>Twee paar dunne sokken werken slechter dan een paar dikke; te veel lagen drukken de doorbloeding weg</li></ul>"),
   ("Sneeuw", "<p>Bij sneeuw is een broek met een elastiek onder de voet nuttig, zodat sneeuw niet in de laars loopt. Een skipak is warm maar lastig bij toiletbezoek; een losse broek met bretels is praktischer.</p>"),
  ]),

 dict(slug="regenkleding", plaat="regen",
  titel="Regenkleding kiezen en onderhouden",
  meta="Waterkolom, ademend vermogen, naden en onderhoud van regenkleding voor kinderen, inclusief impregneren.",
  lead="Regenkleding is de categorie waarin een verkeerde keuze het snelst merkbaar is. Drie eigenschappen bepalen of een jas doet wat hij moet doen.",
  blokken=[
   ("Waterkolom", "<p>De waterkolom geeft aan hoeveel waterdruk een stof weerstaat voordat er vocht doorkomt, uitgedrukt in millimeters. Voor een korte fietstocht is 5.000 voldoende, voor een dag buiten in de regen is 10.000 of meer prettiger.</p><p>Zitten of knielen in nat gras zet veel meer druk op de stof dan regen die erop valt. Daar sneuvelen lichte jassen als eerste.</p>"),
   ("Ademend vermogen", "<p>Een volledig waterdichte stof die geen vocht doorlaat, laat het zweet aan de binnenkant condenseren. Het kind wordt dan alsnog nat, van binnenuit.</p><p>Voor kinderen die veel bewegen, is een jas met ventilatieopeningen onder de armen of in de rug een verbetering.</p>"),
   ("Onderhoud", "<p>De waterafstotende laag aan de buitenkant verzwakt door vuil en door wasmiddelresten. Wassen met een middel voor functionele kleding en daarna kort opwarmen met een strijkijzer op lage stand of in een droger op koele stand activeert de laag opnieuw, mits het label dat toestaat.</p><p>Een jas die water niet meer laat afparelen, is meestal niet kapot maar vuil.</p>"),
  ]),

 dict(slug="zwemkleding", plaat="seizoenen",
  titel="Zwemkleding en zonbescherming",
  meta="Zwemkleding voor kinderen: UV-werende stof, pasvorm, chloorbestendigheid en onderhoud na het zwembad.",
  lead="Zwemkleding heeft twee taken: blijven zitten en de huid beschermen. Beide gaan sneller achteruit dan bij gewone kleding, vooral door chloor.",
  blokken=[
   ("UV-werend materiaal", "<p>Stof met een UPF-waarde houdt een deel van de uv-straling tegen. UPF 50 laat ongeveer een vijftigste deel door. Nat wordt de bescherming van gewoon katoen fors minder, terwijl uv-werende stof zijn waarde grotendeels behoudt.</p><p>Een zwemshirt met lange mouwen scheelt het meeste insmeren, precies op de plekken die het vaakst worden overgeslagen: de schouders en de bovenrug.</p>"),
   ("Pasvorm", "<p>Zwemkleding hoort strak te zitten. Te ruime stof vult zich met water en trekt naar beneden, wat bij zwemles hinderlijk is.</p><p>Voor baby's zijn zwemluiers met elastiek aan been en taille nodig; een gewone luier zuigt vol water.</p>"),
   ("Na het zwemmen", "<p>Chloor blijft in de stof zitten en tast elastaan aan. Direct uitspoelen met koud water verlengt de levensduur meer dan wat dan ook.</p><p>Niet in de droger en niet in de volle zon drogen; beide maken de elastische vezels bros.</p>"),
  ]),
]
