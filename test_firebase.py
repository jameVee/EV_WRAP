import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate("se-02-a72d8-firebase-adminsdk-tc7q3-4136167b73.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

obj = {
    "Day_left":31,
    "Hour_Left":10,
    "Min_Left":59
}

obj2 = {
    "test2" : "jame"
}

db.collection(u'Product').document("1").set(obj2,merge=True)
