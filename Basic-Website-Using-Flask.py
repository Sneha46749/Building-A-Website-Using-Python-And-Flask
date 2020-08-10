from flask import Flask

app = Flask(__name__)  #Creating flask class instance/object

@app.route('/')  #URL where you will view your website and / means the home page
def home():  #This function defines what your web page will do
    return "Homepage here!"

@app.route('/about/')    
def about():
    return "About content"

if __name__=="__main__":
    app.run(debug=True)    
