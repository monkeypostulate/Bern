from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def cbern_welcome_page():
    return """<h1 style = "text-align:center"> Welcome to cbern!</h1>
    <p> This is a great search ecosystem!</p>
    <p>We are planning to have vector search for patent and swiss parlament document</p>
    """

# Run the Flask application if the script is executed
if __name__ == '__main__':
    app.run( host='0.0.0.0',port=8080, debug=True)
