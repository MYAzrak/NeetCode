from collections import defaultdict


# Boyer-Moore Voting Algorithm
# Since the result would be of len == 2 at most, we can make a hashmap of num : count
# for 2 candidate nums only. When the len of the count_dict becomes > 2 then one of these
# nums is incorrect, how do we check? dec the count of each by 1 and if anyone has a count
# = 0 pop it from the dict. At the end, make sure that the remaining nums in the count_dict
# have a count > n//3 using nums.count(num) since they may be misleading.
# Time: O(N)
# Space: O(1)
def majorityElement(nums):
    count = defaultdict(int)

    for num in nums:
        count[num] += 1

        if len(count) <= 2:
            continue

        new_count = defaultdict(int)
        for num, c in count.items():
            if c > 1:
                new_count[num] = c - 1
        count = new_count

    res = []
    for num in count:
        if nums.count(num) > len(nums) // 3:
            res.append(num)

    return res
