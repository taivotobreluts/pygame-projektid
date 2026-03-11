import pygame

# Initsialiseeri pygame
pygame.init()

# Loo aken (laius, kõrgus)
suurus = 300
screen = pygame.display.set_mode([suurus, suurus])
pygame.display.set_caption("Foor - Taivo Tobreluts")

# Värvid (RGB)
must = (0, 0, 0)
hall = (128, 128, 128)
punane = (255, 0, 0)
kollane = (255, 255, 0)
roheline = (0, 255, 0)

# Põhiakna taust
screen.fill(must)

# Foori raam (hall ristkülik)
# Ristküliku asukoht ja suurus
raami_laius = 100
raami_korgus = 260
raami_x = (suurus - raami_laius) // 2  # Tsentreeri horisontaalselt
raami_y = 20
raami_paksus = 2
pygame.draw.rect(screen, hall, (raami_x, raami_y, raami_laius, raami_korgus), raami_paksus)

# Foori tuled (ringid)
# Kolm ringi foori raami sees
ring_raadius = 38

# Punane tuli (ülemine)
punane_x = suurus // 2
punane_y = raami_y + 45
pygame.draw.circle(screen, punane, (punane_x, punane_y), ring_raadius)

# Kollane tuli (keskmine)
kollane_x = suurus // 2
kollane_y = raami_y + 130
pygame.draw.circle(screen, kollane, (kollane_x, kollane_y), ring_raadius)

# Roheline tuli (alumine)
roheline_x = suurus // 2
roheline_y = raami_y + 215
pygame.draw.circle(screen, roheline, (roheline_x, roheline_y), ring_raadius)

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
