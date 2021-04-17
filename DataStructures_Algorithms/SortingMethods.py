# Last element in correct place
def BubbleSort(array):
    for i in range(len(array)-1):
        _sorted = False
        for j in range(len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            _sorted = True
        if not _sorted:
            break
    return array


# Elements from start till i is sorted
def InsertionSort(array):
    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            for j in range(0,i):
                if array[i] < array[j]:
                    popped = array.pop(i)
                    array.insert(j,popped)
    return array


if __name__ == '__main__':
    pass
