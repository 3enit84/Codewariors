def maxInversions(arr):
    Icnt = 0#count iversions
    for i in range(len(arr)): 
        Lcnt = 0#count elements that are less than breaking point
        for j in range(i ,len(arr)): 
            if (arr[i] > arr[j]): 
                Lcnt += 1 
        Gcnt = 0#count elements that are greater than breaking point
        for j in range(i,-1,-1): 
            if (arr[i] < arr[j]): 
                Gcnt += 1
        Icnt += Gcnt * Lcnt 
    return Icnt
print(maxInversions(arr))
