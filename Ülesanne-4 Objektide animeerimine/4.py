import pygame
import sys
import random

# Initsialiseeri pygame
pygame.init()

# Ekraani seaded
ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode([ekraani_laius, ekraani_korgus])
pygame.display.set_caption("Ralli - Taivo Tobreluts")
kell = pygame.time.Clock()

# Tee vahemik (kus autod võivad sõita)
tee_vasak = 150
tee_parem = 490

# Siniste autode seaded (muuda siit)
siniste_arv = 8
sinine_kiirus = 7

# Lae pildid
taust = pygame.image.load("bg_rally.jpg")
punane_auto_pilt = pygame.image.load("f1_red.png")
sinine_auto_pilt = pygame.image.load("f1_blue.png")

# Auto mõõtmed
auto_laius = 45
auto_korgus = 90

# Punane auto positsioon (ekraani all keskel)
punane_x = ekraani_laius // 2 - auto_laius // 2
punane_y = ekraani_korgus - auto_korgus - 10

# Skoor
skoor = 0
font = pygame.font.SysFont("Arial", 30)
fondi_varv = [255, 255, 255]


# Punase auto x-vahemik kogu y-teljel (sest sinised liiguvad ülevalt alla sama rada pidi)
punane_rect = pygame.Rect(punane_x, -ekraani_korgus * 2, auto_laius, ekraani_korgus * 4)


# Funktsioon sinise auto algpositsiooni loomiseks
# Kontrollib, et uus auto ei kattuks teiste siniste ega punase autoga
def loo_sinine_auto(olemasolevad):
    for katse in range(100):
        x = random.randint(tee_vasak, tee_parem - auto_laius)
        y = random.randint(-ekraani_korgus, -auto_korgus)
        uus_rect = pygame.Rect(x, y, auto_laius, auto_korgus)

        # Kontrolli kattuvust punase autoga
        if uus_rect.colliderect(punane_rect):
            continue

        # Kontrolli kattuvust teiste siniste autodega
        kattub = False
        for olemas in olemasolevad:
            olemas_rect = pygame.Rect(olemas[0], olemas[1], auto_laius, auto_korgus)
            if uus_rect.colliderect(olemas_rect):
                kattub = True
                break

        if not kattub:
            return [x, y]

    # Kui 100 katset ei leidnud vaba kohta, paiguta kaugele üles
    return [random.randint(tee_vasak, tee_parem - auto_laius), -ekraani_korgus * 2]


# Loo sinised autod hajutatult (iga järgmine algab kaugemalt ülevalt)
sinised_autod = []
for i in range(siniste_arv):
    auto = loo_sinine_auto(sinised_autod)
    # Hajuta ajaliselt: iga auto algab i * 80 pikslit kaugemalt ülevalt
    auto[1] -= i * 80
    sinised_autod.append(auto)


# Funktsioon skoori kuvamiseks
def kuva_skoor(ekraan, skoor):
    tekst = font.render("Skoor: " + str(skoor), True, fondi_varv)
    ekraan.blit(tekst, [10, 10])


# Põhisilmus
gameover = False

while not gameover:
    kell.tick(60)

    # Kuva taustapilt
    ekraan.blit(taust, (0, 0))

    # Kuva punane auto
    ekraan.blit(punane_auto_pilt, (punane_x, punane_y))

    # Liiguta ja kuva sinised autod
    for auto in sinised_autod:
        # Liiguta alla
        auto[1] += sinine_kiirus

        # Kui auto jõuab alla, alusta uuesti ülevalt (vaba kohta)
        if auto[1] > ekraani_korgus:
            # Teised autod (ilma praeguseta)
            teised = [a for a in sinised_autod if a is not auto]
            uus = loo_sinine_auto(teised)
            auto[0] = uus[0]
            auto[1] = uus[1]
            skoor += 1

        # Kuva sinine auto
        ekraan.blit(sinine_auto_pilt, (auto[0], auto[1]))

    # Kuva skoor
    kuva_skoor(ekraan, skoor)

    # Uuenda ekraani
    pygame.display.flip()

    # Mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

# Lõpeta pygame
pygame.quit()
