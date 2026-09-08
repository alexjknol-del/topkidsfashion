# -*- coding: utf-8 -*-
"""Eigen tekeningen in SVG. Geen externe bestanden, alles staat inline in de pagina."""

K = "#c2573f"   # klei
S = "#6f8b6a"   # salie
Z = "#e3a63c"   # zon
I = "#241f1b"   # inkt
P = "#f4ece2"   # papier
W = "#fffdfa"


def _wrap(vb, body, klas=""):
    return '<svg viewBox="%s" role="img" class="%s" xmlns="http://www.w3.org/2000/svg">%s</svg>' % (vb, klas, body)


def rek():
    """Kledingrek met drie kledingstukken."""
    b = f'''
<rect width="400" height="240" fill="{P}"/>
<line x1="40" y1="52" x2="360" y2="52" stroke="{I}" stroke-width="4" stroke-linecap="round"/>
<line x1="60" y1="52" x2="60" y2="212" stroke="{I}" stroke-width="4"/>
<line x1="340" y1="52" x2="340" y2="212" stroke="{I}" stroke-width="4"/>
<path d="M120 52c0 8-6 10-6 14" stroke="{I}" stroke-width="3" fill="none"/>
<path d="M96 78h48l16 22-14 8-6-8v56H100v-56l-6 8-14-8z" fill="{K}"/>
<path d="M200 52c0 8-6 10-6 14" stroke="{I}" stroke-width="3" fill="none"/>
<path d="M176 78h44l6 20-12 6v58h-38v-58l-12-6z" fill="{S}"/>
<circle cx="198" cy="86" r="5" fill="{W}"/>
<path d="M280 52c0 8-6 10-6 14" stroke="{I}" stroke-width="3" fill="none"/>
<path d="M254 80h44v34l-8 48h-10l-4-34-4 34h-10l-8-48z" fill="{Z}"/>
<circle cx="90" cy="212" r="7" fill="{I}"/><circle cx="310" cy="212" r="7" fill="{I}"/>
'''
    return _wrap("0 0 400 240", b)


def trui():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<path d="M56 62h88l30 26-18 20-12-10v62H56v-62l-12 10-18-20z" fill="{K}"/>
<path d="M78 62c0 12 10 20 22 20s22-8 22-20" fill="none" stroke="{W}" stroke-width="5"/>
<path d="M62 120h76" stroke="{W}" stroke-width="4" stroke-dasharray="10 9"/>
<path d="M62 136h76" stroke="{W}" stroke-width="4" stroke-dasharray="10 9"/>
'''
    return _wrap("0 0 200 200", b)


def tuinbroek():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<path d="M70 40l14 20h32l14-20 8 6-14 26v92h-38v-56h-6v56H42v-92L28 46z" fill="{S}" transform="translate(30,0)"/>
<rect x="86" y="76" width="30" height="24" rx="4" fill="{W}"/>
<circle cx="78" cy="72" r="5" fill="{Z}"/><circle cx="124" cy="72" r="5" fill="{Z}"/>
'''
    return _wrap("0 0 200 200", b)


def laarsjes():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<path d="M52 54h30v66l24 10v18H52z" fill="{Z}"/>
<path d="M118 54h30v66l24 10v18h-54z" fill="{K}"/>
<rect x="46" y="148" width="66" height="12" rx="6" fill="{I}"/>
<rect x="112" y="148" width="66" height="12" rx="6" fill="{I}"/>
<path d="M52 74h30M118 74h30" stroke="{W}" stroke-width="4"/>
'''
    return _wrap("0 0 200 200", b)


def regen():
    b = f'''
<rect width="400" height="220" fill="{P}"/>
<path d="M150 44h100l34 30-20 22-14-12v92H150v-92l-14 12-20-22z" fill="{Z}"/>
<path d="M172 44c0 14 12 22 28 22s28-8 28-22" fill="none" stroke="{W}" stroke-width="5"/>
<rect x="186" y="96" width="28" height="34" rx="5" fill="{W}"/>
<g stroke="{S}" stroke-width="5" stroke-linecap="round">
<path d="M60 40l-8 26M92 66l-8 26M56 104l-8 26M330 48l-8 26M356 84l-8 26M318 120l-8 26"/></g>
<path d="M40 190h320" stroke="{I}" stroke-width="4" stroke-linecap="round"/>
<ellipse cx="120" cy="190" rx="26" ry="6" fill="{S}" opacity=".5"/>
<ellipse cx="286" cy="190" rx="20" ry="5" fill="{S}" opacity=".5"/>
'''
    return _wrap("0 0 400 220", b)


def maatladder():
    b = f'''
