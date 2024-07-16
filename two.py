from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello():
     return "<center><h1 style= background-color:cyan;> Hi I am Ramesh.</h1><center><br><h2>i am here to learn the front-end and back-end this is my simple project using the flask</h2>"
#main program
if __name__=="__main__":
     app.run(debug=True)
