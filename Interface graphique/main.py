from tkinter import Tk,Canvas
from Particule import Particule
from time import sleep
from lib import distance
from Params import *

root = Tk()
root.geometry(str(TAILLE) + 'x' + str(TAILLE))

c = Canvas(root, height=TAILLE, width=TAILLE)
    
c.pack()

particules = set()
derniers_croisements = ()

for i in range(EFFECTIF):
    particules.add(Particule(i+1))

for p in particules:
    p.draw(c)

root.update_idletasks()
root.update()

while True:
    croisements = ()
    for p in particules:
        p.next_move(c)
        for p2 in particules:
            d = distance(p, p2)
            if p2 != p and d <= DC:
                croisement = {p.pid, p2.pid}
                if not croisement in croisements:
                    croisements += croisement,
                    if not croisement in derniers_croisements:    
                        print('Distance entre', p.pid, 'et', p2.pid, '=', d)
    derniers_croisements = croisements

    root.update_idletasks()
    root.update()
    sleep(DELAY)
