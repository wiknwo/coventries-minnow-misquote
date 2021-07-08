'''Script to find longest substring with k distinct characters in a string

    William Ikenna-Nwosu (wiknwo)
'''
def longest_substring_k_distinct_chars(somestring, k):
    character_count_dict = {}
    length_longest_substr = 0
    window_start_index = 0
    for window_end_index in range(len(somestring)):
        right_char = somestring[window_end_index]
        character_count_dict[right_char] = character_count_dict.get(right_char, 0) + 1
        while len(character_count_dict) > k:
            left_char = somestring[window_start_index]
            character_count_dict[left_char] = character_count_dict.get(left_char) - 1
            if character_count_dict.get(left_char) == 0:
                del character_count_dict[left_char]
            window_start_index += 1
        length_longest_substr = max(length_longest_substr, window_end_index - window_start_index + 1)
    return length_longest_substr
    
print(longest_substring_k_distinct_chars('AAAHHIBC', 2))