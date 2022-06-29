from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def level_1():
    return render_template("index.html", num=3,color="blue")  # Return the string 'Hello World!' as a response

@app.route('/play/<int:num>')          # The "@" decorator associates this route with the function immediately following
def level_2(num):
    return render_template("index.html", num=num,color="blue")

@app.route('/play/<int:num>/<string:color>')          # The "@" decorator associates this route with the function immediately following
def level_3(num,color):
    return render_template("index.html", num=num,color=color)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.