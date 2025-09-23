from flask import Flask

# Create a new Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def hello_world():
    return "<h1>Hello, World! This is my Flask App deployed with Jenkins!</h1>"

# Run the app if this script is executed directly
if __name__ == '__main__':
    # The host='0.0.0.0' makes the app publicly accessible on your network
    app.run(host='0.0.0.0', port=5000)
