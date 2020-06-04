import numpy as np
from pylive import live_plotter

size = 500

class Compteur:
    def __init__(self):
        self.nb_croisements = 0
        self.msg_envoyes = 0
        self.msg_recus = 0
        
        self.x_vec = np.linspace(0,1,size+1)[0:-1]
        
        self.line_croisements = []
        self.y_vec_croisements = [0 for i in range(len(self.x_vec))]#np.random.randn(len(self.x_vec))

        self.line_envoyes = []
        self.y_vec_envoyes = [0 for i in range(len(self.x_vec))]

        self.line_recus = []
        self.y_vec_recus = [0 for i in range(len(self.x_vec))]

    def step(self):
        self.y_vec_croisements[-1] = self.nb_croisements
        self.line_croisements = live_plotter(self.x_vec,self.y_vec_croisements,self.line_croisements)
        self.y_vec_croisements = np.append(self.y_vec_croisements[1:],0.0)

        self.y_vec_envoyes[-1] = self.msg_envoyes
        self.line_envoyes = live_plotter(self.x_vec,self.y_vec_envoyes,self.line_envoyes)
        self.y_vec_envoyes = np.append(self.y_vec_envoyes[1:],0.0)

        self.y_vec_recus[-1] = self.msg_recus
        self.line_recus = live_plotter(self.x_vec,self.y_vec_recus,self.line_recus)
        self.y_vec_recus = np.append(self.y_vec_recus[1:],0.0)

    def incr_croisements(self):
        self.nb_croisements += 1
    
    def incr_envoyes(self):
        self.msg_envoyes += 1

    def incr_recus (self):
        self.msg_recus += 1