import pygame
import sys

# Initsialiseeri pygame
pygame.init()

# Ekraani seaded
ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode([ekraani_laius, ekraani_korgus])
pygame.display.set_caption("PingPong")
kell = pygame.time.Clock()

# Värvid (RGB)
hele_sinine = [153, 204, 255]

# Palli seaded
palli_pilt = pygame.image.load("ball-1.png")
palli_suurus = 20
palli_x = ekraani_laius // 2
palli_y = 50
palli_kiirus_x = 3
palli_kiirus_y = 3

# Aluse seaded
aluse_pilt = pygame.image.load("pad.png")
aluse_laius = 120
aluse_korgus = 20
aluse_pilt = pygame.transform.smoothscale(aluse_pilt, [aluse_laius, aluse_korgus])
aluse_x = ekraani_laius // 2 - aluse_laius // 2
aluse_y = int(ekraani_korgus / 1.5)
aluse_kiirus = 4

# Põhisilmus
gameover = False

while not gameover:
    kell.tick(60)

    # Taust
    ekraan.fill(hele_sinine)

    # Liiguta palli
    palli_x += palli_kiirus_x
    palli_y += palli_kiirus_y

    # Pall põrkub seintelt tagasi
    if palli_x <= 0 or palli_x >= ekraani_laius - palli_suurus:
        palli_kiirus_x = -palli_kiirus_x

    if palli_y <= 0 or palli_y >= ekraani_korgus - palli_suurus:
        palli_kiirus_y = -palli_kiirus_y

    # Liiguta alust (automaatselt vasakule-paremale)
    aluse_x += aluse_kiirus

    if aluse_x <= 0 or aluse_x >= ekraani_laius - aluse_laius:
        aluse_kiirus = -aluse_kiirus

    # Kokkupõrke tuvastamine (pall ja alus)
    palli_rect = pygame.Rect(palli_x, palli_y, palli_suurus, palli_suurus)
    aluse_rect = pygame.Rect(aluse_x, aluse_y, aluse_laius, aluse_korgus)

    if palli_rect.colliderect(aluse_rect) and palli_kiirus_y > 0:
        palli_kiirus_y = -palli_kiirus_y

    # Kuva pall ja alus
    ekraan.blit(palli_pilt, (palli_x, palli_y))
    ekraan.blit(aluse_pilt, (aluse_x, aluse_y))

    # Uuenda ekraani
    pygame.display.flip()

    # Mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

# Lõpeta pygame
pygame.quit()
