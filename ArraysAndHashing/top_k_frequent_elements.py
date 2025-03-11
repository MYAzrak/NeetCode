# Sorting + hashmap
# Time: O(nlogn)
# Space: O(n)
def topKFrequent(nums, k: int):
    count = {}
    result = [0]

    for num in nums:
        count[num] = count.get(num, 0) + 1

    for num, count in count.items():
        result.append([num, count])

    result.sort(key=lambda x: x[1])

    for i in range(len(result)):
        result[i] = result[i][0]

    return result[-k:]


# BucketSort
# Time: O(n)
# Space: O(n)
def topKFrequent(nums, k: int):
    count = {}
    bucket = [[] for i in range(len(nums) + 1)]

    for num in nums:
        count[num] = count.get(num, 0) + 1

    for num, count in count.items():
        bucket[count].append(num)

    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result


print(topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
