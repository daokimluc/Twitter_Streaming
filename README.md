Twitter Streaming Web Application
===============

Introduction
----
This is the python project with spark and flask compatibility. The project fetch trending tweets for a given location 
from Twitter API and start fetching it with spark streaming and then send it to the front-end with flask compatibility 
and shows the real time graph of top 10 trending tweets with its count. 


Project Doc
---
Project documentation link : [Documentation file](https://docs.google.com/document/d/1kv1IETPaYimrdfN2FLFbAS1Uc86zhEIh-NERsjWVPMU/edit)


Credentials for fetching Tweets
---
```   
CONSUMER_KEY = 'consumer key'
CONSUMER_SECRET = 'consumer secret key'
ACCESS_TOKEN = 'access token'
ACCESS_SECRET = 'access secret key'
```


Setup for Running the Project
---
```   
1. Open the project TwitterStreaming
2. Run python file 'twitter_app.py'
    -> python twitter_app.py
3. Run pythonn file 'spark_app.py'
    -> python spark_app.py
4. Run python file 'app.py'
    -> python app.py
5. Open the below url in your browser to see the real-time graph
    -> http://localhost:5011

```


Key Entities in Code
----
```   
+-- TwitterStreaming
|       +--static
|           +--images
|           +--styles
|               +--chart.js
|       +--templates
|           +--chart.html
|           +--index.html
|           +--search.html
|       +--app.py
|       +--spark-app.py
|       +--tweet.py
|       +--twitter_app.py
```


Dependencies
----
1. **flask**: It  is a micro web framework written in Python. It is classified as a microframework because it does not 
require particular tools or libraries.

2. **pyspark**: It is the Python API to support Apache Spark. Apache Spark is a distributed framework that can handle 
Big Data analysis. Spark is basically a computational engine, that works with huge sets of data by processing them in 
parallel and batch systems.
 
3. **requests_oauthlib**: It is used to directly fetch new access tokens without going through the normal OAuth workflow

4. **tweepy**: An easy-to-use Python library for accessing the Twitter API

5. **camelcase**: is the practice of writing phrases without spaces or punctuation, indicating the separation of words 
with a single capitalized letter, and the first word starting with either case.