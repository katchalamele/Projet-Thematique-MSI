#### Parametres d'affichage ####
TAILLE  = 800    # Taille de la fenêtre
R = 7            # Taille des rayons des neouds 
RL = 30          # Taille des rayons des Lieux

#### Parametres de déplacement aléatoires des neouds ####
MMD = 5          # Distance Maximale de deplacement par temps
MA = 45          # Angle maximal de rotation par temps (en degrés)
DELAY = 0.5     # Delai entre chaque temps (en seconde)

#### Parametres de l'algorithme ####
EFFECTIF = 20    # Nombre de neouds
NBLIEUX = 5      # Nombre de Lieux Abstraits
TTL = 10          # Time to live
DVM = 300        # Durée de vie des Messages
PCM = 0.2        # Probabilité de création de message (1 => 100%)
CP = 200         # Capacités des noeuds
BT = 50          # Batteries initiales des noeuds
DT = 600         # Durée totale de simulation
LEM = 300        # Limite d'envoie des messages (secondes après lesquelles on envoie plus de message)
DC = 2          # Distance maximale de croisement

Params = {
    'EFFECTIF' : EFFECTIF,
    'NBLIEUX' : NBLIEUX,

    'TTL' : TTL,
    'DVM' : DVM,
    'PCM' : PCM,
    'Capacité' : CP,
    'Batterie' : BT,
    'Durée simulation' : DT,
    'Limite Message' : LEM,
    'DC' : DC
}