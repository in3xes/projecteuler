
# 1 Millionth Lexicographic Permutation of 0,1,2,3,4,5,6,7,8,9


def factorial(n):
    if n==1 or n==0:
        return 1
    if n<0:
        return None
    else:
        return n*factorial(n-1)

def next_smallest(number_list, count):
    return min(number_list[count:])


def find_nth_permutation(num_list, n, permuted_list = []):
    num_count = 0                       # nth smallest number
    list_len = len(num_list)
    try:
        num_count = n // factorial(list_len - 1)
    except:
        return
    permuted_list.append(num_list[num_count]) # Assuming list to be sorted
    num_list.remove(num_list[num_count])
    find_nth_permutation(num_list, n-num_count*factorial(list_len - 1), permuted_list)
    return permuted_list

num_list = range(0, 10)

if __name__ == "__main__":
    print find_nth_permutation(num_list, 999999)

    
    


