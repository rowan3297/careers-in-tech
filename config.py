import os

class DevConfig(object):
    SECRET_KEY = "this is a marvellous idea".encode('utf8')
    GOOGLE_SEARCH_KEY = ""
    GOOGLE_SEARCH_CX = ""
    MONGO_URI = "mongodb://localhost:27017/skills_incubator"
    DEBUG = True
