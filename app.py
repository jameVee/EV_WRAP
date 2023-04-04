from flask import Flask
from flask_restful import Api,Resource

# google sheet
import gspread
sa =  gspread.service_account(filename="se-02-a72d8-759b1dee5bc7.json")
sh = sa.open("Time_Auction_EV")
wks = sh.worksheet("Sheet1")

# Firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate("se-02-a72d8-firebase-adminsdk-tc7q3-4136167b73.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


app = Flask(__name__)
api = Api(app)

#design
class Auction_GoogleSheet(Resource):
    def post(self,Product_Code,Date,Time,Hour_Auction):
        data = [Product_Code,Date,Time,Hour_Auction]
        wks.append_row(data)
        return {"data" : data,"result" : "Append row success."}

class GoogleSheet_to_FireBase(Resource):
    def post(self,Product_Code,Day_left,Hour_Left,Min_Left):
        data = [Product_Code,Day_left,Hour_Left,Min_Left]
        obj = {
            "Day_left" : Day_left,
            "Hour_Left" : Hour_Left,
            "Min_Left" : Min_Left
        }
        db.collection(u'Test').document(Product_Code).set(obj,merge=True)
        return {"data" : data,"result" : "Add data to FireBase Success."}

class Ship_Product_to_Customer(Resource):
    def post(self,Product_Code,Day_left,Hour_Left,Min_Left):
        data = [Product_Code,Day_left,Hour_Left,Min_Left]
        obj = {
            "Day_left" : Day_left,
            "Hour_Left" : Hour_Left,
            "Min_Left" : Min_Left
        }
        db.collection(u'Product').document(Product_Code).set(obj,merge=True)
        return {"data" : data,"result" : "Add data to FireBase Success."}
    def get(self):
        return {"data" : "Hello world!!"}


#call
api.add_resource(Auction_GoogleSheet,"/auction/<int:Product_Code>/<string:Date>/<string:Time>/<int:Hour_Auction>")
api.add_resource(GoogleSheet_to_FireBase,"/GsToFb/<string:Product_Code>/<string:Day_left>/<string:Hour_Left>/<string:Min_Left>")

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
