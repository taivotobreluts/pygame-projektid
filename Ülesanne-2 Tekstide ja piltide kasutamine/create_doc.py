from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Loo uus dokument
doc = Document()

# Pealkiri
title = doc.add_heading('TARKVARAARENDUSE PROJEKTI DOKUMENTATSIOON', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Autor ja ülesanne info
info = doc.add_paragraph()
info.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = info.add_run('\nÜlesanne 2: Tekstide ja piltide kasutamine\n')
run.font.size = Pt(14)
run.font.bold = True
run = info.add_run('Autor: Taivo Tobreluts\n')
run.font.size = Pt(12)
run.font.italic = True

doc.add_paragraph()

# 1. Praktilise töö sooritamise käik
doc.add_heading('1. Praktilise töö sooritamise käik', level=1)

doc.add_heading('Eesmärk:', level=2)
doc.add_paragraph(
    'Luua PyGame mänguaken, kus kuvatakse poe taust, poemüüja ja jutumull tekstiga. '
    'Õppida piltide laadimist, skaleerimist ja positsioneerimist. '
    'Kuvada teksti kindla fondiga jutumulli sees.'
)

doc.add_heading('Lühikirjeldus:', level=2)
doc.add_paragraph(
    'Programm loob 640×480 piksli suuruse akna. '
    'Taustapilt (bg_shop.jpg) kuvatakse täiselt. '
    'Müüja pilt (seller.png, originaal 895×1059 px) vähendatakse 260×330 px peale '
    'kasutades smoothscale() funktsiooni sakisuse vältimiseks. '
    'Müüja paigutatakse positsioonile (105, 150). '
    'Jutumull (chat.png) skaleeritakse 250×200 px peale ja paigutatakse positsioonile (250, 80). '
    'Tekst "Tere, olen Taivo" kuvatakse valgena blackadderitc fondiga (suurus 36) jutumulli keskele.'
)

doc.add_heading('GitHub link:', level=2)
doc.add_paragraph('(Lisa siia oma GitHub repository link)')

doc.add_heading('Töötasid üksi või meeskonnas?', level=2)
doc.add_paragraph('Töötasin üksi.')

doc.add_heading('Kas said abi või abistasid kaasõppijat?', level=2)
doc.add_paragraph(
    'Antud ülesande raames töötasin iseseisvalt. '
    'Kasutasin õppematerjale ja pygame dokumentatsiooni. '
    'Võtsin abi AI assistendilt piltide positsioneerimise ja skaleerimise osas.'
)

doc.add_page_break()

# 2. TI kasutamine
doc.add_heading('2. TI (tehisintellekti) kasutamine', level=1)

doc.add_heading('Kas kasutasid töö käigus tehisintellekti abi?', level=2)
doc.add_paragraph(
    'Jah, kasutasin AI assistenti (Kimi Code CLI) ülesande mõistmiseks, '
    'piltide positsioneerimise parandamiseks ja dokumentatsiooni vormistamiseks.'
)

doc.add_heading('Millist TI-d kasutasid?', level=2)
doc.add_paragraph('Kimi Code CLI (Kimi AI)')

doc.add_heading('Millised olid esitatud küsimused või käsud (promptid)?', level=2)
doc.add_paragraph('Näited küsimustest:')
prompts = [
    'Kuidas laadida ja kuvada pilte PyGame-s?',
    'Mis vahe on pygame.transform.scale() ja smoothscale() vahel?',
    'Kuidas paigutada müüja ja jutumull nii, et see vastaks näidispildile?',
    'Kuidas kasutada erinevaid fonte PyGame-s?',
    'Kuidas tsentreerida tekst jutumulli sisse?'
]
for prompt in prompts:
    p = doc.add_paragraph(style='List Bullet')
    p.add_run(prompt).italic = True

doc.add_heading('Kuidas hindad saadud abi usaldusväärsust?', level=2)
doc.add_paragraph(
    'Saadud abi oli usaldusväärne. AI soovitas õigesti smoothscale() funktsiooni '
    'sakise pildi vältimiseks. Piltide positsioneerimisel kontrollisin tulemust '
    'visuaalselt ja võrdlesin näidispildiga. '
    'Koodi osas kontrollisin pygame ametliku dokumentatsiooni põhjal, '
    'kas funktsioonide kasutus on õige. '
    'Parandasin ise piltide koordinaate, et need paremini näidisele vastaksid.'
)

doc.add_page_break()

# 3. Esinenud probleemid ja lahendused
doc.add_heading('3. Esinenud probleemid ja lahendused', level=1)

doc.add_heading('Probleem 1: Piltide sakisus skaleerimisel', level=2)
doc.add_paragraph(
    'Probleem: Pildid (müüja ja jutumull) olid pärast skaleerimist sakised ja kõrge kvaliteediga.\n'
    'Lahendus: Vahetasin pygame.transform.scale() välja pygame.transform.smoothscale() vastu. '
    'Smoothscale kasutab bilineaarset interpolatsiooni, mis annab sujuvama tulemuse.'
)

doc.add_heading('Probleem 2: Müüja ja jutumulli paigutamine', level=2)
doc.add_paragraph(
    'Probleem: Müüja ja jutumull ei paiknenud samamoodi nagu näidispildil.\n'
    'Lahendus: Proovisin erinevaid X ja Y koordinaate, kuni leidsin õiged väärtused: '
    'müüja (105, 150) ja jutumull (250, 80). '
    'Kasutasin visuaalset kontrolli, et võrrelda tulemust näidispildiga.'
)

doc.add_heading('Probleem 3: Erinevate fontide kasutamine', level=2)
doc.add_paragraph(
    'Probleem: Süsteemi fontidega ei saavutanud soovitud visuaalset tulemust.\n'
    'Lahendus: Leidsin sobiva fondi (blackadderitc), mis annab dekoratiivse väljanägemise. '
    'Proovisin erinevaid fontide suuruseid (alustasin 24-st, lõpuks 36) '
    'et tekst mahuks jutumulli.'
)

doc.add_heading('Probleem 4: Teksti positsioneerimine jutumullis', level=2)
doc.add_paragraph(
    'Probleem: Tekst ei olnud jutumullis keskel.\n'
    'Lahendus: Kasutasin teksti suuruse mõõtmist ja arvutasin positsiooni nii, '
    'et tekst oleks jutumulli keskpunkti suhtes tsentreeritud.'
)

# Salvesta dokument
doc.save('Poemüüja_dokumentatsioon.docx')
print('Dokument "Poemüüja_dokumentatsioon.docx" loodud edukalt!')
