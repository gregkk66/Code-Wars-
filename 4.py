def sum_for_list(lst):
    result=[]
    b=0
    flag=0
    for i in primes(max(map(abs,lst))+1):
        for j in lst:
            if j%i==0:
                flag=True
                b+=j
        if flag==True:
            result.append([i,b])
        flag=0
        b=0
    result.sort(key=lambda x: x[0])
    return result

def primes(n):
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
