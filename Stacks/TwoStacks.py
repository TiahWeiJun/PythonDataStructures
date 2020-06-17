#Game of two stacks by HackerRank


def two_stacks(max_num, stack1, stack2):
    lst1 = []
    lst2 = []
    count1 = 0
    count2 = 0
    for x in stack1:
        count1 += x
        if count1 <= max_num:
            lst1.append(count1)
    
    for y in stack2:
        count2 += y
        if count2 <= max_num:
            lst2.append(count2)  

    countlist = []
    for x in range(len(lst1)):
        for y in range(len(lst2)):
            sum = lst1[x] + lst2[y]
            if sum <= max_num:
                count = x + y + 2
                countlist.append(count)
   
    return max(countlist)

print(two_stacks(20, [4,2,4,6,1], [2,1,8,5]))
    
    
