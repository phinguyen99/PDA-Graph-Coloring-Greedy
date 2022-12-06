from Lectures import Lectures
from Graph import Graph
if __name__ == '__main__':
    lectures =[]
    l1 = Lectures(0,"Theoretical informatics",[1,2,3])
    lectures.append(l1)
    l2 = Lectures(1,"ICT Security",[0,3,4])
    lectures.append(l2)
    l3 = Lectures(2,"Digital Signal Processing",[0,3,5,6])
    lectures.append(l3)
    l4 = Lectures(3,"Analog Technology",[0,1,2,4,5,6,8])
    lectures.append(l4)
    l5 = Lectures(4,"CISCO Academy",[1,3,6,7,8])
    lectures.append(l5)
    l6 = Lectures(5,"Communication technology",[2,3,6])
    lectures.append(l6)
    l7 = Lectures(6,"Modern Communication Technique",[2,3,4,5])
    lectures.append(l7)
    l8 = Lectures(7,"Signals and Systems Analysis",[4])
    lectures.append(l8)
    l9 = Lectures(8,"Speech Processing",[3,4])
    lectures.append(l9)
    ver = len(lectures)
    g = Graph(ver,[[] for i in range(ver)],lectures)

    for x in lectures:
        print("ID Subject: " + str(x.ID) + " 	Subject: " + x.Name)
        # Add the edges to the graph
        for y in x.Clashes:
            g.addEdge(x.ID, y)
    g.greedyColoring()
    