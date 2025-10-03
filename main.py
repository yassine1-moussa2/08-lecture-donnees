"""Imports et définition des variables globales"""
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(l):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open("listes.csv","r",encoding="utf-8") as f:
        for line in f:
            numbers=line.split(r"[;, \t]+"),line.strip()
            row=[str(i) for i in numbers]
            l.append(row)
    return l

def get_list_k(data, k):
    """cette fonction nous donne le k-ième élément de la liste"""
    l=[] #ajout d'une liste vide
    l.append(data[k])
    return l

def get_first(l):
    """cette fonction nous affiche le premier élément de la liste """
    return l[0]

def get_last(l):
    """cette fonction affiche le dernier élément de la liste"""
    return l[-1]

def get_max(l):
    """cette fonction affiche le plus grand élément de la liste"""
    return max(l)

def get_min(l):
    """cette fonction affiche le plus petit élément de la liste"""
    return min(l)

def get_sum(l):
    """cette fonction affiche la somme des élements de la liste"""
    return sum(l)

#### Fonction principale


def main():
    """afficher les résultats souhaités"""
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
        k = 37
    print(k, get_list_k(data, 37))
    print("first:", get_first(data))
    print("last:", get_last(data))
    print("max:", get_max(data))
    print("min:", get_min(data))
    #print("sum:", get_sum(data))

if __name__ == "__main__":
    main()
