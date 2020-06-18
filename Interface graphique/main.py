from tkinter import Tk,Canvas
from time import sleep
from random import choice,random

from Noeud import Noeud
from Lieu import Lieu
from lib import distance
from Params import *
from Compteur import Compteur

root = Tk()
root.geometry(str(TAILLE) + 'x' + str(TAILLE))

c = Canvas(root, height=TAILLE, width=TAILLE)
    
c.pack()
cpt = Compteur()
neouds = ()
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
    p = Noeud(i)
    ld = Lieu(i, "Domicile", "Domicile"+str(i), p.x, p.y)
    p.home = ld
    p.cpt = cpt

    neouds += p,
    lieux_domiciles += ld,

    ld.draw(c)
    p.draw(c)
    p.goto(choice(lieux))

    if(random() < PCM):
        p.createMsg(choice(neouds).uuid, "Message", clock+DVM)
        cpt.incr_envoyes()


root.update_idletasks()
root.update()


while clock < DT:
    croisements = ()
    for p in neouds:
        p.next_move(c)
        for p2 in neouds:
            d = distance(p, p2)
            if p2 != p and d <= DC:
                croisement = {p.uuid, p2.uuid}
                if not croisement in croisements:
                    croisements += croisement,
                    if not croisement in derniers_croisements:
                        #P ET P2 se croisent    
                        #print('noeuds', p.uuid, 'et', p2.uuid, 'se croisent')
                        cpt.incr_croisements()
                        p.send_all(p2)
                        p2.send_all(p)
    derniers_croisements = croisements

    clock+=DELAY

    cpt.step()
    
    if clock%(10*DELAY) < DELAY:
        step+=1
        cpt.logger.info("\n\nClock:"+str(round(clock)))
        cpt.logger.info("nb_croisements: "+str(cpt.nb_croisements))
        cpt.logger.info("msg_envoyes: "+str(cpt.msg_envoyes))
        cpt.logger.info("msg_recus: "+str(cpt.msg_recus))
        cpt.logger.info("satur_reseau: "+str(cpt.satur_reseau)+"\n\n")

        for p in neouds:
            #Suppression de messages expirés
            p.remove_exp_msg(clock)
            
            #Creation probable de nouveaux messages
            if clock < LEM and random() < PCM:
                p.createMsg(choice(neouds).uuid, "Message", clock+DVM)
                cpt.incr_envoyes()
            
            #Retour probable au domiciles
            if p.standby:
                if(random() < 0.2):
                    p.go_home()
                else:
                    p.goto(choice(lieux))
                p.standby=False 

    root.update_idletasks()
    root.update()
    #sleep(DELAY)
cpt.capture_image()

