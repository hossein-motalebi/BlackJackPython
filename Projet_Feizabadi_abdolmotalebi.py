import random
def version1():
    """
    bonjour,
    projet black jack de FEIZABADI,Seyedmohammadghasem et ABDOLMOTALLEBI,Seyed Hossein
    notre projet est divisé en 3 partie comme besoin , Une partie de jeu sans mise,
    une partie de jeu avec mise et un avec mise et le croupier ensemble
    et donc cette partie est la premiere partie sample et sans mise
    (en espérant que vous nous excusiez pour les fautes du français dans les commentaires
    car nous ne somme pas francophone. )
    """
    bonne_reponse={"ouis":["oui","Oui","Yes","yes","ouais","Ouais","yea","yeah","y","OUI"], #les posibilite de variante ouis ou nons utilisatur peut entrer
                "nons":["non","Non","No","no","na","Nah",'nah','nope','n']}
    def paquet(): #def qui contient un paquet de 52 cart dans une list
        a=range(2,11)
        list_de_nombre=["as","valet", "dame", "roi"] 
        list_de_nombre.extend(a)
        paquet=[]
        for i in list_de_nombre: #on crée les cartes en utilisant les nombre de dans notre list
            msg1=str(i)+" de pique"
            paquet.append(msg1)
            msg2=str(i)+" de coeur"
            paquet.append(msg2)
            msg3=str(i)+" de trèfle"
            paquet.append(msg3)
            msg4=str(i)+" de carreau"
            paquet.append(msg4)
        return paquet

    """une fonction supplémentaire pour avoir toutes les valeur"""
    def init_valeur():
        return  {"as":[1,11],"2 ":2,"3 ":3,"3 ":3,"4 ":4,"5 ":5,
                "6 ":6,"7 ":7,"8 ":8,"9 ":9,
                "10":10,"va":10,"da":10,"ro":10}

    def valeurCarte(carte):    #cette fonction renvois le valeur d'une carte demandé
        valeur=init_valeur()
        mot_cle=carte[:2]   #pour  prendre uniquement nom de cartes
        if mot_cle=='as':
            val=int(input('1 ou 11?\n')) #on demande le utilisateur si il veut un valeur de 1 ou 11 pour l'as
            while not(val==1 or val==11):
                val=int(input('1 ou 11?\n'))
        else: val=valeur[mot_cle]
        return val

    def initPioche(n): # cette fonction mettre n fois de la pioche dans une liste et le melange et renvois le list
        import random
        liste=[]
        for i in range(n):
            l=paquet()
            liste+=l
        random.shuffle(liste)
        return liste

    def piocheCarte(p,x=1): #cette fonction renvois X carte au sommet de la pioche p et les suprimer de la pioche
        liste=[]
        for i in range(x):
            liste.append(p.pop())#une fois retirer le premier element, le suivant va le remplacer, donc il faut retirer toujour le premier
        return liste

    def initJoueurs(n): #renvois les nombre de joueurs(n) avec leur nom en les demandant
        liste=[]
        for i in range(n):
            liste.append(input('entrez le nom de joueur:\n'))
        return liste

    """ cette fonction prendre la liste de jouers et les mettre dans un dicionaire avec valeur intiale de 0 """
    def count_joueurs(joueurs): 
        count=dict()
        for m in joueurs:
            count[m]=0
        return count
    """
    une exemple d'éxecution:
    print(count_joueurs(['mamad','hossein','reza','reza']))
    ==>{'mamad': 0, 'hossein': 0, 'reza': 0}
    """

    """ cette function prendre la liste de valeur et utilise la fonction count_joueurs au dussus 
        pour les mettre dans une dictionaire mais ce que cette fonction faire c'est qu'il observe 
        si on a 2 nom qui sont pareille et après si on a une il ajoute une *pour le doublicate
    """
    def initScores(joueurs,v=0): 
        d=dict()
        x=list()
        count=count_joueurs(joueurs)
        for i in joueurs:
            if i in x:#commme on n'a pas droit d'avoir les memes mots cles donc on ajoute un indice si les  noms son identique
                count[i]+=1
                i=i+('*'*count[i])
            x.append(i) #on ajoute les nom qu'on entre dans le dict pour qu'on puisse remarqur le doublicate
            d[i]=v
        return d
    """   
    exemple de éxécution:
    print(initScorese(['mamad','hossein','reza','reza'],5))
    ==> {'mamad': 5, 'hossein': 5, 'reza': 5, 'reza*': 5}
    """
    def premierTour(joueurs): #cette fonction prendre la liste de joueurs et il pioche 2 carte pour chaque joueurs et ajoute 
                            #les valeur des carte pour aux dans une dictionaire et le renvois
        nomandscore=initScores(joueurs)  #on initialise  les joueurs avec un valeur de 0 et les mettre dans cette variable
        cartes=initPioche(len(joueurs)) #la pioche contenant n fois de la pioche principale va se placer dans cette variable
        for i in nomandscore:  # on prendre joueur de (i) de la liste
            n=0               #valeur ini
            listcartesp=piocheCarte(cartes,2)  #on sorte 2 carte de la liste de notre pioche
            for j in listcartesp: # on ajoute les valeur de cela dans un variable 
                n+=valeurCarte(j)
            nomandscore[i]=n #on mis à jour le valeur de joueur
        return nomandscore , cartes

    """ generalement cette fonction c'est pour verifier si on a les score qui sont egale
        donc on a plus d'un gagnant et renvois nom des gagnants.
        cette fonction prendre un score(vol) ( un values de notre dict)
        et le dicionaire et il renvois toutes les cle(les nom) qui ont ce score.
        """
    def keys(dic,val):
        liste=list()
        for i in dic:
            if dic[i]==val:
                liste.append(i)
        return liste

    def gagnant(score): #cette fonction prendre le dictionaire des joueur avec leur score et renvois le gagnant(qui est plus proche de 21)
        values=list(score.values())  #score.valeurs() cette code nous donne les valeur des cle d'un dict donc on les extrit
        ecart=21 #le maximom valeur de point
        vic=0
        for i in values:
            if i<=21 and (21-i)<=ecart: #a chaque boucle on verifie si on a un score plus proche
                vic=i #on enregistre le score de gagnant
                ecart=21-i #ecart garde la distance de plus proche score a 21
        rep=keys(score,vic) #en utilisent cette fonction on prends nom(s) des gagnant(s) dans une list
        rep.append(vic)# on ajoute le score dans la liste avec sa nom
        return rep

    def continu():  #on veut savoir si utilisatur veut continuer ou non
        cont=False #on initialise avec false donc if utilisatur ne tape pas oui le fonction directement renvois false
        msg="Vous voulez continuer?\n"
        continu=input(msg)

        while not(continu in bonne_reponse['ouis']) and not(continu in bonne_reponse['nons']):
            continu=input(msg)
        if continu in bonne_reponse['ouis']: #aprés d'avoir filtrer if le mot entrer n'est pas oui dont il est non
            cont=True
        return cont


    def tourJoueur(j,dict_joueur,cartes,tour,les_perdu):
        """
        ici on prends le noms du joueur les infos sur leurs scores et les cartes qui restebt
        le numero de tours et la dictionnares de ceux qui sont retirés
        on demande à joueur s'il veux continuer on non si oui on pioches une carte 
        puis on vérifie qu'il a passé de 21 ou non pour le retirer de la listes de courants
        et s'il ne veux plus continuer on le retire de liste des courant en plus tous ceux qui
        seront retirés il seront ajouter à la dict les_perdu avec leurs scores'
        """
        print(j,"vous avez fait",tour,"tour","et vous avez",dict_joueur[j],"point")
        cont=continu()
    
        if cont:
            newcart=piocheCarte(cartes)
            dict_joueur[j]+=valeurCarte(newcart[0])
        perdu=dict_joueur[j]>21
        if perdu or not cont:
            les_perdu[j]=dict_joueur[j]
            del dict_joueur[j]



        return dict_joueur,les_perdu




    def tourcomplet(data_init,cartes_init,tour=1):
        """
        ici pour faire un tours complet on prend en argument les un dictionnaire contenant 
        les infos du tour précédent, les cartes qui reste, et le numero de tour
        en utilisant la fonction tourjoueur et un boucle for qui manipule les joueur,
        on appelle la fonction tourjoueurs pour chaque joueur
        """
        liste_joueur=dict(data_init)#on prends un copy pour pouvoir l'utiliser dans le boucle for car il y aura des effets de bords
                                    #sur nos donnée et on n'a pas droit de modifier ce qui est dans la condition de for
        les_perdu=dict()#pour garder ceux qui sont retirés avec leurs scores
        for joueur in liste_joueur:
            data_init,les_perdu=tourJoueur(joueur,data_init,cartes_init,tour,les_perdu)

        return data_init , les_perdu

    

    def partiefini(dic):
        """
        ici on verifie que le dictionnaire qui est passé en argument est vide ou non;
        si oui on retourne False sinon True
        """
        rep=True
        if not(len(dic)):
            rep=False
        return rep 
    def partiecomplet(liste_joueurs,victs):
        """
        ici pour une partie complete on prends en argument une liste des joueurs et la dictionnaire des 
        victoir;
        on initialise un premier tours en utilisant la fonction premiertour() en lui passant
        la liste des joueur et on recupère les infos de premier tours et les cartes qui restent
        puis dans un boucle while à chaque boucle on fait un tour complet en utilisant 
        la fonction tourcomplet() en lui passant les infos de premier tour les cartes et le numéro de tours
        puis à chaque boucle on verifi,e avec la fonctionne partiefini() en lui passant les joueur courants
        ,que la partie est fini ou non,si oui on sort de la boucle et en utilisant la fonction 
        gagnat en lui passant la dict des scores on trouver le (les) gagnant et on ajout 
        1 a leur valeurs dans la dict victs
        """
        premier_tours,cartes=premierTour(liste_joueurs)
        condition=True
        tour=1
        while condition:
            courants,retires=tourcomplet(premier_tours,cartes,tour)
            condition=partiefini(courants)
            tour+=1
        winner=gagnant(retires)
        winner.pop()
        for w in winner:
            victs[w]+=1
        return victs

    p_number=input('entrez le nombre des joueur:\n') #on commence le joue en demande combien de personne veux jouer
    while not ('2' <= p_number <= '9' ): #si il entre moins de 2 personne 1 une personne peut pas jouer avec lui même
        p_number=input('entrez un nombre entre 2 et 10:\n')
    p_number=int(p_number)
    liste_joueurs=initJoueurs(p_number)
    victs=initScores(liste_joueurs)
    rep="OUI"
    while rep in bonne_reponse['ouis']:
        victs=partiecomplet(liste_joueurs,victs)
        print("les points:",victs)
        rep=input("voulez_vous refaire une partie?\n")
    print("fin du jeu")




