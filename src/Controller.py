import os
import Parser as par
import Graph as gr
import AStar as ast
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
        os.system("cls")
        self.__isRunning = True

    def solve(self):
        print("\nAvailable nodes:")
        for node in self.__graph.getNodeList():
            print(f"({node.getId()}) ", end="") 
        print()
        parser = par.Parser()

        isValid = False
        errMsg = ""
        print("\nSelect the starting Node:")
        while not isValid:
            print(errMsg, end="")
            try:
                parser.readCommand()
                startingNode = parser.getData()
                isFound = False
                for node in self.__graph.getNodeList():
                    if startingNode == str(node.getId()):
                        isFound = True
                if not isFound:
                    raise Exception
                isValid = True
            except:
                errMsg="Node does not exist\n"

        isValid = False
        errMsg = ""
        print("\nSelect the destination node:")
        while not isValid:
            print(errMsg, end="")
            try:
                parser.readCommand()
                destinationNode = parser.getData()
                isFound = False
                for node in self.__graph.getNodeList():
                    if destinationNode == str(node.getId()):
                        isFound = True
                if not isFound:
                    raise Exception
                isValid = True
            except:
                errMsg="Node does not exist\n"

        print("\nSolution:")
        if self.__algorithm == "1":
            uCs = ucs.UCS()
            uCs.search(self.__graph, 1, 6)

            print("Path: " + str(uCs.getSolution()["path"]))
            print("Distance: " + str(uCs.getSolution()["cost"]))

        elif self.__algorithm == "2":
            aStar = ast.AStar()
            aStar.findShortestPath(self.__graph, int(startingNode), int(destinationNode))

            print("Path: " + str(aStar.getSolution()["path"]))
            print("Distance: " + str(aStar.getSolution()["distance"]))

    def stop(self):
        self.__isRunning = False

    # === IO ====================================================================
    def readMap(self):
        isValid = False
        errMsg = ""
        parser = par.Parser()
        print("\nSelect a map file")
        while not isValid:
            print(errMsg, end="")

            try:
                parser.readCommand()
                self.__mapPath = parser.getData()
                self.__graph = gr.Graph()
                self.__graph.build(self.__mapPath)
                isValid = True
            except:
                errMsg = "File is invalid\n"
    
    def readAlgorithm(self):
        isValid = False
        errMsg = ""
        parser = par.Parser()
        print("\nSelect an algorithm")
        print("1. Uniform Cost Search (UCS)")
        print("2. A*")
        while not isValid:
            print(errMsg, end="")

            try:
                parser.readCommand()
                self.__algorithm = parser.getData()
                if self.__algorithm != "1" and self.__algorithm != "2":
                    raise Exception
                isValid = True
            except:
                errMsg = "Algorithm is unavailable\n"
    
    def menu(self):
        parser = par.Parser()
        print("\nTry again? (y/n)")
        parser.readCommand()
        if parser.getData() == "n" or parser.getData() == "N":
            self.stop()
        elif parser.getData() == "y" or parser.getData() == "Y":
            self.start()
            pass
    
    # === DISPLAY ===============================================================
    def displaySplash(self):
        print("\n      SHORTEST ROUTE FINDER     ")
        print("\n                by              ")
        print("\nKelvin Rayhan Alkarim (13521005)")
        print(" Ditra Rizqa Amadia (13521019) ")

