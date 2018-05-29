import random
import json

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

players = []
tours = 0
score_joueure1 = 0
score_joueure2 = 0
def fin_jeux(l, tt, pp, nn, nnn, jj):
    global players
    global tours

    
    while True :
        lecture_pierre_tasse(l, tt, jj)
        
        if l == [0] * len(l):
            if jj == nn:
               jj = nnn

            else:
             jj = nn


            score = 0
            _s = 0
            for x in range(1, tours):
              score += x * (10 ** x)

            print("{} vous avez gagné ........................ {}".format(jj, score))

            gan = False
            for player in players:
                if player.name == jj:
                    gan = True
                    if player.score == 0:
                        player.score = score
                    else:
                        if score < player.score:
                            player.score = score

            if not gan:
                players.append(Player(jj, score))

            if jj == nn:
                perd = nnn
            else:
                perd = nn

            perd1 = False
            for player in players:
                if player.name == perd:
                    perd1 = True

            if not perd1:
                players.append(Player(perd, 0))


            with open('players.json', 'w') as results:
                json.dump([player.__dict__  for player in players], results)


            break
            
        if jj == nn:
            jj = nnn

        else:
            jj = nn

def main():
	global players
	global tours
	global score_joueure1
	global score_joueure2

	with open('players.json') as f:
        	players_obj = json.load(f)

	for player_obj in players_obj:
        	player = Player(player_obj["name"], player_obj["score"])
        	players.append(player)

	l = []
	tasse_aux_hasard = random.randint(3, 7)
	pierre_aux_hasard = random.randint(5, 23)
	nom_jr1 = lire_jr1()
	nom_jr2 = lire_jr2()
	
        
            
	for n in [x for x in players if x.name == nom_jr1]:
        	score_joueure1 = n.score
        	print(" {}  ........................... {}".format(nom_jr1, score_joueure1))



	for n in [x for x in players if x.name == nom_jr2]:
	        score_joueure2 = n.score
	        print(" {}  ........................... {}".format(nom_jr2, score_joueure2))


	joueur = nom_jr1 

    
	debut(l, tasse_aux_hasard, pierre_aux_hasard, joueur) 

	fin_jeux(l, tasse_aux_hasard, pierre_aux_hasard, nom_jr1, nom_jr2, joueur) 

def lire_jr1():
    return input("joueur 1:  ")
def lire_jr2():
    return input("joueur 2:  ")

 
def debut(l, h, k, y):

    

    print("-" * 25)
    for i in range(0, h):
        k = random.randint(5, 23)
        _r = 23 - k
        print(' {}| {} {}'.format(i + 1, '*' * k, ' ' * _r) ,'|',k)

        l.append(k)  
    print("-" * 25)

    
def lecture_pierre_tasse(l, tt, jj):
 
    while True:
        
        r1 = input('{},quelle tasse  :' .format(jj))
        r2 = input('{}, commbien du pierre : '.format(jj))


        if (r2 and r1) and (r2.isdigit()) and (r1.isdigit()):
            if (int(r2) > 0) and (int(r1) <= len(l)) and (int(r1) > 0):
                if (int(r2) <= l[int(r1) - 1]):
                    if (int(r2) != 0) and (int(r1) != 0):
                        break
        
        
        print("erreur,essayer une autre fois, {}.".format(joueur))
        
    
    l[int(r1) - 1] -= int(r2)

    
    prochain_tour(l, tt, jj)
 
def prochain_tour(l, rt, jj): 
    global tours
    tours += 1

    print("-" * 25)
    for i in range(0, rt):
        _r = 23 - l[i]
        print(" {} | {} {}".format(i + 1, '*' * l[i], ' ' * _r),'|', l[i])
         
    print("-" * 25)

main()
while 1<2 :
    i=0

