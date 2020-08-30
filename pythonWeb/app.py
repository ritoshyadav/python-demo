from flask import Flask, jsonify, request
app=Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/add_two_nums',methods=["POST"])
def add_two_nums():
    #get x,y fromn the posted data
    dataDict=request.get_json()
    """
    return jsonify(dataDict)
    """
    x=dataDict["x"]
    y=dataDict["y"]

    z=x+y

    retJSON={
        "z":z
    }
    return jsonify(retJSON)
    
if __name__=="__main__":
    app.run(host='0.0.0.0')