def version2_mises():
    """
    bonjour,
    projet black jack de FEIZABADI,Seyedmohammadghasem et ABDOLMOTALLEBI,Seyed Hossein
    notre projet est divisé en 3 partie comme besoin , Une partie de jeu sans mise,
    une partie de jeu avec mise et un avec mise et le croupier ensemble
    et donc cette partie est la deuxième partie avec mise.
    (en espérant que vous nous excusiez pour les fautes du français dans les commentaires
    car nous ne somme pas francophone. )
    """
    bonne_reponse={"ouis":["oui","Oui","Yes","yes","ouais","Ouais","yea","yeah","y"], #les posibilite de variante ouis ou nons que utilisatur peut entrer
                "nons":["non","Non","No","no","na","Nah",'nah','nope','n']}

    def paquet(): #def qui contient un paquet de 52 cart dans une list
        a=range(2,11)
        list_de_nombre=["as","valet", "dame", "roi"] 
        list_de_nombre.extend(a)
        paquet=[]
        for i in list_de_nombre: #on crée les cartes en utilisant les nombre de dans notre list
            msg1=str(i)+" de pique"
            paquet.append(msg1)
            msg2=str(i)+" de coeur"
            paquet.append(msg2)
            msg3=str(i)+" de trèfle"
            paquet.append(msg3)
            msg4=str(i)+" de carreau"
            paquet.append(msg4)
        return paquet

    def init_valeur():
        """une fonction supplémentaire pour avoir toutes les valeur"""
        return  {"as":[1,11],"2 ":2,"3 ":3,"3 ":3,"4 ":4,"5 ":5,
                "6 ":6,"7 ":7,"8 ":8,"9 ":9,
                "10":10,"va":10,"da":10,"ro":10}

    def valeurCarte(carte):    #cette fonction renvois le valeur d'une carte demandé
        valeur=init_valeur()
        mot_cle=carte[:2]   #pour  prendre uniquement nom de cartes
        if mot_cle=='as':
            val=int(input('1 ou 11?\n')) #on demande le utilisateur si il veut un valeur de 1 ou 11 pour l'as
            while not(val==1 or val==11):
                val=int(input('1 ou 11?\n'))
        else: val=valeur[mot_cle]
        return val

    def initPioche(n): # cette fonction mettre n fois de la pioche dans une liste et le melange et renvois le list
        import random
        liste=[]
        for i in range(n):
            l=paquet()
            liste+=l
        random.shuffle(liste)
        return liste

    def piocheCarte(p,x=1): #cette fonction renvois X carte au sommet de la pioche p et les suprimer de la pioche
        liste=[]
        for i in range(x):
            liste.append(p.pop())#une fois retirer le premier element, le suivant va le remplacer, donc il faut retirer toujour le premier
        return liste

    def initJoueurs(n): #renvois la liste de nom des joueur en les demandant 
        liste=[]
        for i in range(n):
            liste.append(input('entrez le nom de joueur:\n'))
        return liste
    def count_joueurs(joueurs): 
        """
        c'est une foncton supplémentaire afin de pouvoir compter la répétition d'un nom dans une liste
        en effet comme on peux pas avoir des joueurs avec les mêmes noms donc dans la foncion 
        initscore on utilise cette fonction pour gérer ce genre de problème
        """
        count=dict()
        for m in joueurs:
            count[m]=0
        return count#un dict qui compte le nombre d'existance un noms dans une liste donnée
    """
    une exemple d'éxecution:
    print(count_joueurs(['mamad','hossein','reza','reza']))
    ==>{'mamad': 0, 'hossein': 0, 'reza': 0}
    """


    def initScores(joueurs,v=0): 
        """ cette function prendre la liste des joueurs et une  valeur pour initizliser puis utilise la fonction count_joueurs au dussus 
            pour les mettre dans une dictionaire mais ce que cette fonction faire c'est qu'il observe 
            si on a des noms qui sont pareille et après si on en a il ajoute une * pour donner uun nom unique à chaque joueur
        """
        d=dict()
        x=list()
        count=count_joueurs(joueurs)
        for i in joueurs:
            if i in x:#commme on n'a pas droit d'avoir les memes mots cles donc on ajoute un indice si les  noms son identique
                count[i]+=1
                i=i+('*'*count[i])
            x.append(i) #on ajoute les nom qu'on entre dans le dict pour qu'on puisse remarqur le doublicate
            d[i]=v
        return d
    """   
    exemple de éxécution:
    print(initScorese(['mamad','hossein','reza','reza'],5))
    ==> {'mamad': 5, 'hossein': 5, 'reza': 5, 'reza*': 5}
    """
    def init_stock(joueurs,v=100):
        """
        dans cette fonctionne on initialise une dictionnare a partire de liste des joueur 
        et on met 100 comme valeur pour chacun
        """
        stock=dict()
        x=list()
        count=count_joueurs(joueurs)
        for i in joueurs:
            if i in x:#commme on n'a pas droit d'avoir les memes mots cles donc on ajoute un indice si les  noms son identique
                count[i]+=1
                i=i+('*'*count[i])
            x.append(i) #on ajoute les nom qu'on entre dans le dict pour qu'on puisse remarqur le doublicate
            stock[i]=100
        return stock

    def premierTour(joueurs,stock,cartes):#cette fonction prendre la liste de joueurs et il pioche 2 carte pour chaque joueurs et ajoute 
                            #les valeur des carte pour aux dans une dictionaire et le renvois
        """                         dans le mise à jours de cette fonction elle prend en 
                                    en argument un enjeu et la dictioonnare des stocke 
                                    et après commencer le tours on demande la somme que les 
                                    joueurs veulent mettre et on fait la soustraction entre 
                                    la mise et le stock pour chacun
                                """
        enjeu=0#initialiser une variable pour porter la somme de tooutes les mise
        nomandscore=initScores(joueurs)  #on initialise  les joueurs avec un valeur de 0 et les mettre dans cette variable
        for i in nomandscore:  # on prendre joueur de (i) de la liste
            print(i,":",end=" ")
            listcartesp=piocheCarte(cartes,2)
            n=0               
            for j in listcartesp: # on ajoute les valeur de cela dans un variable 
                n+=valeurCarte(j)
            print(listcartesp,"(",n,"point)")
            nomandscore[i]=n #on mis à jour le valeur de joueur
            n1=int(input(i+ " combien voulez_vous mettre pour ce tour?\n")) #on demande le valeur joueur veux entrer
            while n1<10 or n1>stock[i]: 
                n1=int(input(i+ " vous pouvez mettre de 10 jusqu'à " +str(stock[i])+'! entrez nouvelle valeur: \n'))
                #en demande jusqu'à ce qu'il entre un valeur qu'il appartient   
            enjeu+=n1
            stock[i]-=n1#on sorte 2 carte de la liste de notre pioche

        return nomandscore , cartes,stock,enjeu

    """ generalement cette fonction c'est pour verifier si on a les score qui sont egale
        donc on a plus d'un gagnant et renvois nom des gagnants.
        cette fonction prendre un score(vol) ( un values de notre dict)
        et le dicionaire et il renvois toutes les cle(les nom) qui ont ce score.
        """
    def keys(dic,val):
        """
        c'est une fonction suplémentaire qui prend en argument une dictionnare et une valeur 
        et il cherche dans lla dict les mots clés ayant la valeur passée en argument 
        et les mettre dans une liste et la revoit'
        """
        liste=list()
        for i in dic:
            if dic[i]==val:
                liste.append(i)
        return liste

    def gagnant(score): #cette fonction prendre le dictionaire des joueur avec leur score et renvois le gagnant(qui est plus proche de 21)
        values=list(score.values())  #score.valeurs() cette code nous donne les valeur des cle d'un dict donc on les extrit
        ecart=21 #le maximom valeur de point
        vic=0
        for i in values:
            if i<=21 and (21-i)<=ecart: #a chaque boucle on verifie si on a un score plus proche
                vic=i #on enregistre le score de gagnant
                ecart=21-i #ecart garde la distance de plus proche score a 21
        rep=keys(score,vic) #en utilisent cette fonction on prends nom(s) des gagnant(s) dans une list
        rep.append(vic)# on ajoute le score dans la liste avec sa nom
        print(rep)
        return rep

    def continu():  #on veut savoir si utilisatur veut continuer ou non
        cont=False #on initialise avec false donc if utilisatur ne tape pas oui le fonction directement renvois false
        msg="Vous voulez continuer? "
        continu=input(msg)
        while not(continu in bonne_reponse['ouis']) and not(continu in bonne_reponse['nons']):
            continu=input(msg)
        if continu in bonne_reponse['ouis']: #aprés d'avoir filtrer if le mot entrer n'est pas oui dont il est non
            cont=True
        return cont


    def tourJoueur(nom,score_joueur,cartes,tour,les_perdu):
        """
        ici on prends le noms du joueur les infos sur leurs scores et les cartes qui restent
        le numero de tours et la dictionnares de ceux qui sont retirés
        on demande à joueur s'il veux continuer on non si oui on pioches une carte 
        puis on vérifie qu'il a passé de 21 ou non pour le retirer de la listes de courants
        et s'il ne veux plus continuer on le retire de liste des courant en plus tous ceux qui
        seront retirés il seront ajouter à la dict les_perdu avec leurs scores'
        """


        print(nom,"vous avez fait",tour,"tour","et vous avez",score_joueur[nom],"point")
        cont=continu()
        if cont:#si le joueur choisi de continuer on pioche une carte pour lui
            newcart=piocheCarte(cartes)
            n=valeurCarte(newcart[0])
            print(newcart,"(",n,"point)")
            score_joueur[nom]+=n
        perdu=score_joueur[nom]>21#on verifie que le score a depasse 21 ou no
        if perdu or not cont:#si le score depasse 21 ou joueur a choisi de ne pas continuer on l'ajoute dans le dict des perdue avec son score et on le retire des jueurs qui sont toujours courants
            les_perdu[nom]=score_joueur[nom]
            del score_joueur[nom]
        
        return score_joueur,les_perdu,cartes




    def tourcomplet(data_init,cartes_init,retires,tour=1):
        """
        ici pour faire un tours complet on prend en argument un dictionnaire contenant 
        les infos du tour précédent, les cartes qui reste,un dictionnaire contenant des joueur retirés et le numero de tour
        en utilisant la fonction tourjoueur et un boucle for qui manipule les joueur,
        on appelle la fonction tourjoueurs pour chaque joueur
        """
        
        liste_joueur=dict(data_init)#on prends un copy pour pouvoir l'utiliser dans le boucle for car il y aura des effets de bords
                                    #sur nos donnée et on n'a pas droit de modifier ce qui est dans la condition de for
        
        for joueur in liste_joueur:
            data_init,retires,cartes_init=tourJoueur(joueur,data_init,cartes_init,tour,retires)

        return data_init , retires,cartes_init
    

    def partiefini(dic):
        """
        ici on verifie que le dictionnaire qui est passé en argument est vide ou non;
        si oui on retourne False sinon True
        """
        rep=True
        if not(len(dic)):
            rep=False
        return rep 
    def partiecomplet(liste_joueurs,victs,stock,cartes):
        """
        ici pour une partie complete on prends en argument une liste des joueurs et la dictionnaire des 
        victoir;
        on initialise un premier tours en utilisant la fonction premiertour() en lui passant
        la liste des joueur et on recupère les infos de premier tours et les cartes qui restent
        puis dans un boucle while à chaque boucle on fait un tour complet en utilisant 
        la fonction tourcomplet() en lui passant les infos de premier tour les cartes et le numéro de tours
        puis à chaque boucle on verifi,e avec la fonctionne partiefini() en lui passant les joueur courants
        ,que la partie est fini ou non,si oui on sort de la boucle et en utilisant la fonction 
        gagnat en lui passant la dict des scores on trouver le (les) gagnant et on ajout 
        1 a leur valeurs dans la dict victs
        """
        """
        pour la version avec des mises on passse en argument les stock restant des joueur  et le passe à la fonction premiertour()
        et on recupère en plus l'enjeu de cette partie et les stocks restant
        """
        
        premier_tours,carte,stock,enjeu =premierTour(liste_joueurs,stock,cartes)
        condition=True
        tour=1
        retires=dict()#pour garder ceux qui sont retirés avec leurs scores
        while condition:
            courants,retires,cartes=tourcomplet(premier_tours,cartes,retires,tour)
            condition=partiefini(courants)
            tour+=1
        winner=gagnant(retires)
        winner.pop()
        for w in winner:
            if len(winner)>1:
                enjeu=round(enjeu/len(winner))#si jamais on aura plus d'un gagnant l'enjeu doit être divisée par le nombre des gagnants
            victs[w]+=1
            stock[w]+=enjeu
            
        return victs,stock,cartes

    p_number=input('entrez le nombre des joueur:\n')
    while not ('2' <= p_number <= '9' ): #on filtre jusqu'à ce que l'utilisateur faire un entrée correcte
        p_number=input('entrez un nombre entre 2 et 10:\n')
    p_number=int(p_number)
    liste_joueurs=initJoueurs(p_number)#on defini une liste en utilisant la fonction initjoueur()
    """
    comme on a besoin d'initialiser un dict avec les noms unique des joueur et 0 pour valeur, 
    en utilisant la fonction initscore() qui renvoit un dict avec les noms unique des joueur comme mot clé 
    et 0 pour valeur, on récupère ce dict 
    """ 
    victs=initScores(liste_joueurs)
    liste_joueur_1=list()
    for i in victs:
        """
        comme s'il y a peut-être des joueur avec les même noms ,on ajoute des * a la fin de leurs noms,
        on doit avoir aussi une liste contenant le avec ces mots uniqiue à partir des noms existants  dans la dictionnaire victs
        """
        liste_joueur_1.append(i)
    stock=init_stock(liste_joueur_1)#initialiser les stock
    condition=True
    cartes=initPioche(p_number)#initialiser les cartes
    while condition and len(liste_joueur_1)>1:
        victs,stock,cartes=partiecomplet(liste_joueur_1,victs,stock,cartes)
        for i in stock:
            """
            ici on verifie les stocke et supprime ceux qui n'ont plus de stock'
            """
            if stock[i]<=0:
                liste_joueur_1.remove(i)
        print("les stock:",stock)
        print("les points:",victs)
        if len(liste_joueur_1)>1:
            rep=input("voulez_vous refaire une partie?\n")
            if rep in bonne_reponse["nons"]:
                condition=False
            else:
                    for p in list(liste_joueur_1):
                        """
                        ici après chaque partie on demande a chaque joueur qu'il veut quitter la table
                        ou non, si oui on le supprime de la liste des joueurs '
                        """
                        rep=input(p+" voulez-vous quitter la table?\n")
                        while rep not in bonne_reponse['ouis'] and rep not in  bonne_reponse['nons']:
                            rep=input(p+" voulez-vous quitter la table?")
                        if rep in bonne_reponse['ouis']:
                            liste_joueur_1.remove(p)
        
    """
    à partir d'ici on a soit la reponse qui était non soit le nombre des joueurs qui est égale à 1
    donc on vérifie et affiche le message nécessaire
    """
    if condition:
        print("fin du jeu")
    else:
        print("fin du jeu",liste_joueur_1[0],"a rammaser toutes les mises")
        
        
        
        
        
        
