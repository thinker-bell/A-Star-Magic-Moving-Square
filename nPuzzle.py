#!/usr/bin/env python3
import time
from datetime import timedelta

class Node:

    #----- Initalize node with pattern gfunction the blanklocation and the move used to reach that state -----#
    def __init__(self,pattern,gfunc,move='start'):
        self.pattern = pattern
        self.gfunc = gfunc
        self.move = move
        #self.expandedStates = expandedStates 
        for (row,i) in zip(pattern,range(len(pattern))):
            if 0 in row:
                #print("reach ?")
                self.blankloc=[i,row.index(0)]
                # print(self.blankloc[0],self.blankloc[1])

    #----- equal magic function to check if states are equal or node element by element-----#
    def __eq__(self,other):
        if other==None:
            return False

        if isinstance(other,Node)!=True:
            raise TypeError

        for i in range(len(self.pattern)):
            for j in range(len(self.pattern)):
                if self.pattern[i][j]!=other.pattern[i][j]:
                    return False
        return True

    #----- magic function to retrive an element from the node like an array -----#
    def __getitem__(self,key):
        if isinstance(key,tuple)!=True:
            raise TypeError
        if len(key)!=2:
            raise KeyError

        return self.pattern[key[0]][key[1]]

    #----- function to calculate hfunction -----#
    #----- calculation for heuristics one -----# 

    def calc_h123func(self):
        self.hfunc = 0
        hval = 0
        n = len(self.pattern)
        total = (n*((n**2)+1))/2

        for i in range(len(self.pattern)):
            for j in range(len(self.pattern)):
                if self.pattern[i][j] == 0:
                    self.pattern[i][j] = (len(self.pattern))**2
        
        for row in (self.pattern):
            if (sum(row)) != total:
                hval += 1
        
        if (n==3):
            sum1 = sum2 = sum3 = 0

            sum1 = self.pattern[0][0] +  self.pattern[1][0] +  self.pattern[2][0]
            sum2 = self.pattern[0][1] +  self.pattern[1][1] +  self.pattern[2][1]
            sum3 = self.pattern[0][2] +  self.pattern[1][2] +  self.pattern[2][2]


            if(sum1 != total):
                hval+=1 
            if(sum2 != total):
                hval+=1 
            if(sum3 != total):
                hval+=1 
            
            sum1 = sum2 = 0

            sum1 = self.pattern[0][0] +  self.pattern[1][1] +  self.pattern[2][2]
            sum2 = self.pattern[2][0] +  self.pattern[1][1] +  self.pattern[0][2]

            if(sum1 != total):
                hval+=1 
            if(sum2 != total):
                hval+=1 

        elif (n==4):
            sum1 = sum2 = sum3 = sum4 = 0

            sum1 = self.pattern[0][0] +  self.pattern[1][0] +  self.pattern[2][0] + self.pattern[3][0]
            sum2 = self.pattern[0][1] +  self.pattern[1][1] +  self.pattern[2][1] + self.pattern[3][1]
            sum3 = self.pattern[0][2] +  self.pattern[1][2] +  self.pattern[2][2] + self.pattern[3][2]
            sum4 = self.pattern[0][3] +  self.pattern[1][3] +  self.pattern[2][3] + self.pattern[3][3]

            if(sum1 != total):
                hval+=1 
            if(sum2 != total):
                hval+=1 
            if(sum3 != total):
                hval+=1 
            if(sum4 != total):
                hval+=1 
            
            sum1 = sum2 = 0

            sum1 = self.pattern[0][0] +  self.pattern[1][1] +  self.pattern[2][2] +  self.pattern[3][3]
            sum2 = self.pattern[0][3] +  self.pattern[1][2] +  self.pattern[2][1] +  self.pattern[3][0]
            
            if(sum1 != total):
                hval+=1 
            if(sum2 != total):
                hval+=1 

        for i in range(len(self.pattern)):
            for j in range(len(self.pattern)):
                if self.pattern[i][j] == (len(self.pattern)**2):
                    self.pattern[i][j] = 0
                    #self.hfunc+=1

                    
        #visitedNodes = visitedNodes += 1 

        self.hfunc = hval
        
        self.ffunc=self.hfunc+self.gfunc

        return self.hfunc,self.gfunc,self.ffunc
    
    
    #----- calculation for heuristics two -----#
    def calc_hfunc(self):
        self.hfunc = 0
        hval = 0
        n = len(self.pattern)
        total = (n*((n**2)+1))/2

        for i in range(n):
            for j in range(n):
                if self.pattern[i][j] == 0:
                    self.pattern[i][j] = (n)**2

        if (n ==4):

            sum1 = self.pattern[0][0] +  self.pattern[0][1] +  self.pattern[0][2] + self.pattern[0][3]
            sum2 = self.pattern[1][0] +  self.pattern[1][1] +  self.pattern[1][2] + self.pattern[1][3]
            sum3 = self.pattern[2][0] +  self.pattern[2][1] +  self.pattern[2][2] + self.pattern[2][3]
            sum4 = self.pattern[3][0] +  self.pattern[3][1] +  self.pattern[3][2] + self.pattern[3][3]

            sum1 = total - sum1 
            sum2 = total - sum2 
            sum3 = total - sum3 
            sum4 = total - sum4 
            
            if(sum1 < 0):
                sum1 = abs(sum1)
            hval = hval + sum1
            if(sum2 < 0):
                sum2 = abs(sum2)
            hval = hval + sum2
            if(sum3 < 0):
                sum3 = abs(sum3)
            hval = hval + sum3
            if(sum4 < 0):
                sum4 = abs(sum4)
            hval = hval + sum4 
            
            sum1 = sum2 = sum3 = sum4 = 0

            sum1 = self.pattern[0][0] +  self.pattern[1][0] +  self.pattern[2][0] + self.pattern[3][0]
            sum2 = self.pattern[0][1] +  self.pattern[1][1] +  self.pattern[2][1] + self.pattern[3][1]
            sum3 = self.pattern[0][2] +  self.pattern[1][2] +  self.pattern[2][2] + self.pattern[3][2]
            sum4 = self.pattern[0][3] +  self.pattern[1][3] +  self.pattern[2][3] + self.pattern[3][3]

            sum1 = total - sum1 
            sum2 = total - sum2 
            sum3 = total - sum3 
            sum4 = total - sum4 
            
            if(sum1 < 0):
                sum1 = abs(sum1)
            hval = hval + sum1
            if(sum2 < 0):
                sum2 = abs(sum2)
            hval = hval + sum2
            if(sum3 < 0):
                sum3 = abs(sum3)
            hval = hval + sum3
            if(sum4 < 0):
                sum4 = abs(sum4)
            hval = hval + sum4 
            
            
            sum1 = sum2 = 0

            sum1 = self.pattern[0][0] +  self.pattern[1][1] +  self.pattern[2][2] +  self.pattern[3][3]
            sum2 = self.pattern[0][3] +  self.pattern[1][2] +  self.pattern[2][1] +  self.pattern[3][0]
            
            sum1 = total - sum1 
            sum2 = total - sum2 
            
            if(sum1 < 0):
                sum1 = abs(sum1)
            hval = hval + sum1
            if(sum2 < 0):
                sum2 = abs(sum2)
            hval = hval + sum2	

        elif (n==3):
            sum1 = self.pattern[0][0] +  self.pattern[0][1] +  self.pattern[0][2]
            sum2 = self.pattern[1][0] +  self.pattern[1][1] +  self.pattern[1][2]
            sum3 = self.pattern[2][0] +  self.pattern[2][1] +  self.pattern[2][2]
            
            sum1 = total - sum1 
            sum2 = total - sum2 
            sum3 = total - sum3

            if(sum1 < 0):
                sum1 = abs(sum1)
            hval = hval + (sum1)
            if(sum2 < 0):
                sum2 = abs(sum2)
            hval = hval + (sum2)
            if(sum3 < 0):
                sum3 = abs(sum3)
            hval = hval + (sum3)
            
            sum1 = sum2 = sum3 = 0

            sum1 = self.pattern[0][0] +  self.pattern[1][0] +  self.pattern[2][0]
            sum2 = self.pattern[0][1] +  self.pattern[1][1] +  self.pattern[2][1]
            sum3 = self.pattern[0][2] +  self.pattern[1][2] +  self.pattern[2][2]
            
            sum1 = total - sum1 
            sum2 = total - sum2 
            sum3 = total - sum3 

            if(sum1 < 0):
                sum1 = abs(sum1)
            hval = hval + (sum1)
            if(sum2 < 0):
                sum2 = abs(sum2)
            hval = hval + (sum2)
            if(sum3 < 0):
                sum3 = abs(sum3)
            hval = hval + (sum3) 
            
            sum1 = sum2 = 0

            sum1 = self.pattern[0][0] +  self.pattern[1][1] +  self.pattern[2][2]
            sum2 = self.pattern[2][0] +  self.pattern[1][1] +  self.pattern[0][2]

            sum1 = total - sum1 
            sum2 = total - sum2

            if(sum1 < 0):
                sum1 = abs(sum1)
            hval = hval + (sum1)
            if(sum2 < 0):
                sum2 = abs(sum2)
            hval = hval + (sum2)

        for i in range(n):
            for j in range(n):
                if self.pattern[i][j] == (n**2):
                    self.pattern[i][j] = 0
                    #self.hfunc+=1

        #print("Heuristic: ", hval)
        #if (self.gfunc > 10):
        #    exit()

        self.hfunc = int(hval)

        self.ffunc=self.hfunc+self.gfunc

        return self.hfunc,self.gfunc,self.ffunc
    

    #----- Fucntion to move the blank tile left if possible -----#
    def moveleft(self):
        
        if self.blankloc[0]==0:
            return None
       
        left = [[self.pattern[i][j] for j in range(len(self.pattern))]for i in range(len(self.pattern))]
        
        #print(left)

        for r in range(len(self.pattern)):
            for c in range(len(self.pattern)):
                if left[r][c] == 0:
                    row = r
                    clm = c
                    break 
              
        left[row][clm] = left[row][clm-1]
        left[row][clm-1] = 0


        if self.hfunc != 0:
            game.heuristicCalculations = game.heuristicCalculations + 1

        return Node(left,self.gfunc+1,'left')

    #----- Fucntion to move the blank tile right if possible -----#
    def moveright(self):
        #print("blank location: ", self.blankloc[0])
        #print(self.pattern)
        if self.blankloc[1]==(len(self.pattern)-1):
            return None

        right = [[self.pattern[i][j] for j in range(len(self.pattern))]for i in range(len(self.pattern))]
        #print(right)
        for r in range(len(self.pattern)):
            for c in range(len(self.pattern)):
                if right[r][c] == 0:
                    row = r
                    clm = c
                    break 
        if (clm != 3):
            right[row][clm] = right[row][clm+1]
            right[row][clm+1] = 0

        if self.hfunc != 0:
            game.heuristicCalculations = game.heuristicCalculations + 1

        return Node(right,self.gfunc+1,'right')

    #----- Fucntion to move the blank tile up if possible -----#
    def moveup(self):
        if self.blankloc[0]==0:
            return None

        up = [[self.pattern[i][j] for j in range(len(self.pattern))]for i in range(len(self.pattern))]
        
        for r in range(len(self.pattern)):
            for c in range(len(self.pattern)):
                if up[r][c] == 0:
                    row = r
                    clm = c
                    break 

        up[row][clm] = up[row-1][clm]
        up[row-1][clm] = 0
        
        if self.hfunc != 0:
            game.heuristicCalculations = game.heuristicCalculations + 1

        return Node(up,self.gfunc+1,'up')

    #----- Fucntion to move the blank tile down if possible -----#
    def movedown(self):
        if self.blankloc[0]==(len(self.pattern) -1):
            return None

        down = [[self.pattern[i][j] for j in range(len(self.pattern))]for i in range(len(self.pattern))]
        
        for r in range(len(self.pattern)):
            for c in range(len(self.pattern)):
                if down[r][c] == 0:
                    row = r
                    clm = c
                    break 
        if (row != 3):
            down[row][clm] = down[row+1][clm]
            down[row+1][clm] = 0

        if self.hfunc != 0:
            game.heuristicCalculations = game.heuristicCalculations + 1

        return Node(down,self.gfunc+1,'down')

    #----- Fucntion to check and perform all the moves according to possiblity and weather the next move is closed or not -----#
    #----- Close this node and all the new nodes to open list -----#
    def moveall(self,game):
        left = self.moveleft()
        left = None if game.isclosed(left) else left
        right = self.moveright()
        right = None if game.isclosed(right) else right
        up = self.moveup()
        up = None if game.isclosed(up) else up
        down = self.movedown()
        down = None if game.isclosed(down) else down

        game.closeNode(self)
        game.openNode(left)
        game.openNode(right)
        game.openNode(up)
        game.openNode(down)
        #game.expandedStates = game.expandedStates + 1

        return left,right,up,down

    #----- Fucntion to print the array in beautifed format -----#

    def print(self):
        n = len(self.pattern)
        print("\nThe A* value is: \n")
        print("f(n) = g(n) + h(n)\n{} = {} + {}\n".format(str(self.ffunc),str(self.gfunc),str(self.hfunc)))
        
        for i in range(n):
            for j in range(n):
                if self.pattern[i][j] == 0:
                    self.pattern[i][j] = (n**2)
                    break
        
        print(self.move+str(self.gfunc))
        for i in range(len(self.pattern)):
            print(self.pattern[i])

        for i in range(n):
            for j in range(n):
                if self.pattern[i][j] == (n**2):
                    self.pattern[i][j] = 0
                    break 
        

