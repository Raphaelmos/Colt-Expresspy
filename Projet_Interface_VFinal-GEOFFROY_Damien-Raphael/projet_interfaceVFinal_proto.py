from cgitb import text
from tempfile import TemporaryDirectory
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image #pip install pillow
import pygame #pip install pygame
from pygame import mixer
import time 
import random
import tkinter.font as font
pygame.init()
#Classe qui représente le jeu
from bandit import *
# game=Tk()
# game.title("rd")
# game.geometry("800x600")
# Code explained in every part and can also have a english version in the future 
# Problems can appear if everything isn't installed for example the music and mp3 format can witness issues 
class Jeu(tk.Tk):
    def __init__(self):    
        
        super().__init__()
        self.title("Colt Express GEOFFROY Damien , Raphael")
        self.geometry("1280x800")

        self.resizable(False,False)
        pygame.mixer.init()
        pygame.mixer.music.load('GhostTownTriumph-HangmanAdamPage_Entrance_Theme.mp3')
        pygame.mixer.music.play(loops=-1)

        self.attributes('-fullscreen', True) 


        def home():#---------- Caracteristique de la page Home, on supprime les fond et boutons inutile et on lance la fonction jeu
            self.pageRules_bg.place_forget()
            self.pageRules2_bg.place_forget()

            
            self.btn_rules_1_PosAlt.place_forget()
            self.btn_rules_2.place_forget()
            self.btn_Home_PosAlt1.place_forget()
            self.btn_Home_PosAlt2.place_forget()

            
            self.btn_game.place(x=1105, y = 395)
            self.btn_rules.place(x=1105, y = 503)
            self.btn_quitMenuPrinc.place(x=1075, y = 610)
            self.pageHome_bg.place(x=0, y = 0)

            

        def game(): #---------- Caracteristique de la page Jeu, on supprime les fond et boutons inutile et on lance la fonction jeu
            self.pageHome_bg.destroy()
            self.pageRules_bg.destroy()
            self.pageRules2_bg.destroy()

            self.btn_game.destroy()
            self.btn_rules.destroy()
            self.btn_quitMenuPrinc.destroy()

            
            def Lancement():
                self.pageNombreJeu_bg.destroy()
                self.nombre_joueur = int(str(nb_joueur.get()))
                self.train()
            
            self.pageNombreJeu_bg.place(x=0, y = 0)
            var_nbJoueur= StringVar()
            nb_joueur = Entry(self,textvariable=var_nbJoueur, bg="#444243",fg="white",font=("Arial", 30),justify="right", highlightthickness=2, width=6,border=0) 
            nb_joueur.config(highlightbackground = "lightgray", highlightcolor="lightgray")
            nb_joueur.place(x=790, y=150)

            self.btn_nb_joueur =Button(self, text="Continuer",font=("Arial", 18),bg="#444243",fg="white", command=Lancement, border=0,activebackground="#444243", activeforeground="darkred")
            self.btn_nb_joueur.place(x=815, y=220)

            # self.nombre_joueur = 5
            
            
            

        def rules(): #---------- Caracteristique de la page Regles 1 , on supprime les fond et boutons inutile et on place que les utiles
            self.pageHome_bg.place_forget()
            self.pageRules2_bg.place_forget()

            self.btn_game.place_forget()
            self.btn_rules.place_forget()
            self.btn_quitMenuPrinc.place_forget()
            self.btn_rules_1_PosAlt.place_forget()
            self.btn_Home_PosAlt2.place_forget()

            self.btn_Home_PosAlt1.place(x=1010, y = 607)
            self.btn_rules_2.place(x=955, y = 450)
            self.pageRules_bg.place(x=0, y=0)
        
        def rules2(): #---------- Caracteristique de la page Regles 2 , on supprime les fond et boutons inutile et on place que les utiles
            self.pageHome_bg.place_forget()
            self.pageRules_bg.place_forget()

            self.btn_Home_PosAlt1.place_forget()
            self.btn_rules_2.place_forget()

            self.btn_Home_PosAlt2.place(x=602, y = 18)
            self.btn_rules_1_PosAlt.place(x=100, y = 575)
            self.pageRules2_bg.place(x=0, y=0)

        


        #--------Creation des Fonds du Menu Principal----------------
        self.backgroundMainMenu_image=ImageTk.PhotoImage(Image.open("colt_express_mainmenu2.jpg"))
        self.pageHome_bg=Label( self, image=self.backgroundMainMenu_image)
        self.pageHome_bg.place(x=0, y = 0)
     

        self.backgroundRules_image=ImageTk.PhotoImage(Image.open("rules.png"))
        self.pageRules_bg = Label( self, image=self.backgroundRules_image)
    
        self.backgroundRules2_image=ImageTk.PhotoImage(Image.open("Rules2.png"))
        self.pageRules2_bg = Label( self, image=self.backgroundRules2_image)

        self.backgroundNombreJeu_image=ImageTk.PhotoImage(Image.open("nb_joueur_bg.png"))
        self.pageNombreJeu_bg = Label( self, image=self.backgroundNombreJeu_image)



        #-------- Bouton Principaux de la page daccueil "Home" ------------
        texte_game= font.Font(family='Helvetica', size=22, weight='bold',underline=1)
        self.btn_game = Button(self, text= "Play" , font=texte_game ,border=0,bg="#fee0b7", activebackground="#fee0b7", fg="red", activeforeground="blue",command=game)

        texte_regle_menu= font.Font(family='Helvetica', size=18, weight='bold',underline=1)
        self.btn_rules = Button(self, text= "Regles" , font=texte_regle_menu ,border=0,bg="#fee0b7", activebackground="#fee0b7", fg="red", activeforeground="blue",command=rules)

        texte_quitter_jeu= font.Font(family='Helvetica', size=15, weight='bold',underline=1)
        self.btn_quitMenuPrinc = Button(self, text= "Quitter Le Jeu" , font=texte_quitter_jeu ,border=0,bg="#fee0b7", activebackground="#fee0b7", fg="red", activeforeground="blue",command=quit)


        #-------- Boutons de la page "Regles 1" , ils ont des positions et caractéristique differente -----------------
        texte_home_pre1= font.Font(family='Helvetica', size=25, weight='bold',underline=1)
        self.btn_Home_PosAlt1=Button(self, text= "Home" , font=texte_home_pre1 ,border=0,bg="#d98a40", activebackground="#d98a40", fg="red", activeforeground="blue",command=home)

        texte_rules_suiv= font.Font(family='Helvetica', size=20, weight='bold',underline=1)
        self.btn_rules_2 = Button(self, text= "Regles Suivante" , font=texte_rules_suiv ,border=0,bg="#d98a40", activebackground="#d98a40", fg="red", activeforeground="blue",command=rules2)


        #-------- Boutons de la page "Regles 2" , ils ont des positions et caractéristique differente de la page "Regle1"-----------------
        texte_home_pre2= font.Font(family='Helvetica', size=28, weight='bold',underline=1)
        self.btn_Home_PosAlt2=Button(self, text= "Home" , font=texte_home_pre2 ,border=0,bg="#e3923a", activebackground="#e3923a", fg="red", activeforeground="blue",command=home)

        texte_rules_pre= font.Font(family='Helvetica', size=20, weight='bold',underline=1)
        self.btn_rules_1_PosAlt = Button(self, text= "Regles Precedentes" , font=texte_rules_pre ,border=0,bg="#ec9b35", activebackground="#ec9b35", fg="red", activeforeground="blue",command=rules)

       

        #---------Placement des boutons pour la page d'accueil--------------
 
        self.btn_game.place(x=1105, y = 395)
        self.btn_rules.place(x=1105, y = 503)
        self.btn_quitMenuPrinc.place(x=1075, y = 610)


        # self.nombre_joueur = 6
        # self.train()
       

    def train(self):
        fichier = open("ID_liste_wagons.txt")
        ids = []
        for ligne in fichier:
            ligne = ligne.rstrip("\n")
            ids.append(ligne)
        fichier.close()

        
        # nombre_joueur= int(input("Combien de joueur vont jouer ?"))
        self.canvas_train2= Canvas(self, width=1100, height=800, bg="red")
        self.canvas_train2.place(x=0, y=0)

        self.backgroundJeu=ImageTk.PhotoImage(Image.open("backgroundJeu2.png"))
        self.canvas_train2.create_image(0, 0, image=self.backgroundJeu, anchor="nw") 

        # Data to be written
        self.label_x=-50

        # while ( self.label_x < 1000 ):
        
        
        
        self.imgs = []
        creation = True

        if (self.nombre_joueur <=0):
            self.nombre_joueur=1
        if (self.nombre_joueur >=10):
            self.nombre_joueur= 10
        while creation == True:
            for i in range(self.nombre_joueur):
                
                taille_differente=[602,390,267,200,160,134,115,100,89,80,72]
                image_wagon = Image.open("wagon3.png")
                
                largeur_wagon=taille_differente[self.nombre_joueur-1]
                nouvelleTaille_image_wagon= image_wagon.resize((largeur_wagon, 350))
                self.imgs.append(ImageTk.PhotoImage(nouvelleTaille_image_wagon))

                self.canvas_train2.create_image(largeur_wagon*i , 250, image=self.imgs[-1], anchor="nw") 
 
                


            # 678  X  358
            print(largeur_wagon)
            indice_decallage=  largeur_wagon * (self.nombre_joueur) 

            taille_loc_differente=[478,309,226,170,134,113,97,85,75,68,62]
            image_wagon = Image.open("locomotive3.png")
            largeur_locomotive=taille_loc_differente[self.nombre_joueur-1]
            nouvelleTaille_image_locomotive= image_wagon.resize((largeur_locomotive, 358))
            self.imgs.append(ImageTk.PhotoImage(nouvelleTaille_image_locomotive))

            self.canvas_train2.create_image(indice_decallage, 250, image=self.imgs[-1], anchor="nw") 

           
            
        
            creation = False
            self.bandit()

        
    def bandit(self):

        self.image_bandit = Image.open("voleur.png")
        self.image_bandit= self.image_bandit.resize((70, 100))
        self.image_bandit=ImageTk.PhotoImage(self.image_bandit)
        self.create_image((0, 0),anchor=NW,image=self.image_bandit) 

        texte_bouton= font.Font(family='Helvetica', size=18, weight='bold',underline=1)
        # self.TEST = Button(self, text= "BOUTON" , font=texte_bouton ,border=0,bg="#fee0b7", activebackground="#fee0b7", fg="red", activeforeground="blue",command=lambda:Bandit(self, 0,0,self.label_x ).deplacer())
        self.TEST = Button(self, text= "BOUTON" , font=texte_bouton ,border=0,bg="#fee0b7", activebackground="#fee0b7", fg="red", activeforeground="blue")
        self.TEST.place(x=1200,y=200)


        texte_quitter_jeu2= font.Font(family='Helvetica', size=15, weight='bold',underline=1)
        self.btn_quitMenu2 = Button(self, text= "Quitter Le Jeu" , font=texte_quitter_jeu2 ,border=0,bg="#fee0b7", activebackground="#fee0b7", fg="red", activeforeground="blue",command=quit)
        self.btn_quitMenu2.place(x=1200,y=400)

    #essai de boutons
  #  def ui(self):

   #     self.play = Frame(self.win, bg="black", height=int(self.height*0.2), width=int(self.width*0.2))
