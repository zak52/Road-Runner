__author__= "Zach Kaufman"

import math
from matplotlib import pyplot as plt
import numpy as np

# Function that checks to makes sure a given node is in
# a given list of nodes
def inList(node, listNodes):
    if (listNodes != []):
        for items in listNodes:
            if node.nodeName == items.nodeName:
                return bool(True)
    return bool(False)



# maze runner class to create graph and run BFS
class mapGraph:

    # the maze image displayed in an array format
    mazeImage = []

    # this is the four corners that we get from clicking
    corners = []

    # this is the number of verticle nodes in the maze
    verticleNodes = 0

    # this is the number of horizontal nodes in the maze
    horizontalNodes = 0

    # the start node
    startNode = None

    # the end node that we need to find
    endNode = None

    # the clicks for the end and start node
    endStart = []

    # the addition to the y addition to get the next
    # y coordinate
    yAddition = 0

    # the addition to the y addition to get the next
    # x coordinate
    xAddition = 0

    # the graph that we get from the maze that we use at the start
    graph = []

    # the amount of nodes open at a given time
    openList = []

    # wiether you want to show every step of the solver
    verboseType = bool(True)

    # the currentnode the solver is on
    currentNode = None

    # all the nodes in the given graph
    allNodes = []

    # incrementer
    x = 0

    # incrementer
    y = 0

    # the list that a node is expanding
    nodeExpansion = []

    # the number of nodes that is searched
    numberofSearchNodes = 0

    # Simple search Node class
    # class is imbeded inside this class
    class searchNode:
        
        # creates a new search node with the nodename
        def __init__(self, nodeName, xLocation, yLocation):
            self.nodeName = nodeName
            self.xLocation = xLocation
            self.yLocation = yLocation
            self.nodeChildren = []
            self.depth= -1
            self.parentNode = []
            



    # the constructor class for the maze
    def __init__(self, imageFile):
        print("Solving: ", imageFile, " with Breadth First Search:")
        self.mazeImage = plt.imread(imageFile) # loads the image into python
        plt.imshow(self.mazeImage) # gets the array of pixels of the image
        self.corners = plt.ginput(4) # the amount of clicks we get from the image, corners
        self.endStart = plt.ginput(2) # the end and start node, not implemented
        self.verticleHorizontalNodes() 
        #self.startNode = self.endStart[0] if implement this
        #self.endNode = self.endStart[1]
        self.xAddition = (self.corners[0][0] + self.corners[1][0])/int(self.horizontalNodes)
        self.yAddition = (self.corners[0][1] + self.corners[2][1])/int(self.verticleNodes)
        self.convertToUsAble()
        self.BFS(self.graph[0], self.graph[len(self.graph)-1])
        self.printSearchStats()


    # gets the number of veritcle and horizontal squares from the user
    # to split up the graph into an equal amount of squares
    def verticleHorizontalNodes(self):
        print("Enter the number of verticle Nodes: ")
        self.verticleNodes = input()
        print("Enter the number of horizontal Nodes: ")
        self.horizontalNodes = input()

    # starts to convert the image into a useable graph
    # gets all the nodes from the maze and turns into a graph
    def convertToUsAble(self):
        self.x = 0
        self.y = 0
        while( self.y < int(self.verticleNodes)):
            while( self.x < int(self.horizontalNodes) ):
                # gets the nodes for the maze by adding the y and x additions to the corners
                nodeName = (chr(ord('A') + self.x)) + chr(ord('A') + self.y)
                self.graph.append(self.searchNode(nodeName, self.corners[0][0] + (self.xAddition * self.x)
                                  , self.corners[0][1] + (self.yAddition * self.y)))
                self.x =  self.x + 1
            self.y = self.y + 1
            self.x = 0


    # sees if the given location is inside of the graph
    def contains(self, xLocation, yLocation):
        index = 0
        for i in self.graph:
            if int(i.xLocation) == int(xLocation) and int(i.yLocation) == int(yLocation):
                return index
            index = index + 1
        return -1

    # data dump of all the nodes in the graph
    def printNodes(self):
        i = 0
        while( i < len(self.graph)):
            print (self.graph[i].nodeName, ", ", self.graph[i].xLocation, ", ", self.graph[i].yLocation)
            i = i + 1


     # gets the children of the given parent node       
    def adjacentNodes(self, parentNode):
        addNode = None
        upIndex = self.contains(parentNode.xLocation, parentNode.yLocation - self.yAddition) # if a node is uptop
        downIndex = self.contains(parentNode.xLocation, parentNode.yLocation + self.yAddition) # if a node is below
        leftIndex = self.contains(parentNode.xLocation - self.xAddition, parentNode.yLocation) # if a node is left
        rightIndex = self.contains(parentNode.xLocation + self.xAddition, parentNode.yLocation) # if a node is right
        indexes = [upIndex, downIndex, leftIndex, rightIndex]
        index = 0
        while index < 4:
            if indexes[index] != -1: # checks to see if the node is actually in the maze
                # creates a crop between the given node and potential children
                img_crop = self.mazeImage[int(parentNode.xLocation):int(self.graph[indexes[index]].xLocation),
                                  int(parentNode.yLocation):int(self.graph[indexes[index]].yLocation), : ]
                # checks to see if all the pixels are white between the two points
                isWhite = np.sum(img_crop)
                if (isWhite == 0): 
                    if not inList(self.graph[indexes[index]], parentNode.parentNode):
                        self.graph[indexes[index]].depth = parentNode.depth + 1
                        self.graph[indexes[index]].parentNode.append(parentNode)
                        parentNode.nodeChildren.append(self.graph[indexes[index]])             
            index = index + 1
        

    # checks to see if 2 nodes are equal to eachother
    def equalTo(self, node1, node2):
        if (node1.nodeName == node2.nodeName):
            return True
        else:
            return False


    # The same BFS algorithm that we used on the second project
    # nothing super special here
    def BFS(self, startNode, endNode):
        self.startNode = startNode
        self.startNode.depth = 0
        self.endNode = endNode
        self.openList.append(self.startNode)
        self.currentNode = self.startNode
        if self.verboseType:
                self.displayOpenList()
        while not self.equalTo(self.currentNode, self.endNode):
            if self.verboseType:
                print("\nExploring Node: ", self.currentNode.nodeName)

            if self.currentNode.nodeName not in self.nodeExpansion:
                self.nodeExpansion.append(self.currentNode)
                self.numberofSearchNodes = self.numberofSearchNodes + 1

            self.adjacentNodes(self.currentNode)
            self.insertToOpen(self.currentNode.nodeChildren, self.currentNode)
            self.currentNode = self.openList[0]
            


    # my insert to open function that inserts new children to the open list
    # this is the same algorithm as before where it adds to the end of list
    def insertToOpen(self, addToList, parentNode):
        if self.verboseType and parentNode != '':
            print ("Inserting New Children:", end = " ")
            index = 0
            for children in parentNode.nodeChildren:
                if not inList(children, self.nodeExpansion):
                    print(children.nodeName, end = ", ")
                    index = index + 1
        if inList(parentNode, self.openList):
            self.openList.remove(parentNode)

        index = 0
        if parentNode != '':
            for children in parentNode.nodeChildren:
                if not inList(children, self.nodeExpansion):
                    index = index + 1

        for child in addToList:
            if not inList(child, self.openList) and not inList(child, self.nodeExpansion):
                self.openList.append(child)
        if self.verboseType:
            self.displayOpenList()

    # displays the open list for the verbose mode only
    def displayOpenList(self):
        print("")
        index = 0
        while index < len(self.openList):
            print("( ", self.openList[index].nodeName, ", ", self.openList[index].depth, end = "),")
            index = index + 1

    # prints the final stats of the maze and algorithm
    def printSearchStats(self):
        print("\n\n-----------------------------------------------")
        print("Search Summary Stats:")
        print("Start Node: ", self.startNode.nodeName)
        print("End Node: ", self.endNode.nodeName)
        print("search total of ", self.numberofSearchNodes,
                " out of total of ", int(self.verticleNodes)*int(self.horizontalNodes))
        print("Ended at Node: ", self.currentNode.nodeName)
        print("Node Expansion:", end = "[")
        for nodes in self.nodeExpansion:
            print(nodes.nodeName, end = ",")
        print("]")

        
