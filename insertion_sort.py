from __future__ import print_function

def insertion_sort(array):
    for index in range(1, len(array)):
        while 0 < index and array[index] < array[index - 1]:
            array[index], array[
                index - 1] = array[index - 1], array[index]
            index -= 1

    return array
    
if __name__ == '__main__':
    try:
        raw_input
    except NameError:
        raw_input = input
        
    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(insertion_sort(unsorted))
