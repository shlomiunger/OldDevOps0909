import requests
from flask import Flask, request

app = Flask("something")


@app.route('/whatismyname', methods=['GET', 'POST', 'DELETE'])
def hello():
    my_score = 1
    if request.method == 'GET':
        return "mazda, citroen, chevrolet"
    elif request.method == 'POST':
        return "saved new car"
    return "<h1>" + str(my_score) + "</h1>"


@app.route('/cars', methods=['GET', 'POST', 'DELETE'])
def get_cars():
    if request.method == 'GET':
        my_file = open("cars.txt", "r")
        return my_file.readlines()



@app.route('/')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=True)