<rect width="400" height="220" fill="{P}"/>
<line x1="46" y1="30" x2="46" y2="190" stroke="{I}" stroke-width="4"/>
'''
    y = 46
    hoogtes = [("50", 26), ("74", 40), ("92", 52), ("110", 66), ("134", 82), ("152", 96), ("176", 112)]
    for label, hh in hoogtes:
        b += f'<line x1="40" y1="{y}" x2="58" y2="{y}" stroke="{I}" stroke-width="3"/>'
        b += f'<text x="12" y="{y+5}" font-size="13" fill="{I}" font-family="Georgia,serif">{label}</text>'
        b += f'<rect x="78" y="{y-9}" width="{hh*2}" height="18" rx="9" fill="{K if int(label)%3==0 else S}" opacity=".85"/>'
        y += 21
    b += f'<text x="78" y="206" font-size="13" fill="#6d635a" font-family="Georgia,serif">maat in centimeters lichaamslengte</text>'
    return _wrap("0 0 400 220", b)


def kleurenwaaier():
    kleuren = [K, Z, S, "#8d6e8a", "#3f6b7d", "#d9a08c", "#2f3b30"]
    b = f'<rect width="400" height="180" fill="{P}"/>'
    x = 30
    for i, c in enumerate(kleuren):
        h = 90 + (i % 3) * 22
        b += f'<rect x="{x}" y="{150-h}" width="38" height="{h}" rx="10" fill="{c}"/>'
        x += 50
    b += f'<line x1="20" y1="152" x2="380" y2="152" stroke="{I}" stroke-width="3" stroke-linecap="round"/>'
    return _wrap("0 0 400 180", b)


def wolvezel():
    b = f'''
<rect width="400" height="200" fill="{P}"/>
<path d="M30 130c30-60 70-60 100 0s70 60 100 0 70-60 100 0" fill="none" stroke="{S}" stroke-width="7" stroke-linecap="round"/>
<path d="M30 156c30-60 70-60 100 0s70 60 100 0 70-60 100 0" fill="none" stroke="{K}" stroke-width="5" stroke-linecap="round" opacity=".75"/>
<circle cx="86" cy="62" r="26" fill="{W}" stroke="{I}" stroke-width="3"/>
<circle cx="120" cy="52" r="18" fill="{W}" stroke="{I}" stroke-width="3"/>
<path d="M300 40c22 0 34 16 34 32s-14 26-34 26-34-10-34-26 12-32 34-32z" fill="{Z}" opacity=".85"/>
'''
    return _wrap("0 0 400 200", b)


def wasmachine():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<rect x="34" y="34" width="132" height="132" rx="16" fill="{W}" stroke="{I}" stroke-width="4"/>
<circle cx="100" cy="112" r="40" fill="{P}" stroke="{I}" stroke-width="4"/>
<path d="M64 112c14-12 22 12 36 0s22 12 36 0" fill="none" stroke="{S}" stroke-width="5"/>
<circle cx="56" cy="56" r="6" fill="{K}"/><circle cx="78" cy="56" r="6" fill="{Z}"/>
<rect x="112" y="50" width="42" height="12" rx="6" fill="{P}"/>
'''
    return _wrap("0 0 200 200", b)


def seizoenen():
    b = f'''
<rect width="400" height="200" fill="{P}"/>
<circle cx="70" cy="100" r="42" fill="{S}" opacity=".9"/>
<path d="M70 74v52M52 96l18 10 18-10" stroke="{W}" stroke-width="5" fill="none" stroke-linecap="round"/>
<circle cx="170" cy="100" r="42" fill="{Z}" opacity=".9"/>
<circle cx="170" cy="100" r="16" fill="{W}"/>
<g stroke="{W}" stroke-width="4" stroke-linecap="round"><path d="M170 68v-8M170 140v8M138 100h-8M202 100h8M148 78l-6-6M192 122l6 6M192 78l6-6M148 122l-6 6"/></g>
<circle cx="270" cy="100" r="42" fill="{K}" opacity=".9"/>
<path d="M270 76c10 8 16 18 8 30-6 9-18 10-24 2-7-10 2-24 16-32z" fill="{W}"/>
<circle cx="370" cy="100" r="42" fill="#5d7a8c" opacity=".9"/>
<g stroke="{W}" stroke-width="4" stroke-linecap="round"><path d="M370 76v48M350 88l40 24M390 88l-40 24"/></g>
'''
    return _wrap("0 0 400 200", b)


