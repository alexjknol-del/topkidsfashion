# -*- coding: utf-8 -*-
"""Merkvideo's. Pas na een klik wordt er een iframe geladen, dus geen extern
verzoek zolang de bezoeker niets aanklikt."""

# (merkslug, video-id, Nederlandse omschrijving, kanaalnaam)
VIDEOS = [
    ("mini-rodini", "bvMk-rHEPXM", "Mini Rodini laat de Field Notes-collectie voor herfst en winter zien", "Mini Rodini"),
    ("mini-rodini", "8izHmUHk578", "Camp Rodini, de pre-collectie voor herfst en winter", "Mini Rodini"),
    ("mini-rodini", "_BEO9p8H33w", "Agatha, een film bij de herfstcollectie", "Mini Rodini"),
    ("bobo-choses", "1ySGaHL-stE", "Pickles, de zomercollectie voor kinderen en baby's", "Bobo Choses"),
    ("bobo-choses", "GiCuLK_9juQ", "Een geanimeerd prentenboek bij de zomercollectie", "Bobo Choses"),
    ("bobo-choses", "XW1v9tbmOb8", "All About Monsters, geanimeerd boek bij de winterlijn", "Bobo Choses"),
    ("tiny-cottons", "84jHjTxrjvI", "Een korte film bij de herfst- en wintercollectie", "tinycottons"),
    ("tiny-cottons", "ze_yXt21m6U", "De collectie Face Your Faces in beeld", "tinycottons"),
    ("maileg", "6lFMbFr5dHg", "LouiMax droomt ervan groot te zijn, een korte film voor kinderen", "Maileg"),
    ("maileg", "gEwNtjGQbZ0", "Grote schoonmaak in het muizenhuis", "Maileg"),
    ("name-it", "0oDotfV6UJ8", "Winterjassen van dichtbij bekeken", "NAME IT"),
    ("name-it", "Hna_-2AJSZA", "Softshell en regenkleding in beeld", "NAME IT"),
    ("les-deux", "1q7skgnKgB8", "De creatief directeur over de herfstcollectie", "Les Deux"),
    ("les-deux", "zjIXqtTyZnY", "De creatief directeur over de zomercollectie", "Les Deux"),
    ("american-vintage", "HiLi2WdckfY", "Made in Marseille, een portret van het merk", "American Vintage"),
    ("american-vintage", "VmCeNTIvmSk", "De film bij de voorjaars- en zomercollectie", "American Vintage"),
    ("jollein", "o67gxr-LHck", "Hoe een voetenzak wordt gebruikt", "Jollein Official"),
    ("jollein", "1o3UPQH-rPc", "Een wikkeldeken stap voor stap", "Jollein Official"),
    ("feetje", "ebYUfai_SCk", "Breigoed uit de basiscollectie", "Feetje"),
    ("donsje-amsterdam", "GxN6J-xxJB8", "Een kijkje in een van de werkplaatsen", "Donsje Amsterdam"),
    ("donsje-amsterdam", "iAqwO1I5oMk", "De voorjaars- en zomercollectie in beeld", "Donsje Amsterdam"),
    ("micro-step", "zfIzZo6ouDo", "De Pedalflow, een opvouwbare fiets van Micro", "Micro Mobility Official"),
    ("micro-step", "C8UmEyh1MEo", "Mini en Maxi Micro Deluxe met verlichte wielen", "Micro Mobility Official"),
    ("studio-noos", "Y1Zk4ojpLqo", "De nieuwste tas uit de familie", "Studio Noos"),
    ("studio-noos", "6NOHuklooJ4", "De mini crossbody van dichtbij", "Studio Noos"),
    ("hello-hossy", "CosV-uTjXwY", "De tassen uit de collectie van 2025", "Hello Hossy"),
    ("hello-hossy", "xMQRnY_VZE4", "De tassen uit de collectie van 2026", "Hello Hossy"),
    ("hello-hossy", "fA6vrn1uaUs", "De sneakers uit de collectie van 2026", "Hello Hossy"),
    ("piupiuchick", "XN5huNHhmb8", "I'm with the Band, de herfst- en wintercollectie", "Piupiuchick"),
    ("piupiuchick", "6H3T_D6fYKA", "My First Love, de voorjaars- en zomercollectie", "Piupiuchick"),
    ("piupiuchick", "pZ6umlcP6Xg", "Vida Bonita, een eerdere wintercollectie", "Piupiuchick"),
    ("the-new-society", "8t9HArgW0EE", "Ode to an Endless Summer, de zomercollectie", "The New Society"),
    ("the-new-society", "GaYEmnWFlPo", "Artemisa, een voorjaarscollectie", "The New Society"),
    ("the-new-society", "932QwSQL6XA", "It's Written in the Stars, de wintercollectie", "The New Society"),
    ("alix-the-label-mini", "hM4MDHikUT4", "Cape Town Chronicles, de zomercampagne", "ALIX The Label"),
    ("alix-the-label-mini", "u6wn3F22y9o", "Marrakesh Adventure, een eerdere campagne", "ALIX The Label"),
    ("sproet-sprout", "TLO09sbHv3A", "Een korte introductie van het merk", "Sproet & Sprout"),
    ("sproet-sprout", "OuyrwF49aJU", "De zomercollectie is online", "Sproet & Sprout"),
    ("sproet-sprout", "Rrs1IvAf5IM", "De capsulecollectie rond Mickey Mouse", "Sproet & Sprout"),
]


def speler(vid, tekst, kanaal):
    return (
        '<div class="video">'
        '<button class="doek" data-id="%s" data-titel="%s" aria-label="Video afspelen: %s">'
        '<span class="knop"></span></button>'
        '<div class="bij"><b>%s</b><span>Kanaal %s &middot; de video wordt pas geladen na een klik</span></div>'
        '</div>' % (vid, tekst.replace('"', "&quot;"), tekst.replace('"', "&quot;"), tekst, kanaal)
    )


def voor(slug, maximaal=3):
    rij = [v for v in VIDEOS if v[0] == slug][:maximaal]
    if not rij:
        return ""
    kaarten = "".join(speler(v[1], v[2], v[3]) for v in rij)
    kop = "<h2>Beeld van het merk</h2>"
    return kop + '<div class="rooster k2">%s</div>' % kaarten
