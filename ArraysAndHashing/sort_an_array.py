# Merge Sort
# Time: O(nlogn) we divide logn times and we merge n values
# Space: O(n)
def sortArray(nums):
    # Merges the left and right halves of the array
    def merge(arr, L, M, R):
        # We get the left & right so that we do not override the array
        left, right = arr[L : M + 1], arr[M + 1, R + 1]
        i, j, k = L, 0, 0  # i for arr, j for left, and k for right. This is used as 3-
        # pointers for merging in a sorted manner

        while j < len(left) and k < len(right):  # Runs until one finishes
            if left[j] <= right[k]:
                arr[i] = left[j]
                j += 1
            else:
                arr[i] = right[k]
                k += 1
            i += 1
        while j < len(left):  # Append the rest (if any)
            arr[i] = left[j]
            j += 1
            i += 1
        while k < len(right):  # Append the rest (if any)
            arr[i] = right[k]
            k += 1
            i += 1

    # Divides until we reach the base case
    def merge_sort(arr, l, r):
        if l == r:  # Base case
            return

        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)

    merge_sort(nums, 0, len(nums) - 1)
    return nums
