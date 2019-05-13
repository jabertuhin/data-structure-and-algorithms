"""
This code was partially done by Udacity DS and Algo in python course.
"""


def binary_search(input_array, value):
    left = 0
    right = len(input_array)-1
    while (left<=right):
        mid = (left+right)//2        
        if input_array[mid] == value:
            return mid
        elif input_array[mid] > value:
            right = right - 1
        else:
            left = left + 1
    return -1


if __name__ == "__main__":
    test_list = [1, 3, 9, 11, 15, 19, 29]
    test_val1 = 25
    test_val2 = 15
    print(binary_search(test_list, test_val1))
    print(binary_search(test_list, test_val2))