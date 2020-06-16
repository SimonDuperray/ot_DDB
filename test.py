import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

def getPreciseData(category):
    """
        Affichage de la répartition des messages 
        en fonction du paramètre
    """
    # stockage du DataFrame dans une constante
    df = pd.read_csv('dataset.csv', error_bad_lines=False, delimiter=";")
    # création de la liste des valeurs uniques
    slices = []
    for i in range(len(df[category].value_counts())):
        slices.append(df[category].value_counts()[i])
    # création de la liste de labels
    labels = list(df[category].unique())
    # création du diagramme (histogramme)
    fig, ax = plt.subplots()
    plt.bar(labels, slices)
    plt.title("Répartition des messages p/r " + category)
    # légende horizontale inclinée de 45deg
    plt.xticks(rotation=45)
    plt.savefig('current_graph.png')
    plt.close()