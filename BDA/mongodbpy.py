
import pymongo
import time
client = pymongo.MongoClient("mongodb+srv://omarkhatib96:azert@cluster0.j4dua.mongodb.net/")




pipeline_film_par_an=[{'$group':{"_id":"$year","total":{"$sum":1}}},{'$sort': {'total':-1}}]
pipeline_films_par_note=[{'$group':{'_id':"$info.rating",'total':{'$sum':1}}},{'$sort': {'total':-1}}]#classement par ordre d'effectif de note décroissant 
pipeline_films_par_note_2=[{'$group':{'_id':"$info.rating",'total':{'$sum':1}}},{'$sort': {'_id':-1}}]#classement par ordre de note décroissant


def create_collection(cursor,collection_name):
    collection=client.mydb[collection_name]
    for document in cursor:
        collection.insert_one(document)
    
    return collection



#collection_2000=create_collection(cursor_2000,"mycollection_2000")
#print(collection_2000.find().count())


#Les collections de différentes tailles
collection=client.mydb.mycollection
collection_10= client.mydb.mycollection_10
collection_100= client.mydb.mycollection_100
collection_250= client.mydb.mycollection_250
collection_1000= client.mydb.mycollection_1000
collection_2000= client.mydb.mycollection_2000


def req1(Collection):
    start_time=time.time()
    resultat=Collection.find({"title":"Police Academy 4: Citizens on Patrol"})
    return resultat, time.time()-start_time
def req2(Collection):
    start_time=time.time()
    resultat=Collection.find({"year":2009})
    return resultat,time.time()-start_time

def req3(Collection):
    start_time=time.time()
    resultat=Collection.count()
    return resultat,time.time()-start_time



def req4(Collection):
    start_time=time.time()
    resultat= Collection.find({"directors":"James Wan"})
    return resultat,time.time()-start_time

def req5(Collection):
    start_time=time.time()
    resultat=Collection.find({ "info.genres":"Horror"})
    return resultat,time.time()-start_time

def req6(Collection):
    start_time=time.time()

    resultat=Collection.find({ "info.rating":9})
    return resultat,time.time()-start_time

def req7(Collection):
    start_time=time.time()
    resultat=Collection.aggregate(pipeline_film_par_an)
    return resultat,time.time()-start_time

def req8(Collection):
    start_time=time.time()
    resultat= Collection.aggregate(pipeline_films_par_note_2)
    return resultat,time.time()-start_time
def req9(Collection):
    start_time=time.time()

    resultat= Collection.find({"info.directors":{'$size':2}},{"info.directors":1,"title":1,"year":1}).sort([("info.directors", 1)])
    return resultat,time.time()-start_time

def req10(Collection):
    start_time=time.time()
    resultat=Collection.find({"info.directors":{'$size':1}},{"info.directors":1,"title":1,"year":1,"_id":0}).sort([("info.directors", 1)])
    return resultat ,time.time()-start_time





def show_docs(cursor):
    for doc in cursor:
        print(doc)




def show_table():
    from texttable import Texttable

    tab=[[1,'find({"title":"Police Academy 4: Citizens on Patrol"}'],[2,'find({"year":2009})'],[3,'count()'],[4,'find({"directors":"James Wan"})'],[5,'find({ "info.genres":"Horror"})'],[6,'find({ "info.rating":9}'],[7,"nombre de films par an"],[8,"nombre de film par note+classement par ordre décroissant"],[9,'les films qui ont deux réalisateurs']]
    table=Texttable()
    table.add_rows(tab)
    print(table.draw())
import numpy as np
temps_exe=np.zeros((6,9))


#collection of 10 data
r,t1=req1(collection_10)
temps_exe[0][0]=t1
r,t1=req2(collection_10)
temps_exe[0][1]=t1

r,t1=req3(collection_10)
temps_exe[0][2]=t1
print("for 10",r,t1)

r,t1=req4(collection_10)
temps_exe[0][3]=t1

r,t1=req5(collection_10)
temps_exe[0][4]=t1

r,t1=req6(collection_10)
temps_exe[0][5]=t1


r,t1=req7(collection_10)
temps_exe[0][6]=t1

