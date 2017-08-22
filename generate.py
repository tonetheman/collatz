
def gen1(n):
    if (n%2)==0:
        return n/2
    return 3*n + 1

def gengen(n):
    # yield n
    while True:
        n = gen1(n)
        if n==1:
            yield n
            break
        else:
            yield n

def make_list(n):
    if n==0: return []
    res = [i for i in gengen(n)]
    return res

def count_len(n):
    if n==0:
        return 0
    # print("counting for",n)
    count = 0
    for i in gengen(n):
        count = count+1
    return count

def test():
    res = make_list(9)
    print(len(res), res)
    print(count_len(9))

def find_max_seqlen(n):
    max_len = -1
    for i in range(n):
        res = count_len(i)
        if res>max_len:
            max_len = res
            index = i

    print(index, max_len)

def count_even_odd(n):
    even = 0
    odd = 0
    for i in range(1,n):
        l = count_len(i)
        if (l%2)==0:
            even = even + 1
        else:
            odd = odd + 1
    print("even", even)
    print("odd",odd)

count_even_odd(100000)
