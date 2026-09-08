# topkidsfashion.nl

Statische gids over kindermode. De site wordt gegenereerd met Python zonder externe pakketten.

## Bouwen

    python3 build.py

De site komt in `dist/`. Daarna controleren met:

    python3 check.py

check.py controleert interne links, ankerteksten, aanspreekvormen, kostenwoorden,
dubbele titels en meta-omschrijvingen, en de sitemap.

## Opbouw

- `core.py` paginaschil, navigatie, opmaak en het wegschrijven van dist
- `art.py` eigen tekeningen en merkemblemen in SVG
- `video.py` merkvideo's, geladen na een klik
- `content_merken.py` merkgegevens
- `content_stijl.py` artikelen over combineren en opbouwen
- `content_maten.py` maattabellen
- `content_materialen.py` materialen, keurmerken en onderhoud
- `content_seizoen.py` kleding per seizoen
