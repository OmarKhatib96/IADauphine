# Databricks notebook source
# MAGIC %md # Exploring the Movielens dataset with the Spark RDD API

# COMMAND ----------

# MAGIC %matplotlib inline
# MAGIC 
# MAGIC import urllib
# MAGIC import urllib.request as req
# MAGIC import zipfile
# MAGIC import glob
# MAGIC import matplotlib.pyplot as plt
# MAGIC import numpy as np
# MAGIC import pandas as pd
# MAGIC 
# MAGIC import pyspark
# MAGIC from pyspark.sql import SparkSession

# COMMAND ----------

# MAGIC %md ### Downloading the dataset

# COMMAND ----------

url = 'http://files.grouplens.org/datasets/movielens/ml-20m.zip'
filehandle, _ = urllib.request.urlretrieve(url)
zip_file_object = zipfile.ZipFile(filehandle, 'r')
zip_file_object.namelist()

zip_file_object.extractall()

movies_path = "file:///databricks/driver/ml-20m/movies.csv"
ratings_path = "file:///databricks/driver/ml-20m/ratings.csv"

# COMMAND ----------

# MAGIC %md ### Loading the data

# COMMAND ----------

ss = SparkSession.builder \
    .master("local[*]")  \
    .appName('movielens-rdd') \
    .getOrCreate()

sc = ss.sparkContext
sc

# COMMAND ----------

# MAGIC %md Loading data with Spark Dataframe API.  
# MAGIC Loading a csv with the RDD API is not supported out of the box and is painful to implement.

# COMMAND ----------

ratings_df = spark.read.options(header=True, inferSchema=True).csv(ratings_path)

# COMMAND ----------

# MAGIC %md Did you notice this created a job in the Spark UI? I thought Spark was lazy until we requested an action ?  
# MAGIC Rerun the same command with inferSchema=False and compare the schema with the command df.printSchema(). Can you understand why Spark triggered a job and what it was for ?

# COMMAND ----------

ratings_df.take(1)

# COMMAND ----------

ratings_rdd = ratings_df.rdd.map(lambda x: x.asDict())

# COMMAND ----------

ratings_rdd.take(10)

# COMMAND ----------

movies_df = spark.read.options(header=True, inferSchema=True).csv(movies_path)

# COMMAND ----------

movies_rdd = movies_df.rdd.map(lambda x: x.asDict())

# COMMAND ----------

movies_rdd.take(10)

# COMMAND ----------

# MAGIC %md The ratings RDD is a bit large (about 2 min to run a request on it on a docker container with two cores). You can work on a smaller version of it to develop and debug your job and then run it on the full RDD to get the result.  
# MAGIC Why do we persist the small RDD and not the regular one ?

# COMMAND ----------

ratings_small_rdd = ratings_rdd.filter(lambda x: x['userId'] < 20000).persist(pyspark.StorageLevel.DISK_ONLY)

# COMMAND ----------

# MAGIC %md You may have issues with Persist command. When sampling and doing data analysis on a dataset good practice is to write a new dataset once and for all so speed up analyses.

# COMMAND ----------

sampled_path = "file:///databricks/driver/ml-20m/sampled_ratings.csv"
ratings_df.sample(fraction=0.1).write.format("csv").save(sampled_path, mode="overwrite",header=True)

# COMMAND ----------

ratings_small_df = spark.read.options(header=True, inferSchema=True).csv(sampled_path)
ratings_small_rdd = ratings_small_df.rdd.map(lambda x: x.asDict())

# COMMAND ----------

# MAGIC %md ### Q1. How many ratings ?

# COMMAND ----------

ratings_small_rdd.count()
ratings_small_rdd.take(2)



# COMMAND ----------



# COMMAND ----------

# MAGIC %md ### Q2. How many users ?
# MAGIC 
# MAGIC Read the documentation for the distinct function in the RDD API.
# MAGIC Where is the userId column ? What happened during the sampling ? Check the 'save' api for a solution.
# MAGIC Can you compute it without using distinct ?

# COMMAND ----------

ratings_small_rdd.map(lambda x:x['userId']).distinct().count()

#r_small=ratings_small_rdd.groupBy("rating").show()
#second_method
#keyBy: RDD[dict]=>PairRDD[Userid,dict]
#mapvalues:PairRDD[Userid,dict]=>PairRDD(Userid,1)
#reduceByKey:=>PairRDD[UserId,1]
#count
#deuxième solution
def extract_user(record):
  return record['userId']