"""
    bonjour,
    projet black jack de FEIZABADI,Seyedmohammadghasem et ABDOLMOTALLEBI,Seyed Hossein
    notre projet est divis� en 3 partie comme besoin , Une partie de jeu sans mise,
    une partie de jeu avec mise et un avec mise et le croupier ensemble
    et donc cette partie est la troisi�me partie avec mise et le croupier avec 4 niveau de difficult�.
    (en esrant que vous nous excusiez pour les fautes du fran�ais dans les commentaires
    car nous ne somme pas francophone. )"""
def init_valeur():
        """une fonction supplémentaire pour avoir toutes les valeur"""
        return  {"as":[1,11],"2 ":2,"3 ":3,"3 ":3,"4 ":4,"5 ":5,
                "6 ":6,"7 ":7,"8 ":8,"9 ":9,
                "10":10,"va":10,"da":10,"ro":10}
    
liste_carte_pioche=list()
def decisionaleatoire(): #cette fonction renvois un booléne False ou True par hasard
    cont=False
    a=random.randint(0,1) # il nous donne sois 0 soin 1 par hasard, lorsqu'il est 1 il renvois True , 0 renvois False
    if a==1:
        cont=True
    return cont
""" dans cette fonction on a donc 3 posibilite , on donne sois 0 ou 0.5 ou 1 comme
    argument �  la fonction et si cela et 0 il renvois False(non continue pas) si 0.5
    il utilise fonction decisionaleatoir  au dessus et il renvois aleatoirement False ou True
    si 1 il renvois True donc il cont toutes le temp"""
