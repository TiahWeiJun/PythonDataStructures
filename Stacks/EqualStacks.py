#Equal Stacks problem from HackerRank

#h1, h2 and h3 are lists 
def equal_stacks(h1, h2, h3):
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    while not (sum1 == sum2 and sum2 == sum3):
        largest = max(sum1, sum2, sum3)
        if largest == sum1:
            h1.pop(0)
            sum1 = sum(h1)
        if largest == sum2:
            h2.pop(0)
            sum2 = sum(h2)
        if largest == sum3:
            h3.pop(0)
            sum3 = sum(h3)
    return sum1



h1 = [3,2,1,1,1]      
h2 = [4,3,2]
h3 = [1,1,4,1]
print(equal_stacks(h1, h2, h3))
