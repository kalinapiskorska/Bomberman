import pygame, sys
pygame.init()
#tworzenie okna (?) gry
screen = pygame.display.set_mode((800,670))

#tytuł i ikonka
pygame.display.set_caption("Bomberman")
icon = pygame.image.load('bomba.jpg')
pygame.display.set_icon(icon)


# GRACZ - BOMBERMAN
 # grafika
playerImg = pygame.image.load('alien.png')
# początkowe położenie - oś X i oś Y
player_on_X = 360
player_on_Y = 480
# zmienne potrzebne do ruchu gracza - na osi X i osi Y
player_move_X = 0
player_move_Y = 0

# funkcja "rysująca" gracza w oknie gry - w nawiasie lokalizacja gracza
def player_appear():
    screen.blit(playerImg, (int(player_on_X), int(player_on_Y)))

# lista współrzędnych prostokątów, które są przeszkodami
# istotne dla niewchodzenia na przeszkody - sprawdzane w "collision" przez
# funkcję .collidelist()
walls = []
for i in range(8):
    for j in range(6):
        rec_on_X = [20,120,220,320,420,520,620,720]
        rec_on_Y= [80,180,280,380,480,580]
        walls.append([rec_on_X[i], rec_on_Y[j],35,35])

# ta funkcja poniżej sprawia, że poruszanie się graczem jest bardziej płynne
# i jak trzymam klawisz to gracz nadal się porusza (bez tego trzeba przyciskać
# strzałkę 40 razy żeby się ruszył o parę cm
pygame.key.set_repeat(20,20)

while True:
    # z tego co zrozumiałam, musimy pamiętać, żeby cały kod był pisany w tej pętli bo inaczej kapica i
    # padnie, wiec pamietajcie o wciąęciu <3
    #kolorek tła - RGB
    screen.fill((99, 184, 72))

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

    # int przy playerach bo python się czepiał
    # player_box to prostokąt otaczajacy gracza - jeżeli koliduje z przeszkodami
    # z listy "walls" to funkcja collidelist zwraca wartość równą indeksowi
    # prostokąta kolidującego z tej listy
    # np. player_box koliduje z drugim prostokątem na liście (indeks = 1) -
    # wtedy collision = 1. Jeżeli nic nie koliduje collision = -1
    player_box = pygame.Rect(int(player_on_X+3), int(player_on_Y),35, 40)
    # odkomentuj poniższe żeby zobaczyć jak wygląda player box:
    # pygame.draw.rect(screen, (255, 203, 179),pygame.Rect(int(player_on_X+3), int(player_on_Y),35, 40))

    collision = player_box.collidelist(walls)

    #obsługa zdarzeń - pętla żeby okno się nie zamykało
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit(0)

        # RUCH GRACZA sterowany strzałkami
        # gdy naciskam klawisz (keydown), gracz się rusza po osiach X, Y
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if collision < 0:
                    # collision opisane wyżej
                    # jeżeli nie ma kolizji player_box i przeszkody to się rusza
                    # normalnie
                    player_move_X = -5
                else:
                    # jeżeli jest kolizja to ruch jest spowolniony
                    player_move_X = -0.5
            elif event.key == pygame.K_RIGHT:
                if collision < 0:
                    player_move_X = 5
                else:
                    player_move_X = 0.5
            if event.key == pygame.K_DOWN:
                if collision < 0:
                    player_move_Y = 5
                else:
                    player_move_Y = 0.5
            elif event.key == pygame.K_UP:
                if collision < 0:
                    player_move_Y = -5
                else:
                    player_move_Y = -0.5

        # gdy przestaję naciskać, puszcza klawisz (keyup),
        # gracz przestaje się ruszać
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_move_X = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                player_move_Y = 0

        # dodajemy do każdej współrzędnej lokalizacji gracza wartość ruchu
        # równą 5 lub -5 (wyzanczone przy kontroli klawiszy)
        player_on_X += player_move_X
        player_on_Y += player_move_Y

        # granice - jeżeli gracz wychodzi za granicę okna gry
        # to pojawia się w tym samym miejscu, przed samą granicą
        if player_on_X <= 0:
            player_on_X = 0
        elif player_on_X >= 750:
            player_on_X = 750
        if player_on_Y <= 45:
            player_on_Y = 45
        elif player_on_Y >= 600:
            player_on_Y = 600

        # przywołanie tej funkcji = gracz pojawia się na ekranie
        player_appear()

        pygame.display.update()
