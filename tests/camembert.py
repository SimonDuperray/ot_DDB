def getPreciseData(category):
    """
        Affiche un camembert de la répartition des messages 
        en fonction du paramètre
    """
    # main('dataset.csv')
    # création de la liste des valeurs uniques
    slices = []
    for i in range(len(df[category].value_counts())):
        slices.append(df[category].value_counts()[i])
    # création de la liste de labels
    labels = list(df[category].unique())
    # création du diagramme
    plt.pie(slices, labels=labels, shadow=True, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})
    plt.title("Répartition messages p/r " + category)
    plt.tight_layout()
    plt.savefig('current_graph.png')
    plt.close()