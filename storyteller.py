"""
@author: raw
"""

from flask import Flask, request, render_template, jsonify
import socket,json,os

#import hashlib

app = Flask(__name__)

host = socket.gethostname()

story = {
    "INIT":{ "sentences" : ["You are standing in a small alley. Roman houses are rising around you.",
"You can see a balcony to one apartment where doors are open.","There are no one else to see here.","From the street you can hear the crowd of roman citizens, slaves, soldiers going on with their everyday life.","High above your head you can see dark and stormy clouds are gathering."],
"actions": [{"discription":"Wait and see","result":"You wait in silence", "tag":"WAIT"},{"discription":"Look at balcony", "result":"You look up to the balcony","tag":"BALCONY"},{"discription":"Look at end of alley", "result":"You walk slowly to the end of the alley", "tag":"ENDOF"}]
    },
    "WAIT": {"sentences":["You wait in silence concentrating on all the sounds surrounding you."],
        "actions":[{"discription":"Go back to main alley", "result":"You walk back to center of the alley","tag":"GOBACK"}]
    },
    "BALCONY": {"sentences":["The balcony is two storages up.","There are no one up there. A curtain flickers in the wind.","A grapevine is climbing its way along the wall."],
        "actions":[{"discription":"Go back to main alley", "result":"You walk back to center of the alley", "tag":"GOBACK"}]
    },
        "ENDOF": {"sentences":["You go deeper into the alley","The end of the alley is all in shadows","Some old boxes lean to a wall here."],
        "actions":[{"discription":"Go back to main alley", "result":"You walk back to center of the alley", "tag":"GOBACK"}]
    },
    "GOBACK":{"sentences" : ["You are back in the small alley. Roman houses are rising around you.",
"You can see a balcony to one apartment where doors are open.","There are no one else to see here."],
"actions": [{"discription":"Wait and see","result":"You wait in silence", "tag":"WAIT"},{"discription":"Look at balcony", "result":"You look up to the balcony", "tag":"BALCONY"},{"discription":"Look at end of alley", "result":"You walk slowly to the end of the alley", "tag":"ENDOF"}]
    }
}


sentences = ["You are standing in a small alley. Roman houses are rising around you.",
"You can see a balcony to one apartment where doors are open.","There are no one else to see here.","From the street you can hear the crowd of roman citizens, slaves, soldiers going on with their everyday life.","High above your head you can see dark and stormy clouds are gathering."]

actions = [{"discription":"Wait and see", "tag":0},{"discription":"Look at balcony", "tag":1},{"discription":"Look at end of alley", "tag":2}]

@app.route("/")
@app.route("/home")
def home():
    return render_template("front.htm")

@app.route('/load', methods=['POST','GET'])
def editorLoad():
    print("Received input")
    print(request.data)
    msgObj = json.loads(request.data)
    storypart = story[msgObj["response"]]
    ##filecontent=file.read() 
    return jsonify({"response":"storyline","content":storypart["sentences"],"actions":storypart["actions"]})

"""
@app.route('/load', methods=['POST','GET'])
def editorLoad():
    print("Received input")
    print(request.data)
    msgObj = json.loads(request.data)
    file = open(msgObj["request"], "r") 
    filecontent=file.read() 
    return jsonify({"response":msgObj["request"],"content":filecontent})

def createStructure(dirv):
    fileList = os.walk(dirv)
    root,dirs,files = next(fileList)
    subfiles = subFiles(root,files)
    return [{"name":dirv,"content":subStructure(root,dirs,files,fileList)+subfiles}]

def subStructure(root,dirs,files,fileList):
    output = []
    for dirName in dirs:
        root,dirs,files = next(fileList)
        subfiles = subFiles(root,files)
        #print(root)
        #for filename in files:
        #    print(filename)
        if len(dirs)>0:
            output.append({"name":dirName,"content":subStructure(root,dirs,files,fileList)+subfiles})
        else:
            output.append({"name":dirName,"content":subfiles})
    return output

def subFiles(root,files):
    output = []
    for filename in files:
        output.append({"name":root.replace("\\","/")+"/"+filename})
    return output  
             

@app.route('/list', methods=['POST','GET'])
def editorList():
    print("Received input")
    print(request.data)
    msgObj = json.loads(request.data)
    fileStructure = createStructure(msgObj["request"]) 
    #print(fileStructure)
    return jsonify({"response":fileStructure})

@app.route('/save', methods=['POST','GET'])
def editorSave():
    print("Received input")
    print(request.data)
    msgObj = json.loads(request.data)
    file = open(msgObj["request"], "w") 
    file.write(msgObj["content"]) 
    return jsonify({"response":"File was saved ok!"})

"""


if __name__ == '__main__':
    app.run(debug=True,port=5003)
    #app.run(host='0.0.0.0',debug=True,port=80)