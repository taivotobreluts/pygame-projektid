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

# Muuda müüja suurust, et see mahuks aknasse
seller_suurus = (240, 285)
seller = pygame.transform.scale(seller, seller_suurus)

# Muuda jutumulli suurust
chat_suurus = (300, 238)
chat = pygame.transform.scale(chat, chat_suurus)

# Kuva taustapilt
screen.blit(bg_shop, (0, 0))

# Kuva müüja (paigutame vasakule alla)
seller_x = 20
seller_y = korgus - seller_suurus[1] + 20
screen.blit(seller, (seller_x, seller_y))

# Kuva jutumull (paigutame müüja kohale)
chat_x = 180
chat_y = 50
screen.blit(chat, (chat_x, chat_y))

# Lisa tekst jutumulli sisse
font = pygame.font.SysFont("blackadderitc", 29)
tekst = font.render("Tere, olen Taivo Tobreluts", True, valge)
tekst_x = chat_x + 32
tekst_y = chat_y + 90
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