#	    if self.play:
#			imgpath = Image.open("play.png").resize((int(self.width * 0.10), int(self.height*0.10)), Image.NEAREST)
#			img = ImageTk.PhotoImage(imgpath)
#			self.playBtn = Button(self.play, image=img, command=self.PlayTurn)
#			self.playBtn.image = img
#			self.playBtn.place(anchor="nw", x=0, y=self.height*0.05)
#		    self.play.place(x=self.width*0.8, y=self.height*0.6)
#		    self.stats = Frame(self.win, bg="black", height=int(self.height*0.2), width=int(self.width*0.2))
#		if self.stats:
#			self.playerNum = Label(self.stats, text=f"Joueur numéro : {self.bandit+1}").place(anchor="nw")
#			self.playersNum = Label(self.stats, text=f"{len(NOMS_BANDITS)} joueur(s) dans la partie").place(anchor="nw", y=int(self.height * 0.05))
#			self.posMarsh = Label(self.stats, text=f"Marshall dans le wagon:{-1}").place(anchor="nw",x=int(self.width * 0.1), y=int(self.height * 0.05))
#		self.stats.place(x=self.width*0.8, y=self.height*0.8)       
        
        
        
        
    #     taille_differente=[602,390,267,200,160,134,115,100,89,80,72]


    #     self.canvas_bandit= Canvas(self, width=1100, height=800, bg="red")
    #     self.canvas_bandit.place(x=0, y=0)
        

    #     self.image_bandit = Image.open("voleur.png")
        
    #     nouvelleTaille_image_bandit=  self.image_bandit.resize((70, 100))
    #     self.image_bandit= ImageTk.PhotoImage(nouvelleTaille_image_bandit)
        
    #     self.canvas_bandit.create_image(100 , 250, image=self.image_bandit, anchor="nw") 





    #     taille_differente=[602,390,267,200,160,134,115,100,89,80,72]

    #     self.label_x= ( taille_differente[self.nombre_joueur] ) / 2

    #     xort=True
    #     # while (xort==True):
        # def avancer(self):

        #     self.image_bandit.place_forget()
        #     self.label_x += 50
        #     self.image_bandit.placeconfigure(x=self.label_x, y=0)
        #     return self.label_x
        



        # @classmethod
        # def 
                    
