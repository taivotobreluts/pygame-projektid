from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# Loo uus dokument
doc = Document()

# Pealkiri
title = doc.add_heading('Foori programmi dokumentatsioon', 0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# Autor
author = doc.add_paragraph()
author.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = author.add_run('Autor: Taivo Tobreluts')
run.font.size = Pt(12)
run.font.italic = True

doc.add_paragraph()

# Sissejuhatus
doc.add_heading('1. Sissejuhatus', level=1)
doc.add_paragraph(
    'See dokument kirjeldab Pythoni programmi, mis kasutab pygame teeki '
    'liiklustulede (foori) kuvamiseks graafilises aknas. '
    'Programm loob 300x300 piksli suuruse akna, kus kuvatakse vertikaalne foor '
    'kolme tulega: punane, kollane ja roheline.'
)

# Nõuded
doc.add_heading('2. Süsteemi nõuded', level=1)
doc.add_paragraph('Programmi käivitamiseks on vajalikud järgmised komponendid:')
nouded = doc.add_paragraph(style='List Bullet')
nouded.add_run('Python 3.x').bold = True
nouded = doc.add_paragraph(style='List Bullet')
nouded.add_run('pygame teek').bold = True
doc.add_paragraph(
    'Pygame saab installida käsuga: pip install pygame'
)

# Programmi struktuur
doc.add_heading('3. Programmi struktuur', level=1)

doc.add_heading('3.1. Initsialiseerimine', level=2)
doc.add_paragraph(
    'Programmi alguses initsialiseeritakse pygame ja luuakse aken '
    'mõõtmetega 300x300 pikslit. Aknale määratakse pealkirja "Foor - Taivo Tobreluts".'
)

doc.add_heading('3.2. Värvide määramine', level=2)
doc.add_paragraph('Programmis kasutatakse RGB värvisüsteemi järgmiste värvidega:')
tbl = doc.add_table(rows=5, cols=3)
tbl.style = 'Light Grid Accent 1'
hdr_cells = tbl.rows[0].cells
hdr_cells[0].text = 'Värv'
hdr_cells[1].text = 'RGB väärtus'
hdr_cells[2].text = 'Kasutus'

row = tbl.rows[1].cells
row[0].text = 'Must'
row[1].text = '(0, 0, 0)'
row[2].text = 'Taust'

row = tbl.rows[2].cells
row[0].text = 'Hall'
row[1].text = '(128, 128, 128)'
row[2].text = 'Foori raam'

row = tbl.rows[3].cells
row[0].text = 'Punane'
row[1].text = '(255, 0, 0)'
row[2].text = 'Ülemine tuli'

row = tbl.rows[4].cells
row[0].text = 'Kollane'
row[1].text = '(255, 255, 0)'
row[2].text = 'Keskmine tuli'

doc.add_paragraph()
doc.add_paragraph('Roheline (0, 255, 0) - Alumine tuli')

doc.add_heading('3.3. Graafiliste elementide joonistamine', level=2)
doc.add_paragraph(
    'Programm joonistab järgmised graafilised elemendid:'
)
elemendid = [
    ('Taust', 'Must ristkülik katab kogu akna'),
    ('Raam', 'Hall ristkülik (100x260 pikslit) tsentreeritud aknas'),
    ('Punane tuli', 'Ring raadiusega 35 pikslit, ülemine'),
    ('Kollane tuli', 'Ring raadiusega 35 pikslit, keskmine'),
    ('Roheline tuli', 'Ring raadiusega 35 pikslit, alumine')
]
for nimi, kirjeldus in elemendid:
    p = doc.add_paragraph(style='List Bullet')
    p.add_run(nimi + ': ').bold = True
    p.add_run(kirjeldus)

# Põhisilmus
doc.add_heading('4. Põhisilmus (Main Loop)', level=1)
doc.add_paragraph(
    'Pärast graafika joonistamist käivitub põhisilmus, mis hoiab akna avatuna. '
    'Silmus töötab seni, kuni kasutaja sulgeb akna (pygame.QUIT sündmus). '
    'See tagab, et programm ei lõpetaks kohe tööd, vaid ootaks kasutaja tegevust.'
)

# Kasutatud funktsioonid
doc.add_heading('5. Kasutatud pygame funktsioonid', level=1)
funktsioonid = [
    ('pygame.init()', 'Initsialiseerib pygame teegi'),
    ('pygame.display.set_mode()', 'Loob graafilise akna'),
    ('pygame.display.set_caption()', 'Määrab akna pealkirja'),
    ('pygame.draw.rect()', 'Joonistab ristküliku'),
    ('pygame.draw.circle()', 'Joonistab ringi'),
    ('pygame.display.flip()', 'Uuendab ekraani sisu'),
    ('pygame.event.get()', 'Võtab sündmused järjekorrast'),
    ('pygame.quit()', 'Lõpetab pygame töö')
]
for funktsioon, kirjeldus in funktsioonid:
    p = doc.add_paragraph(style='List Bullet')
    p.add_run(funktsioon).bold = True
    p.add_run(' - ' + kirjeldus)

# Järeldus
doc.add_heading('6. Järeldus', level=1)
doc.add_paragraph(
    'Antud programm demonstreerib pygame teegi põhifunktsionaalsust '
    'graafiliste kujundite joonistamiseks. Foori näide on hea algus '
    'graafilise programmeerimise õppimisel, kuna see hõlmab nii '
    'ristkülikute kui ka ringide joonistamist ning kasutab '
    'värvide määramist RGB väärtustega.'
)

doc.add_paragraph(
    'Edasised täiendused võiksid hõlmata foori tulede vilkumist, '
    'ajastust või interaktiivsust kasutaja sisendi kaudu.'
)

# Salvesta dokument
doc.save('Foori_dokumentatsioon.docx')
print('Dokument "Foori_dokumentatsioon.docx" loodud edukalt!')
