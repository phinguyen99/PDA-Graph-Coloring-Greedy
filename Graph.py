from termcolor import colored
# Class color in terminal Visual Studio Code
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Graph:

    # default constructor
    def __init__(self, ver, adjacent,lectures):
        self.ver = ver
        self.adjacent = [[] for i in range(ver)]
        self.lectures= lectures
    
    # Function for create an edge to graph, protection against double addition
    # An undirected graph is created
    def addEdge(self, v ,w):
        if (self.adjacent[v].count(w)<=0 and self.adjacent[w].count(v)<=0):
            self.adjacent[v].append(w)
            self.adjacent[w].append(v)
    # Assigning colors by greedy algorithm, 
	# starting from 0, thanks to our the vertex with the most edges
    def greedyColoring(self):
        red = 0 # result[0]
        blue =0
        green = 0
        yellow = 0
        un = 0
        
        # Initialize all the color of vertices is None -1
        result =[-1] * self.ver

        # Set the first color of vertex 0
        #result[0] = 0

        # available[] is the field where available colors are stored.
        # value: True means, that the color was assigned to the adjacent vertex.
        available = [False] * self.ver

        # Sort the vertices by the number of adjacent vertices 
        swapped =True
        while swapped:
            swapped = False
            for i in range(self.ver - 1):
                if (len(self.lectures[i].Clashes) < len(self.lectures[i+1].Clashes)):
                    swap_lecture = self.lectures[i]
                    self.lectures[i] = self.lectures[i+1]
                    self.lectures[i+1] = swap_lecture
                    swapped = True

        
        # Add colors to each vertex, vertex has more adjacents --> will be first
        for x in self.lectures:
            u = x.ID
            # Iterates through all neighboring vertices and marks them as available.
            for i in self.adjacent[u]:
                if (result[i] != -1):
                    available[result[i]] = True
            # Sorting conditions, distribution and number of individual colors
            # mark will show us what (the order of ) color (0,1,2,3,...) would match that vertex?
            mark = 0
            while mark <self.ver:
                if (available[mark] ==False):
                    break
                mark +=1
            if (mark ==0):
                red +=1
            elif (mark ==1):
                blue+=1
            elif (mark ==2):
                green+=1
            elif (mark ==3):
                yellow +=1
            else:
                un +=1

            # Add the color found to the vertex, in this work, we chose only 4 colors, but in field result[] for big input
            # it can display the max(result[]) + 1 --> maximun colors needed
            result[u] = mark
            for i in self.adjacent[u]:
                if (result[i] !=-1):
                    available[result[i]] = False
        # print the adjacent vertices of each vertex
        print(self.adjacent)

        # Print the result
        color = [colored("Red",'red'),colored("Blue",'blue'),colored("Green",'green'),colored("Yellow",'yellow'),"Uncertain"]
        timeslots = [[] for i in range(4)]
        for x in self.lectures:
            u = x.ID

            # Pozor: The ID subject, we marked from 0 to n-1 but the order of Lecture will be 1 to n
            print("Subject ID " + str(x.ID) + " --> Color: " +bcolors.BOLD+ color[result[u]])
            timeslots[result[u]].append("Lecture "+str(x.ID+1))

        for i in range (4):
             print("Timeslot " + str(i+1)+ " : "+str(timeslots[i]))