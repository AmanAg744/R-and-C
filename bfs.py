# blind search \ find all possible routes first
# 2 lists queue and visited node set
# definately gives the shortest path
from pyMaze import maze,agent,COLOR,textLabel
def BFS(m,start=None):
    if start == None:
        start = (m.rows,m.cols)
    frontier = [start]
    explore = [start]
    bfspath = dict()
    while len(frontier)>0:
        curr_cell=frontier.pop(0)
        if curr_cell == (1,1):
            break
        for d in 'NSEW':
            if m.maze_map[curr_cell][d] == True:
                if d == 'E':
                    child_cell = (curr_cell[0],curr_cell[1]+1)
                elif d == 'W':
                    child_cell = (curr_cell[0],curr_cell[1]-1)
                elif d == 'N':
                    child_cell = (curr_cell[0]-1,curr_cell[1])
                elif d == 'S':
                    child_cell = (curr_cell[0]+1,curr_cell[1])
                if child_cell in explore:
                    continue
                else:
                    frontier.append(child_cell)
                    explore.append(child_cell)
                    bfspath[child_cell]=curr_cell
    fwdpath = dict()
    cell = (1,1)
    while cell != start:
        fwdpath[bfspath[cell]]=cell
        cell = bfspath[cell]
    return fwdpath            
                
                       
if __name__ == '__main__':

    m=maze(7,7)             # can use rows and columns numbers for the maze
    m.CreateMaze(loopPercent=40)          # can set goal or pattern Horizontal and vertical or loops in the maze
    path = BFS(m)
    a = agent(m,footprints=True,filled=True,color='green')   #default agent on the start cell of the maze 
    m.tracePath({a:path})
    l = textLabel(m,'Lenght of the shortest path',len(path)+1)    # generates a text label with the title given by the user
    m.run()

 # if multiple paths are there the chosen path is the shortest path to the goal