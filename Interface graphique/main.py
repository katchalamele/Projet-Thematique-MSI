from tkinter import Tk,Canvas
from Particule import Particule
from Lieu import Lieu
from time import sleep
from lib import distance
from Params import *
from random import choice,random

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
                        p.send_all(p2)
                        p2.send_all(p)
    derniers_croisements = croisements

    clock+=DELAY

    if clock%10 < DELAY and not any([(not p.standby) for p in particules]):
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
                p.standby=False


    

    root.update_idletasks()
    root.update()
    sleep(DELAY)
