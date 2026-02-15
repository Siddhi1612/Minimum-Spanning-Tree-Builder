#sys is the system library, to access the parsed parameter with json
import sys, graph_wrapper, json
#subprocess in order to maintain matplotlib on the main thread
if len(sys.argv) < 2:
    print("Error: no payload provided")
    sys.exit(1)

#brings the dictionary back from the json that got parsed into terminal
payload = json.loads(sys.argv[1])
graph_wrapper.graph(payload[0], payload[1])
