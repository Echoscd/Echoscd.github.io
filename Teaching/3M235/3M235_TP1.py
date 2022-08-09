# 3M235 TP1
# Script incomplet créant un mini moteur de rendu 3D.
# Le script est abondamment commenté pour faciliter sa lecture.
# Les parties à compléter sont indiquées par des !!!TO DO!!!
# S'il est complété de manière correcte, son exécution doit ouvrir une fenêtre dans laquelle est représenté un cube de couleur.
# Les actions de la souris (clic+déplacement) doivent faire tourner le cube en 3D de manière naturelle (si le mouvement est peu
# naturel ou si le cube se déforme c'est que certaines des parties complétées sont à revoir).

import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin

def mult(q1,q2):
    # Ecrire ici la fonction permettant de faire la multiplication 
    # des quaternions q1 et q2
    # !!!TO DO!!!!
    return # !!!TO DO!!!!
    
def conj(q):
    # Ecrire ici la fonction renvoyant le quaternion conjugué du quaternion
    # fourni en entrée
    # !!!TO DO!!!!
    return # !!!TO DO!!!!
def rot(v,q):
    # écrire ici la fonction permettant d'appliquer au vecteur v la rotation
    # décrite par le quaternion (supposé de norme unité) q
    # !!!TO DO!!!!  
    return # !!!TO DO!!!!

# On liste ici les 8 sommets d'un cube de coté 2 dans R^3 centré en l'origine      
points=np.array([
                    [-1,-1,-1],
                    [1,-1,-1],
                    [1,-1,1],
                    [-1,-1,1],
                    [-1,1,-1],
                    [1,1,-1],
                    [1,1,1],
                    [-1,1,1]
                ])
# On liste ici les 6 faces de ce sommets, chaque face étant une liste de 4 indices de sommets (se référant à la liste "points" ci-dessus).
# La première face comporte ainsi les sommets  [-1,-1,-1], [1,-1,-1], [1,-1,1] et [-1,-1,1].
idx_faces = np.array([
        [0,1,2,3],
        [1,5,6,2],
        [2,6,7,3],
        [4,5,6,7],
        [0,3,7,4],
        [0,1,5,4]
        ])
        
# Les couleurs qui seront appliquées aux faces, pour une visualisation facilitée.
color_faces=['red','green','blue','orange','black','yellow']

# On crée une classe "scene", il s'agit juste d'un conteneur qui regroupe les sommets, les faces et les couleurs des faces 
# (qui sont passées dans l'ordre au constructeur __inti__ de la classe).
class Scene:
    def __init__(self,points,idx_faces,color_faces):
        self.points=points
        self.nbr_points = points.shape[0]
        self.idx_faces=idx_faces
        self.nbr_faces = idx_faces.shape[0]
        self.color_faces=color_faces
        return

# On crée une classe Camera. Le constructeur de la classe commence par creer un espace de tracé (via l'appel à plt.subplots() 
# de matplotlib), construit des polygones (classe plt.Polygon de matplotlib) pour chacune des faces, et les ajoutes à la figure. 
# Noter que la camera est initialisée avec un repère égal à celui de la scène. 
class Camera:
    def __init__(self,scene):
        self.scene=scene
        # création de la figure (fig) et des axes (ax)
        self.fig,self.ax=plt.subplots()
        # initialisation de point_de_vue confondue avec le repère canonique.
        self.point_de_vue=np.array([0,0,0,1])
        # créations des faces (avec couleur attribuées et un peu de transparence (alpha=0.5) pour une meilleure visualisation.
        self.faces = [plt.Polygon([scene.points[i][:2] 
                for i in scene.idx_faces[j]],facecolor=scene.color_faces[j],alpha=0.5) 
                for j in range(len(scene.idx_faces))]
        # limites de visualisation selon chaque axe du plan de la camera 
        self.ax.set_xlim([-3,3])
        self.ax.set_ylim([-3,3])
        # ajout effectif des faces au tracé.
        for face in self.faces:
            self.ax.add_patch(face)
    def maj_point_de_vue(self,dx,dy):
        # dx et dy correspondent au nombre de pixels dont a été bougée la souris depuis la dernière mise à jour.
        # On transforme ces deux nombres en des angles de rotation suivant x et y (penser que x et y sont dans le plan
        # de caméra, alors que z est perpendiculaire à l'écran: si la souris est bougée à l'horizontal (dx non nul) on veut
        # faire pivoter la scène/caméra suivant l'axe y (négativement); inversement si la souris est bougée verticalement (dy non nul)
        # on veut faire pivoter la scène/caméra suivant l'axe x (faire un dessin pour bien comprendre!).
        theta_x = dy/100
        theta_y=-dx/100
        # Ecrire ici un quaternion correspondant à une rotation d'angle theta_x suivant l'axe x
        qx = # !!!TO DO!!!!
        # Ecrire ici un quaternion correspondant à une rotation d'angle theta_y suivant l'axe y
        qy = # !!!TO DO!!!!
        # Ecrire ici la mise à jour du quaternion self.point_de_vue en le composant (= multipliant!) avec les rotations q_x et q_y.
        self.point_de_vue = # !!!TO DO!!!!
        # On appelle ensuite la fonction de tracé avec le nouveau point de vue (cfr ci-dessous)
        self.maj_rendu()
    def maj_rendu(self):
        # On calcule les coordonnées des sommets de la scène dans le nouveau repère de caméra :
        # Ecrire ici la liste des points de la scène auxquels on applique la rotation déterminée par le quaternion self.point_de_vue
        projected_points = # !!!TO DO!!!!
        # On met à jour les coordonnées des sommets des faces dans le nouveau repère.
        for i in range(len(self.faces)):
            self.faces[i].set_xy([projected_points[j][:2] for j in self.scene.idx_faces[i]])
        # Et on demande enfin à matplotlib de raffraichir le tracé avec ces nouvelles données.
        self.fig.canvas.draw()
        
