data1 = []  # Liste pour stocker les dictionnaires
rating={}
data=[]


with open('data_study.txt', 'r') as file:
        lines = file.readlines()  # Lire chaque ligne du fichier
        print()


keys = [key.strip() for key in lines[0].split("|") if key.strip()]  # Les clés sont dérivées de la première ligne
print(keys)
for line in lines[1:]:  # Commencer à l'index 1 pour ignorer l'en-tête
        values = [value.strip() for value in line.split("|") if value.strip()]  # Nettoyer les valeurs
        data1.append(dict(zip(keys, values))) 

print(data1)