def kast():
    b = f'''
<rect width="400" height="240" fill="{P}"/>
<rect x="40" y="30" width="320" height="180" rx="12" fill="{W}" stroke="{I}" stroke-width="4"/>
<line x1="200" y1="30" x2="200" y2="210" stroke="{I}" stroke-width="4"/>
<line x1="56" y1="86" x2="184" y2="86" stroke="{I}" stroke-width="3"/>
<line x1="216" y1="130" x2="344" y2="130" stroke="{I}" stroke-width="3"/>
<rect x="66" y="96" width="26" height="46" rx="6" fill="{K}"/>
<rect x="100" y="96" width="26" height="46" rx="6" fill="{S}"/>
<rect x="134" y="96" width="26" height="46" rx="6" fill="{Z}"/>
<rect x="60" y="152" width="120" height="46" rx="8" fill="{P}" stroke="{I}" stroke-width="3"/>
<rect x="226" y="44" width="44" height="72" rx="8" fill="{S}" opacity=".8"/>
<rect x="282" y="44" width="44" height="72" rx="8" fill="{K}" opacity=".8"/>
<rect x="226" y="146" width="100" height="48" rx="8" fill="{P}" stroke="{I}" stroke-width="3"/>
<circle cx="190" cy="120" r="5" fill="{I}"/><circle cx="210" cy="120" r="5" fill="{I}"/>
'''
    return _wrap("0 0 400 240", b)


def naaimachine():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<path d="M34 140h132v20H34z" fill="{I}"/>
<path d="M46 60h84v52H60z" fill="{K}"/>
<rect x="46" y="112" width="108" height="28" rx="6" fill="{W}" stroke="{I}" stroke-width="3"/>
<path d="M130 60h24v52" stroke="{I}" stroke-width="6" fill="none"/>
<line x1="142" y1="112" x2="142" y2="134" stroke="{S}" stroke-width="4"/>
<circle cx="58" cy="52" r="10" fill="{Z}"/>
'''
    return _wrap("0 0 200 200", b)


def cirkelkind():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<circle cx="100" cy="72" r="30" fill="{Z}"/>
<path d="M70 66c0-22 60-22 60 0" fill="{K}"/>
<circle cx="90" cy="76" r="3.5" fill="{I}"/><circle cx="110" cy="76" r="3.5" fill="{I}"/>
<path d="M92 88c5 5 11 5 16 0" stroke="{I}" stroke-width="3" fill="none" stroke-linecap="round"/>
<path d="M64 174v-34c0-20 16-32 36-32s36 12 36 32v34z" fill="{S}"/>
<path d="M84 112h32" stroke="{W}" stroke-width="4"/>
'''
    return _wrap("0 0 200 200", b)


def hanger():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<path d="M100 52c-9 0-14 6-14 12 0 5 3 8 7 10L40 112c-6 4-4 12 4 12h112c8 0 10-8 4-12l-53-38c4-2 7-5 7-10 0-6-5-12-14-12z" fill="none" stroke="{I}" stroke-width="5" stroke-linejoin="round"/>
<circle cx="100" cy="42" r="7" fill="{K}"/>
<path d="M60 140h80" stroke="{S}" stroke-width="6" stroke-linecap="round"/>
'''
    return _wrap("0 0 200 200", b)


def tas():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<path d="M52 78h96l10 88H42z" fill="{K}"/>
<path d="M76 78V64c0-14 10-22 24-22s24 8 24 22v14" fill="none" stroke="{I}" stroke-width="5"/>
<circle cx="100" cy="116" r="12" fill="{W}"/>
'''
    return _wrap("0 0 200 200", b)


def knuffel():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<circle cx="66" cy="60" r="18" fill="{Z}"/><circle cx="134" cy="60" r="18" fill="{Z}"/>
<circle cx="100" cy="88" r="42" fill="{Z}"/>
<circle cx="86" cy="82" r="4.5" fill="{I}"/><circle cx="114" cy="82" r="4.5" fill="{I}"/>
<ellipse cx="100" cy="98" rx="14" ry="10" fill="{W}"/>
<circle cx="100" cy="94" r="4" fill="{I}"/>
<path d="M68 132c0 26 64 26 64 0" fill="{K}"/>
<rect x="66" y="130" width="68" height="42" rx="18" fill="{K}"/>
'''
    return _wrap("0 0 200 200", b)


def step():
    b = f'''
