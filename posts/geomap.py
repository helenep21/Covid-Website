from geopy.geocoders import Nominatim
from datetime import datetime
import folium
import sqlite3

def carto():
    connexion = sqlite3.connect("./db.sqlite3")
    curseur = connexion.cursor() 
    
    #Par Adresse
    curseur.execute("SELECT up.address, up.city,up.country, SUM(ca.quantite) FROM auth_user as au, commande_article as ca, users_profile as up, commande_commande as cc WHERE up.user_id=au.id AND au.username=cc.username AND cc.id=ca.id;")
    result = curseur.fetchone()
    listAdresse=[]
    listVille=[]
    listPays=[]
    listCom=[]
    while result:
        listAdresse.append(result[0])
        listVille.append(result[1])
        listPays.append(result[2])
        listCom.append(result[3])
        result = curseur.fetchone()
    geolocator = Nominatim(user_agent="myGeocoder", timeout=3)
    lat=[]
    lng=[]
    for i in range(len(listAdresse)):
        lieu=listAdresse[i]+','+listVille[i]+','+listPays[i]
        info=geolocator.geocode(lieu)
        lat.append(info.latitude)
        lng.append(info.longitude)
    
    
    
    m = folium.Map(location=[lat[0], lng[0]])
    for i in range(len(listAdresse)):
        folium.Circle(
            radius=listCom[i]*5000,
            location=[lat[i], lng[i]],
            popup=listAdresse[i],
            color='blue',
            fill=False,
        ).add_to(m)
    m.save('./templates/carteAdresse.html')
    
    
    #Par Ville
    curseur.execute("SELECT up.city,up.country, SUM(ca.quantite) FROM auth_user as au, commande_article as ca, users_profile as up, commande_commande as cc WHERE up.user_id=au.id AND au.username=cc.username AND cc.id=ca.id GROUP BY up.city;")
    result=curseur.fetchone()
    Villes=[]
    Pays=[]
    CompteurCommande=[]
    while result:
        Villes.append(result[0])
        Pays.append(result[1])
        CompteurCommande.append(result[2])
        result=curseur.fetchone()
    
    geolocator = Nominatim(user_agent="myGeocoder", timeout=3)
    lat=[]
    lng=[]
    for i in range(len(Villes)):
        lieu=Villes[i]+","+Pays[i]
        info=geolocator.geocode(lieu)
        lat.append(info.latitude)
        lng.append(info.longitude)

    m = folium.Map(location=[lat[0], lng[0]],zoom_start=6)
    for i in range(len(Villes)):
        folium.Circle(
            radius=CompteurCommande[i]*5000,
            location=[lat[i], lng[i]],
            popup=Villes[i],
            color='blue',
            fill=False,
        ).add_to(m)
    m.save('./templates/carteVille.html')
    
    #Par Pays
    curseur.execute("SELECT up.country, SUM(ca.quantite) FROM auth_user as au, commande_article as ca, users_profile as up, commande_commande as cc WHERE up.user_id=au.id AND au.username=cc.username AND cc.id=ca.id GROUP BY up.country;")
    result=curseur.fetchone()
    Pays=[]
    CommandeTot=[]
    while result:
        Pays.append(result[0])
        CommandeTot.append(result[1])
        result=curseur.fetchone()
    
    geolocator = Nominatim(user_agent="myGeocoder", timeout=3)
    lat=[]
    lng=[]
    for i in range(len(Pays)):
        info=geolocator.geocode(Pays[i])
        lat.append(info.latitude)
        lng.append(info.longitude)
        
    m = folium.Map(location=[lat[0], lng[0]],zoom_start=6)
    for i in range(len(Pays)):
        folium.Circle(
            radius=CommandeTot[i]*5000,
            location=[lat[i], lng[i]],
            popup=Pays[i],
            color='blue',
            fill=False,
        ).add_to(m)
    m.save('./templates/cartePays.html')
    