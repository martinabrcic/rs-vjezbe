
def primes_in_range(start, end):

    list_prostih = []
    
    for i in range(start, end + 1):
        if i > 1:
            is_prime = True
            for j in range(2, i):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                list_prostih.append(i)
    
    return list_prostih

print(primes_in_range(1,10))