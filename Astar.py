# reason to use over bfs is its more efficient 
# searches minimum spaces to find the optimal path
# informed search algorithm
# priority queue - item with the most priority comes out first
from pyMaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
import math

def h(cell1,cell2):
    x1,y1 = cell1
    x2,y2 = cell2
    return abs(x1-x2)+abs(y1-y2)

def aStar(m):
    start = (m.rows,m.cols)
    g_score = {cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score = {cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))
    aPath = dict()
    open = PriorityQueue()
    open.put(h(start,(1,1)),h(start,(1,1)),start)
 
    while not open.empty():
        curr_cell = open.get([2])
        if curr_cell == (1,1):
            break
        for d in 'NSEW':
            if m.maze_map[curr_cell][d]==True:
                if d == 'E':
                    child_cell = (curr_cell[0],curr_cell[1]+1)
                elif d == 'W':
                    child_cell = (curr_cell[0],curr_cell[1]-1)
                elif d == 'N':
                    child_cell = (curr_cell[0]-1,curr_cell[1])
                elif d == 'S':
                    child_cell = (curr_cell[0]+1,curr_cell[1])
                temp_g_score = g_score[curr_cell]+1
                temp_f_score = temp_g_score + h(child_cell,(1,1))

                if temp_f_score<f_score(child_cell):
                    g_score[child_cell] = temp_g_score
                    f_score[child_cell] = temp_f_score
                    open.put(f_score[child_cell],h(child_cell,(1,1)),child_cell)
                    aPath[child_cell] = curr_cell
    fwdpath = dict()
    cell = (1,1)
    while cell != start:
        fwdpath[aPath[cell]]=cell
        cell = aPath[cell]
    return fwdpath
                







if __name__ == '__main__':

    m=maze(5,5)             # can use rows and columns numbers for the maze
    m.CreateMaze()          # can set goal or pattern Horizontal and vertical or loops in the maze
    
    path = aStar(m)
    a=agent(m,footprints=True) 
    m.tracePath({a:path})    

    m.run()
