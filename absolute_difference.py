def find_min_absolute_difference(ls,n):
    """
    time  --> o(nlogn)
    space --> o(n)
    """
    ls.sort()
    ans=1*10**9
    for i in range(1,n):
        ans =min(ans,(ls[i]-ls[i-1]))
    return ans



if __name__ == '__main__':
    n=int(input())
    assert n >=2,"The size of the array must be greater than or equal to 2";
    ls=list(map(int,input().split()))
    print(find_min_absolute_difference(ls,n))
    #print(find_min_absolute_difference.__doc__)



