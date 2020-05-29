import pygame, sys
pygame.init()
#tworzenie okna (?) gry
screen = pygame.display.set_mode((800,670))

#tytuł i ikonka
pygame.display.set_caption("Bomberman")
icon = pygame.image.load('bomba.jpg')
pygame.display.set_icon(icon)

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


# rzędy murków
    for i in range(8):
        for j in range(6):
            rec_on_X = [20,120,220,320,420,520,620,720]
            rec_on_Y = [80,180,280,380,480,580]
            pygame.draw.rect(screen, (203, 203, 179),pygame.Rect(rec_on_X[i],rec_on_Y[j],40,40))

    pygame.display.update()
