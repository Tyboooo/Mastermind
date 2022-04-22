from random import randint
COLORS = [(128,128,128),(255,0,0),(0,255,0),(0,0,255),(255,0,255),(255,255,0)]
COULEURS_UNIQUES = True
def setup():
    size(800,600)
    global tour
    global souris
    global plateau
    global tests_realises
    global etat_jeu
    etat_jeu =0
    tests_realises =[]
    tour = 11
    souris = None
    plateau = [[None for i in range(4)] for i in range(12)]
    global combinaison_SECRETE
    combinaison_SECRETE = genere_combinaison_secrete()
    textSize(30)


def draw():
    global souris
    global etat_jeu
    if etat_jeu==0:
        gestionPlateau()
        background(128,64,0)
        afficherPlateau()
        afficherInterface()
        if souris!=None:
            fill(COLORS[souris][0],COLORS[souris][1],COLORS[souris][2])
            ellipse(mouseX,mouseY,50,50)
    else:
        textSize(50)
        if mouseX in range(310,511) and mouseY in range(200,291):
            fill(0,150,150)
        else:fill(0,255,255)
        rect(310,200,200,90,10)
        fill(255)
        if etat_jeu==1:
            text("Bravo !",330,260)

        else:
            text("Perdu !",330,260)

def gestionPlateau():
    global plateau
    global tour
    global tests_realises
    if None not in plateau[tour]:
        if tour:
            tests_realises.append(evalue_combinaison(plateau[tour]))
            tour -=1
        else:
            global etat_jeu
            etat_jeu = 2
    
def afficherPlateau():
    global plateau
    global tests_realises
    
    for i in range(len(tests_realises)):
        fill(50)
        rect(690-i*60+20,20,40,50,5)
        fill(255)
        text(str(tests_realises[i][0]),690-i*60+30,55)
        fill(50)
        rect(690-i*60+20,425,40,50,5)
        fill(255,0,0)
        text(str(tests_realises[i][1]),690-i*60+30,467)
        if 4 in tests_realises[i]:
            global etat_jeu
            etat_jeu = 1
    
    
    fill(50)
    rect(15,65,770,370,15)
    for j in range(4):
        for i in range(12):
            if plateau[i][j] ==None:
                fill(0)
                ellipse(i*60+70,j*83+120,40,40)
            else:
                fill(COLORS[plateau[i][j]][0],COLORS[plateau[i][j]][1],COLORS[plateau[i][j]][2])
                ellipse(i*60+70,j*83+120,50,50)
    
def afficherInterface():
    for i in range(6):
        fill(COLORS[i][0],COLORS[i][1],COLORS[i][2])
        ellipse(i*80+200,520,50,50)
                
def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**.5

def genere_combinaison_secrete():
  combinaison = []
  while len(combinaison) < 4:
    couleur = randint(0,5)
    if not (COULEURS_UNIQUES):
      combinaison.append(couleur)
    else:
      deja = False
      ind = 0
      while not (deja) and ind < len(combinaison):
        if combinaison[ind] == couleur:
          deja = True
        else:
          ind = ind + 1
      if not (deja):
        combinaison.append(couleur)
  return combinaison

def evalue_combinaison(combinaison):
    global combinaison_SECRETE
    nb_bien_places = 0
    nb_mal_places= 0
    print(combinaison,combinaison_SECRETE)
    for i in range(len(combinaison)): 
        if combinaison[i] == combinaison_SECRETE[i]:
            nb_bien_places =  nb_bien_places +  1
        else:
            for j in range(len(combinaison)):
                if combinaison[i] == combinaison_SECRETE[j] and i != j:
                    nb_mal_places = nb_mal_places+1
    return [nb_bien_places,nb_mal_places]


def mousePressed():
    if etat_jeu:
        if mouseX in range(310,511) and mouseY in range(200,291):setup()
    else:
        global souris
        for i in range(6):
            if distance(mouseX,mouseY,i*80+200,520)<=50:
                souris = i
                break
            
def mouseReleased():
    global souris
    global tour
    global plateau
    for i in range(4):
        if distance(mouseX,mouseY,tour*60+70,i*83+120)<=40:
            plateau[tour][i]=souris
            break
    souris = None
