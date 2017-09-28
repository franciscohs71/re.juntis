from pymongo import MongoClient
from bson.objectid import ObjectId
import os, time, sys, csv,io,codecs,re
db = 0

def connect_Mongo():
	client = MongoClient("mongodb://rejuntis:uergs123@juntis-shard-00-00-gwz7q.mongodb.net:27017,juntis-shard-00-01-gwz7q.mongodb.net:27017,juntis-shard-00-02-gwz7q.mongodb.net:27017/test?ssl=true&replicaSet=Juntis-shard-0&authSource=admin",
		ssl = True)
	global db	
	db = client.test
	global db_Disc
	db_Disc = client.Discplinas
	global db_Prof
	db_Prof = client.Professores 


def get_ProfessorId(_id):
	cursor = db_Prof.professores.find({'_id': ObjectId(_id)})
	for document in cursor:
		return document

def get_ProfessorEmail(email):
        cursor = db_Prof.Professores.find({'email': email})
        for document in cursor:
                return document

def get_Professor():
        cursor = db_Prof.Professores.find()
        for document in cursor:
                return document

#connect_Mongo()
#print(get_professor())

