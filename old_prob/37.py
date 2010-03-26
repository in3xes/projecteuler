import primegenerator
import itertools

def trunc_left(num_str, len_str = None):
    if len_str is None:
        len_str = len(num_str)

    left_pos = 1
    while left_pos < len_str:
        yield num_str[left_pos:]
        left_pos += 1

def trunc_right(num_str, len_str = None):
    if len_str is None:
        len_str = len(num_str)
        
    right_pos = len_str - 1
    while right_pos > 0:
        yield num_str[:right_pos]
        right_pos -= 1

def main():
    known_primes = []
    for prime in primegenerator.primes_generator(limit=1000000):
        known_primes.append(str(prime))

    count_success = 0
    sum_success = 0
    
    for prime in known_primes:
        if prime[0] not in ['2','3','5','7'] or \
           prime[len(prime)-1] not in ['2','3','5','7']:
            continue
        
        check = 1
        
        for tl, tr in itertools.izip(trunc_left(prime), trunc_right(prime)):
            if tl not in known_primes or tr not in known_primes:
                check = 0
                break

        if check == 1:
            count_success += 1
            sum_success += int(prime)
            print prime
            if count_success == 15:
                return
            


if __name__ == "__main__":
    main()
            
        
    
    
