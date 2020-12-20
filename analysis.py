import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import datetime
import random

def openDataFrame():
    """
        FONCTIONNEL
        Stockage du DataFrame
    """
    global df
    df = pd.read_csv('dataset.csv', error_bad_lines=False, delimiter=";", encoding="ISO-8859-1")

def histogrammeBot(category, number):
    """
        FONCTIONNEL
        Paramètres: -> category: AUTHOR CHANNEL DATE
                    -> number  : taille du classement
        Fonction: Envoi d'un histogramme en message privé.
        Modifications: None
    """

    # Récupération du DataFrame
    openDataFrame()

    # Récuperation des labels et des valeurs
    labels_list = list(df[category].value_counts().head(number).index)
    data_list = list(df[category].value_counts().head(number))

    # Lambda expression pour générer des couleurs aléatoires
    get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF),range(n)))

    # Création, enregistrement et suppression de l'histogramme
    for k in range(len(labels_list)):
        plt.bar(labels_list[k], data_list[k], label=labels_list[k], color=get_colors(1))
    
    plt.title("Activité des: "+ category)
    plt.xticks(rotation=20)
    plt.xlabel(category)
    plt.ylabel('values')
    plt.legend()
    plt.savefig('hist.png')
    plt.close()

def classementBot(category, number):
    """
        FONCTIONNEL
        Paramètres: -> category: AUTHOR CHANNEL DATE
                    -> number  : taille du classement
        Fonction: Envoi du classement en message privé
        Modifications: None
    """
    # Récupération du DataFrame
    openDataFrame()

    # # On retourne les 'number' premières valeurs de 'category'
    # return df[category].value_counts().head(number)
    
    # Récupération des labels et des valeurs du jour
    labels_list = list(df[category].value_counts().head(number).index)
    data_list = list(df[category].value_counts().head(number))

    # Création et stockage des valeurs et des labels dans un dictionnaire (mise en page)
    global cls_
    cls_ = {}
    for i in range(len(labels_list)):
        if(str(labels_list[i]) not in cls_.keys()):
            cls_[str(labels_list[i])] = int(data_list[i])
    return cls_

def camembertBot(category, number):
    """
        FONCTIONNEL
        Paramètres: -> category: AUTHOR CHANNEL DATE
                    -> number  : taille du classement
        Fonction: Envoi d'un diagramme camembert en message privé
        Modifications: None
    """

    # Récupération du DataFrame
    openDataFrame()

    # Récuperation des labels et des valeurs
    labels_list = list(df[category].value_counts().head(number).index)
    data_list = list(df[category].value_counts().head(number))

    # Génération d'une liste de couleurs aléatoires
    # colors = []
    # for i in range(len(labels_list)):
    #     rd_nb = random.randint(0, 16777215)
    #     hex_nb = str(hex(rd_nb))
    #     hex_nb = '#'+hex_nb[2:]
    #     colors.append(hex_nb)

    # Création du diagramme
    # plt.pie(data_list, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'},colors=colors)
    plt.pie(data_list, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
    plt.title("Répartition messages p/r " + category)
    plt.legend(labels_list)
    plt.tight_layout()
    plt.savefig('cam.png')
    plt.close()

def clsPdf(category, number):
    """
        FONCTIONNEL
        Paramètres: -> category: AUTHOR CHANNEL DATE
                    -> number  : taille du classement
        Fonction: On retourne un dictionnaire avec les labels les plus actifs et les valeurs correspondantes
        Modifications: None
    """

    # Récupération du DataFrame
    openDataFrame()

    # Récupération de la date du jour pour actualiser le titre
    todayDate = datetime.datetime.now()
    currentDate = str(todayDate.year)+str('/')+str(todayDate.month)+str('/')+str(todayDate.day)

    # Création du nouveau DataFrame avec les données correponsantes à la date du jour
    new_df = df[df['DATE']==currentDate]

    # Récupération des labels et des valeurs du jour
    labels_list = list(new_df[category].value_counts().head(number).index)
    data_list = list(new_df[category].value_counts().head(number))

    # Création et stockage des valeurs et des labels dans un dictionnaire (mise en page)
    cls_ = {}
    for i in range(len(labels_list)):
        if(str(labels_list[i]) not in cls_.keys()):
            cls_[str(labels_list[i])] = int(data_list[i])
    return cls_

def graphsPdf(category, number):
    """ 
        FONCTIONNEL
        Paramètres: -> category: AUTHOR CHANNEL DATE
                    -> number  : taille du classement
        Fonction: On sauvegarde le graphique 'category'/'number' avec les données du jour
        Modifications: None
    """

    # Récupération du DataFrame
    openDataFrame()

    # Récupération de la date du jour pour actualiser le titre
    todayDate = datetime.datetime.now()
    currentDate = str(todayDate.year)+str('/')+str(todayDate.month)+str('/')+str(todayDate.day)

    # Création du nouveau DataFrame avec les données correponsantes à la date du jour
    new_df = df[df['DATE']==currentDate]

    # Récupération des labels et des valeurs du jour
    labels_list = list(new_df[category].value_counts().head(number).index)
    data_list = list(new_df[category].value_counts().head(number))

    # Lambda expression pour générer des couleurs aléatoires
    get_colors = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF), range(n)))
    
    # Création, enregistrement, exploitation et suppression du diagramme camembert
    for j in range(len(labels_list)):
        plt.bar(labels_list[j], data_list[j], label=labels_list[j], color=get_colors(1))
    
    plt.title("Activité des: "+ category)
    plt.xticks(rotation=20)
    plt.xlabel(category)
    plt.ylabel('values')
    plt.legend()
    title_graph = "graphs-mail/current_" + str(category)+str(".png")
    plt.savefig(title_graph)
    plt.close()