# Program to sort a list using insertion sort

def insertion_sort(arr): 
    for i in range(1,len(arr)): 
        key = arr[i]                           
        temp = i-1                               
        while temp>=0 and key<arr[temp]:  
                arr[temp + 1] = arr[temp]    
                temp -= 1                          
        arr[temp + 1] = key   
    return arr                 
    
arr = insertion_sort([12,98,23,54,22,76])
print("Sorted list is:",end = ' ')
print(*[x for x in arr], sep = ',')