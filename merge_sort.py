from __future__ import print_function

def merge_sort(array):
    length = len(array)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(array[:midpoint])
        right_half = merge_sort(array[midpoint:])
        i = 0
        j = 0
        k = 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < right_length:
            array[k] = right_half[j]
            j += 1
            k += 1

    return array


if __name__ == '__main__':
    try:
        raw_input          
    except NameError:
        raw_input = input  

    user = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user.split(',')]
    print(merge_sort(unsorted))
    

