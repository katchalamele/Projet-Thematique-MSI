import numpy as np
from pylive import *
from Params import DELAY,DT
import logging
logging.basicConfig(filename='simulation.log',level=logging.INFO)

size = round(DT/DELAY)

class Compteur:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        self.nb_croisements = 0
        self.msg_envoyes = 0
        self.msg_recus = 0
        self.satur_reseau = 0
        self.l_crois_min = [0 for i in range(round(60/DELAY))] # pour recuperer dynamiquement le nombre de croisement par minute
        
        self.x_vec = np.linspace(-DT,0,size+1)[0:-1]
        
        self.line_croisements = []
        self.y_vec_croisements = [0 for i in range(len(self.x_vec))]#np.random.randn(len(self.x_vec))

        self.line_envoyes = []
        self.y_vec_envoyes = [0 for i in range(len(self.x_vec))]

        self.line_recus = []
        self.y_vec_recus = [0 for i in range(len(self.x_vec))]

        self.line_crois_min = []
        self.y_vec_crois_min = [0 for i in range(len(self.x_vec))]

        self.line_satur_reseau = []
        self.y_vec_satur_reseau = [0 for i in range(len(self.x_vec))]

    def step(self):
        self.y_vec_croisements[-1] = self.nb_croisements
        self.y_vec_envoyes[-1] = self.msg_envoyes
        self.y_vec_recus[-1] = self.msg_recus
        self.y_vec_crois_min[-1] = self.l_crois_min[-1] - self.l_crois_min[0]
        self.y_vec_satur_reseau[-1] = self.satur_reseau

        self.line_croisements, self.line_envoyes, self.line_recus, self.line_crois_min, self.line_satur_reseau = live_plotter(self.x_vec,self.y_vec_croisements,self.y_vec_envoyes,self.y_vec_recus,self.y_vec_crois_min,self.y_vec_satur_reseau,self.line_croisements,self.line_envoyes,self.line_recus,self.line_crois_min,self.line_satur_reseau)
        
        self.y_vec_croisements = np.append(self.y_vec_croisements[1:],0.0)
        self.y_vec_envoyes = np.append(self.y_vec_envoyes[1:],0.0)
        self.y_vec_recus = np.append(self.y_vec_recus[1:],0.0)
        self.y_vec_crois_min = np.append(self.y_vec_crois_min[1:],0.0)
        self.y_vec_satur_reseau = np.append(self.y_vec_satur_reseau[1:],0.0)

        self.l_crois_min.pop(0)
        self.l_crois_min.append(self.nb_croisements)

    def incr_croisements(self):
        self.nb_croisements += 1
    
    def incr_envoyes(self):
        self.msg_envoyes += 1

    def incr_recus (self):
        self.msg_recus += 1
    
    def incr_satur_reseau (self):
        self.satur_reseau += 1
    
    def decr_satur_reseau (self):
        self.satur_reseau -= 1

    def capture_image(self):
        plt.savefig('Résultats_test.png')