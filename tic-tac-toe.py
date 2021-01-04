import pygame 
from pygame.locals import *
import math
import sys
pygame.init()
icon = pygame.image.load("tic-tac-toe.png")
ximg = pygame.image.load("x.png")
oimg = pygame.image.load("o.png")
font = pygame.font.SysFont("comicsansms",72)
font2 = pygame.font.SysFont("comicsansms",32)
available = pygame.font.get_fonts()

poss = []
player = "x"
place1 = False
place2 = False
place3 = False
place4 = False
place5 = False
place6 = False
place7 = False
place8 = False
place9 = False
i = 0
player1o = False
player1x = False
player2o = False
player2x = False
player3o = False
player3x = False
player4o = False
player4x = False
player5o = False
player5x = False
player6o = False
player6x = False
player7o = False
player7x = False
player8o = False
player8x = False
player9o = False
player9x = False
o = ""
t = ""
th = ""
f = ""
fi = ""
s = ""
se = ""
e = ''
n = ""
screen = pygame.display.set_mode((601,601))
pygame.display.set_caption("tic tac toe - manas")
pygame.display.set_allow_screensaver(True)
pygame.display.set_icon(icon)
board = pygame.image.load("background.png")

clock = pygame.time.Clock()

def check_places(mousex,mousey):
    global place1
    global place2
    global place3
    global place4 
    global place5 
    global place6 
    global place7 
    global place8 
    global place9 
    global i
    global o 
    global t 
    global th 
    global f 
    global fi 
    global s 
    global se 
    global e 
    global n 
    distance1 = math.sqrt(math.pow(mousex-103,2)+math.pow(mousey-107,2))
    distance2 = math.sqrt(math.pow(mousex-295,2)+math.pow(mousey-108,2))
    distance3 = math.sqrt(math.pow(mousex-485,2)+math.pow(mousey-136,2))
    distance4 = math.sqrt(math.pow(mousex-84,2)+math.pow(mousey-309,2))
    distance5 = math.sqrt(math.pow(mousex-302,2)+math.pow(mousey-316,2))
    distance6 = math.sqrt(math.pow(mousex-501,2)+math.pow(mousey-307,2))
    distance7 = math.sqrt(math.pow(mousex-75,2)+math.pow(mousey-476,2))
    distance8 = math.sqrt(math.pow(mousex-310,2)+math.pow(mousey-455,2))
    distance9 = math.sqrt(math.pow(mousex-489,2)+math.pow(mousey-490,2))
    if distance1 < 100 and o != "x" and o != "o":
        place1 = True
        i+=1
    elif distance2 < 100 and t != "x" and t!= "o":
        place2 = True
        i+=1
    elif distance3 < 100 and th != "x" and th != "o":
        place3 = True
        i+=1
    elif distance4 < 100 and f!= "x" and f!= "o":
        place4 = True
        i+=1
    elif distance5 < 100 and fi != "x" and fi != "o":
        place5 = True
        i+=1
    elif distance6 < 100 and s != "o" and s!= "x":
        place6 = True
        i+=1
    elif distance7 < 100 and se!= "x" and se!= "o":
        place7 = True
        i+=1
    elif distance8 < 100 and e != "x" and e != 'o':
        place8 = True
        i+=1
    elif distance9 < 100 and n != "x" and n!="o":
        place9 = True
        i+=1
    else:
        i -1

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            running = False
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            strpos = str(pos)
            words = strpos.strip("()")
            word = words.replace(",","")
            l = word.split(" ")
            for ll in l:
                poss.append(ll)
            x = int(pos[0])
            y = int(pos[1])
            check_places(x,y)
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 9:
                print("it is x's turn") 
                player = "x"
            if i == 2 or i == 4 or i == 6 or i == 8:
                print("it is o's turn")
                player = "o"
    screen.blit(board,(0,0))
    if place1 and o != "x" and o != 'o':
        if player == "x":
            player1x = True
            o = "x"
        if player == "o":
            player1o = True
            o = "o"
        place1 = False
    elif place2 and t != "x" and t != "o":
        if player == "x":
            player2x = True
            t = "x"
        if player == "o":
            player2o = True
            t = "o"
        place2 = False
    elif place3 and th != "x" and th != "o":
        if player == "x":
            player3x = True
            th = "x"
        if player == "o":
            player3o = True
            th = 'o'
        place3 = False
    elif place4 and f != "x" and f != "o":
        if player == "x" :
            player4x = True
            f = "x"
        if player == "o":
            player4o = True
            f = "o"
        place4 = False
    elif place5 and fi != "x" and fi != "o":
        if player == "x":
            player5x = True
            fi = "x"
        if player == "o":
            player5o = True
            fi = 'o'
        place5 = False
    elif place6 and s != "o" and s != "x":
        if player == "x":
            player6x = True
            s = "x"
        if player == "o":
            player6o = True
            s = "o"
        place6 = False
    elif place7 and se != "x" and se != "o":
        if player == "x":
            player7x = True
            se = "x"
        if player == "o":
            player7o = True
            se = "o"
        place7 = False
    elif place8 and e != "x" and e != "o":
        if player == "x":
            player8x = True
            e = "x"
        if player == "o":
            player8o = True
            e = "o"
        place8 = False
    elif place9 and n != "x" and n!= "o":
        if player == "x":
            player9x = True
            n = "x"
        if player == "o":
            player9o = True
            n = "o"
        place9 = False
    else:
      i - 1
    if player1o:
            screen.blit(oimg,(17,27))
    if player1x:
        screen.blit(ximg,(17,27))
    if player2o:
            screen.blit(oimg,(210,27))
    if player2x:
        screen.blit(ximg,(210,27))
    if player3o:
            screen.blit(oimg,(390,27))
    if player3x:
        screen.blit(ximg,(390,27))
    if player4o:
            screen.blit(oimg,(17,220))
    if player4x:
        screen.blit(ximg,(17,220))
    if player5o:
            screen.blit(oimg,(210,220))
    if player5x:
        screen.blit(ximg,(210,220))
    if player6o:
            screen.blit(oimg,(395,220))
    if player6x:
        screen.blit(ximg,(395,220))
    if player7o:
            screen.blit(oimg,(17,390))
    if player7x:
        screen.blit(ximg,(17,390))
    if player8o:
            screen.blit(oimg,(210,390))
    if player8x:
        screen.blit(ximg,(210,390))
    if player9o:
            screen.blit(oimg,(390,390))
    if player9x:
        screen.blit(ximg,(390,390))
    if o == "x" and t == "x" and th == "x" or f == "x" and fi == "x" and s == "x" or se == "x" and e == "x" and n == "x" or o == "x" and f == "x" and se == "x" or t == "x" and fi == "x" and e == "x" or th == "x" and s == "x" and n == "x" or th == "x" and fi == "x" and se == "x"or o == "x" and fi == "x" and n == "x":
        print("x has won")
        Running_2 = True
        while Running_2:
            screen.fill((255,0,80))
            text = font.render("has won",True,(23,157,200))
            text2 = font2.render("press any key to continue...",True,(23,157,200))
            screen.blit(ximg,(5,110))
            screen.blit(text,(150,150))
            screen.blit(text2,(120,295))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                   Running_2 = False
            pygame.display.update()
        i = 0
        print(i)
        o = ""
        t = ""
        th = ""
        f = ""
        fi = ""
        s = ""
        se = ""
        e = ''
        n = ""
        player1o = False
        player1x = False
        player2o = False
        player2x = False
        player3o = False 
        player3x = False
        player4o = False
        player4x = False
        player5o = False
        player5x = False
        player6o = False
        player6x = False
        player7o = False
        player7x = False
        player8o = False
        player8x = False
        player9o = False
        player9x = False
    elif o == "o" and t == "o" and th == "o" or f == "o" and fi == "o" and s == "o" or se == "o" and e == "o" and n == "o" or o == "o" and f == "o" and se == "o" or t == "o" and fi == "o" and e == "o" or th == "o" and s == "o" and n == "o" or th == "o" and fi == "o" and se == "o"or o == "o" and fi == "o" and n == "o":
        print("o has won")
        Running_2 = True
        while Running_2:
            screen.fill((23,157,200))
            text = font.render("has won",True,(241,99,123))
            text2 = font2.render("press any key to continue...",True,(241,99,123))
            screen.blit(oimg,(22,112))
            screen.blit(text,(230,150))
            screen.blit(text2,(150,350))  
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                   Running_2 = False
                if event.type == QUIT:
                   sys.exit()
            pygame.display.update()
        i = 1
        o = ""
        t = ""
        th = ""
        f = ""
        fi = ""
        s = ""
        se = ""
        e = ''
        n = ""
        player1o = False
        player1x = False
        player2o = False
        player2x = False
        player3o = False 
        player3x = False
        player4o = False
        player4x = False
        player5o = False
        player5x = False
        player6o = False
        player6x = False
        player7o = False
        player7x = False
        player8o = False
        player8x = False
        player9o = False
        player9x = False
    elif i >= 9 :
      print("it is a tie")
      Running_2 = True
      while Running_2:
            screen.fill((23,157,200))
            text = font.render("It is a tie",True,(241,99,123))
            text2 = font2.render("press any key to continue...",True,(241,99,123))
            screen.blit(text,(230,150))
            screen.blit(text2,(150,350))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                   Running_2 = False
                if event.type == QUIT:
                   sys.exit()
            pygame.display.update()
      i = 1
      o = ""
      t = ""
      th = ""
      f = ""
      fi = ""
      s = ""
      se = ""
      e = ''
      n = ""
      player1o = False
      player1x = False
      player2o = False
      player2x = False
      player3o = False 
      player3x = False
      player4o = False
      player4x = False
      player5o = False
      player5x = False
      player6o = False
      player6x = False
      player7o = False
      player7x = False
      player8o = False
      player8x = False
      player9o = False
      player9x = False
      pygame.display.update()
        
    
    clock.tick(32)              
    pygame.display.update()