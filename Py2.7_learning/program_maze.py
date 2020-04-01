import sys

def print_maze(maze,x,y):
    for i in range(len(maze)):
        s = ''
        for j in range(len(maze)):
            if i == x and j == y:
                s += 'X'
            elif maze[i][j] == 1:
                s += '1'
            else:
                s += '.'
        print s
    print ' '


class My_run(object):

    def __init__(self,my_task):
        self.my_task = my_task

    def front_x(self,pos_x):
        if self.orientation%4==1:
            return pos_x+1
        elif self.orientation%4==3:
            return pos_x-1
        else:
            return pos_x

    def front_y(self,pos_y):
        if self.orientation%4==0:
            return pos_y-1
        elif self.orientation%4==2:
            return pos_y+1
        else:
            return pos_y

    def face_check(self):
        if self.my_task.go():
            self.black_box[self.front_y(self.box_y)][self.front_x(self.box_x)]=0 
            self.front_go()            
            if self.box_y == 0:
                temp =[[]]
                for i in range(len(self.black_box[1])):
                    temp[0].append(5)
                self.black_box = temp + self.black_box
                self.box_y+=1
            elif self.box_x == len(self.black_box[0])-1:
                for i in range(len(self.black_box)):
                    self.black_box[i].append(5)
            elif self.box_y == len(self.black_box)-1:
                temp =[[]]
                for i in range(len(self.black_box[1])):
                    temp[0].append(5)
                self.black_box = self.black_box + temp
            elif self.box_x == 0:
                temp = [5]
                for i in range(len(self.black_box)):
                    self.black_box[i] = temp + self.black_box[i]
                self.box_x+=1
        else:
            self.black_box[self.front_y(self.box_y)][self.front_x(self.box_x)]=1

    def right(self):
        if self.orientation%4==0:
            return self.black_box[self.box_y][self.box_x+1]
        elif self.orientation%4==1:
            return self.black_box[self.box_y+1][self.box_x]
        elif self.orientation%4==2:
            return self.black_box[self.box_y][self.box_x-1]
        else:
            return self.black_box[self.box_y-1][self.box_x]

    def left(self):
        self.orientation += 2
        temp = self.right()
        self.orientation = self.orientation - 2
        return temp

    def front(self):
        if self.orientation%4==0:
            return self.black_box[self.box_y-1][self.box_x]
        elif self.orientation%4==1:
            return self.black_box[self.box_y][self.box_x+1]
        elif self.orientation%4==2:
            return self.black_box[self.box_y+1][self.box_x]
        else:
            return self.black_box[self.box_y][self.box_x-1]

    def front_go(self):
        if self.orientation%4==0:
            self.box_y = self.box_y-1
        elif self.orientation%4==1:
            self.box_x = self.box_x+1
        elif self.orientation%4==2:
            self.box_y = self.box_y+1
        else:
            self.box_x = self.box_x-1

    def back(self):
        self.orientation += 2
        temp = self.front()
        self.orientation = self.orientation - 2
        return temp

    def maze_cont(self,my_task):
        self.black_box = [[5,5,5],[5,0,5],[5,5,5]]
        self.box_y = 1
        self.box_x = 1
        self.orientation = 0

        count = 0

        while not self.my_task.found() and count <10000:
            count+=1
            self.orientation = self.orientation%4
            if (self.right() + self.front() + self.left()+ self.back() == 3 \
                    or self.right() + self.front() + self.left()+ self.back() == 8)\
                    and self.black_box[self.box_y][self.box_x]!=1:
                    temp = 0
                    if self.right() == 0 or self.right() == 5:
                        temp = 1
                    elif self.front() ==0 or self.front() ==5:
                        temp = 0
                    elif self.left()==0 or self.left()==5:
                        temp = 3
                    elif self.back()==0 or self.back()==5:
                        temp = 2
                    for i in range(temp):
                        self.my_task.turn_right()
                        self.orientation +=1
                    self.black_box[self.box_y][self.box_x] = 1
            if self.front() ==5:
                self.face_check()
            elif self.right() ==5:
                self.my_task.turn_right()
                self.orientation +=1
                self.face_check()
            elif self.back() ==5:
                self.my_task.turn_right()
                self.my_task.turn_right()
                self.orientation+=2
                self.face_check()
            elif self.left() ==5:
                self.my_task.turn_left()
                self.orientation+=3
                self.face_check()

            if self.front() == 0:
                if self.left() == 0:
                    self.my_task.turn_left()
                    self.orientation+=3
                    self.my_task.go()
                    self.front_go()
                else:
                    self.my_task.go()
                    self.front_go()
                
                if self.left() ==0:
                    self.my_task.turn_left()
                    self.orientation+=3
                    self.my_task.go()
                    self.front_go()

            else:
                self.my_task.turn_right()
                self.orientation+=1 