def probabilite(x):
        prob=x
        if prob==0.5:
            cont=decisionaleatoire()
        elif prob==0:
            cont=False
        elif prob==1:
            cont=True
        return cont
""" pour commencer on a choisi si la ecarte est moins 13 il continue , si la ecarte
    est entre 13 et 17 il choisi par hasard si il est superieur de 17 il arrete """
def initprob(score,bord1=13 ,bord2=17): #la fonction recevois le score de machine
        prob=0.5  # �  la fun on donne cette variable �  notre fonction au dessus pour le lire 
        if score<=bord1:
            prob=1
        elif bord1<score<=bord2:
            prob=0.5
        elif score>bord2:
            prob=0
        cont=probabilite(prob)
        return cont
""" en utilisant cette fonciton on met tout les valeur des carte qui sont d�j� pioch� dans une liste""" 
def listevaleur(dec):
        listval=list()
        for i in dec:
            valeur=init_valeur()
            mot_cle=i[:2]   #pour prendre uniquement nom de cartes
            if mot_cle=='as':
                val=1
            else: val=valeur[mot_cle]
            listval.append(val)
        return listval
""" en utilisant cette fonction en compte les carte grands avec valeur de 10
    et les carte petite qui sont d�j� pioch�e et donc on peut savoir il nous reste
    plus des carte avec grand valeur ou petite dans le pioche et dans on prend moins de risk
    quand il a bcp de grande valeur qu'il reste dans le pioche et en prend moins de risk 
    en opposite """
