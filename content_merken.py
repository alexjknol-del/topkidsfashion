# -*- coding: utf-8 -*-
"""Merkgegevens. Het aanbod per merk is afgeleid van de categorieen die de
winkel voert; de omschrijvingen gaan over wat een merk maakt en hoe het draagt."""

SHOP = "https://www.hedgehoganddeer.nl/collections/"

# slug, naam, collectie, icoon, kort, aanbod, alinea's, tip
MERKEN = [
 dict(slug="mini-rodini", naam="Mini Rodini", col="mini-rodini", icoon="kleding",
  kort="Zweeds merk met dierenprints, felle kleuren en biologisch katoen.",
  aanbod="jassen, vesten, sweaters, jurken, broeken, leggings en gilets",
  tekst=[
   "Mini Rodini komt uit Zweden en is opgericht door illustrator Cassandra Rhodin. Dat is terug te zien in de prints: tijgers, panda's, zeemeerminnen en ruimtevaarders die met de hand getekend zijn en over het hele kledingstuk doorlopen. Het merk werkt vrijwel volledig met biologisch katoen en gerecyclede vezels.",
   "De pasvorm is ruim. Sweaters en joggingbroeken zitten los om het lijf, met stevige boorden aan mouw en enkel, zodat een maat langer meegaat dan de leeftijd op het label doet vermoeden. Kleding van Mini Rodini gaat vaak door naar een tweede kind, en dat is precies waar de stevige stoffen op gebouwd zijn.",
   "Een print van Mini Rodini vraagt om rust eromheen: een effen broek onder een sweater met een groot dessin, of andersom. Wie twee prints wil combineren, kiest twee stukken uit dezelfde collectie, want daar zijn de kleuren op elkaar afgestemd.",
  ],
  tip="Kies bij twijfel de kleinste van twee maten als het om een sweater gaat; de mouwen zijn aan de lange kant."),

 dict(slug="bobo-choses", naam="Bobo Choses", col="bobo-choses", icoon="kleding",
  kort="Spaans merk dat elke collectie om een verhaal heen bouwt.",
  aanbod="sokken en rokken uit de lopende collectie",
  tekst=[
   "Bobo Choses uit Barcelona werkt met thema's. Elke collectie krijgt een verhaal, een eigen kleurenpalet en zelfs een animatiefilm, waarna de prints daar allemaal uit voortkomen. Groente die praat, monsters die vriendelijk kijken, zonnen met een gezicht: het is speels zonder kinderachtig te worden.",
   "De pasvorm is recht en ruim, met veel aandacht voor detail aan de binnenkant. Ribboorden, brede halsopeningen en zachte binnenzijden maken de kleding geschikt voor kinderen die zelf willen aan- en uitkleden.",
   "Sokken en accessoires zijn de eenvoudigste manier om met dit merk te beginnen. Ze passen bij vrijwel elke effen outfit en geven een neutrale set direct een eigen toon.",
  ],
  tip="De felle kleuren van Bobo Choses blijven het best op kleur bij een wasbeurt op dertig graden, binnenstebuiten."),

 dict(slug="tiny-cottons", naam="Tiny Cottons", col="tiny-cottons", icoon="kleding",
  kort="Spaans merk met rustige kleuren, fijne kwaliteit en subtiele prints.",
  aanbod="t-shirts, jurken, sweaters, shorts en broeken",
  tekst=[
   "Tiny Cottons is ontstaan in Barcelona en houdt het rustiger dan de meeste kindermerken. De prints zijn klein en vaak grappig bedoeld, de kleuren blijven binnen een palet van gebroken wit, oud roze, olijf en donkerblauw.",
   "Het merk werkt veel met pima-katoen, een katoensoort met een lange vezel die zacht blijft en minder snel gaat pluizen. Dat verschil is vooral merkbaar aan t-shirts en leggings die vaak in de was gaan.",
   "Omdat de kleuren rustig zijn, laat Tiny Cottons zich makkelijk combineren met wat er al in de kast ligt. Een shirt van dit merk past onder een felle jas van een ander merk zonder dat het gaat schreeuwen.",
  ],
  tip="Rustige tinten uit deze collectie werken goed als basis onder de fellere stukken van andere merken."),

 dict(slug="konges-slojd", naam="Konges Sl&oslash;jd", col="konges-slojd", icoon="baby",
  kort="Deens merk voor baby en kind, van rompers tot broodtrommels.",
  aanbod="jassen, jurken, t-shirts, rompers, babykleding, rugzakken en broodtrommels",
  tekst=[
   "Konges Sl&oslash;jd komt uit Denemarken en heeft een herkenbare stijl: zachte tinten, kleine bloemenprints en veel biologisch katoen. Het assortiment loopt van babykleding tot spullen voor de eerste schooldag, waardoor een compleet setje binnen een merk te vinden is.",
   "De babylijn valt op door praktische details: drukknopen in het kruis, omslagen aan de mouw die de handjes bedekken en labels aan de buitenkant. Voor de wat oudere kinderen zijn er rugzakken en broodtrommels in dezelfde kleuren.",
   "De collecties wisselen per seizoen, maar de kleurstelling blijft door de jaren heen consistent. Kleding van twee seizoenen terug past daardoor nog steeds bij de nieuwe stukken.",
  ],
  tip="De rugzakken zijn er in twee formaten; de kleinste is bedoeld voor peuters en zit hoger op de rug."),

 dict(slug="lil-atelier", naam="Lil&rsquo; Atelier", col="lil-atelier", icoon="baby",
  kort="Rustige, gedekte kleuren en natuurlijke stoffen voor baby en kind.",
  aanbod="mutsen, jassen, babyjasjes, longsleeves, rompers, vestjes en jeans",
  tekst=[
   "Lil&rsquo; Atelier is de rustige lijn binnen de Deense familie waar ook Name It onder valt. Waar Name It kleurrijk en direct is, kiest Lil&rsquo; Atelier voor gedekte tinten: zand, salie, roest en gebroken wit, vaak in katoen met een zichtbare structuur.",
   "Het merk heeft een breed babyaanbod. Rompers, vestjes en mutsen sluiten qua kleur op elkaar aan, zodat losse stukken uit verschillende collecties samen toch een set vormen.",
   "Voor kinderen die naar school gaan zijn er jeans, sweaters en jassen in dezelfde kleuren. Dat maakt het merk bruikbaar als basis, met stukken van feller gekleurde merken erbovenop.",
  ],
  tip="Wie een neutrale basis opbouwt, komt met dit merk het verst; de kleuren wisselen per seizoen nauwelijks."),

 dict(slug="name-it", naam="Name It", col="name-it", icoon="kleding",
  kort="Deens merk met een breed basisaanbod voor elke dag.",
  aanbod="jeans, jurken, schoenen, blouses en buitenkleding",
  tekst=[
   "Name It is een Deens merk dat zich richt op de kleding waar elke dag doorheen gaat: jeans, shirts, jurken en buitenkleding. Het merk maakt veel eigen basics en vult die aan met seizoensstukken.",
   "Buitenkleding is een sterk punt. Softshelljassen, regenpakken en gevoerde jassen zijn getest op waterkolom en naden, en de meeste modellen hebben verstelbare mouwen en een capuchon die los kan.",
   "Doordat het aanbod groot is, loopt de pasvorm per lijn uiteen. Jeans vallen aan de smalle kant, sweaters juist ruim.",
  ],
  tip="Regen- en softshellkleding van dit merk gaat langer mee als de rits na het drogen open blijft staan."),

 dict(slug="les-deux", naam="Les Deux", col="les-deux", icoon="kleding",
  kort="Deens merk met een klassieke, sportieve lijn voor jongens.",
  aanbod="caps, t-shirts, longsleeves, hoodies, sweaters en joggingbroeken",
  tekst=[
   "Les Deux komt uit Kopenhagen en begon met herenkleding. De kinderlijn heeft dezelfde toon: rustige kleuren, een klein logo op de borst en stoffen die er na een jaar nog netjes uitzien.",
   "Het aanbod bestaat vooral uit sweatshirts, hoodies, longsleeves en joggingbroeken. De sweaters zijn zwaarder dan gemiddeld, waardoor ze hun vorm houden en niet gaan hangen bij de zakken.",
   "Voor kinderen die niet van drukke prints houden is dit een bruikbaar merk. Een hoodie in donkerblauw of zand past bij vrijwel alles wat er verder in de kast ligt.",
  ],
  tip="De caps hebben een verstelbare sluiting achter en groeien daardoor een aantal seizoenen mee."),

 dict(slug="american-vintage", naam="American Vintage", col="american-vintage", icoon="kleding",
  kort="Frans merk uit Marseille, bekend om zachte gewassen tricot.",
  aanbod="gilets, longsleeves, t-shirts, joggingbroeken, sweaters, vesten en jeans",
  tekst=[
   "American Vintage is een Frans merk uit Marseille. Het bekendste kenmerk is het gewassen tricot: shirts en sweaters voelen vanaf de eerste dag aan alsof ze al vaker gedragen zijn, zonder dat de vorm verloren gaat.",
   "De kleuren zijn gedempt en vaak in verlopen tinten geverfd, waardoor twee stukken uit dezelfde kleurfamilie nooit helemaal gelijk zijn. Dat hoort bij het merk en is geen fout in de verf.",
   "De pasvorm is ruim en lang. Een sweater valt over de heup, mouwen komen tot over de hand. Wie een strakkere pasvorm wil, kan een maat kleiner nemen.",
  ],
  tip="Gewassen tricot blijft het langst mooi als het plat gedroogd wordt en niet in de droger gaat."),

 dict(slug="alix-the-label", naam="ALIX The Label", col="alix-the-label-mini", icoon="kleding",
  kort="Nederlands merk met een uitgesproken, stadse lijn voor meisjes.",
  aanbod="jassen, broeken, sweaters, joggingbroeken, t-shirts, rokken en jeans",
  tekst=[
   "De minilijn van ALIX The Label vertaalt de damescollectie naar kindermaten. Dat betekent uitgesproken stoffen: satijn, ribtricot, imitatieleer en jeans met een bewerkte wassing.",
   "De collectie werkt in setjes. Een joggingbroek en sweater in dezelfde kleur zijn samen een pak, los gedragen passen ze bij de rest van de kast.",
   "Doordat de stoffen wat zwaarder zijn dan bij gemiddelde kinderkleding, houden de modellen hun lijn. Dat maakt de kleding geschikt voor gelegenheden waar een net setje gevraagd wordt, zonder dat het stijf staat.",
  ],
  tip="Satijnen en glanzende stoffen uit deze lijn kunnen het beste binnenstebuiten gewassen worden."),

 dict(slug="piupiuchick", naam="Piupiuchick", col="piupiuchick", icoon="kleding",
  kort="Portugees merk met retro silhouetten en zachte kleuren.",
  aanbod="broeken, blouses, shorts, jeans, sweaters, truien en longsleeves",
  tekst=[
   "Piupiuchick komt uit Portugal en kijkt duidelijk naar kleding van vroeger. Kragen zijn breder, broeken hebben een hoge taille en de prints doen denken aan een schoolfoto uit de jaren zeventig.",
   "Het merk maakt kleding in unisex modellen. Blouses, sweaters en broeken zitten los en zijn niet aan een van beide kanten van de winkel gebonden, wat ze bruikbaar maakt binnen een gezin met meerdere kinderen.",
   "De stoffen zijn overwegend katoen en katoenmengsels met een zichtbare structuur. Ze kreuken wat sneller dan gladde tricot, maar dat past bij het beeld dat het merk zoekt.",
  ],
  tip="De collecties krijgen elk seizoen een naam en een eigen palet; stukken uit dezelfde naam combineren vanzelf."),

 dict(slug="the-new-society", naam="The New Society", col="the-new-society", icoon="kleding",
  kort="Spaans merk met natuurlijke materialen en een rustige lijn.",
  aanbod="shorts, t-shirts, longsleeves, tops, broeken, joggingbroeken en leggings",
  tekst=[
   "The New Society is een Spaans merk dat werkt met natuurlijke materialen: katoen, linnen en wol, vaak in een ongebleekte tint. Het silhouet is ruim en recht, met weinig sluitingen.",
   "De collectie loopt door naar damesmaten, waardoor sommige modellen in het klein en het groot bestaan. Voor gezinnen die dat leuk vinden is dat een van de weinige merken waar dat kan.",
   "De kleuren blijven binnen een smal palet. Dat maakt het merk geschikt als rustige laag onder of over stukken met een print.",
  ],
  tip="Linnen uit deze collectie wordt zachter na elke wasbeurt; strijken hoeft niet."),

 dict(slug="enfant", naam="En Fant", col="enfant", icoon="regen",
  kort="Deens merk met een groot aanbod buitenkleding en basics.",
  aanbod="jeans, blouses, colsjaals, truien, vesten, sweaters, regenlaarzen en jassen",
  tekst=[
   "En Fant is een Deens merk met een breed assortiment: van blouses en truien tot regenlaarzen en winterjassen. Het merk is vooral bekend om buitenkleding die tegen een Noord-Europees seizoen kan.",
   "Regenpakken en laarzen zijn eenvoudig van vorm en ruim gesneden, zodat er een dikke trui onder past. Naden zijn gelast in plaats van gestikt, wat het aantal plekken waar water doorheen kan beperkt.",
   "Daarnaast maakt het merk breigoed en jeans in rustige kleuren, waardoor buiten- en binnenkleding uit hetzelfde merk bij elkaar passen.",
  ],
  tip="Regenlaarzen drogen het snelst met de schacht omgeslagen, zodat er lucht in kan."),

 dict(slug="jollein", naam="Jollein", col="jollein", icoon="baby",
  kort="Nederlands babymerk voor slapen, verzorgen en spelen.",
  aanbod="slaapzakken, rammelaars, speendoekjes, muziekmobielen, bijtringen en babyboekjes",
  tekst=[
   "Jollein is een Nederlands merk dat zich volledig op de eerste jaren richt. Slaapzakken, wikkeldekens, speendoekjes en muziekmobielen vormen de kern van de collectie.",
   "De slaapzakken zijn er in dikte per seizoen. De dunne uitvoering is bedoeld voor een warme kamer, de gewatteerde voor koudere nachten. Halsopening en armsgaten zijn krap gehouden om te voorkomen dat een baby in de zak wegzakt.",
   "Kleuren en dessins lopen door het hele assortiment, zodat een wikkeldeken, een boxkleed en een slaapzak samen een geheel vormen.",
  ],
  tip="Kies de lengte van een slaapzak op de lichaamslengte, niet op de leeftijd van het kind."),

 dict(slug="feetje", naam="Feetje", col="feetje", icoon="baby",
  kort="Nederlands babymerk met veel breigoed en pyjama's.",
  aanbod="babybroekjes, longsleeves, sweaters, pyjama's en breigoed",
  tekst=[
   "Feetje is een Nederlands merk dat al generaties lang babykleding maakt. Het aanbod bestaat uit veel gebreide stukken, boxpakjes en pyjama's in effen kleuren met kleine motieven.",
   "Het merk werkt met een basislijn die het hele jaar leverbaar blijft. Wie een romper of pyjama in een grotere maat wil bijkopen, vindt vaak nog dezelfde kleur.",
   "De pasvorm is ruim rond de buik en smal aan de enkel, wat prettig zit onder een slaapzak.",
  ],
  tip="Gebreide babykleding kan het beste liggend drogen, anders rekken de schouders uit."),

 dict(slug="a-tiny-story", naam="A Tiny Story", col="babyface", icoon="baby",
  kort="Newbornlijn uit Naarden, in maat 50 tot en met 74.",
  aanbod="babybroekjes, longsleeves, vestjes, slofjes, rompers, mutsen en boxpakjes",
  tekst=[
   "A Tiny Story is de newbornlijn van het Nederlandse Babyface uit Naarden en loopt van maat 50 tot en met 74. De collectie is bedoeld voor de eerste maanden en bestaat vooral uit combineerbare stukken in zachte tinten.",
   "Rompers, broekjes en vestjes zijn ontworpen om door elkaar heen te dragen. Binnen een collectie sluiten de kleuren op elkaar aan, zodat een setje ook klopt als de onderdelen op verschillende momenten gekocht zijn.",
   "De stoffen zijn zacht en dun, met platte naden en drukknopen die met een hand te sluiten zijn.",
  ],
  tip="Maat 50 is vaak maar enkele weken bruikbaar; maat 56 als eerste maat is voor veel babies praktischer."),

 dict(slug="stains-and-stories", naam="Stains &amp; Stories", col="stains-stories", icoon="kleding",
  kort="Steviger lijn uit Naarden voor kinderen van maat 80 tot 140.",
  aanbod="longsleeves, tops, t-shirts, broeken, jeans en buitenjassen",
  tekst=[
   "Stains &amp; Stories komt uit dezelfde Naardense familie als Babyface en richt zich op oudere kinderen, van maat 80 tot en met 140. De naam verwijst naar kleding die tegen buitenspelen kan.",
   "De collectie leunt op stevige stoffen: dikkere jersey, canvas en denim, met verstevigde knieen en naden. De kleuren zijn donkerder dan in de babylijnen, wat vlekken minder zichtbaar maakt.",
   "Het silhouet is ruim, met veel joggingbroeken en longsleeves die als basis dienen voor een schooljaar.",
  ],
  tip="Verstevigde knieen zijn te herkennen aan de dubbele stiksels aan de binnenkant van de broekspijp."),

 dict(slug="charlie-petite", naam="Charlie Petite", col="charlie-petite", icoon="kleding",
  kort="Nederlands merk met vrolijke prints en veel jeans.",
  aanbod="jeans, rokken, joggingbroeken, tops, longsleeves, sokken en sweaters",
  tekst=[
   "Charlie Petite maakt kleding met een duidelijk eigen handschrift: veel bloemen, hartjes en tekstprints, gecombineerd met denim in verschillende wassingen.",
   "De jeans zijn een groot deel van de collectie. Ze zijn er in rechte en wijdere modellen, meestal met een verstelbaar elastiek in de band zodat de broek langer past.",
   "Prints en effen stukken uit dezelfde collectie zijn op elkaar afgestemd, wat het combineren makkelijk maakt voor kinderen die zelf hun kleren kiezen.",
  ],
  tip="Een verstelbaar taille-elastiek zit meestal onder een knoopje aan de binnenkant van de band."),

 dict(slug="daily-seven", naam="Daily Seven", col="daily-seven", icoon="kleding",
  kort="Basiskleding voor elke dag, in effen kleuren en losse pasvorm.",
  aanbod="sweaters, shorts, t-shirts, broeken, joggingbroeken, jeans en jurken",
  tekst=[
   "Daily Seven maakt wat de naam belooft: kleding voor zeven dagen per week. Sweaters, t-shirts en joggingbroeken in effen kleuren vormen de kern van de collectie.",
   "De pasvorm is los en de stoffen zijn dik genoeg om regelmatig gewassen te worden zonder dat de kleur snel vervaagt. Boorden aan mouw en enkel zijn breed uitgevoerd.",
   "Omdat de kleuren per seizoen deels terugkeren, is het merk geschikt om een basisgarderobe mee aan te vullen zonder dat het bij elkaar gezocht hoeft te worden.",
  ],
  tip="Effen sweaters in gedekte kleuren zijn de rustigste laag onder een jas met een print."),

 dict(slug="daily-brat", naam="Daily Brat", col="daily-brat", icoon="kleding",
  kort="Zomerse shirts en shorts met grafische prints.",
  aanbod="t-shirts en shorts",
  tekst=[
   "Daily Brat maakt vooral lichte zomerkleding: t-shirts en shorts met grafische prints in heldere kleuren. De prints zijn groot en simpel van vorm, wat goed werkt op een klein kledingstuk.",
   "De stof is dun en luchtig, bedoeld voor warme dagen en voor over zwemkleding. De halsopeningen zijn ruim, zodat een shirt snel over een nat hoofd gaat.",
   "Het aanbod is beperkt van omvang, waardoor de stukken zich eenvoudig laten combineren met basics van andere merken.",
  ],
  tip="Grote opgedrukte prints blijven het langst heel bij wassen op dertig graden en drogen zonder droger."),

 dict(slug="petit-blush", naam="Petit Blush", col="petit-blush", icoon="kleding",
  kort="Zachte tinten, blouses en jumpsuits met oog voor detail.",
  aanbod="jumpsuits, shorts, jasjes, t-shirts, blouses, tops en sweaters",
  tekst=[
   "Petit Blush kiest voor zachte kleuren en verzorgde details: kleine kraagjes, ruches aan de mouw en knoopjes die bij de stof kleuren.",
   "Jumpsuits en blouses vormen het hart van de collectie. Ze zijn bedoeld als een compleet setje in een keer, wat de ochtend eenvoudiger maakt.",
   "Doordat de kleuren licht zijn, komen ze het best tot hun recht bij rustige schoenen en een effen jas.",
  ],
  tip="Lichte tinten blijven mooier als ze apart van donkere kleding gewassen worden."),

 dict(slug="baje-studio", naam="Baje Studio", col="baje-studio", icoon="kleding",
  kort="Jurken, rokken en blouses met een uitgesproken vorm.",
  aanbod="jurken, t-shirts, rokken, blouses, jeans en joggingbroeken",
  tekst=[
   "Baje Studio maakt kleding met een duidelijke vorm: jurken met volume, rokken met een brede zoom en blouses met een opvallende kraag.",
   "De collectie leunt op stoffen met structuur, zoals broderie, ribtricot en denim, waardoor een eenvoudig model toch iets te zien geeft.",
   "Naast de opvallende stukken zijn er basics in dezelfde kleuren, zodat een jurk met volume gedragen kan worden met een rustige legging of shirt eronder.",
  ],
  tip="Een jurk met volume valt het mooist met een strakke laag eronder in dezelfde kleurfamilie."),

 dict(slug="jenest", naam="Jenest", col="jenest", icoon="kleding",
  kort="Rustige zomerkleding met veel aandacht voor pasvorm.",
  aanbod="sokken, shorts, t-shirts, gilets en tops",
  tekst=[
   "Jenest maakt kleding in een smal kleurenpalet: zand, oud roze, olijf en gebroken wit. De collectie is compact en bestaat uit stukken die onderling te combineren zijn.",
   "Shorts en t-shirts hebben een rustige pasvorm zonder overbodige details, waardoor ze zich makkelijk laten mengen met kleding van andere merken.",
   "De kleuren blijven per seizoen dicht bij elkaar, wat het merk geschikt maakt om een basis mee uit te bouwen.",
  ],
  tip="Sokken in dezelfde kleurfamilie als de broek maken een outfit visueel langer."),

 dict(slug="bruno-bruno-nation", naam="Bruno Bruno Nation", col="bruno-bruno-nation", icoon="kleding",
  kort="Sportief en ruim, met sweatpants, hoodies en jackets.",
  aanbod="longsleeves, tops, t-shirts, broeken, shorts, jassen, sweatpants en sweaters",
  tekst=[
   "Bruno Bruno Nation richt zich op sportieve kleding: sweatpants, hoodies, t-shirts en jacks in een ruime pasvorm.",
   "De stukken zijn eenvoudig van vorm en werken in lagen. Een longsleeve onder een t-shirt of een hoodie onder een jack is de manier waarop de collectie bedoeld is.",
   "De kleuren zijn overwegend gedekt, met hier en daar een fel accent in een logo of bies.",
  ],
  tip="Sweatpants met een boord aan de enkel blijven beter zitten op een step of fiets."),

 dict(slug="jelly-mallow", naam="Jelly Mallow", col="jelly-mallow", icoon="kleding",
  kort="Koreaans merk met vrolijke, grafische kinderkleding.",
  aanbod="blouses, broeken, leggings, t-shirts, longsleeves, rokken en shorts",
  tekst=[
   "Jelly Mallow is een Koreaans merk. De prints zijn groot en grafisch, met veel fruit, gezichten en simpele vormen in heldere kleuren.",
   "De pasvorm is ruim en de stoffen zijn zacht. Broeken hebben meestal een volledige elastische band, wat handig is voor kinderen die zichzelf aankleden.",
   "Een enkel stuk uit deze collectie is genoeg om een verder rustige outfit vrolijk te maken.",
  ],
  tip="Bij een groot printshirt werkt een effen broek in een kleur uit de print zelf het beste."),

 dict(slug="sproet-en-sprout", naam="Sproet &amp; Sprout", col="sproet-sprout", icoon="kleding",
  kort="Vrolijke prints met een knipoog naar vroeger.",
  aanbod="leggings, sokken, rokken, sweaters, zwemkleding en t-shirts",
  tekst=[
   "Sproet &amp; Sprout maakt kleding met kleine, vrolijke prints en veel gele en groene tinten. De stijl heeft iets ouderwets zonder oubollig te worden.",
   "De collectie bestaat uit korte reeksen die elkaar snel opvolgen, met per reeks een eigen thema. Losse stukken uit verschillende reeksen combineren goed omdat de kleuren dicht bij elkaar blijven.",
   "Leggings en sokken zijn de meest gedragen stukken en zijn stevig genoeg voor dagelijks gebruik.",
  ],
  tip="Een gekleurde legging is de eenvoudigste manier om een effen jurk of tuniek af te maken."),

 dict(slug="labo-de-colores", naam="Labo de Colores", col="labo-de-colores", icoon="kleding",
  kort="Kleine collectie met denim, rokken en jurken.",
  aanbod="denim, rokken, jurken, t-shirts en truien",
  tekst=[
   "Labo de Colores heeft een compacte collectie waarin denim de hoofdrol speelt, aangevuld met rokken, jurken en truien.",
   "De stukken zijn eenvoudig van vorm en bedoeld om lang mee te gaan. Denim wordt in verschillende wassingen aangeboden, van bijna onbewerkt tot lichter gewassen.",
   "Doordat de collectie klein is, sluiten de kleuren onderling goed aan.",
  ],
  tip="Onbewerkt denim geeft de eerste wasbeurten wat kleur af; apart wassen is dan verstandig."),
]

