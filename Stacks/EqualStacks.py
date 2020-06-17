#Equal Stacks problem from HackerRank

#h1, h2 and h3 are lists 
def equal_stacks(h1, h2, h3):
    sizeh1 = sum(h1)
    sizeh2 = sum(h2)
    sizeh3 = sum(h3)

    while not (sizeh1 == sizeh2 == sizeh3):
        lst = [sizeh1, sizeh2, sizeh3]
        max_value = max(lst)
        if sizeh1 == max_value:
            h1.pop(0)
            sizeh1 = sum(h1)
        if sizeh2 == max_value:
            h2.pop(0)
            sizeh2 = sum(h2)
        if sizeh3 == max_value:
            h3.pop(0)
            sizeh3 = sum(h3)
    if sizeh1 == 0:
        print("No answer")
    else:
        print(sizeh1)


h1 = [2,2,3,1,2]      
h2 = [4,1,1]
h3 = [2,1,2]
equal_stacks(h1, h2, h3)
