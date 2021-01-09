

import pymongo
client = pymongo.MongoClient("mongodb+srv://omarkhatib96:azert@cluster0.j4dua.mongodb.net/")



req1=client.mydb.mycollection.find({"title":"Police Academy 4: Citizens on Patrol"})
req2=client.mydb.mycollection.find({"year":2009})
req3=client.mydb.mycollection.count()
req4=client.mydb.mycollection.find({"directors":"James Wan"} )
req5=client.mydb.mycollection.find({ "info.genres":"Horror"})
req6=client.mydb.mycollection.find({ "info.rating":9})



pipeline_film_par_an=[{'$group':{"_id":"$year","total":{"$sum":1}}},{'$sort': {'total':-1}}]
pipeline_films_par_note=[{'$group':{'_id':"$info.rating",'total':{'$sum':1}}},{'$sort': {'total':-1}}]#classement par ordre d'effectif de note décroissant 
pipeline_films_par_note_2=[{'$group':{'_id':"$info.rating",'total':{'$sum':1}}},{'$sort': {'_id':-1}}]#classement par ordre de note décroissant


agg1=client.mydb.mycollection.aggregate(pipeline_film_par_an)
agg2=client.mydb.mycollection.aggregate(pipeline_films_par_note_2)



req7=client.mydb.mycollection.find({"info.directors":{'$size':2}},{"info.directors":1,"title":1,"year":1}).sort([("info.directors", 1)])
req8=client.mydb.mycollection.find({"info.directors":{'$size':1}},{"info.directors":1,"title":1,"year":1,"_id":0}).sort([("info.directors", 1)])


def show_docs(cursor):
    for doc in cursor:
        print(doc)


show_docs(agg1)

