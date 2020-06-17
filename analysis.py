import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import datetime

def openDataFrame():
    """
        FONCTIONNEL
        Stockage du DataFrame
    """
    # stockage du DataFrame dans une constante
    global df
    df = pd.read_csv('dataset.csv', error_bad_lines=False, delimiter=";", encoding="ISO-8859-1")

def histogrammeBot(category, number):
    """
        FONCTIONNEL
        Envoi d'un histogramme en message privé
    """
    # open dataframe
    openDataFrame()
    labels_list = list(df[category].value_counts().head(number).index)
    data_list = list(df[category].value_counts().head(number))
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
        Envoi classement en message privé
    """
    openDataFrame()
    return df[category].value_counts().head(number)

def camembertBot(category, number):
    """
        FONCTIONNEL
        Test envoi camembert selection dataframe
    """
    openDataFrame()
    labels_list = list(df[category].value_counts().head(number).index)
    data_list = list(df[category].value_counts().head(number))
    # création du diagramme
    plt.pie(data_list, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
    plt.title("Répartition messages p/r " + category)
    plt.legend(labels_list)
    plt.tight_layout()
    plt.savefig('cam.png')
    plt.close()

def clsPdf(category, number):
    """
        FONCTIONNEL
        Envoi du classement sous forme de dictionnaire pour mise en page sur le pdf
    """
    openDataFrame()
    todayDate = datetime.datetime.now()
    currentDate = str(todayDate.year)+str('/')+str(todayDate.month)+str('/')+str(todayDate.day)
    new_df = df[df['DATE']==currentDate]
    labels_list = list(new_df[category].value_counts().head(number).index)
    data_list = list(new_df[category].value_counts().head(number))
    cls_ = {}
    for i in range(len(labels_list)):
        if(str(labels_list[i]) not in cls_.keys()):
            cls_[str(labels_list[i])] = int(data_list[i])
    return cls_

def graphsPdf(category, number):
    """ 
        FONCTIONNEL
        Envoi des graphs pour les afficher sur le pdf
    """
    openDataFrame()
    todayDate = datetime.datetime.now()
    currentDate = str(todayDate.year)+str('/')+str(todayDate.month)+str('/')+str(todayDate.day)
    new_df = df[df['DATE']==currentDate]
    labels_list = list(new_df[category].value_counts().head(number).index)
    data_list = list(new_df[category].value_counts().head(number))
    fig, ax = plt.subplots()
    plt.bar(labels_list, data_list)
    plt.title("Activité des: "+ category)
    plt.xticks(rotation=45)
    title_graph = "graphs-mail/current_" + str(category)+str(".png")
    plt.savefig(title_graph)
    plt.close()
    labels=[]
