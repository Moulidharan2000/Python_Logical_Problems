# A consecutive-run is a list of adjacent, consecutive integers. This list can be either increasing or decreasing.
# Create a function that takes a list of numbers and returns the length of the longest consecutive-run.
# To illustrate:
#
# longestRun([1, 2, 3, 5, 6, 7, 8, 9]) ➞ 5
# # Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).
# Examples
# longest_run([1, 2, 3, 10, 11, 15]) ➞ 3
# # Longest consecutive-run: [1, 2, 3].
#
# longest_run([5, 4, 2, 1]) ➞ 2
# # Longest consecutive-run: [5, 4] and [2, 1].
#
# longest_run([3, 5, 7, 10, 15]) ➞ 1

def consecutive(sample_list):
    # sample_list.sort()
    # count = 0
    # for i in range(len(sample_list)-1):
    #     if sample_list[i+1] - sample_list[i] == 1:
    #         count += 1
    #     else:
    #         count = 1
    #
    # print(count)

    i = 0
    max_len, cur_max_len = 1, 1
    nums = list(set(sample_list))
    nums.sort()
    while i < len(nums) - 1:
        if nums[i + 1] - nums[i] == 1:
            cur_max_len += 1
        else:
            cur_max_len = 1
        i += 1
        if cur_max_len > max_len:
            max_len = cur_max_len
    return max_len if nums != [] else 0


if __name__ == '__main__':
    print(consecutive([1, 8, 3, 5, 6, 7, 8, 10]))
    print(consecutive([1, 2, 3, 10, 11, 15]))
    print(consecutive([5, 4, 2, 1]))
    print(consecutive([3, 5, 7, 10, 15]))
