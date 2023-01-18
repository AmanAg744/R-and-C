# blind search  find all possible routes first
# 2 lists stacked and visited node set
# only gives the path may not be the shortest
from pyMaze import maze,agent,COLOR,textLabel
def DFS(m,start=None):
    if start == None:
        start = (m.rows,m.cols)
    frontier = [start]
    explore = [start]
    dfspath = dict()
    while len(frontier)>0:
        curr_cell=frontier.pop()
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
                    dfspath[child_cell]=curr_cell
    fwdpath = dict()
    cell = (1,1)
    while cell != start:
        fwdpath[dfspath[cell]]=cell
        cell = dfspath[cell]
    return fwdpath            
                
                       
if __name__ == '__main__':

    m=maze(50,50)             # can use rows and columns numbers for the maze
    m.CreateMaze(loopPercent=100)          # can set goal or pattern Horizontal and vertical or loops in the maze
    path = DFS(m)
    a = agent(m,footprints=True,filled=True,color='green')   #default agent on the start cell of the maze 
    m.tracePath({a:path})
    l = textLabel(m,'Lenght of the path',len(path)+ 1)    # generates a text label with the title given by the user

    m.run()

 # if multiple paths are there the chosen path is any random path to the goal not the shoretest one