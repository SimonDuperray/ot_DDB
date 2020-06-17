import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import datetime

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
        Modifications: -> Changer la palette de couleurs  
                       -> Légende en dehors du graphique
    """

    # Récupération du DataFrame
    openDataFrame()

    # Récuperation des labels et des valeurs
    labels_list = list(df[category].value_counts().head(number).index)
    data_list = list(df[category].value_counts().head(number))

    # Création de l'histogramme
    fig, ax = plt.subplots()
    plt.bar(labels_list, data_list)
    plt.title("Répartition des messages p/r " + category)

    # légende horizontale inclinée de 45deg
    plt.xticks(rotation=45)
    plt.savefig('hist.png')
    plt.close()

def classementBot(category, number):
    """
        FONCTIONNEL
        Paramètres: -> category: AUTHOR CHANNEL DATE
                    -> number  : taille du classement
        Fonction: Envoi du classement en message privé
        Modifications: -> Mise en page dans l'embed à revoir
    """
    # Récupération du DataFrame
    openDataFrame()

    # On retourne les 'number' premières valeurs de 'category'
    return df[category].value_counts().head(number)

def camembertBot(category, number):
    """
        FONCTIONNEL
        Paramètres: -> category: AUTHOR CHANNEL DATE
                    -> number  : taille du classement
        Fonction: Envoi d'un diagramme camembert en message privé
        Modifications: -> Changer la palette de couleurs 
                       -> Personnaliser le graphique
    """

    # Récupération du DataFrame
    openDataFrame()

    # Récuperation des labels et des valeurs
    labels_list = list(df[category].value_counts().head(number).index)
    data_list = list(df[category].value_counts().head(number))

    # Création du diagramme
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
        Modifications: -> Changer la palette de couleurs 
                       -> Personnaliser le graphique
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

    # Création, enregistrement, exploitation et suppression du diagramme camembert
    fig, ax = plt.subplots()
    plt.bar(labels_list, data_list)
    plt.title("Activité des: "+ category)
    plt.xticks(rotation=45)
    title_graph = "graphs-mail/current_" + str(category)+str(".png")
    plt.savefig(title_graph)
    plt.close()
    labels=[]
