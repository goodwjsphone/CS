#big d's shortest path
import json
#assighn map to maze
file = open("maze.JSON","r")

speed = 1

maze = json.load(file)


file.close()



#loop though maze and find shortest path.
def short(maze):
    D = []
    for y in range (len(maze)):
        for x in range (len(maze)):

            if 0 < y:    
                top = [x,y-1]
            else:
                top = []
            if 0 < x:
                left = [x-1,y]
            else:
                left = []
            if 50 > x:
                right = [x+1,y]
            else:
                right = []
            if 50 > y:
                bottom = [x, y+1]
            else: bottom = []
            
            maze[x][y] = [top, bottom, left, right]
            D = maze            
    return(D)

#main prog
#maze[][]
D = short(maze)
savefile = input("file to save ")
ajlist = open(savefile,"w+")
json.dump(D,ajlist)
ajlist.close()


print(D)