r,t1=req8(collection_10)
temps_exe[0][7]=t1

r,t1=req9(collection_10)
temps_exe[0][8]=t1


#collection of 100 data

r,t1=req1(collection_100)
temps_exe[1][0]=t1

r,t1=req2(collection_100)
temps_exe[1][1]=t1

r,t1=req3(collection_100)
temps_exe[1][2]=t1

r,t1=req4(collection_100)
temps_exe[1][3]=t1

r,t1=req5(collection_100)
temps_exe[1][4]=t1

r,t1=req6(collection_100)
temps_exe[1][5]=t1


r,t1=req7(collection_100)
temps_exe[1][6]=t1

r,t1=req8(collection_100)
temps_exe[1][7]=t1
r,t1=req9(collection_100)
temps_exe[1][8]=t1

#collection of 250 data


r,t1=req1(collection_250)
temps_exe[2][0]=t1

r,t1=req2(collection_250)
temps_exe[2][1]=t1

r,t1=req3(collection_250)
temps_exe[2][2]=t1

r,t1=req4(collection_250)
temps_exe[2][3]=t1

r,t1=req5(collection_250)
temps_exe[2][4]=t1

r,t1=req6(collection_250)
temps_exe[2][5]=t1


r,t1=req7(collection_250)
temps_exe[2][6]=t1

r,t1=req8(collection_250)
temps_exe[2][7]=t1

r,t1=req9(collection_250)
temps_exe[2][8]=t1

#collection of 1000 data

r,t1=req1(collection_1000)
temps_exe[3][0]=t1

r,t1=req2(collection_1000)
temps_exe[3][1]=t1

r,t1=req3(collection_1000)
temps_exe[3][2]=t1

r,t1=req4(collection_1000)
temps_exe[3][3]=t1

r,t1=req5(collection_1000)
temps_exe[3][4]=t1

r,t1=req6(collection_1000)
temps_exe[3][5]=t1

r,t1=req7(collection_1000)
temps_exe[3][6]=t1

r,t1=req8(collection_1000)
temps_exe[3][7]=t1

r,t1=req9(collection_1000)
temps_exe[3][8]=t1


#collection of 2000 data

r,t1=req1(collection_2000)
temps_exe[4][0]=t1

r,t1=req2(collection_2000)
temps_exe[4][1]=t1

r,t1=req3(collection_2000)
temps_exe[4][2]=t1

r,t1=req4(collection_2000)
temps_exe[4][3]=t1

r,t1=req5(collection_2000)
temps_exe[4][4]=t1

r,t1=req6(collection_2000)
temps_exe[4][5]=t1

r,t1=req6(collection_2000)
temps_exe[4][6]=t1

r,t1=req7(collection_2000)
temps_exe[4][7]=t1

r,t1=req8(collection_2000)
temps_exe[4][8]=t1
r,t1=req9(collection_2000)


#collection complète
r,t1=req1(collection)
temps_exe[5][0]=t1

r,t1=req2(collection)
temps_exe[5][1]=t1

r,t1=req3(collection)
temps_exe[5][2]=t1

r,t1=req4(collection)
temps_exe[5][3]=t1

r,t1=req5(collection)
temps_exe[5][4]=t1

r,t1=req6(collection)
temps_exe[5][5]=t1



r,t1=req7(collection)
temps_exe[5][6]=t1

r,t1=req8(collection)
temps_exe[5][7]=t1
r,t1=req9(collection)
temps_exe[5][8]=t1


show_table()

import matplotlib.pyplot as plt

req=[i for i in range(9)]
plt.plot(req, temps_exe[0],label="10 documents")
plt.plot(req, temps_exe[1],label="100 documents")
plt.plot(req, temps_exe[2],label="250 documents")
plt.plot(req, temps_exe[3],label="1000 documents")
plt.plot(req, temps_exe[4],label="2000 documents")
plt.plot(req, temps_exe[5],label="4609 documents")
plt.xlabel('numéro de requêtes')
plt.ylabel("temps d'exécution de la requête en secondes")
plt.title("Temps d'exécution en fonction de la taille de la collection")
plt.legend()
plt.savefig("temps d'exécution.jpg")

plt.show()


