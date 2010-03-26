

class grid:
    def __init__(self, n = 20):
        self.n = n
        self.points = [[0]*n for i in xrange(n)]
        self.active_x, active_y = 0, 0

    def move_right(self, x, y):
        if y+1 >= n:
            raise OutOfBoundsError
        return x, y+1

    def move_down(self, x, y):
        if x+1 >= n:
            raise OutOfBoundsError
        return x+1, y
    
    def travel(self, x, y):
        for i in xrange(1,3):
            check = 0
            if i==1:
                try:
                    self.active_x, self.active_y = move_right (x,y)
                except OutOfBoundsError:
                    check +=1 
                    pass
                
            if i==2:
                try:
                    self.active_x, self.active_y = move_down (x,y)
                except OutOfBoundsError:
                    check += 1
                    pass

            
start_x, start_y = 0, 0
grid_main = grid(n = 20)

