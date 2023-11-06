from flask import Flask, render_template , request
import numpy as np
app=Flask(__name__)
import pickle
import joblib
model=pickle.load(open('class.pkl', 'rb'))
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/data')
def data():
    return render_template("predict.html")

@app.route('/predict' , methods = ["POST"])
def predict():
   #  set1=request.form["set1"]
   #  set2=request.form["set2"]
   #  set3=request.form["set3"]
   #  set4=request.form["set4"] 
   #  set5=request.form["set5"] 
   #  set6=request.form["set6"] 
   #  set7=request.form["set7"] 
   #  set8=request.form["set8"]
   #  set9=request.form["set9"]
   #  set10=request.form["set10"]
   #  set11=request.form["set11"]
   #  set12=request.form["set12"] 
   #  set13=request.form["set13"]
   #  set14=request.form["set14"]
   #  set15=request.form["set15"]
   #  set16=request.form["set16"]
   #  set17=request.form["set17"]
   #  set18=request.form["set18"]
   #  x_test = np.array([int(set1),int(set2),int(set3),int(set4),int(set5),int(set6),int(set7),int(set8),int(set9),int(set10),int(set11),int(set12),int(set13),int(set14),int(set15)])
    x_test = [[(yo) for yo in request.form.values()]]
    prediction= model.predict(x_test)
    prediction=prediction[0]
    if prediction == 1:
       return render_template("secondpage.html",y="Normal Find")
    elif prediction == 2:
       return render_template("secondpage.html",y="Metastases")
    elif prediction == 3:
       return render_template("secondpage.html",y="align Lymph")
    elif prediction == 4:
       return render_template("secondpage.html",y="Fibrosis")
app.run(debug=True)