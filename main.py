from flask import Flask,render_template # here "Flask" is a class 
import pandas as pd
app = Flask("__name__")  # here "app" is website object

stations = pd.read_csv("data_small/stations.txt",skiprows=20)

@app.route("/")
def home():
    return render_template("home.html",data =stations)

@app.route("/api/v1/<station>/<date>")
def about(station,date):
    path ="data_small/TG_STAID"
    filename = "data_small/TG_STAID" + str(station).zfill(6)+ ".txt"
    df =pd.read_csv(filename,skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE']=="1860-01-05"]['   TG'].squeeze()/10


    return {"station": station,
            "data": date,
            "temperature": temperature}

if __name__ =="__main__" :
    app.run(debug=True)