def comptvaldec(liste_val):
        big=0
        low=0
        bigs=False
        for val in liste_val:
            if val>=10:
                big+=1
            else:
                low+=1
        if big>low:
            bigs=False
        return bigs
""" � ce niveau l� il choisi plus intelligemment , pour savoir qu'il met combien de kepec il voit
    son point et point des autre,par exemple si il y a qqn autre qui a entre 19-21 points avant lui
    si il a moins de cela il met le minimum et apr�s dans les tour suivants il ne continue pas.
    si il vois autre moins de 19 points il essaye de calcul est choisi il veut mettre plus que min ou pas.

    pour savoir qu'il cont ou pas il vois cartes des autre avant lui et il ne continue pas si il n'a pas le meilleure
    cartes compares a les autres jusqu'� l� , si non il d�cide en utilisant probabilit� qu'il d�cide ou pas
    et aussi il rends compte les cart qui sont d�j� pioch�e et comem il est indique dans les commentaire
    de fonction comptvaldec si il nous reste bcp de grande cartes on prend moins de risk"""
def inteligent(partie,botpoint=None,botstock=None,score_autre=None): 
        def miser():
            mismin=False # si il est True on cont pas, et on met le minimum point 
            for i in score_autre:
                if i>=18>botpoint or 11<=botpoint<=17 :
                    mismin=True #� ce point l� il y a qqn qui a un point sup�rieur de nous, donc on mais le minimum 
            if botpoint==21:
                mis=botstock
            elif 17<=botpoint<=20: #if son point et entre 18-20 il mais 80 pourcent of kopecs
                    mis=(80/100)*botstock
            elif botpoint<=11:
                if botstock>=25: #car on as minimim de 10 pour rester
                    mis=(40/100)*botstock
            if mismin:
                mis=10
            return round(mis)
            
        def cont():
            cont=False
            bigs=comptvaldec(listevaleur(liste_carte_pioche))
            if bigs:
                cont=initprob(botpoint,11,14) #plus de hauts valeur il reste dans les cartes d�j� pioche moins de chance pour les nouvelle hauts valeur
            else:
                cont=initprob(botpoint,15,17)
            for i in score_autre:
                if i>=18>botpoint :  
                    cont=True
            return cont

        def val_as():
            aas=1
            if botpoint >= 11:
                aas=1
            else: aas=11 
            return aas
        return eval(partie)()      
""" il fait tout les decision aleatoirment en utilisent fonc decisionaleatoir
    qui choisi une bol aleatoir en utilisant fonction random de python""" 
print('hi')
def aleatoir_complet(partie,botpoint=0,botstock=None,score_autre=None):
        def miser():
            mis=random.randint(10,botstock) #le croupier choisi aléatoirment in veut mettre combien
            return round(mis)
        def cont():
            cont=decisionaleatoire() #le croupier choisi aléatoirment il veux continiue ou pas
                                    #et donc il envois True ou False pour continuer
            return cont                        
        def val_as():
            ass=1
            bol=decisionaleatoire() #cela renvois aléatoirment True ou False
            if bol: #si bol et True donc en choisi 11 comme aas si non on choisi comme valeur de as
                ass=11
            return ass
    
        return eval(partie)()
"""�  cette niveau le croupier se comporte démi aléatoirement c-� -d il choisi le montant de kopec
    aléatoirment mais entre un intervale spécifié et aussi il choisi valeur de aas avec plus de prudent """
def demi_aleatoir(partie,botpoint=0,botstock=None,score_autre=None):
        def miser():
            if botstock>20:
                mis=(random.randrange(10,50,10)/100)*botstock #le croupier choisi aléatoirment in veut mettre combien
                while mis<10:
                    mis=(random.randrange(10,50,10)/100)*botstock   
            else: mis=10
            return round(mis)
        def cont():
            cont=decisionaleatoire() #le croupier choisi aléatoirment il veux continue ou pas
                                    #et donc il envois True ou False pour continuer
            return cont 
        def val_as():
            if botpoint >= 11:
                ass=1
            else: #si bol et True donc en choisi 11 comme aas si non on choisi comme valeur de as
                bol=decisionaleatoire() #cela renvois aléatoirment True ou False
                if bol: #si bol et True donc en choisi 11 comme aas si non on choisi comme valeur de as
                    ass=11
            return ass
        return eval(partie)()
"""�  ce niveau l�  il choisi comme une personne normale qui vient de commoncer �  jouer et 
    il ne connais pas bien le joue
    c-� -d sauf il a une bonne point de carte il met petite montant de kepec
    (en regardant uniquement son cartes et points),et pour savoir qu'il continue ou pas
    en utilisant probabilité  il choisi de continuer (uniquement en regardant son cartes et points)  """
def normal(partie,botpoint=0,botstock=None,score_autre=None):
        def miser():
            if botpoint==21:
                mis=botstock
                
            elif 18<=botpoint<=20: #if son point et entre 18-20 il mais 80 pourcent of kopecs
                mis=(80/100)*botstock
            else: 
                if botstock>20:
                    mis=(random.randrange(10,50,10)/100)*botstock #le croupier choisi aléatoirment in veut mettre combien
                    while mis<10:
                        mis=(random.randrange(10,50,10)/100)*botstock   
                else: mis=10
            return round(mis)
        def cont():
            cont=initprob(botpoint,13,17)
            return cont
        def val_as():
                if botpoint >= 11:
                    ass=1
                else: ass=11 #si bol et True donc en choisi 11 comme aas si non on choisi comme valeur de as
                return ass
        return eval(partie)()





