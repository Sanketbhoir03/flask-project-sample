from flask import Flask

# Create a new Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return "<h1>Hello, World! This is my Flask App deployed with Jenkins!</h1>"

# In your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
