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
lieux_travail = ()
lieux_pause = ()
lieux_domiciles = ()

derniers_croisements = ()

for i in range(1, NBLIEUX_T+1):
    lt = Lieu(i, "Travail", "Travail"+str(i))
    lieux_travail += lt,
    lt.draw(c)

for i in range(1, NBLIEUX_P+1):
    lp = Lieu(i, "Pause", "Pause"+str(i))
    lieux_pause += lp,
    lp.draw(c)
    

for i in range(1, EFFECTIF+1):
    p = Particule(i)
    ld = Lieu(i, "Domicile", "Domicile"+str(i), p.x, p.y)

    particules += p,
    lieux_domiciles += ld,

    p.draw(c)
    ld.draw(c)
    p.goto(choice(lieux_travail))

    if(random() < 0.5):
        p.createMsg(choice(particules).uuid, "Message")


root.update_idletasks()
root.update()

b = 0

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
                        print('Distance entre', p.uuid, 'et', p2.uuid, '=', d)
                        p.send_all(p2)
    derniers_croisements = croisements

    b+=DELAY
    if b%10 < 0.05 and not any([(not p.standby) for p in particules]):
        print("deede")
        for p in particules:
            p.goto(choice(lieux_pause))
            p.standby=False


    

    root.update_idletasks()
    root.update()
    sleep(DELAY)
