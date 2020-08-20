from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Testing connection"


@app.route("/test", methods=['POST'])
def givenString():
    req_data = request.get_json()
    
    string = req_data['string_to_cut']

    return '<h1>This is a test.</h1>'

    def modifyString():
        pass




if __name__ == "__main__":
    app.run()






#Use Postman to send POST request to the server "string_to_cut"
#Write function to return a new string containing every third letter from the original string 
#Return modified string