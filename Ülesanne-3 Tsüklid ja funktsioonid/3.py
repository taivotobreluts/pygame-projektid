import pygame
import sys

# Initsialiseeri pygame
pygame.init()

# Ruudustiku seaded (muuda siit)
#ruudu_suurus = 20
ruudu_suurus = 20
#ridade_arv = 24
ridade_arv = 24
#veergude_arv = 32
veergude_arv = 32
#joone_varv = [255, 0, 0]        # punane
joone_varv = [255, 0, 0]
#ruudu_varv = [153, 255, 153]    # hele roheline
ruudu_varv = [153, 255, 153]

# Ekraani seaded
ekraan = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Harjutamine")


# Funktsioon ruudustiku joonistamiseks
def joonista_ruudustik(ekraan, ruudu_suurus, ridade_arv, veergude_arv, joone_varv, ruudu_varv):

    # Joonistab ekraanile ruudustiku.
    #Parameetrid:
    #ekraan        pygame ekraani objekt
    #ruudu_suurus  ühe ruudu külje pikkus pikslites
    #ridade_arv    mitu rida ruute joonistada
    #veergude_arv  mitu veergu ruute joonistada
    #joone_varv    joonte värv
    #ruudu_varv    ruutude täitevärv

    for rida in range(ridade_arv):
        for veerg in range(veergude_arv):
            x = veerg * ruudu_suurus
            y = rida * ruudu_suurus
            # Joonista täidetud ruut
            pygame.draw.rect(ekraan, ruudu_varv, [x, y, ruudu_suurus, ruudu_suurus])
            # Joonista ruudu äärejoon
            pygame.draw.rect(ekraan, joone_varv, [x, y, ruudu_suurus, ruudu_suurus], 1)


# Põhisilmus - hoia aken avatuna
gameover = False

while not gameover:

    # Joonista ruudustik funktsiooniga
    joonista_ruudustik(ekraan, ruudu_suurus, ridade_arv, veergude_arv, joone_varv, ruudu_varv)

    # Uuenda ekraani
    pygame.display.flip()

    # Mängu sulgemine ristist
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

# Lõpeta pygame
pygame.quit()