def version3_croupier():




   """
    dans la version avec les croupier on a ecrit les différant typpes de croupier avec les différante
    algorithme de décision dans les différants cas et dans tout le programme �  chaque fois qu'onn dois 
    interagire avec l'utilisateur si le joueur est un croupier on appele la fontions concernants de ce cas 
    au lieu de demander �  l'utilisateur quoi faire 
    """



   """
    dans cette version on utilise la méthode eval() de python qu'on a appris dans le livre
    informatique pour la premiere année de licence;
    en effet l'idée c'est de réduire les ligne du code mais dans tous cas on sait bien 
    écrire une structure au lieu de la méthode eval().
    par exemple:
    >>>def test(x):
        y=x+2
        return y
    >>>def test1(x):
        y=x-2
        return y
    >>>ex=input("entrez le nom du foncton:")
    entrez le nom du fonction: test1
    >>>if ex=="test":
            ex=test
    elsif ex=="test1:
            ex=test1
    >>>ex(2)
    0

    qui est égale � :
    >>>ex=eval(ex)
    >>>ex(4)
    2
    """
   bonne_reponse={"ouis":["oui","Oui","Yes","yes","ouais","Ouais","yea","yeah","y"], #les posibilite de variante ouis ou nons que utilisatur peut entrer
                "nons":["non","Non","No","no","na","Nah",'nah','nope','n']}
   bonne_reponse_type_croupier=["aleatoir_complet","demi_aleatoir","normal","inteligent"]#définir des nons  des différants niveaux de croupier 

   def paquet(): #cette fonction renvoit une liste de 52 carteS
        a=range(2,11)
        list_de_nombre=["as","valet", "dame", "roi"] 
        list_de_nombre.extend(a)
        paquet=[]
        for i in list_de_nombre: #on crée les cartes en utilisant les nombre de dans notre list
            msg1=str(i)+" de pique"
            paquet.append(msg1)
            msg2=str(i)+" de coeur"
            paquet.append(msg2)
            msg3=str(i)+" de trèfle"
            paquet.append(msg3)
            msg4=str(i)+" de carreau"
            paquet.append(msg4)
        return paquet


   def init_valeur():
        """une fonction supplémentaire pour avoir toutes les valeur"""
        return  {"as":[1,11],"2 ":2,"3 ":3,"3 ":3,"4 ":4,"5 ":5,
                "6 ":6,"7 ":7,"8 ":8,"9 ":9,
                "10":10,"va":10,"da":10,"ro":10}
   def valeurCarte(carte,croupier=False,type_croupier=None,score=None,stock1=None):    #cette fonction renvois le valeur d'une carte demandé
        """
        en effet dans la version avec croupier cette fonction prends en argument la carte,
        le statut de joueur qu'il est croupier in nons et si oui le type de croupier
        c'est parce que au lieu d'interagir avec l'utilisateur pour un croupier on doit appeler 
        sa fonction qui est pour cette interaction 
        """
        valeur=init_valeur()
        mot_cle=carte[:2]   #pour  prendre uniquement nom de cartes
        if croupier:   #ici on verifie que le joueur est un croupier ou non    
            if mot_cle=='as':
                val=type_croupier(partie="val_as",botpoint=score,botstock=stock)#si la carte est "as" au lieu de demander la valeur de "as" on appelle la fonction qui est pour cette interaction
            else: val=valeur[mot_cle]

        else:
            if mot_cle=='as':
                val=int(input('1 ou 11?\n')) #on demande �  l'utilisateur s'il veut la valeur de 1 ou 11 pour l'as
                while not(val==1 or val==11):
                    val=int(input('1 ou 11?\n'))
            else: val=valeur[mot_cle]
        return val

   def initPioche(n): # cette fonction mettre n fois de la pioche dans une liste et le melange et renvois le list
        import random
        liste=[]
        for i in range(n):
            l=paquet()
            liste+=l
        random.shuffle(liste)
        return liste
   def piocheCarte(p,x=1): #cette fonction renvois X carte au sommet de la pioche p et les suprimer de la pioche
        liste=[]
        for i in range(x):
            carte=p.pop(0)
            liste_carte_pioche.append(carte)
            liste.append(carte)#une fois retirer le premier element, le suivant va le remplacer, donc il faut retirer toujour le premier
        return liste
   def initJoueurs(n): #renvois la liste de nom des joueur en les demandant 
        liste=[]
        for i in range(n):
            liste.append(input('entrez le nom de joueur\n'))
        return liste
   def count_joueurs(joueurs): 
        """
        c'est une foncton supplémentaire afin de pouvoir compter la répétition d'un nom dans une liste
        en effet comme on peux pas avoir des joueurs avec les mêmes noms donc dans la foncion 
        initscore on utilise cette fonction pour gérer ce genre de problème
        """
        count=dict()
        for m in joueurs:
            count[m]=0
        return count#un dict qui compte le nombre d'existance un noms dans une liste donnée
   """
    une exemple d'éxecution:
    print(count_joueurs(['mamad','hossein','reza','reza']))
    ==>{'mamad': 0, 'hossein': 0, 'reza': 0}
    """

   def initScores(joueurs,v=0,demande_croupier=True): 
        
        """ cette function prendre la liste des joueurs et une  valeur pour initizliser puis utilise la fonction count_joueurs au dussus 
            pour les mettre dans une dictionaire mais ce que cette fonction faire c'est qu'il observe 
            si on a des noms qui sont pareille et après si on en a il ajoute une * pour donner uun nom unique �  chaque joueur
        """
        """
        dans la version avec croupier on ajoute un argumet "demande_croupier" et si ce sera True 
        pour chaque utilisateur il demande s'il veux utiliser un croupier pour cette partie ou non
        et si oui il doit choisir un type parmis les types de croupier
        et si demande_croupier est False on ne demande rien �  l'utilisateur et on initiaalise 
        juste un dict avec les valeurs v  
        """
        if demande_croupier:
            d=dict()
            x=list()
            is_croupier=dict()
            type_croupier=dict()
            count=count_joueurs(joueurs)
            for i in joueurs:
                if i in x:#commme on n'a pas droit d'avoir les memes mots cles donc on ajoute un indice si les  noms son identique
                    count[i]+=1
                    i=i+('*'*count[i])
                rep=input(i+"  voudriez-vous utiliser un croupier?(oui/non)\n")
                while rep not in bonne_reponse["ouis"] and rep not in bonne_reponse["nons"] :
                    rep=input(i+"  voudriez-vous utiliser un croupier?(oui/non)\n")
                if rep in bonne_reponse["ouis"]:
                    is_croupier[i]=True
                    t_c=input("parmi la liste ci_dessus chisissez le type de croupier\n"+"aleatoir_complet "+"demi_aleatoir "+"normal "+"inteligent\n")
                    while t_c.lower() not in bonne_reponse_type_croupier:
                        t_c=input("parmi la liste ci_dessus chisissez le type de croupier\n"+"aleatoir_complet "+"demi_aleatoir "+"normal "+"inteligent\n")
                    type_croupier[i]=eval(t_c)
                else:
                    is_croupier[i]=False
                    type_croupier[i]=None
                x.append(i) #on ajoute les nom qu'on entre dans le dict pour qu'on puisse remarqur le doublicate
                d[i]=v
            return d , is_croupier , type_croupier 
        else:
            d=dict()
            x=list()
            count=count_joueurs(joueurs)
            for i in joueurs:
                if i in x:#commme on n'a pas droit d'avoir les memes mots cles donc on ajoute un indice si les  noms son identique
                    count[i]+=1
                    i=i+('*'*count[i])
                x.append(i) #on ajoute les nom qu'on entre dans le dict pour qu'on puisse remarqur le doublicate
                d[i]=v
            return d

   def init_stock(joueurs,v=100):
        """
        dans cette fonctionne on initialise une dictionnare a partire de liste des joueur 
        et on met 100 comme valeur pour chacun
        """
        stock=dict()
        for i in joueurs:
            stock[i]=100
        return stock
   def premierTour(joueurs,stock,cartes):#cette fonction prendre la liste de joueurs et il pioche 2 carte pour chaque joueurs et ajoute 
                            #les valeur des carte pour aux dans une dictionaire et le renvois
        """ dans le mise �  jours de cette fonction elle prend en 
            en argument un enjeu et la dictioonnare des stocke 
            et après commencer le tours on demande la somme que les 
            joueurs veulent mettre et on fait la soustraction entre 
            la mise et le stock pour chacun"""
        """
        dans la version avec le croupier on prends �  partir du fonction initscore() le dict is_croupier contenant le statut des joueur
        c_� _d les mot clés sont les noms des joueur et si c'est un croupier la valeur est True, False sinon, 
        et le dict type_croupier contenant les noms des jouers comme mot clé et les type de croupier qu'il ont déja 
        choisi
        """
        score_autres=list()
        enjeu=0#initialiser une variable pour porter la somme de tooutes les mise
        nomandscore,is_croupier,type_croupier=initScores(joueurs)  #on initialise  les joueurs avec un valeur de 0 et les mettre dans cette variable
        for i in nomandscore:  # on prendre joueur de (i) de la liste
                            #valeur ini
            print(i,":",end=" ")
            listcartesp=piocheCarte(cartes,2)#piocher 2 premieres cartes pour chacun
            n=0
            for j in listcartesp: # on compte le score de chaque joueur a partir des cartes piochés
                n+=valeurCarte(j,is_croupier[i],type_croupier[i],score=n,stock1=stock[i])
            print(listcartesp,"(",n,"point)")
            score_autres.append(n)
            nomandscore[i]=n #on mis �  jour le valeur de joueur
            if is_croupier[i]:#on verifie que lle joueur est un croupier ou non
                n1=type_croupier[i](partie="miser",botstock=stock[i],botpoint=n,score_autre=score_autres)#pour un croupier au lieu de demander la mise �  l'utilisateur on appelle la fonction de mise de ce croupier 
                print(i," a choisi",str(n1),"pour miser")
            else:    
                n1=0
                while n1<=15 or n1>stock[i]:#on filtre pour que l'utilisateur entre le nombre entre le minimun et son stock
                    n1=int(input(i+ " vous pouvez mettre de 10 jusqu'� " +str(stock[i])+'! entrez nouvelle valeur: \n'))
                #en demande jusqu'� ce qu'il entre un valeur qu'il appartient   
            enjeu+=n1
            stock[i]-=n1
        return nomandscore , cartes,stock,enjeu,is_croupier,type_croupier
   def keys(dic,val):
        """
        c'est une fonction suplémentaire qui prend en argument une dictionnare et une valeur 
        et il cherche dans lla dict les mots clés ayant la valeur passée en argument 
        et les mettre dans une liste et la revoit'
        """
        liste=list()
        for i in dic:
            if dic[i]==val:
                liste.append(i)
        return liste

   def gagnant(score): #cette fonction prendre le dictionaire des joueur avec leur score et renvois le gagnant(qui est plus proche de 21)
        values=list(score.values())  #score.valeurs() cette code nous donne les valeur des cle d'un dict donc on les extrit
        ecart=21 #le maximom valeur de point
        vic=0
        for i in values:
            if i<=21 and (21-i)<=ecart: #a chaque boucle on verifie si on a un score plus proche
                vic=i #on enregistre le score de gagnant
                ecart=21-i #ecart garde la distance de plus proche score a 21
        rep=keys(score,vic) #en utilisent cette fonction on prends nom(s) des gagnant(s) dans une list
        rep.append(vic)# on ajoute le score dans la liste avec sa nom
        print("gagnant=",rep)
        return rep

   def continu(nom,is_croupier,type_croupier,score=None,score_autres=None):  #on veut savoir si utilisatur veut continuer ou non cette fonction renvoit True or False
        """
        dans la version avec croupier on passe en argument le dict de statut des joueurs et le type des croupier 
        """
        cont=False #on initialise avec false donc if utilisatur ne tape pas oui le fonction directement renvois false
        if is_croupier[nom]:#si le joueur un crouupier au lieu de demander �  l'utilisateur on appele la fonction de croupier choisi
            cont=type_croupier[nom](partie="cont",botpoint=score,score_autre=score_autres)  
        else:
            msg="Vous voulez continuer?\n"
            continu=input(msg)
            while not(continu in bonne_reponse['ouis']) and not(continu in bonne_reponse['nons']):
                continu=input(msg)
            if continu in bonne_reponse['ouis']: #aprés d'avoir filtrer if le mot entrer n'est pas oui dont il est non
                cont=True
        return cont

   def tourJoueur(nom,score_joueur,cartes,tour,les_perdu,is_croupier,type_croupier,score_autres):
        """
        ici on prends le noms du joueur les infos sur leurs scores et les cartes qui restent
        le numero de tours et la dictionnares de ceux qui sont retirés
        on demande �  joueur s'il veux continuer on non si oui on pioches une carte 
        puis on vérifie qu'il a passé de 21 ou non pour le retirer de la listes de courants
        et s'il ne veux plus continuer on le retire de liste des courant en plus tous ceux qui
        seront retirés il seront ajouter �  la dict les_perdu avec leurs scores'
        """
        """
        dans la version avec croupier on passe en argument le statut des joueur et le types des croupier
        """

        print(nom," vous avez fait",tour,"tour","et vous avez",score_joueur[nom],"point")
        cont=continu(nom,is_croupier,type_croupier,score=score_joueur[nom],score_autres=score_autres)#ici on passe aussi le statut des joueur et le type des croupier au fonction continu() parce qu'il en a besoin dans cette version
        con="de countinuer"
        if not cont:
            con="de ne pas countinuer"
        print(nom," vous avez choisi",con)
        if cont:#si le joueur choisi de continuer on pioche une carte pour lui
            newcart=piocheCarte(cartes)
            n=valeurCarte(newcart[0],is_croupier[nom],type_croupier[nom],score=score_joueur[nom])#dans cette version la fonction valeurcarte() a besoin de statut du joueur et le type de croupier
            print(newcart,"(",n,"point)")
            score_joueur[nom]+=n
        perdu=score_joueur[nom]>21#on verifie que le score a depasse 21 ou no
        if perdu or not cont:#si le score depasse 21 ou joueur a choisi de ne pas continuer on l'ajoute dans le dict des perdue avec son score et on le retire des jueurs qui sont toujours courants
            les_perdu[nom]=score_joueur[nom]
            del score_joueur[nom]
        
        return score_joueur,les_perdu,cartes
   def tourcomplet(data_init,cartes_init,is_croupier,type_croupier,retires,tour=1):
        """
        ici pour faire un tours complet on prend en argument un dictionnaire contenant 
        les infos du tour précédent, les cartes qui reste,un dictionnaire contenant des joueur retirés et le numero de tour
        en utilisant la fonction tourjoueur et un boucle for qui manipule les joueur,
        on appelle la fonction tourjoueurs pour chaque joueur
        """
        """
        dans cette versions la fontion tourjoueur() a besoin de statuts des joueur et les type de croupier 
        donc cette fonction doit prendre en plus les dictionnaires contenant ces informations et 
        les passer dans la fonction tourjoueur() 
        """
        liste_joueur=dict(data_init)#on prends un copy pour pouvoir l'utiliser dans le boucle for car il y aura des effets de bords
                                    #sur nos donnée et on n'a pas droit de modifier ce qui est dans la condition de for
        
        for joueur in liste_joueur:
            score_autre=data_init.values()
            data_init,retires,cartes_init=tourJoueur(joueur,data_init,cartes_init,tour,retires,is_croupier,type_croupier,score_autre)

        return data_init , retires,cartes_init
   def partiefini(dic):
        """
        ici on verifie que le dictionnaire qui est passé en argument est vide ou non;
        si oui on retourne False sinon True
        """
        rep=True
        if not(len(dic)):
            rep=False
        return rep 
   def partiecomplet(liste_joueurs,victs,stock,cartes):
        """
        ici pour une partie complete on prends en argument une liste des joueurs ,la dictionnaire des 
        victoir,les stocks des joueur et les cartes qui restent;
        on initialise un premier tours en utilisant la fonction premiertour() en lui passant
        la liste des joueur et on recupère les infos de premier tours et les cartes qui restent
        puis dans un boucle while �  chaque boucle on fait un tour complet en utilisant 
        la fonction tourcomplet() en lui passant les infos de premier tour les cartes et le numéro de tours
        puis �  chaque boucle on verifi,e avec la fonctionne partiefini() en lui passant les joueur courants
        ,que la partie est fini ou non,si oui on sort de la boucle et en utilisant la fonction 
        gagnat en lui passant la dict des scores on trouver le (les) gagnant et on ajout 
        1 a leur valeurs dans la dict victs
        """
        """
        pour la version avec des mises on passse en argument les stock restant des joueur  et le passe �  la fonction premiertour()
        et on recupère en plus l'enjeu de cette partie et les stocks restant
        """
        """
        pour la version avec les croupier dans le premier tour on initialise le statut des joueur et les types des croupier 
        et les récupère pour passé dans la fonction tourcomplet
        """
        premier_tours,cartes,stock,enjeu,is_croupier,type_croupier =premierTour(liste_joueurs,stock,cartes)
        condition=True
        tours=1
        retires=dict()#pour garder ceux qui sont retirés avec leurs scores
        while condition:#on boucle pour faire les tours complete
            courants,retires,cartes=tourcomplet(premier_tours,cartes,is_croupier,type_croupier,retires,tour=tours)
            condition=partiefini(courants)
            tours+=1
        """
        �  partir d'ici la partie est fini et il n'y a plus de joueur courant
        et le dict retires contient les joueur avec leurs scores finale
        """
        winner=gagnant(retires)#on trouve le gagnant
        winner.pop()#comme la fonction gagnant renvois une liste des gagnant avec le score �  la dérnier indice on supprime le score
        for w in winner:
            if len(winner)>1:
                enjeu=round(enjeu/len(winner))#si jamais on aura plus d'un gagnant l'enjeu doit être divisée par le nombre des gagnants
            victs[w]+=1
            stock[w]+=enjeu#on ajoute l'enjeu �  socks de gagnat
            
        return victs,stock,cartes

   p_number=input('entrez le nombre des joueur:\n')
   while not ('2' <= p_number <= '9' ): #on filtre jusqu'�  ce que l'utilisateur faire un entrée correcte
        p_number=input('entrez un nombre entre 2 et 10:\n')
   p_number=int(p_number)
   liste_joueurs=initJoueurs(p_number)#on defini une liste en utilisant la fonction initjoueur()
   """
    comme on a besoin d'initialiser un dict avec les noms unique des joueur et 0 pour valeur, 
    en utilisant la fonction initscore() qui renvoit un dict avec les noms unique des joueur comme mot clé 
    et 0 pour valeur, on récupère ce dict 
    """ 
   """
    dans la version avec les croupier on doit lui passer False pour demande_croupier pour qu'il renvoit juste un dict contenant des noms 
    unique et 0 pour valeurs
    """
   victs=initScores(liste_joueurs,demande_croupier=False)
   liste_joueur_1=list()
   for i in victs:
        """
        comme s'il y a peut-être des joueur avec les même noms ,on ajoute des * a la fin de leurs noms,
        on doit avoir aussi une liste contenant le     count[i]+=1
                    i=i+('*'*count[i])vec ces mots uniqiue �  partir des noms existants  dans la dictionnaire victs
        """
        liste_joueur_1.append(i)
   stock=init_stock(liste_joueur_1)#initialiser les stock
   condition=True
   cartes=initPioche(p_number)#initialiser les cartes
   while condition and len(liste_joueur_1)>1:
        victs,stock,cartes=partiecomplet(liste_joueur_1,victs,stock,cartes)
        for i in stock:
            """
            ici on verifie les stocke et supprime ceux qui n'ont plus de stock'
            """

            if stock[i]<=0:
                liste_joueur_1.remove(i)
        
        print("les stock:",stock)
        print("les points:",victs)
        if len(liste_joueur_1)>1:
            rep=input("voulez_vous refaire une partie?\n")
            if rep in bonne_reponse["nons"]:
                condition=False
            else:
                    for p in list(liste_joueur_1):
                        """
                        ici après chaque partie on demande a chaque joueur qu'il veut quitter la table
                        ou non, si oui on le supprime de la liste des joueurs '
                        """
                        rep=input(p+"  voulez-vous quitter la table?\n")
                        while rep not in bonne_reponse['ouis'] and rep not in  bonne_reponse['nons']:
                            rep=input(p+"  voulez-vous quitter la table?\n")
                        if rep in bonne_reponse['ouis']:
                            liste_joueur_1.remove(p)
        
   """
    �  partir d'ici on a soit la reponse qui était non soit le nombre des joueurs qui est égale �  1
    donc on vérifie et affiche le message nécessaire
    """
   if condition:
        print("fin du jeu")
   else:
        print("fin du jeu",liste_joueur_1[0],"a rammaser toutes les mises")

   """
    on a lanc� le jeu 12 fois et avec 4 joueur chacun un croupier diff�rant et on a eu les score suivant
    intelligent: environ 80% bon choix pour miser 
                environ 60% bon choix pour continuer 
                environ 90% pour choix de valeur de AS
    normal     : environ 60% bon choix pour miser 
                environ 70% bon choix pour continuer 
                environ 80% pour choix de valeur de AS
    demi_aleatoir: environ 40% bon choix pour miser 
                environ 40% bon choix pour continuer 
                environ 50% pour choix de valeur de AS
    aleatoir   : environ 30% bon choix pour miser 
                environ 20% bon choix pour continuer 
                environ 30% pour choix de valeur de AS
                
    """


condition=True 
rep='oui'
while rep.lower()=='oui':
    choix=input("bienvenue en jeu blackjack en 3 version\nparmi les version ci-desssus,\
choisissez un\n1: version simple\n2: version avec les mises\n3: version avec les croupier\n")
    while choix not in ["1","2","3"]:
        choix=input("bienvenue en jeu blackjack en 3 version\nparmi les version ci-desssus,\
choisissez un\n1: version simple\n2: version avec les mises\n3: version avec les croupier\n")
    if choix=="1":
        version1()
    elif choix=="2":
        version2_mises()
    else:
        version3_croupier()
    rep=input('voudriez vous rejouer?(oui/non)')
print("au revoir ")