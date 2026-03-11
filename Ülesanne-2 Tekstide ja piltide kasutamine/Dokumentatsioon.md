# Ülesanne 2: Tekstide ja piltide kasutamine

**Autor:** Taivo Tobreluts

---

## 1. Praktilise töö sooritamise käik

### Eesmärk

Luua PyGame mänguaken, kus kuvatakse poe taust, poemüüja ja jutumull tekstiga. Õppida piltide laadimist, skaleerimist ja positsioneerimist. Kuvada teksti kindla fondiga jutumulli sees.

### Lühikirjeldus

Programm loob 640×480 piksli suuruse akna. Taustapilt (bg_shop.jpg) kuvatakse täiselt. Müüja pilt (seller.png, originaal 895×1059 px) vähendatakse 260×330 px peale kasutades `smoothscale()` funktsiooni sakisuse vältimiseks. Müüja paigutatakse positsioonile (105, 150). Jutumull (chat.png) skaleeritakse 250×200 px peale ja paigutatakse positsioonile (250, 80). Tekst "Tere, olen Taivo" kuvatakse valgena blackadderitc fondiga (suurus 36) jutumulli keskele.

### GitHub link

https://github.com/taivotobreluts/pygame-projektid

### Töötasid üksi või meeskonnas?

Töötasin üksi.

### Kas said abi või abistasid kaasõppijat?

Antud ülesande raames töötasin iseseisvalt. Kasutasin õppematerjale ja pygame dokumentatsiooni. Võtsin abi AI assistendilt piltide positsioneerimise ja skaleerimise osas.

---

## 2. TI (tehisintellekti) kasutamine

### Kas kasutasid töö käigus tehisintellekti abi?

Jah, kasutasin AI assistenti (Kimi Code CLI) ülesande mõistmiseks, piltide positsioneerimise parandamiseks ja dokumentatsiooni vormistamiseks.

### Millist TI-d kasutasid?

Kimi Code CLI (Kimi AI)

### Millised olid esitatud küsimused või käsud (promptid)?

- Kuidas laadida ja kuvada pilte PyGame-s?
- Mis vahe on `pygame.transform.scale()` ja `smoothscale()` vahel?
- Kuidas paigutada müüja ja jutumull nii, et see vastaks näidispildile?
- Kuidas kasutada erinevaid fonte PyGame-s?
- Kuidas tsentreerida tekst jutumulli sisse?

### Kuidas hindad saadud abi usaldusväärsust?

Saadud abi oli usaldusväärne. AI soovitas õigesti `smoothscale()` funktsiooni sakise pildi vältimiseks. Piltide positsioneerimisel kontrollisin tulemust visuaalselt ja võrdlesin näidispildiga. Koodi osas kontrollisin pygame ametliku dokumentatsiooni põhjal, kas funktsioonide kasutus on õige. Parandasin ise piltide koordinaate, et need paremini näidisele vastaksid.

---

## 3. Esinenud probleemid ja lahendused

### Probleem 1: Piltide sakisus skaleerimisel

**Probleem:** Pildid (müüja ja jutumull) olid pärast skaleerimist sakised ja kõrge kvaliteediga.

**Lahendus:** Vahetasin `pygame.transform.scale()` välja `pygame.transform.smoothscale()` vastu. Smoothscale kasutab bilineaarset interpolatsiooni, mis annab sujuvama tulemuse.

### Probleem 2: Müüja ja jutumulli paigutamine

**Probleem:** Müüja ja jutumull ei paiknenud samamoodi nagu näidispildil.

**Lahendus:** Proovisin erinevaid X ja Y koordinaate, kuni leidsin õiged väärtused: müüja (105, 150) ja jutumull (250, 80). Kasutasin visuaalset kontrolli, et võrrelda tulemust näidispildiga.

### Probleem 3: Erinevate fontide kasutamine

**Probleem:** Süsteemi fontidega ei saavutanud soovitud visuaalset tulemust.

**Lahendus:** Leidsin sobiva fondi (blackadderitc), mis annab dekoratiivse väljanägemise. Proovisin erinevaid fontide suuruseid (alustasin 24-st, lõpuks 36), et tekst mahuks jutumulli.

### Probleem 4: Teksti positsioneerimine jutumullis

**Probleem:** Tekst ei olnud jutumullis keskel.

**Lahendus:** Kasutasin teksti suuruse mõõtmist ja arvutasin positsiooni nii, et tekst oleks jutumulli keskpunkti suhtes tsentreeritud.

---

## Lisa: Kasutatud värvid

Programmis defineeritakse värvid RGB süsteemis:

| Värv    | RGB väärtus       | Kasutus          |
|---------|-------------------|------------------|
| Valge   | (255, 255, 255)   | Tekst jutumullis |

---

## Lisa: Kasutatud pygame funktsioonid

| Funktsioon | Kirjeldus |
|------------|-----------|
| `pygame.init()` | Initsialiseerib pygame teegi |
| `pygame.display.set_mode()` | Loob graafilise akna |
| `pygame.display.set_caption()` | Määrab akna pealkirja |
| `pygame.image.load()` | Laeb pildifaili |
| `pygame.transform.smoothscale()` | Muudab pildi suurust sakisust vältides |
| `pygame.font.SysFont()` | Loob fondi teksti jaoks |
| `font.render()` | Renderdab teksti pildiks |
| `screen.blit()` | Kuvab pildi ekraanil |
| `pygame.display.flip()` | Uuendab ekraani sisu |
| `pygame.event.get()` | Võtab sündmused järjekorrast |
| `pygame.quit()` | Lõpetab pygame töö |
