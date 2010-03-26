import pdb

class triangle:
    def __init__(self, n=20):
        self.n = n
        self.path_sum = 0
        self.path_sum_list = []

    def init_from_file(self, file_name):
        f = open(file_name, 'r')
        self.n = f.read().count('\n') + 1
        self.make_points (self.n)
        f.close()
        f = open(file_name, 'r')
        for r, line in enumerate(f):
            line_list = map(int, line.split(' '))
            for y, point in enumerate(self.points[r]):
                if point != -1:
                    self.points[r][y] = line_list[y]
        f.close()
        
    def make_points(self, n):
        self.points = [[-1]*n for i in xrange(n)]
        for r, i in enumerate(xrange(0, n)):
            self.points[r][:i+1] = [0 for j in xrange(0,i+1)]
                    
    def __str__(self):
        return str(self.points).replace(', -1','').replace('], ', '\n')

def get_pair(tri_obj, x_index, y_index):
    if tri_obj.points[x_index][y_index] != -1:
        return tri_obj.points[x_index+1][y_index], tri_obj.points[x_index+1][y_index+1]

    else:
        return None
    
def reduce_pair(points):
    return max(points[0], points[1])

def reduce_point(tri_obj, x_index, y_index):
    return tri_obj.points[x_index][y_index] + reduce_pair(get_pair(tri_obj, x_index, y_index))

def reduce_all(tri):
    rows = len(tri.points)
    
    for i in xrange(rows - 2, -1, -1):
        for j in xrange(0, i+1):
            tri.points[i][j] = reduce_point(tri, i, j)
            
    return tri

def main():
    
    tri = triangle()
    tri.init_from_file('/home/_inXs_/triangle.txt')
    print tri
    print
    print "The maximum sum is:"
    reduced_tri = reduce_all(tri)
    print reduced_tri.points[0][0]

    print
    print
    print "The reduced triangle is:"
    print reduced_tri


if __name__ == "__main__":
    main()
    
