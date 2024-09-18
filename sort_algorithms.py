# Sorting algorithms

def insertion_sort(elements):
    for i in range(1, len(elements)): # element[0] is itself already sorted
        j = i - 1
        while (j >= 0) and elements[j+1] < elements[j]:
            elements[j], elements[j+1] = elements[j+1], elements[j]
            j = j - 1
    return elements

elements = [3, 5, 2, 1, 8, 7]
print(insertion_sort(elements))

