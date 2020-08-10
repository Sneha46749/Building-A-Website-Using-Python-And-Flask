from flask import Flask, render_template  #render_template accesses an HTML file stored in python file anywhere

app = Flask(__name__) 

@app.route('/')  
def home():  
    return render_template("home.html")

@app.route('/about/')    
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)    
