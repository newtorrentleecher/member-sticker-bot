#The PyMongo distribution contains tools for interacting with MongoDB database from Python
import pymongo

#def adduser(update, context):
#   db(update)
def db(data):
    DATABASE_NAME = '' #Your Database Name here.
    myclient = pymongo.MongoClient()
    database = myclient[DATABASE_NAME]

    userid = data.message.chat.id
    chattype = data.message.chat.type

    if chattype == 'private':
        collection = database["users"]

    result = collection.find_one({'userid': userid})

    try:
        result['userid']
        userexist = True
    except:
        userexist = False

    username = data.message.chat.username
    firstname = data.message.chat.first_name
    lastname = data.message.chat.last_name


    user = {}
    user['userid'] = userid
    user['chattype'] = chattype 
    user['username'] = username
    user['firstname'] = firstname
    user['lastname'] = lastname

    if (userexist == False):
        collection.insert_one(user)
