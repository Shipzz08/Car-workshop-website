from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")  # Connection to MongoDB, replace with your MongoDB connection string
db = client["mydatabase"]  # Replace "mydatabase" with your database name
collection = db["user_data"]  # Collection to store user data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_data = {
        'name': request.form['name'],
        'email': request.form['email'],
        'date' : request.form['date'],
        'message' : request.form['message'],
        'time' : request.form['time']
    }
    collection.insert_one(user_data)
    return 'Appointment scheduled Data successfully stored in MongoDB!'

if __name__ == '__main__':
    app.run(debug=True, port=5001)
