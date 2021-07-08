'''Find the max sum subarray of a fixed size k

Example input: [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
'''
import sys

def find_max_sum_sub_array(arr, k):
    max_value, runningsum = -sys.maxsize, 0
    subarray, max_subarray = [0] * k, [-sys.maxsize] * k

    for i in range(len(arr) - (k - 1)):
        for j in range(k):
            subarray[j] = arr[i + j]
        max_value = max(max_value, sum(subarray))
    
    return max_value

my_list = [4, 2, 1, 7, 8, 1, 2, 8, 1, 0]
print(find_max_sum_sub_array(my_list, 3))