def maze_controller(mr):
    my_var = My_run(mr)
    my_var.maze_cont(mr)
    

class MazeRunner(object):
    
    def __init__(self, maze, start, finish):
        self.__maze = maze
        self.__rotation = (1,0)
        self.__x = start[0]
        self.__y = start[1]
        self.__finish = finish

    def go(self):
        x = self.__x + self.__rotation[0]
        y = self.__y + self.__rotation[1]
        if x > len(self.__maze)-1 \
            or y > len(self.__maze)-1 \
            or x < 0 or y < 0 \
            or self.__maze[x][y] == 1:
            return False
        self.__x = x
        self.__y = y
        #print_maze(self.__maze, self.__x, self.__y)
        return True
    
    def turn_left(self):
        left_rotation = {
            (0,1): (1,0),
            (1,0): (0,-1),
            (0,-1): (-1,0),
            (-1,0): (0,1),
        }
        self.__rotation = left_rotation[self.__rotation]
        return self
    
    def turn_right(self):
        right_rotation = {
            (1,0): (0,1),
            (0,-1): (1,0),
            (-1,0): (0,-1),
            (0,1): (-1,0),
        }
        self.__rotation = right_rotation[self.__rotation]
        return self
    
    def found(self):
        return self.__x == self.__finish[0] and self.__y == self.__finish[1]


maze_example1 = {
    'm': [
        [0,1,0,0,0],
        [0,1,1,1,1],
        [0,0,0,0,0],
        [1,1,1,1,0],
        [0,0,0,1,0],
    ],
    's': (0,0),
    'f': (4,4)
}
maze_runner = MazeRunner(maze_example1['m'], maze_example1['s'], maze_example1['f']) 
maze_controller(maze_runner)
print maze_runner.found()


maze_example2 = {
    'm': [
        [0,0,0,0,0,0,0,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,0,0,0,0],
        [1,1,1,1,0,1,0,1],
        [0,0,0,0,0,1,0,1],
        [0,1,0,1,1,1,1,1],
        [1,1,0,0,0,0,0,0],
        [0,0,0,1,1,1,1,0],
    ],
    's': (7,7),
    'f': (0,0)
}
maze_runner = MazeRunner(maze_example2['m'], maze_example2['s'], maze_example2['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True


maze_example3 = {
    'm': [
        [0,0,0,0,0,0,0,0,0,0,0],
        [1,0,1,1,1,0,1,1,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,0,1,0,1],
        [1,0,1,0,1,1,1,0,1,0,1],
        [1,0,1,0,0,0,0,0,1,0,1],
    ],
    's': (0,5),
    'f': (10,5)
}
maze_runner = MazeRunner(maze_example3['m'], maze_example3['s'], maze_example3['f'])
maze_controller(maze_runner)
print maze_runner.found()   # True

maze_example4 = {
    'm': [
        [0,0,0,0,1,0,1,0,0,0,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [1,1,0,1,0,0,0,1,0,1,1],
        [0,1,0,1,0,1,0,1,0,1,0],
        [0,1,0,0,0,1,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,1,1,1,0,1,1,1,1,0],
        [0,0,0,0,0,0,0,0,0,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example4['m'], maze_example4['s'], maze_example4['f']) 
maze_controller(maze_runner) 
print maze_runner.found() # True

maze_example5 = {
    'm': [
        [0,0,0,1,1,0,1,1,0,0,0],
        [0,1,0,0,0,0,0,0,0,1,0],
        [0,1,0,1,1,1,1,1,0,1,0],
        [0,0,0,1,0,0,0,1,0,0,0],
        [0,0,1,1,0,0,0,1,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
        [0,0,1,0,0,0,0,0,1,0,0],
        [0,0,1,1,1,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,1,0,1,0,1,0,0],
    ],
    's': (0,5),
    'f': (4,5)
}
maze_runner = MazeRunner(maze_example5['m'], maze_example5['s'], maze_example5['f']) 
maze_controller(maze_runner) 
print maze_runner.found() # True
