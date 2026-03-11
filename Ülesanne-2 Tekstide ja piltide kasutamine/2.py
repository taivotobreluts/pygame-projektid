import pygame

# Initsialiseeri pygame
pygame.init()

# Loo aken (laius, kõrgus)
laius = 640
korgus = 480
screen = pygame.display.set_mode([laius, korgus])
pygame.display.set_caption("Poemüüja - Taivo Tobreluts")

# Värvid (RGB)
valge = (255, 255, 255)

# Lae pildid
bg_shop = pygame.image.load("bg_shop.jpg")
seller = pygame.image.load("seller.png")
chat = pygame.image.load("chat.png")

# Muuda müüja suurust, et ta mahuks aknasse
# orig. dimensioonid 895x1059
# jagan kolmega
seller_suurus = (260, 330)
seller = pygame.transform.smoothscale(seller, seller_suurus)

# Muuda jutumulli suurust
chat_suurus = (250, 200)
chat = pygame.transform.smoothscale(chat, chat_suurus)

# Kuva taustapilt
screen.blit(bg_shop, (0, 0))

# Kuva müüja
seller_x = 105
seller_y = 150
screen.blit(seller, (seller_x, seller_y))

# Kuva jutumull (paigutame müüja kohale)
chat_x = 250
chat_y = 80
screen.blit(chat, (chat_x, chat_y))

# Lisa tekst jutumulli sisse
font = pygame.font.SysFont("blackadderitc", 36)
tekst = font.render("Tere, olen Taivo", True, valge)
tekst_x = chat_x + 35
tekst_y = chat_y + 70
screen.blit(tekst, (tekst_x, tekst_y))

# Uuenda ekraani
pygame.display.flip()

# Põhisilmus - hoia aken avatuna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Lõpeta pygame
pygame.quit()