# class Bandit(Canvas): #herite de canvas
#     def __init__(self,jeu,x,y,label_x): #APPEL de x et y comme ca on peut modifier apres et  jeu qui prendra self donc LENSEMBLE DE JEU
#         super().__init__(height=100, width=50)    #herite de toute la classe Jeu  ET ON PRECISE SEULEMENT QUELQUE PARAMAETER
#         self.x= x 
#         self.y=y 
#         self.place(x=self.x, y=self.y)#place canvass au coordonee donnee 
#         self.jeu= jeu
#         self.label_x= label_x
#         print(type(jeu))
#         # self.canvas_tronne= jeu.

        

#         self.image_bandit = Image.open("voleur.png")
#         self.image_bandit= self.image_bandit.resize((70, 100))
#         self.image_bandit=ImageTk.PhotoImage(self.image_bandit)
#         self.create_image((0, 0),anchor=NW,image=self.image_bandit) #coord X Y du canvas  accrocher au point Nord-est , et limage  

        
#         # self.label_x = -50 
#         self.deplacer()
        

#     def deplacer(self):
             
#         if(self.label_x <= 0 ):
#             self.place_forget()
#             self.fichier_pos_Ennemy = open("position_ennemy.txt","w+")
            
#             content = self.fichier_pos_Ennemy.readlines()

