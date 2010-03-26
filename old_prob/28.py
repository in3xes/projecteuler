

def mark_spiral(spiral, max_x, max_y, min_x, min_y, current_x, current_y, current_num):

    n = len(spiral)
    
    for y in xrange(current_y + 1, max_y + 2):
        spiral[current_x][y] = current_num
        if current_num == n*n:
            return spiral, max_x, max_y, min_x, min_y, current_x, current_y, current_num
        current_num += 1
        current_y = y
        if current_y > max_y:
            max_y = current_y

    
    for x in xrange(current_x + 1, max_x + 2):
        spiral[x][current_y] = current_num
        if current_num == n*n:
            return spiral, max_x, max_y, min_x, min_y, current_x, current_y, current_num

        current_num += 1
        current_x = x
        if current_x > max_x:
            max_x = current_x

    for y in xrange(current_y - 1, min_y - 2, -1):
        spiral[current_x][y] = current_num
        if current_num == n*n:
            return spiral, max_x, max_y, min_x, min_y, current_x, current_y, current_num

        current_num += 1
        current_y = y
        if current_y < min_y:
            min_y = current_y

            
    for x in xrange(current_x - 1, min_x - 2, -1):
        spiral[x][current_y] = current_num
        if current_num == n*n:
            return spiral, max_x, max_y, min_x, min_y, current_x, current_y, current_num

        current_num += 1
        current_x = x
        if current_x < min_x:
            min_x = current_x

    return spiral, max_x, max_y, min_x, min_y, current_x, current_y, current_num

def get_diagonals_sum(spiral):
    left_sum = 0
    right_sum = 0
    n = len(spiral)
    for x in xrange(0, n):
        left_sum += spiral[x][x]
        if x != n-x-1:
            right_sum += spiral[x][n-x-1]

    return left_sum + right_sum
        
        
def make_spiral(n):
    spiral=[[0]*n for i in xrange(0,n)]
    center_x = center_y = int(n/2)
    current_x = current_y = center_x
    spiral[current_x][current_y] = 1
    current_num = 2
    step_num = 1
    max_x = min_x = current_x
    max_y = min_y = current_y
    #while current_x != 0 and current_y != n-1:
    while current_num != n*n:
        spiral, max_x, max_y, min_x, min_y, current_x, current_y, current_num = mark_spiral(spiral, max_x, max_y, min_x, min_y, current_x, current_y, current_num)


    return spiral

spiral=make_spiral(1001)
print "The sum of both diagonals is", get_diagonals_sum(spiral)
