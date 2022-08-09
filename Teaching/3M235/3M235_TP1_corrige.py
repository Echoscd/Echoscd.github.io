import matplotlib.pyplot as plt
import numpy as np
from math import cos, sin

def mult(q1,q2):
    s=q1[0]*q2[0]-q1[1:].dot(q2[1:])
    v=q1[0]*q2[1:]+q2[0]*q1[1:]+np.cross(q1[1:],q2[1:])
    return np.hstack(([s],v))
    
def conj(q):
    return np.array([q[0],-q[1],-q[2],-q[3]])

def rot(v,q):
    return mult(conj(q),mult(np.hstack(([0],v)),q))[1:]
       
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
idx_faces = np.array([
        [0,1,2,3],
        [1,5,6,2],
        [2,6,7,3],
        [4,5,6,7],
        [0,3,7,4],
        [0,1,5,4]
        ])
        
color_faces=['red','green','blue','orange','black','yellow']

class Scene:
    def __init__(self,points,idx_faces,color_faces):
        self.points=points
        self.nbr_points = points.shape[0]
        self.idx_faces=idx_faces
        self.nbr_faces = idx_faces.shape[0]
        self.color_faces=color_faces
        return
        
    
class Souris:
    def __init__(self,camera):
        self.bouton_enfonce=False
        self.clic_x=0
        self.clic_y=0
        self.move_x=0
        self.move_y=0
        self.camera=camera
        camera.fig.canvas.mpl_connect('button_press_event',self.clic_bouton)
        camera.fig.canvas.mpl_connect('button_release_event',self.relache_bouton)
        camera.fig.canvas.mpl_connect('motion_notify_event',self.bouge_souris)
    def clic_bouton(self,event):
        self.bouton_enfonce = True
        self.clic_x=event.x
        self.clic_y=event.y
    def relache_bouton(self,event):
        self.bouton_enfonce = False
    def bouge_souris(self,event):
        if not self.bouton_enfonce: return
        self.move_x = event.x-self.clic_x
        self.move_y = event.y-self.clic_y
        self.clic_x=event.x
        self.clic_y=event.y
        self.camera.maj_point_de_vue(self.move_x,self.move_y)

class Camera:
    def __init__(self,scene):
        self.scene=scene
        self.fig,self.ax=plt.subplots()
        self.point_de_vue=np.array([0,0,0,1])
        self.faces = [plt.Polygon([scene.points[i][:2] 
                for i in scene.idx_faces[j]],facecolor=scene.color_faces[j],alpha=0.5) 
                for j in range(len(scene.idx_faces))]
        self.ax.set_xlim([-3,3])
        self.ax.set_ylim([-3,3])
        for face in self.faces:
            self.ax.add_patch(face)
    def maj_point_de_vue(self,dx,dy):
        theta_x = dy/100
        theta_y=-dx/100
        qx=np.array([cos(theta_x/2),sin(theta_x/2),0,0])
        qy=np.array([cos(theta_y/2),0,sin(theta_y/2),0])
        self.point_de_vue=mult(mult(self.point_de_vue,qx),qy)
        self.maj_rendu()
    def maj_rendu(self):
        projected_points=[rot(point,self.point_de_vue) for point in self.scene.points]
        for i in range(len(self.faces)):
            self.faces[i].set_xy([projected_points[j][:2] for j in self.scene.idx_faces[i]])
        self.fig.canvas.draw()
        



scene = Scene(points,idx_faces,color_faces)
camera = Camera(scene)
souris = Souris(camera)

plt.show()

        
    
    
    
    
