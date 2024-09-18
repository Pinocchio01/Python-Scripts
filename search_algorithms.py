# Searching algorithms

"Only return True or False, modify if need index."

def linear_search(elements, item):
    index = 0
    found = False   # bool variable must be capitalized
    while index <= len(elements)-1 and found is False:
        if elements[index] == item:
            found = True
        else:
            index = index + 1
    return found

def binary_search(elements, item):
    start = 0
    end = len(elements) - 1
    while start <= end:
        mid = (start + end) // 2
        if elements[mid] == item:
            return True
        else:
            if item < elements[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return False

def interpolation_search(elements, item):
    l = 0; r = len(elements) - 1
    while l < r:
        # find x: expectation of item index
        p = (item - elements[l]) / (elements[r] - elements[l])
        n = r - l
        x = l + int(n*p)    # floor
        x = max(l, min(x,r))    # ensure x is between l and r
        # compare
        if elements[x] == item:
            return True
        # if not equal, narrow the range
        elif elements[x] < item:
            l = x + 1
        else:
            r = x - 1
    return False
        

if __name__ == '__main__':
    elements = [1, 3, 9, 8, 2, 4, 6]
    # linear search
    print("linear search:")
    print(linear_search(elements, 3))
    print(linear_search(elements, 5), '\n')
    # binary search
    print("binary search:")
    print(binary_search(elements, 3))
    print(binary_search(elements, 5), '\n')
    # interpolation search
    print("interpolation search:")
    print(interpolation_search(elements, 3))
    print(interpolation_search(elements, 5), '\n')








    