MERKEN += [
 dict(slug="hvid", naam="Hvid", col="hvid", icoon="baby",
  kort="Gebreide slofjes, slaapzakken en dekens van merinowol.",
  aanbod="babyslofjes, gebreide slaapzakken en accessoires van merinowol",
  tekst=[
   "Hvid werkt vrijwel uitsluitend met merinowol. Die vezel is fijner dan gewone schapenwol, kriebelt daardoor nauwelijks en houdt warm zonder dat een baby oververhit raakt.",
   "De collectie bestaat uit slofjes, mutsjes, dekens en gebreide slaapzakken in ongeverfde of licht geverfde tinten. Het breisel is los, waardoor lucht door de steken kan.",
   "Merinowol hoeft zelden gewassen te worden. Luchten is meestal genoeg, wat het onderhoud van deze stukken eenvoudig maakt.",
  ],
  tip="Merinowol wassen op het wolprogramma met wolwasmiddel; nooit in de droger."),

 dict(slug="hello-hossy", naam="Hello Hossy", col="hello-hossy", icoon="accessoires",
  kort="Frans merk met petten, tassen en zonnebrillen.",
  aanbod="petten, zonnebrillen, rugzakken en sporttassen",
  tekst=[
   "Hello Hossy is een Frans merk dat begon met petten en het assortiment uitbreidde met tassen, zonnebrillen en sneakers.",
   "De petten hebben een klep die stevig genoeg is om vorm te houden en een sluiting achter die meegroeit. Kleur en print wisselen per collectie, van effen tot bloemenmotieven.",
   "De rugzakken zijn compact en licht, bedoeld voor een beker en een broodtrommel en niet voor een volle schooldag.",
  ],
  tip="Een pet houdt zijn vorm het best als hij niet in de wasmachine gaat maar met de hand wordt schoongemaakt."),

 dict(slug="mimi-en-lula", naam="Mimi &amp; Lula", col="mimi-lula-1", icoon="accessoires",
  kort="Brits merk met haarspeldjes, elastiekjes en toverstaffen.",
  aanbod="haarknipjes, haarelastieken, tassen, sieraden, toverstaffen en rokken",
  tekst=[
   "Mimi &amp; Lula is een Brits merk dat vooral bekend is om haaraccessoires: speldjes in de vorm van dieren, elastiekjes met bloemen en diademen.",
   "De accessoires worden in setjes verkocht, wat handig is omdat speldjes nu eenmaal kwijtraken. De clips zijn van metaal met een kunststof figuur erop.",
   "Naast haaraccessoires maakt het merk verkleedspullen zoals toverstaffen en vleugels, in dezelfde vrolijke stijl.",
  ],
  tip="Kleine clips zijn bedoeld voor fijn haar; de grotere klemmen houden dikkere staarten beter vast."),

 dict(slug="studio-noos", naam="Studio Noos", col="studio-noos", icoon="tassen",
  kort="Nederlands merk met teddytassen en hydrofiele doeken.",
  aanbod="tassen, rugtassen en hydrofiele doeken",
  tekst=[
   "Studio Noos uit Nederland is bekend geworden met tassen van teddystof: zacht, licht en ruim genoeg voor een dag met kinderen.",
   "Naast de grote schoudertassen zijn er kleine crossbodymodellen voor kinderen zelf, in dezelfde stof en kleuren.",
   "De hydrofiele doeken van het merk zijn dun geweven en drogen snel, waardoor ze bruikbaar zijn als spuugdoek, zonnescherm over de kinderwagen of licht dekentje.",
  ],
  tip="Teddystof laat pluis los in de eerste weken; even uitschudden voor gebruik scheelt."),

 dict(slug="donsje-amsterdam", naam="Donsje Amsterdam", col="donsje-amsterdam", icoon="accessoires",
  kort="Amsterdams merk met leren schoentjes en handgemaakte details.",
  aanbod="tassen, blouses, gilets, jurken, rokken, leggings, sweaters en vesten",
  tekst=[
   "Donsje Amsterdam begon met leren babyschoentjes met een diertje erop en is uitgegroeid naar een volledige collectie kleding en accessoires.",
   "Het handwerk is het kenmerk: applicaties worden per stuk aangebracht, waardoor geen twee exemplaren precies gelijk zijn. Het merk laat zien in welke werkplaatsen dat gebeurt.",
   "De kleding is rustig van kleur, met de accessoires als opvallend element. Een eenvoudige outfit met een tas of schoen van dit merk is een compleet beeld.",
  ],
  tip="Leren schoentjes blijven soepel met een beetje kleurloze schoencreme, ook bij babymaten."),

 dict(slug="fushi-amsterdam", naam="Fushi Amsterdam", col="fushi-amsterdam", icoon="sieraden",
  kort="Kettingen en fijne sieraden voor kinderen en volwassenen.",
  aanbod="kettingen en fijne sieraden",
  tekst=[
   "Fushi Amsterdam maakt fijne sieraden in kleine maten, geschikt voor kinderen maar ook draagbaar door volwassenen.",
   "De collectie bestaat vooral uit kettingen met een klein hangertje: een letter, een hart of een steen. De sluitingen zijn licht uitgevoerd zodat ze bij een flinke ruk loslaten.",
   "Sieraden zijn een van de weinige cadeaus die met de leeftijd meegaan; een korte ketting wordt later een armband.",
  ],
  tip="Bewaar fijne kettingen los van elkaar, dan blijven ze knoopvrij."),

 dict(slug="bibi-en-camille", naam="Bibi &amp; Camille", col="bibi-camille", icoon="sieraden",
  kort="Oorbellen en kleine sieraden in overzichtelijke setjes.",
  aanbod="oorbellen",
  tekst=[
   "Bibi &amp; Camille maakt oorbellen in kleine maten en eenvoudige vormen: rondjes, sterretjes, hartjes en bloemen.",
   "De sluitingen zijn klein uitgevoerd, wat prettig zit onder een muts of helm.",
   "Doordat de modellen eenvoudig zijn, blijven ze bruikbaar als een kind ouder wordt en de rest van de garderobe verandert.",
  ],
  tip="Voor pas gezette oorgaatjes zijn gladde, kleine modellen zonder uitsteeksels het prettigst."),

 dict(slug="jellycat", naam="Jellycat", col="jellycat", icoon="speelgoed",
  kort="Britse knuffels met een herkenbare, zachte pluche.",
  aanbod="knuffels in verschillende formaten",
  tekst=[
   "Jellycat is een Brits merk dat knuffels maakt in een pluche die duidelijk anders aanvoelt dan gemiddeld: langharig, soepel en zwaar genoeg om te blijven liggen.",
   "Het assortiment loopt van klassieke konijnen tot groenten met een gezicht. Elk model bestaat in meerdere formaten, wat handig is als er een reserve-exemplaar nodig is.",
   "De ogen en neuzen zijn geborduurd in plaats van vastgezet met kunststof onderdelen, waardoor de knuffels ook voor de allerkleinsten geschikt zijn.",
  ],
  tip="Een reserve-knuffel meewassen met de originele zorgt dat beide er hetzelfde uit gaan zien."),

 dict(slug="maileg", naam="Maileg", col="maileg", icoon="speelgoed",
  kort="Deense muizen, huisjes en accessoires om mee te spelen.",
  aanbod="muizen en bijbehorende accessoires",
  tekst=[
   "Maileg uit Denemarken maakt kleine textielfiguren, vooral muizen, met bijpassende kleding, meubels en doosjes.",
   "De figuren worden verkocht in een doosje dat als bed dienstdoet. Kleding en accessoires zijn los verkrijgbaar, waardoor een verzameling in jaren kan groeien.",
   "De maten zijn onderling afgestemd: kleding van de ene muis past op een andere van hetzelfde formaat.",
  ],
  tip="De muizen zijn niet wasbaar in de machine; oppervlakkig reinigen houdt de kleding heel."),

 dict(slug="micro", naam="Micro", col="micro-step", icoon="buiten",
  kort="Zwitserse steppen voor peuters tot pubers.",
  aanbod="steppen, accessoires en sokken",
  tekst=[
   "Micro is een Zwitsers merk dat steppen maakt in leeftijdsgebonden modellen. De kleinste heeft drie wielen en stuurt door leunen, de grotere twee wielen en een gewoon stuur.",
   "Onderdelen zijn los te vervangen: wielen, remmen en sturen. Een step gaat daardoor vaak door meerdere kinderen in een gezin.",
   "De vouwmodellen zijn bedoeld voor korte ritten en passen ingeklapt in een fietstas of onder een kinderwagen.",
  ],
  tip="Wielen die scheef aflopen zijn los te vervangen zonder de hele step te vervangen."),

 dict(slug="rice", naam="Rice", col="rice", icoon="interieur",
  kort="Deens merk met kleurrijk melamine en textiel.",
  aanbod="wiegdekens, bekers en servies",
  tekst=[
   "Rice uit Denemarken staat bekend om kleur. Het servies van melamine is stevig, lichtgewicht en valt zonder te breken, wat het geschikt maakt voor kinderhanden.",
   "Naast servies maakt het merk textiel zoals dekentjes en manden, in dezelfde felle tinten en met vrolijke motieven.",
   "Melamine hoort niet in de magnetron. Afwassen in de machine kan wel, mits op een programma dat niet te heet wordt.",
  ],
  tip="Melamine blijft het langst mooi op het bovenste rek van de vaatwasser."),

 dict(slug="your-wishes", naam="Your Wishes", col="your-wishes-1", icoon="baby",
  kort="Babykleding in effen tinten met kleine, grafische prints.",
  aanbod="babybroekjes, longsleeves, rompers, mutsjes, speenkoorden en sokjes",
  tekst=[
   "Your Wishes maakt babykleding in een rustig kleurenpalet met kleine grafische prints, vaak niet meer dan een streep of een stip.",
   "De collectie bestaat uit losse stukken die als set werken: een romper, een broekje en een mutsje in dezelfde tint.",
   "De stof is zacht katoen met wat rek, waardoor een romper langer past dan de maat doet vermoeden.",
  ],
  tip="Een speenkoord hoort kort te zijn; te lange koorden zijn niet veilig in bed."),
]

# Merken zonder eigen pagina, wel op het overzicht
KORT = [
 ("Alwero", "alwero", "Poolse wolproducten, waaronder sloffen van vilt en wol."),
 ("Atelier Pomme", "atelier-pomme", "Speendoekjes en kleine babyspullen in zachte tinten."),
 ("Emile et Ida", "emile-et-ida", "Frans merk met truien, sweaters en sandalen in klassieke vormen."),
 ("Goldie + Ace", "goldie-ace", "Australisch merk met vrolijke, eenvoudige kinderkleding."),
 ("Moonie", "moonie", "Slaapknuffels met een nachtlampje en zachte ruis."),
 ("Navy Natural", "navy-natural", "Kleine collectie rokken, broeken en tops in natuurlijke tinten."),
 ("Ratatam", "ratatam", "Franse ballen in vrolijke kleuren en formaten."),
 ("Salted Stories", "salted-stories", "Zwemkleding voor het strand en het zwembad."),
 ("Vondels", "vondels", "Nederlandse glaskunst, van bekers tot decoratie."),
]
