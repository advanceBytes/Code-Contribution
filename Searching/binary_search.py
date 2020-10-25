def binary_search(my_list, element_to_be_searched):
    start,end  = 0,len(my_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if my_list[mid] == element_to_be_searched: return mid
        else:
            if my_list[mid] < element_to_be_searched: start = mid + 1
            else: end = mid - 1
    return -1


if __name__ == "__main__":
    my_list = list(map(int,input('Enter Elements of array : \n').strip().split(' ')))
    element_to_be_searched = int(input("Enter element to be searched :\n"))
    ans = binary_search(my_list, element_to_be_searched)
    
    if ans >= 0:
        print("Element found at index ", ans)
    else:
        print("Element not found")
