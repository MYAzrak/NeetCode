# Using slicing and sorting
# Time: O(nlogn)
# Space: O(1)
def merge(nums1, m: int, nums2, n: int) -> None:
    nums1[m:] = nums2
    nums1.sort()


# Using three pointers and begin merging from the end of nums1 since
# we know it would be zeros
# Time: O(n)
# Space: O(1)
def merge(nums1, m: int, nums2, n: int) -> None:
    end_ptr = len(nums1) - 1  # Points to the end of nums1 where we would merge
    nums1_ptr = m - 1  # Points to the last number != 0 in nums1
    nums2_ptr = n - 1  # Points to the last number in nums2
    while nums2_ptr >= 0 and nums1_ptr >= 0:
        if nums1[nums1_ptr] >= nums2[nums2_ptr]:
            nums1[end_ptr] = nums1[nums1_ptr]
            nums1_ptr -= 1
        else:
            nums1[end_ptr] = nums2[nums2_ptr]
            nums2_ptr -= 1
        end_ptr -= 1

    # Fill nums1 with leftover nums1 elements
    while nums2_ptr >= 0:
        nums1[end_ptr] = nums2[nums2_ptr]
        end_ptr -= 1
        nums2_ptr -= 1


print(merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
print(merge(nums1=[1], m=1, nums2=[], n=0))
print(merge(nums1=[0], m=0, nums2=[1], n=1))
print(merge(nums1=[2, 0], m=1, nums2=[1], n=1))