# On crée une classe Souris. Le constructeur de la classe (la fonction __init__) reçoit une instance de caméra. 
# Cette classe va interagir avec la figure matplolib de la caméra.    
class Souris:
    def __init__(self,camera):
        # la variable booléene bouton_enfonce contiendra True si le bouton gauche est maintenu enfoncé, et False sinon
        self.bouton_enfonce=False
        # les coordonnées du dernier clic gauche (seront mis à jour plus bas)
        self.clic_x=0
        self.clic_y=0
        # les déplacements de la souris en horizontal et vertical lors d'un clic maintenu + déplacement de souris
        self.move_x=0
        self.move_y=0
        self.camera=camera
        # Ici on lie l'événement 'button_press_event' (qu'envoie matplotlib à chaque fois que le bouton de la souris 
        # est pressé au dessus de l'espace de la figure) à la fonction self.clic_bouton (que nous crééons nous-même).
        # Idem pour les messages prédéfinis 'button_release_event' et  'motion_notify_event'.
        # Cfr par exemple https://matplotlib.org/users/event_handling.html
        camera.fig.canvas.mpl_connect('button_press_event',self.clic_bouton)
        camera.fig.canvas.mpl_connect('button_release_event',self.relache_bouton)
        camera.fig.canvas.mpl_connect('motion_notify_event',self.bouge_souris)
    # Les fonctions de call-back que nous définissons (event est la variable reçue de la part de matplotlib).    
    def clic_bouton(self,event):
        # En cas de clicl gauche on passe bouton_enfonce à True et on actualise clic_x et clic_y 
        self.bouton_enfonce = True
        self.clic_x=event.x
        self.clic_y=event.y
    def relache_bouton(self,event):
        # Rien d'autre à faire ici que de passer bouton_enfonce à False
        self.bouton_enfonce = False
    def bouge_souris(self,event):
        # L'utilisateur bouge la souris au dessus de la figure :
        # 1) Si le bouton n'est pas enfonce, on ne fait rien
        if not self.bouton_enfonce: return
        # 2) Sinon : on calcule de déplacement depuis la dernière mise à jour
        self.move_x = event.x-self.clic_x
        self.move_y = event.y-self.clic_y
        # On met à jour clic_x et clic_y avec les coordonnées actuelles (même si cela ne correspond pas à un clic...)
        self.clic_x=event.x
        self.clic_y=event.y
        # On appelle la fonction de mise à jour du point de vue de la caméra associée (la caméra qui a été passée dans le constructeur __init__ ci-dessus.
        self.camera.maj_point_de_vue(self.move_x,self.move_y)

# Finalement le programme lui-même

# Création d'une instance de Scene
scene = Scene(points,idx_faces,color_faces)
# Création d'un instance de Camera (on passe la scene au constructeur)
camera = Camera(scene)
# Création d'une instance de Souris (on passe la camera au constructeur)
souris = Souris(camera)
# On lance le tracé initial (tant que la figure n'est pas fermée par l'utilisateur, le tracé sera mis à jour par les
# actions de la souris si nécessaire).
plt.show()