#ratings_small_rdd.keyBy(lambda x:x['userId'] ).take(1)
ratings_small_rdd.keyBy(extract_user ).mapValues(lambda x:1).reduceByKey(lambda x,y:1).count()

# COMMAND ----------

# MAGIC %md ### Q3. How many ratings per grade ?
# MAGIC 
# MAGIC How many users rated a movie with grade r for r in [0,5]?    
# MAGIC Plot it. Do you notice something unusual ?

# COMMAND ----------



# COMMAND ----------

ratings_per_grade = ratings_small_rdd.keyBy(lambda x : x['rating']).mapValues(lambda x : 1).reduceByKey(lambda x,y : x+y).collect()

dict_ratings_per_grade = dict(ratings_per_grade)
plt.bar(dict_ratings_per_grade.keys(), dict_ratings_per_grade.values(), width=0.5, color='g')


# COMMAND ----------

# MAGIC %md ### Q4. Histogram of number of ratings per user
# MAGIC 
# MAGIC Plot the distribution of the number of movies rated per user. In other words, what is the fraction of users that rated between bins[i] and bins[i+1] movies for the following bins.  
# MAGIC What is the average and median number of ratings per user?

# COMMAND ----------

bins = np.unique(np.logspace(0, 160, base=1.05, num=50, dtype='int32'))
bins

# COMMAND ----------

def bucketize(x):
  return np.digitize(x,bins)




ratings_count_per_user_per_bucket = ratings_small_rdd.keyBy(lambda x : x['userId']).mapValues(lambda x : 1).reduceByKey(lambda x,y : x+y).map(lambda x : (bucketize(x[1]),1)).reduceByKey(lambda x,y : x+y).collect()




#map(lambda x:(bucketize(x[1]),1))reduceByKey(lambda x,y:x+y).collect()

df = pd.DataFrame(ratings_count_per_user_per_bucket, columns=["bucket_id", "count"])
df = df.sort_values(by="bucket_id").reset_index(drop=True)
df.plot.bar()
#we have to associate each user to a bucket and sum the number of users in each bucket
#for this we will need 

# COMMAND ----------

df=pd.DataFrame(ratings_count_per_user_per_bucket,columns=["bucket_id","count"])




# COMMAND ----------

# MAGIC %md ### Q5. Most popular movies
# MAGIC 
# MAGIC What are the 20 movies with the most ratings ?  
# MAGIC We would like the answer with the movie title and not the movie id.  
# MAGIC Look at the documentation of the join and top functions.

# COMMAND ----------

#RDD[movieId,RatingCount]
nb_ratings_per_movies=ratings_small_rdd.map(lambda  x:(x['movieId'],1)).reduceByKey(lambda x,y:x+y)
movie_by_id_rdd=movies_rdd.keyBy(lambda x:x['movieId']).mapValues(lambda x:x['title'])
rating_with_title=nb_ratings_per_movies.join(movie_by_id_rdd).mapValues(lambda x:{'rating':x[0],'title':x[1]}).values()      
rating_with_title.top(20,key=lambda x:['rating'])
#RDD[MovieID,MovieName]
#RDD[movieID,{RatingCount,MovieName}]
#RDD[RatingCount,MovieName]
#call the top function


#Accumulator:
#my_counter=sc.accumulator(8)
#def getUserId(x):
#global my_counter*if x['userId']

# COMMAND ----------

# MAGIC %md ### Q6. Writing partioned datasets
# MAGIC 
# MAGIC The ratings dataset is available as one big csv file. It is not very convenient since we have to go through the entire file to look for ratings for a specific userId. Moreover, we cannot open only a small part of the dataset.  
# MAGIC Could you write the ratings dataset into 16 files located in /tmp/ratings/part=X/ratings.csv for X in [0, 16[ where userId in part=X are such that userId % 16 == X ?  Your function should return the list of written files with the number of ratings for each file.
# MAGIC Look at the documentation of partitionBy and mapPartitionsWithIndex.

# COMMAND ----------

# MAGIC %md ### Q7. Most popular genre per year
# MAGIC 
# MAGIC For every year since 1980, determine what is the most popular genre.  
# MAGIC Look at the documentation of the flatMap function.

# COMMAND ----------

# MAGIC %md ### Q8.  Best movies
# MAGIC 
# MAGIC Amongst the movies with at least 1000 ratings, what are the top 20 movies per median rating ?

# COMMAND ----------

ss.stop()
