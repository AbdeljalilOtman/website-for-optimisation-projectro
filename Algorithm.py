from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Home.html', result=None)

@app.route('/submit', methods=['POST'])
def submit():
    user_input = list(request.form.get('Input2'))



    import math
    data1 = []  # Liste pour stocker les dictionnaires
    rating={}
    data=[]
    with open('data_study.txt', 'r') as file:
        lines = file.readlines() 

    keys = [key.strip() for key in lines[0].split("|") if key.strip()]  # Les clés sont dérivées de la première ligne

    for line in lines[1:]:  # Commencer à l'index 1 pour ignorer l'en-tête
        values = [value.strip() for value in line.split("|") if value.strip()]  # Nettoyer les valeurs
        data1.append(dict(zip(keys, values)))  # Créer un dictionnaire en associant les clés et les valeurs de chaque ligne
    data1.append({keys[0] : str(int(data1[-1]['Seance']) + 1),
         keys[1] : request.form.get('Input1'), 
         keys[2] : request.form.get('Input2'),
         keys[3] : request.form.get('Input3'),
         keys[4] : request.form.get('Input4'),
         keys[5] : request.form.get('Input5')})
    data_list=[list(data1[i].values()) for i in range(1,len(data1)) if data1[i]!={}]
    ata = []
    for i in data_list:
        l=[]
        for j in range(1,5):
            l.append(float(i[j]))
        data.append(l)
    for i in range(len(data)):
        rating[tuple(data[i])] = float(data_list[i][-1])


    def nearBy(L, pos): #the closest tuple to (a, b, c, d)  and pos is the position of the selected column

        Liste_Tuple_Distance=[]

        data2 = data.copy()
        data2.remove(L)

        L2 = L.copy()
        L2.pop(pos)

        x = L2[0]
        pos_x = L.index(x)
        y = L2[1]
        pos_y = L.index(y)
        z = L2[2]
        pos_z = L.index(z)


        for liste in data2:
            distance = math.sqrt(math.pow(x-liste[pos_x],2)+math.pow(y-liste[pos_y],2)+math.pow(z-liste[pos_z],2))
            Liste_Tuple_Distance.append([liste,distance])

        Liste_Tuple_Distance.sort(key = lambda x:x[1])


        return Liste_Tuple_Distance[0]




    def difference_rating_near(L,pos):
        return rating[tuple(L)]-rating[tuple(nearBy(L,pos)[0])]


    def get_optimal(data, rating):
        taille=len(data)
        data.sort(key =  lambda x:rating[tuple(x)])
        data_top100 = [data[taille-i] for i in range(1,100)]

        n=4

        liste_optimal_colonne = []

        for pos in range(n):
            liste_tuple_diffRating = []
            for liste in data_top100:
                liste_tuple_diffRating.append([liste,difference_rating_near(liste,pos)])

            liste_tuple_diffRating.sort(key = lambda x:x[1])
            liste_optimal_colonne.append(liste_tuple_diffRating[len(liste_tuple_diffRating)-1][0][pos])

        return liste_optimal_colonne
    
    L = get_optimal(data, rating)
    L[1] = L[1]/60
    L[2] = L[2]/60


    
    return render_template('Home.html', result=L)

@app.route('/about')
def about():
    return render_template('About.html')  # Create About.html template

@app.route('/contact')
def contact():
    return render_template('Contact.html')  # Create Contact.html template

if __name__ == '__main__':
    app.run(debug=True)
