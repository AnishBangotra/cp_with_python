from numpy import *
#-------------Variables----------------------
player='0'
game_is_running=True
marked=set()
stack=[]
pathcount=0
#definig maze and starting logic and implimentation
maze = array([ ["#","#","#","#","#","0","#","#"],
               ["#"," "," "," "," "," "," ","#"],
               ["#"," ","#"," ","#","#"," ","#"],
               ["#"," ","#"," ","#","#"," ","#"],
               ["#"," ","#"," "," "," "," ","#"],
               ["#"," ","#"," ","#"," ","#","#"],
               ["#"," "," "," ","#"," "," ","#"],
               ["#"," ","#","#","#","#"," ","#"],
               ["#"," "," "," "," "," "," ","#"],
               ["#","#","X","#","#","#","#","#"]
             ])

#----------functions---------------------
#in this function looking for adjacent positins for player
def neighbour(pos,maze):
    ns=[]
    y,x = pos
    max_X = len(maze[0])
    max_Y = len(maze)
    if x > 0:
        ns.append((y,x-1))
    if x < max_X-1:
        ns.append((y,x+1))
    if y > 0:
        ns.append((y-1,x))
    if y < max_Y:
        ns.append((y+1,x))
    return ns


#In this function we printing maze with path followed by player!!
def printmaze(maze,marked):
    for elements in marked:
        row1,col1=elements
        maze[row1][col1]='|'
    print(maze)
    return maze

#implimentation of logic for all n positions for player to get to x and count the path!!
for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == player and (row,col) not in marked:
            marked.add((row,col))
            pathcount=1
            stack=[(row,col)]
#checking for further neighbouring elements and checking for blank space and X excluding # and marked elements!!
            while stack:
                current= stack.pop()
                neibor=neighbour(current, maze)
                for n in neibor:
                    y, x = n
                    if maze[y][x]=='X' and maze[y][x]!='#' and maze[y][x]!=' ' and (y,x) not in marked:
                        marked.add((y,x))
                        pathcount+=1
                        break
                    elif maze[y][x] == ' ' and maze[y][x]!= '#' and (y,x) not in marked:
                        marked.add((y,x))
                        pathcount+=1
                        stack.append((y,x))

print(pathcount)
printmaze(maze, marked)


#This game follows the breadth first search algorithm similar to depth first search!!
#inputgivenlist
#loop running through all of the elements just like normal depth first search
#whenever it finds the 0 player initialises with that pos of 0
#create a neighbour function and apply to it at that position for its adjacent positions
#making conditions so that player will not look in those path positions which player passed already
#result would be printing through the shortest path of the player to reach the position






#qu=qu.queue()
#qu.put(' ')
#add=''
#while True:
#    for j in ['L','R'.'U','D']:
#        put=add+j
#        if valid(as):
#            qu.put(put)
