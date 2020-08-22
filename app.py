from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Testing connection"


@app.route("/test", methods=['POST'])
def givenString():
    req_data = request.get_json()
    
    cutting_string = req_data['string_to_cut']


    def modify_string():
       return(cutting_string[2:len(cutting_string):3])


    modified_string = {"return_string": modify_string()}

    return (modified_string)




if __name__ == "__main__":
    app.run()