<rect width="200" height="200" fill="{P}"/>
<circle cx="56" cy="150" r="20" fill="none" stroke="{I}" stroke-width="6"/>
<circle cx="150" cy="150" r="20" fill="none" stroke="{I}" stroke-width="6"/>
<path d="M56 150h80" stroke="{K}" stroke-width="8" stroke-linecap="round"/>
<path d="M136 150L146 60" stroke="{I}" stroke-width="7" stroke-linecap="round"/>
<path d="M124 58h40" stroke="{S}" stroke-width="8" stroke-linecap="round"/>
'''
    return _wrap("0 0 200 200", b)


def sterren():
    b = f'''
<rect width="400" height="120" fill="{P}"/>
<g fill="{Z}"><circle cx="60" cy="60" r="9"/><circle cx="140" cy="40" r="6"/><circle cx="210" cy="70" r="11"/>
<circle cx="290" cy="44" r="7"/><circle cx="350" cy="74" r="9"/></g>
<path d="M20 100c60-30 120 20 180-10s120 10 180-20" fill="none" stroke="{S}" stroke-width="5" stroke-linecap="round"/>
'''
    return _wrap("0 0 400 120", b)


ICONEN = {
    "kleding": trui,
    "baby": cirkelkind,
    "schoenen": laarsjes,
    "accessoires": hanger,
    "tassen": tas,
    "speelgoed": knuffel,
    "interieur": kast,
    "sieraden": sterren,
    "buiten": step,
    "regen": regen,
}


def icoon(soort):
    return ICONEN.get(soort, trui)()


# ---------------------------------------------------------------- emblemen
PALET = ["#c2573f", "#6f8b6a", "#e3a63c", "#8d6e8a", "#3f6b7d", "#b8794a", "#5f7a52", "#c98a7a"]
TINT = ["#f4ece2", "#efe7dd", "#f2ece4", "#efe9e3"]


def _shirt(c):
    return f'<path d="M62 62h76l28 24-16 20-12-10v66H62v-66l-12 10-16-20z" fill="{c}"/><path d="M84 62c0 10 8 17 16 17s16-7 16-17" fill="none" stroke="{W}" stroke-width="5"/>'

def _jurk(c):
    return f'<path d="M74 58h52l16 18-14 12 20 74H64l20-74-14-12z" fill="{c}"/><path d="M86 58c0 9 6 15 14 15s14-6 14-15" fill="none" stroke="{W}" stroke-width="4"/>'

def _broek(c):
    return f'<path d="M64 56h72l6 108h-32l-10-62-10 62H58z" fill="{c}"/><path d="M64 74h72" stroke="{W}" stroke-width="4"/>'

def _jas(c):
    return f'<path d="M66 58h68l24 22-14 18-10-8v74H66V90l-10 8-14-18z" fill="{c}"/><path d="M100 62v100" stroke="{W}" stroke-width="4"/><circle cx="112" cy="96" r="4" fill="{W}"/><circle cx="112" cy="120" r="4" fill="{W}"/>'

def _muts(c):
    return f'<path d="M52 130c0-30 22-52 48-52s48 22 48 52z" fill="{c}"/><rect x="44" y="128" width="112" height="20" rx="10" fill="{W}" stroke="{c}" stroke-width="3"/><circle cx="100" cy="66" r="12" fill="{c}"/>'

def _sok(c):
    return f'<path d="M78 46h34v58l32 24c10 8 6 26-8 28-8 1-14-2-20-7l-38-32V46z" fill="{c}"/><path d="M78 62h34" stroke="{W}" stroke-width="5"/>'

def _schoen(c):
    return f'<path d="M46 118c14-4 22-14 26-30l6-24h26v34l38 16c14 6 18 14 18 24H46z" fill="{c}"/><rect x="42" y="138" width="122" height="14" rx="7" fill="{I}"/><path d="M92 92l30 12M88 106l34 14" stroke="{W}" stroke-width="4"/>'

def _tas(c):
    return f'<path d="M56 76h88l10 84H46z" fill="{c}"/><path d="M78 76V62c0-13 10-22 22-22s22 9 22 22v14" fill="none" stroke="{I}" stroke-width="5"/><circle cx="100" cy="112" r="11" fill="{W}"/>'

def _bal(c):
    return f'<circle cx="100" cy="104" r="52" fill="{c}"/><path d="M48 104h104M100 52c18 20 18 84 0 104M100 52c-18 20-18 84 0 104" fill="none" stroke="{W}" stroke-width="4"/>'

def _beker(c):
    return f'<path d="M66 62h68l-8 90H74z" fill="{c}"/><path d="M134 80c16 0 22 12 22 22s-8 20-20 20" fill="none" stroke="{c}" stroke-width="8"/><path d="M70 86h60" stroke="{W}" stroke-width="5"/>'

def _ketting(c):
    return f'<path d="M56 60c0 44 20 66 44 66s44-22 44-66" fill="none" stroke="{c}" stroke-width="6"/><path d="M100 126l14 22h-28z" fill="{Z}"/><circle cx="100" cy="158" r="10" fill="{c}"/>'

def _knuffel(c):
    return f'<circle cx="70" cy="66" r="16" fill="{c}"/><circle cx="130" cy="66" r="16" fill="{c}"/><circle cx="100" cy="94" r="38" fill="{c}"/><circle cx="88" cy="88" r="4.5" fill="{I}"/><circle cx="112" cy="88" r="4.5" fill="{I}"/><ellipse cx="100" cy="104" rx="12" ry="9" fill="{W}"/><rect x="70" y="132" width="60" height="36" rx="16" fill="{c}"/>'

def _slaapzak(c):
    return f'<path d="M70 58h60c8 0 12 6 12 14v70c0 12-8 20-20 20H78c-12 0-20-8-20-20V72c0-8 4-14 12-14z" fill="{c}"/><path d="M70 58c8 12 52 12 60 0" fill="none" stroke="{W}" stroke-width="5"/><path d="M100 84v66" stroke="{W}" stroke-width="4"/>'

def _boekje(c):
    return f'<path d="M46 60h48c8 0 6 6 6 10v82c0-6-6-10-12-10H46z" fill="{c}"/><path d="M154 60h-48c-8 0-6 6-6 10v82c0-6 6-10 12-10h42z" fill="{c}" opacity=".75"/><path d="M100 70v82" stroke="{W}" stroke-width="4"/>'

def _step(c):
    return f'<circle cx="60" cy="146" r="18" fill="none" stroke="{I}" stroke-width="6"/><circle cx="146" cy="146" r="18" fill="none" stroke="{I}" stroke-width="6"/><path d="M60 146h76" stroke="{c}" stroke-width="9" stroke-linecap="round"/><path d="M134 146L144 62" stroke="{I}" stroke-width="7" stroke-linecap="round"/><path d="M122 60h42" stroke="{c}" stroke-width="9" stroke-linecap="round"/>'

def _bloem(c):
    return f'<g fill="{c}"><ellipse cx="100" cy="60" rx="16" ry="26"/><ellipse cx="100" cy="112" rx="16" ry="26"/><ellipse cx="74" cy="86" rx="26" ry="16"/><ellipse cx="126" cy="86" rx="26" ry="16"/></g><circle cx="100" cy="86" r="15" fill="{Z}"/><path d="M100 128v34" stroke="{S}" stroke-width="6" stroke-linecap="round"/>'

VORMEN = [_shirt, _jurk, _broek, _jas, _muts, _sok, _schoen, _tas, _bal, _beker,
          _ketting, _knuffel, _slaapzak, _boekje, _step, _bloem]

GROEP = {
    "kleding": [0, 1, 2, 3, 5, 4],
    "baby": [12, 0, 5, 4, 2],
    "accessoires": [4, 7, 15, 5, 10],
    "tassen": [7, 4, 5],
    "schoenen": [6, 5, 7],
    "speelgoed": [11, 8, 13, 14],
    "interieur": [9, 13, 15],
    "sieraden": [10, 15, 4],
    "buiten": [14, 8, 6],
    "regen": [3, 6, 4],
}


def embleem(index, soort, rond=False):
    reeks = GROEP.get(soort, GROEP["kleding"])
    vorm = VORMEN[reeks[index % len(reeks)]]
    kleur = PALET[index % len(PALET)]
    tint = TINT[index % len(TINT)]
    svg = _wrap("0 0 200 200", vorm(kleur))
    klas = "embleem rond" if rond else "embleem"
    return '<div class="%s" style="background:%s">%s</div>' % (klas, tint, svg)
