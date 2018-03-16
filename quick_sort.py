from __future__ import print_function

def quick_sort(array):
    array_length = len(array)
    if( array_length <= 1):
        return array
    else:
        PIVOT = array[0]
        GREATER = [ element for element in array[1:] if element > PIVOT ]
        LESSER = [ element for element in array[1:] if element <= PIVOT ]
        return quick_sort(LESSER) + [PIVOT] + quick_sort(GREATER)


if __name__ == '__main__':
    try:
        raw_input          
    except NameError:
        raw_input = input 

    user = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [ int(item) for item in user.split(',') ]
    print( quick_sort(unsorted) )