class Game:

    #---- Initilaize Node with start, a hashtable of open nodes, a hashtable of closed Node and add the start to the open node ----#
    #---- Open nodes is a hash table based on 'f function' and Closed nodes is a hash table based on 'h function' ----#
       
    def __init__(self,start,expandedStates,heuristicCalculations):
        self.expandedStates = expandedStates
        self.heuristicCalculations = heuristicCalculations
        self.start = start
        self.open = {}
        self.closed = {}
        _,_,ffunc = self.start.calc_hfunc()
        self.open[ffunc] = [start]

    #---- Fucntion to check weather a node is in closed node or not ----#
    def isclosed(self,node):
        if node==None:			#return True if no node
            return True

        #calculate hfucntion to check in that list of the hash table
        hfunc,_,_ = node.calc_hfunc()

        if hfunc in self.closed:
            for x in self.closed[hfunc]:
                if x==node:
                    return True

        return False

    #---- Function to add a node to the closed list and remove it from the open nodes list ----#
    def closeNode(self,node):
        if node==None:		#return back if no node
            return

        hfunc,_,ffunc= node.calc_hfunc()
        self.open[ffunc].remove(node)	#remove from the list of the ffunction of the hash table for open nodes
        if len(self.open[ffunc])==0:
            del self.open[ffunc]		#remove the attribute for a ffunction if its list is empty

        if hfunc in self.closed:
            self.closed[hfunc].append(node)
        else:
            self.closed[hfunc] = [node]

        return

    #---- Function to add a node to the open list after its initilaized ----#
    def openNode(self,node):
        if node==None:
            return

        #Calculate ffucntion to add the node to the list of that ffucntion in hash table
        _,_,ffunc = node.calc_hfunc()
        if ffunc in self.open:
            self.open[ffunc].append(node)
        else:
            self.open[ffunc] = [node]

        return

    #---- Function to solve the game using A star algorithm ----#
    def solve(self):

        solved = False 
        presentNode = None
        
        while(solved != True):
            i=0
            while i not in self.open:
                i+=1							#Check for the list with least 'ffunction' to pick a node from that list
            presentNode = self.open[i][-1]		
            presentNode.moveall(self)			#Expand that node for next possible moves
            self.expandedStates = self.expandedStates + 1
            


            if (self.expandedStates >= 50000):
                print("No solution in 50000 iterarions")
                exit()
            

            if (presentNode.hfunc == 0 ):
                solved = True
                print("\n---------------PERFORMANCE---------------\n")
                print("Square size: {} x {}".format(str(len(presentNode.pattern)),str(len(presentNode.pattern))))
                print("The total amount of visited Nodes: ", self.expandedStates)
                print("The total number of heuristic calculations: ", self.heuristicCalculations)
                print("Final number of moves made: ", presentNode.ffunc)
                print("\n-----------------------------------------")
                presentNode.print()

    #---- Print the solution in reverse direction i.e. from goal to start----#
        '''
        while presentNode.move!='start':
            if (presentNode.gfunc <= 5):
                presentNode.print()
            #presentNode.print()
            # do reverse move that what was done to reach the state to backtrack along the solution
            if presentNode.move == 'up':
                presentNode = presentNode.movedown()
            elif presentNode.move == 'down':
                presentNode = presentNode.moveup()
            elif presentNode.move == 'right':
                presentNode = presentNode.moveleft()
            elif presentNode.move == 'left':
                presentNode = presentNode.moveright()

            hfunc,_,_ = presentNode.calc_hfunc()
            for i in self.closed[hfunc]:
                if i==presentNode:
                    presentNode = i

        return
        '''

