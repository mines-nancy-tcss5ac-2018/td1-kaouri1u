f=open('p022_names.txt','r')
l=f.split(',') #ceci permet d'obtenir une liste des noms.
l1=sorted(l) #ceci permet de trier les noms dans l'ordre alphabétique.
def valeur_lettre(x):
    if 65<=ord('x')<=90:   #les lettres majuscules sont codées entre 65 et 90.
        return ord('x')-64
    elif 97<=ord('x')<=122: #les lettres miniscules sont codées entre 97 et 122.
        return ord('x')-96
assert valeur_lettre('a')==97
l2=[]
for i in range (len(l1)):
    s=0
    for j in range(len(l1[i])):
        s=s+valeur_lettre(l1[i][j]) # s est la somme des valeurs de chaque lettre dans le nom d'indice i dans la liste l1
    l2+=[s*(i+1)] #J'ajoute les scores de chaque nom dans la liste l2
f.close()



    