#             for line in content:
     
#                 for i in line:
#                     if i.isdigit() == True:
#                         self.pos_ennemy= int(i)

#             # self.pos_ennemy= int(self.pos_ennemy)
            
#             self.label_x =self.pos_ennemy+  50

            





#             self.place(x=self.label_x, y=0)
#             self.label_x= repr(self.label_x)
#             self.fichier_pos_Ennemy.write(self.label_x)
#             self.fichier_pos_Ennemy.close()

#             # return self.label_x
#             # self.after(1000, self.deplacer)    
        
#         elif ( 0 < self.label_x ) and (self.label_x < 600) :
#             self.place_forget()
#             sens_direction= random.randint(0, 1)
#             if sens_direction == 0:
#                 self.label_x -= 50
#             else:
#                 self.label_x += 50
#             # self.label_x += 50
#             self.place(x=self.label_x, y=0)
#             # return self.label_x
#             # self.after(1000, self.deplacer)

          

#         elif(600 <= self.label_x ):
#             self.place_forget()
#             self.label_x -= 50
#             self.place(x=self.label_x, y=0)
#             return self.label_x
#             # self.after(1000, self.deplacer)        
        
#         print(self.label_x)
        
#         # return 1 
    
                 

        # root = Tk()
        # cnv = Canvas(jeu.canvas_train, bg="white", width=200, height = 200)
        # cnv.place(x=0, y=0)
    
    
        # root.mainloop()


    # def quitterJeu(self): #Pour le bouton quitter , on ferme la fenetre de jeu
    #     self.quit()

    

Jeu_Colt= Jeu()
    


#---------Touche clavier Pour Indice
def indiceClavier(event):
        event=True
        Jeu_Colt.fonction()
        # return mon_jeu     
#indiceU(event=True)
Jeu_Colt.bind("<Key-i>",indiceClavier)
Jeu_Colt.bind("<Key-I>",indiceClavier)

# #---------Touche Clavier Pour Reinitialiser
# def resetAllClavier(event):
#         event=True
#         mon_jeu.resetAll()
#         return mon_jeu    
# #resetAllU(event=True)
# mon_jeu.bind("<Key-r>",resetAllClavier)
# mon_jeu.bind("<Key-R>",resetAllClavier)

# #---------Touche Clavier Pour Validation
# def validationClavier(event):
#         event=True
#         mon_jeu.validation()
#         return mon_jeu   
# #validationU(event=True)
# mon_jeu.bind("<Key-v>",validationClavier)
# mon_jeu.bind("<Key-V>",validationClavier)

# #---------Touche Clavier  Pour Eteindre Musique
# def musiqueOffClavier(event):
#         event=True
#         mon_jeu.musiqueEteint()
#         return mon_jeu   
# mon_jeu.bind("<Key-m>",musiqueOffClavier)
# mon_jeu.bind("<Key-M>",musiqueOffClavier)

# #---------Touche Clavier  Pour Allumer Musique
# def musiqueOnClavier(event):
#         event=True
#         mon_jeu.musique()
#         return mon_jeu   
# mon_jeu.bind("<Key-o>",musiqueOnClavier)
# mon_jeu.bind("<Key-O>",musiqueOnClavier)


# #---------Touche Clavier  Pour Quitter le jeu
# def QuitterJeuClavier(event):
#         event=True
#         mon_jeu.quit()
#         return mon_jeu   
# mon_jeu.bind("<Key-q>",QuitterJeuClavier)
# mon_jeu.bind("<Key-Q>",QuitterJeuClavier)





Jeu_Colt.mainloop()
