from tkinter import Tk,Canvas
from Particule import Particule
from Lieu import Lieu
from time import sleep
from lib import distance
from Params import *
from random import choice,random
from pylive import live_plotter
import numpy as np

root = Tk()
root.geometry(str(TAILLE) + 'x' + str(TAILLE))

c = Canvas(root, height=TAILLE, width=TAILLE)
    
c.pack()

particules = ()
lieux = ()
lieux_domiciles = ()

derniers_croisements = ()

clock = 0
step = 1
nb_croisements = 0

# Création des Lieux
for i in range(1, NBLIEUX+1):
    lt = Lieu(i, "Lieu Abstrait", "Lieu"+str(i))
    lieux += lt,
    lt.draw(c)
    

# Création des Noeuds et de leurs domiciles et creation des premiers messaegs
for i in range(1, EFFECTIF+1):
    p = Particule(i)
    ld = Lieu(i, "Domicile", "Domicile"+str(i), p.x, p.y)
    p.home = ld

    particules += p,
    lieux_domiciles += ld,

    ld.draw(c)
    p.draw(c)
    p.goto(choice(lieux))

    if(random() < PCM):
        p.createMsg(choice(particules).uuid, "Message", clock+DVM)


root.update_idletasks()
root.update()


size = 500
x_vec = np.linspace(0,1,size+1)[0:-1]
y_vec = [0 for i in range(len(x_vec))]#np.random.randn(len(x_vec))
line1 = []


while True:
    croisements = ()
    for p in particules:
        p.next_move(c)
        for p2 in particules:
            d = distance(p, p2)
            if p2 != p and d <= DC:
                croisement = {p.uuid, p2.uuid}
                if not croisement in croisements:
                    croisements += croisement,
                    if not croisement in derniers_croisements:
                        #P ET P2 se croisent    
                        print('noeuds', p.uuid, 'et', p2.uuid, 'se croisent')
                        nb_croisements += 1
                        p.send_all(p2)
                        p2.send_all(p)
    derniers_croisements = croisements

    clock+=DELAY

    y_vec[-1] = nb_croisements
    line1 = live_plotter(x_vec,y_vec,line1)
    y_vec = np.append(y_vec[1:],0.0)

    """ if clock%10 < DELAY and not any([(not p.standby) for p in particules]):
        step+=1
        print("####STEP", step, "  Clock:", round(clock)," ####")
        for p in particules:
            #Suppression de messages expirés
            p.remove_exp_msg(clock)
            
            #Creation de nouveaux messages
            if(random() < 0.1):
                p.createMsg(choice(particules).uuid, "Message", clock+DVM)

        if step%5 == 0:
            for p in particules:
                p.go_home()
        else:
            for p in particules:
                p.goto(choice(lieux))
                p.standby=False """
    
    if clock%5 < DELAY:
        step+=1

        for p in particules:
            #Suppression de messages expirés
            p.remove_exp_msg(clock)
            
            #Creation de nouveaux messages
            if(random() < 0.1):
                p.createMsg(choice(particules).uuid, "Message", clock+DVM)

            if p.standby:
                if(random() < 0.2):
                    p.go_home()
                else:
                    p.goto(choice(lieux))
                p.standby=False

    

    root.update_idletasks()
    root.update()
    sleep(DELAY)
