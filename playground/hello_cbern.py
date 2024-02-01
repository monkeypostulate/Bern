from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def cbern_welcome_page():
    return "<h1> Welcome to cbern!</h1> <p> This is a great search ecosystem!</p>"

# Run the Flask application if the script is executed
if __name__ == '__main__':
    app.run(debug=True)
