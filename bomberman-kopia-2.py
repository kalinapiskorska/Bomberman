import pygame, sys, random
pygame.init()
#tworzenie okna (?) gry
screen = pygame.display.set_mode((800,670))

#tytuł i ikonka
pygame.display.set_caption("Bomberman")
icon = pygame.image.load("bomba.jpg")
pygame.display.set_icon(icon)
COUNTDOWN=pygame.USEREVENT + 1

# GRACZ - BOMBERMAN
 # grafika
bombimg=pygame.image.load("bombaboom.png")
expimg=pygame.image.load("wybuchstraszny.png")
playerImg = pygame.image.load("alien.png")
# początkowe położenie - oś X i oś Y
player_on_X = 360
player_on_Y = 480
# zmienne potrzebne do ruchu gracza - na osi X i osi Y
player_move_X = 0
player_move_Y = 0

# funkcja "rysująca" gracza w oknie gry - w nawiasie lokalizacja gracza
def player_appear():
    screen.blit(playerImg, (int(player_on_X), int(player_on_Y)))
    player_box = pygame.Rect(int(player_on_X+3), int(player_on_Y),35, 40)
    return player_box



# lista współrzędnych prostokątów, które są przeszkodami
# istotne dla niewchodzenia na przeszkody - sprawdzane w "collision" przez
# funkcję .collidelist()


bomb_x=0
bomb_y=0
# ta funkcja poniżej sprawia, że poruszanie się graczem jest bardziej płynne
# i jak trzymam klawisz to gracz nadal się porusza (bez tego trzeba przyciskać
# strzałkę 40 razy żeby się ruszył o parę cm
pygame.key.set_repeat(20,20)

# początkowe miejsce przeciwnika, bo w pętli wariuje
#1
enemyX1 = random.randint(0,765)
enemyY1 = random.randint(45,620)
#2
enemyX2 = random.randint(0,765)
enemyY2 = random.randint(45,620)
#3
enemyX3 = random.randint(0,765)
enemyY3 = random.randint(45,620)
#4
enemyX4 = random.randint(0,765)
enemyY4 = random.randint(45,620)

enemies=[]
def enemyspawn(x,y,list):
    enemies.append(pygame.Rect(x, y,35, 40))


def enemyupdate(list):
    for e in list:
        screen.blit(enemyImg,e)
    del list[:]

walls = []
def Walls(list):
    for i in range(8):
        for j in range(6):
            rec_on_X = [20,120,220,320,420,520,620,720]
            rec_on_Y = [80,180,280,380,480,580]
            list.append([rec_on_X[i], rec_on_Y[j],35,35])
            pygame.draw.rect(screen, (203, 203, 179),pygame.Rect(rec_on_X[i],rec_on_Y[j],40,40))


def Walls2():
    #murek góry - miejsce na wynik i dane
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(0,0,800,45))
    #murek dolny
    pygame.draw.rect(screen, (203, 203, 179), pygame.Rect(0,660,800,15))


def plant_bomb():
    global bomb_x,bomb_y
    bomb_x=int(player_on_X)
    bomb_y=int(player_on_Y)
    pygame.time.set_timer(COUNTDOWN, 3000)
    screen.blit(bombimg,(bomb_x,bomb_y))
    return bomb_x,bomb_y

def explode(enemies):
    global bomb_x,bomb_y
    screen.blit(expimg,(bomb_x,bomb_y))
    expl_box=expl_box=pygame.Rect(bomb_x, bomb_y,100, 100)
    for e in enemies[:]:
        if expl_box.colliderect(e):
            enemies.remove(e)
    pygame.time.set_timer(COUNTDOWN, 0)
    return enemies


clock = pygame.time.Clock()
while True:
    clock.tick(60)
    # z tego co zrozumiałam, musimy pamiętać, żeby cały kod był pisany w tej pętli bo inaczej kapica i
    # padnie, wiec pamietajcie o wciąęciu <3
    #kolorek tła - RGB
    screen.fill((99, 184, 72))
    # przywołanie tej funkcji = gracz pojawia się na ekranie
    screen.blit(playerImg, (int(player_on_X), int(player_on_Y)))
    player_box = pygame.Rect(int(player_on_X+3), int(player_on_Y),35, 40)
    #rysowanko bloków/murów
    Walls(walls)
    Walls2()
    collision = player_box.collidelist(walls)

    # rzędy murków


    # int przy playerach bo python się czepiał
    # player_box to prostokąt otaczajacy gracza - jeżeli koliduje z przeszkodami
    # z listy "walls" to funkcja collidelist zwraca wartość równą indeksowi
    # prostokąta kolidującego z tej listy
    # np. player_box koliduje z drugim prostokątem na liście (indeks = 1) -
    # wtedy collision = 1. Jeżeli nic nie koliduje collision = -1

    # odkomentuj poniższe żeby zobaczyć jak wygląda player box:
    # pygame.draw.rect(screen, (255, 203, 179),pygame.Rect(int(player_on_X+3), int(player_on_Y),35, 40))



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
            if event.key == pygame.K_RIGHT:
                if collision < 0:
                    player_move_X = 5
                else:
                    player_move_X = 0.5
            if event.key == pygame.K_DOWN:
                if collision < 0:
                    player_move_Y = 5
                else:
                    player_move_Y = 0.5
            if event.key == pygame.K_UP:
                if collision < 0:
                    player_move_Y = -5
                else:
                    player_move_Y = -0.5




            if event.key == pygame.K_SPACE:
                plant_bomb()



        if event.type==COUNTDOWN :
            explode(enemies)







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



    #Enemy img
    enemyImg = pygame.image.load("enemy.png")

    #początkowy ruch - każdy przeciwnik w inną stronę, żeby jakaś różnorodność była
    #1
    enemyX1_change = 2
    enemyY1_change = 0
    enemyX1 += enemyX1_change
    enemyY1 += enemyY1_change
    #2
    enemyX2_change = 0
    enemyY2_change = 2
    enemyX2 += enemyX2_change
    enemyY2 += enemyY2_change
    #3
    enemyX3_change = -2
    enemyY3_change = 0
    enemyX3 += enemyX3_change
    enemyY3 += enemyY3_change
    #4
    enemyX4_change = 0
    enemyY4_change = -2
    enemyX4 += enemyX4_change
    enemyY4 += enemyY4_change

    #teleportowanie po wpadnieciu w sciane
    #1
    if enemyX1 >= 765:
        enemyX1_change = - 765
        enemyX1 += enemyX1_change
    #2
    if enemyY2 >= 620:
        enemyY2_change = -620
        enemyY2 += enemyY2_change
    #3
    if enemyX3 <=0:
        enemyX3_change = +765
        enemyX3 += enemyX3_change
    #4
    if enemyY4 <=45:
        enemyY4_change = +620
        enemyY4 += enemyY4_change


    #spawn przeciwników




    enemyspawn(enemyX1, enemyY1,enemies)
    enemyspawn(enemyX2, enemyY2,enemies)
    enemyspawn(enemyX3, enemyY3,enemies)
    enemyspawn(enemyX4, enemyY4,enemies)

    enemyupdate(enemies)

    pygame.display.flip()
