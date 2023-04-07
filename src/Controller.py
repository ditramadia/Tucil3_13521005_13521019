import Parser as par
import Graph as gr
import UCS as ucs

class Controller:
    # === CONSTRUCTOR ===========================================================
    def __init__(self):
        self.__isRunning = False
        self.__algorithm = None
        self.__mapPath = None
        self.__graph = None

    # === STATES ================================================================
    def isRunning(self):
        return self.__isRunning
    
    # === CONTROLS ==============================================================
    def start(self):
        self.__isRunning = True

    def stop(self):
        self.__isRunning = False

    # === IO ====================================================================
    def readMap(self):
        parser = par.Parser()
        print("Masukan file map")
        parser.readCommand()
        self.__mapPath = parser.getData()

        self.__graph = gr.Graph()
        self.__graph.build(self.__mapPath)
        
        self.__graph.printAdjMatrix()
        self.__graph.printNodeList()
        uCs = ucs.UCS()
        route, cost = uCs.search(self.__graph, 1, 6)
        print(route)
        print(cost)
        
    
    def readAlgorithm(self):
        parser = par.Parser()
        print("Pilih algoritma")
        print("1. Uniform Cost Search (UCS)")
        print("2. A*")
        parser.readCommand()
        self.__algorithm = parser.getData()
    
    def solve(self):
        parser = par.Parser()
        print("Pilih Starting Node:")
        parser.readCommand()
        startingNode = parser.getData()
        print("Pilih Destination Node:")
        parser.readCommand()
        destinationNode = parser.getData()

        if self.__algorithm == "2":
            aStar = ast.AStar()
            aStar.findShortestPath(self.__graph, int(startingNode), int(destinationNode))

            print("Solusi:")
            print("Path: " + str(aStar.getSolution()["path"]))
            print("Distance: " + str(aStar.getSolution()["distance"]))
