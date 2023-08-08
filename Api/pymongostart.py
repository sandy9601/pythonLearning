from pymongo import MongoClient
from flask import Flask, request, jsonify,make_response
import datetime

app = Flask(__name__)

client = MongoClient("localhost", 27017)
db = client.test_sample_database
collection = db.test_sample_collection


@app.post("/create")

def create_user():
    data=request.json
    data.update({"time_stamp": datetime.datetime.now(tz=datetime.timezone.utc)})
    print(data)
    db.collection.insert_one(data)
    response = make_response("user created", 201)
    return response


@app.get("/get")

def get_user():
    data=request.args.get("name")
    print(data)
    user=db.collection.find_one({"name":data}, {"_id": 0})
    print(user)
    return (
        jsonify(
            {
                "message": "user datails found.",
                "success": True,
                "payload": user,
            }
        ),
        500,
    )

if __name__ == "__main__":
    app.run(debug=True)
