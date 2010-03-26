## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##
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

    def get_path(self, row_num, allowed_index_list = [0]):
        #pdb.set_trace()
        row_original = self.points[row_num]
        row_sorted = sorted(self.points[row_num], reverse = True)
        for row_elem in row_sorted:
            elem_index = row_original.index(row_elem)
            if elem_index in allowed_index_list:
                print "Number=", row_elem
                self.path_sum += row_elem
                
                if row_num == len(self.points) - 1:
                    return
                row_num_passed = row_num + 1
                allowed_index_list_passed = [elem_index, elem_index + 1]
                self.get_path(row_num_passed, allowed_index_list_passed)
                
        print "sum=", self.path_sum
        self.path_sum_list.append(self.path_sum)
                
tri = triangle()
tri.init_from_file('triangle')
print tri
tri.get_path(0)
print tri.path_sum
print "Max=", max(tri.path_sum_list)            
