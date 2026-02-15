import webview
#json is imported as it's a string representation of a dictionary
import json
import subprocess, sys

mainInput = {}


class API:
    #following methods are all for moving into the new pages
    def loadinputs(self):
        print("Loading inputs page...")
        self.window.evaluate_js('window.location.href = "inputs.html"')
    
    def submitInput(self, data):
        global mainInput
        mainInput = data
        print(f"Received: {data}")
        #this statement branches to different pages based on the selected algorithm
        if mainInput["userAlgorithm"] == "prim":
            self.window.evaluate_js('window.location.href = "primtype.html"')
            return 
        mainInput["primType"] = ""
        self.window.evaluate_js('window.location.href = "computeEdges.html"')
    #method for the primType
    def submitPrimType(self, data):
        global mainInput
        mainInput["primType"] = data
        self.window.evaluate_js('window.location.href = "computeEdges.html"')
    

    def getdata(self):
        #can aonly parse thorugh a string, so 
        return json.dumps(mainInput)
    
    def runalg(self,data):
        payload = [mainInput, data]
        #helps to start the drawing of the graph by running plotter.py
        #also does so by passing the parameters: payload
        subprocess.Popen(
            #meant to parse the data as a string to send over Popen
            [sys.executable, "plotter.py", json.dumps(payload)],
            stdout=sys.stdout,
            stderr=sys.stderr,
            text=True
        )

api = API()
#this is the main program to move to a different page
window = webview.create_window('MST Tool', 'graphical_UI/start.html', js_api=api)
api.window = window
webview.start()
