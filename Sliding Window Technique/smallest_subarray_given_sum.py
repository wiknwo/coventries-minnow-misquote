'''Find smallest subarray that is greater than or equal to sum

    William Ikenna-Nwosu (wiknwo)
'''
import sys

def smallest_subarray_given_sum(targetsum, arr):
    minimum_window_size, window_sum, window_start_index = sys.maxsize, 0, 0
    for window_end_index in range(len(arr)):
        window_sum += arr[window_end_index]
        while window_sum >= targetsum:
            minimum_window_size = min(minimum_window_size, window_end_index - window_start_index + 1)
            window_sum -= arr[window_start_index]
            window_start_index += 1
    return minimum_window_size

my_list = [4, 2, 2, 7, 8, 1, 2, 8, 10]
targetsum = 8
print(smallest_subarray_given_sum(targetsum, my_list))

