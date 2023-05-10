
def count_primes(num):
    diapazon = range(0, num+1)
    amount = 0
    for i in diapazon:
        if i >= 2:
            count = 0
            for dayof in range(1, i+1):
                if i % dayof == 0:
                    count += 1
            if count == 2:
                amount += 1
    return amount




# Check
print(count_primes(10))