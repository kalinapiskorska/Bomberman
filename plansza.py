import pygame, sys
pygame.init()
#tworzenie okna (?) gry
screen = pygame.display.set_mode((800,670))

#tytuł i ikonka
pygame.display.set_caption("Bomberman")
icon = pygame.image.load('bomba.jpg')
pygame.display.set_icon(icon)

#szare kwadraty aka murki
#boardImg = pygame.image.load('zielony_kwadrat.png')
#boardX= 200
#boardY = 150

def board():
    screen.blit(boardImg, (boardX, boardY))

while True:
    # z tego co zrozumiałam, musimy pamiętać, żeby cały kod był pisany w tej pętli bo inaczej kapica i padnie, wiec pamietajcie o wciąęciu <3
    #kolorek tła - RGB
    screen.fill((99, 184, 72))

    #obsługa zdarzeń - pętla żeby okno się nie zamykało
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit(0)

    #rysowanko bloków/murów
    #murek góry - miejsce na wynik i dane
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(0,0,800,45))
    #murek dolny
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(0,660,800,15))

    # pierwsza kolumna murków
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(20,80,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(20,180,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(20,280,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(20,380,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(20,480,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(20,580,40,40))

    # druga kolumna murków
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(120,80,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(120,180,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(120,280,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(120,380,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(120,480,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(120,580,40,40))

    # trzecia kolumna murków
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(220,80,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(220,180,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(220,280,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(220,380,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(220,480,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(220,580,40,40))

    # czwarta kolumna murkow
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(320,80,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(320,180,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(320,280,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(320,380,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(320,480,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(320,580,40,40))

    # piąta kolumna murków
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(420,80,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(420,180,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(420,280,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(420,380,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(420,480,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(420,580,40,40))

    # szósta kolumna murków
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(520,80,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(520,180,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(520,280,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(520,380,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(520,480,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(520,580,40,40))

    #siódma kolumna murków
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(620,80,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(620,180,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(620,280,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(620,380,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(620,480,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(620,580,40,40))

    # ósma kolumna murków
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(720,80,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(720,180,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(720,280,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(720,380,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(720,480,40,40))
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(720,580,40,40))


    pygame.display.update()