if __name__ == '__main__':  
    start_time = time.monotonic()
    
    #----- Read the square in from a Text File -----#

    file = open("3x3_TestSq2.txt", "r")
    contents = file.read()
    matrix = contents.split("\n")
    file.close()
    #print(matrix)


    for i in range(len(matrix)):
        matrix[i] = int(matrix[i])
        if matrix[i] == len(matrix):
            matrix[i] = 0

    #print(matrix)
    if len(matrix) == 9:
        startloc = [matrix[0:3],matrix[3:6],matrix[6:]]
    elif len(matrix) == 16:
        #print("Here")
        startloc = [matrix[0:4],matrix[4:8],matrix[8:12],matrix[12:]]
    #print(startloc)
    #----- Initalize start node -----#

    start = Node(startloc,0)

    #----- Initilaize Game -----#

    game = Game(start,0,0)

    game.solve() #Solve Game

    #----- Print the starting square -----#

    print("\n\nThis is the starting square: \n")
    
    for i in range(len(start.pattern)):
            for j in range(len(start.pattern)):
                if start.pattern[i][j] == 0:
                    start.pattern[i][j] = ((len(start.pattern))**2)
                    break

    for i in range(len(start.pattern)):
        print(start.pattern[i])
    print("")

    end_time = time.monotonic()
    print("Execution time: ",timedelta(seconds= end_time-start_time))

