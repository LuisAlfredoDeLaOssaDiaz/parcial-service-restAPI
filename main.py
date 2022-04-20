from flask import Flask, jsonify, request
import json

app = Flask(__name__)

users = [ 
    {
        "Username" : "Admin",
        "Age" : "25"
    },
    {
        "Username" : "Luis",
        "Age" : "25"
    }
]

@app.route('/users', methods=['GET'])
def getAllUsers():
    return jsonify(users), 200

@app.route('/users/<username>', methods=['GET'])
def getlUsersByUsername(username):
    result = next((user for user in users if user["Username"] == username),None)
    if result is not None:
        return jsonify(result), 200
    else: 
        return "User not found", 404

@app.route('/users', methods=['POST'])
def addUser():
    body = json.loads(request.data)

    userName = body["Username"]
    age = body["Age"]

    newUser = {
        "Username": userName,
        "Age": age
    }

    users.append(newUser)
    return jsonify(newUser), 200


@app.route('/users/<username>', methods=['DELETE'])
def deleteUser(username):
    userFound = None
    for index, user in enumerate(users):
        if user["Username"] == username:
            userFound = user
            users.pop(index)
    if userFound is not None:
        return "User deleted", 200
    else: 
        return "User not found", 404

@app.route('/users/<username>', methods=['PUT'])
def updateUser(username):
    body = json.loads(request.data)

    newUsername = body["Username"]
    newAge = body["Age"]

    updatedUser = {
        "Username": newUsername,
        "Age": newAge
    }

    userUpdated = None

    for index, user in enumerate(users):
        if user["Username"] == username:
            userUpdated = updatedUser
            users[index] = updatedUser
            
    if userUpdated is not None:
        return "User Updated", 200
    else: 
        return "User not found", 404

if __name__ == "__main__":
    app.run(debug=True)