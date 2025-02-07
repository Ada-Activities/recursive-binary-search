def binary_search(numbers, target):
    if not numbers:
        return False
        
    middle_index = len(numbers) // 2
    if numbers[middle_index] == target:
        return True
    elif numbers[middle_index] > target:
        return binary_search(numbers[:middle_index], target)
    else:
        return binary_search(numbers[middle_index +1:], target)

# print(binary_search([0,1,2,3,4], 4))
# print(binary_search([0,1,2,3,4], 5))

def min_sum(numbers, k):

    #find the length of the given array
    nums_len = len(numbers)

    # if the subarray is longer than the original array, raise an error
    if nums_len < k:
        raise ValueError("k must be an integer between 1 and len(numbers)")

    # get the sum of the first window
    window_sum = sum(numbers[:k])
    
    # initialize the minimum overall sum to the sum of the first window
    min_sum = window_sum

    # our for loop will be the start index of each window
    # our last window will start at nums_len - k
    for i in range(nums_len - k):
        # to shift the window, subtract the value at the window's current starting index from its sum
        window_sum -= numbers[i] 
        # shift the window to the right by adding the value at the k + ith index to replace the value just removed
        window_sum += numbers[k + i]
        # set the overall minimum subarray sum to either the sum of the new window
        # or the minimum subarray sum calculated so far, whichever is smaller
        min_sum = min(min_sum, window_sum)
    
    # return the minimum sum
    return min_sum

def min_sum(numbers, k):

    # initially overestimate what the minimum sum of any k consecutive elements in the array is 
    min_sum = float('inf')

    nums_len = len(numbers)

    # if the subarray is longer than the original array, raise an error
    if nums_len < k:
        raise ValueError("k must be an integer between 1 and len(numbers)")

    # the outer loop will be the start index of each subarray we look at
    # Our last possible subarray will start at with the nums_len - k element
    # since range is exclusive we add 1
    for i in range(nums_len - k + 1):
        # variable to hold the sum of the subarray we are looking at
        current_sum = 0
        # we want our subarray to go from numbers[i:(i+k)]
        # so our inner loop repeats k times so we can access the value at numbers[i]... numbers[i+k]
        for j in range(k):
            # add the value of each element in subarray to current_sum
            current_sum = current_sum + numbers[i + j]
        
        # set min_sum to whichever is smaller: 
            # sum of current subarray current_sum or the min_sum found so far
        min_sum = min(current_sum, min_sum)

    # return the result once we've checked all subarrays
    return min_sum

print(min_sum([-1, 5, 3, 1, -3, 2], 2))
print(min_sum([1, 2, 3, 4, 5], 3))
print(min_sum([1, 2, 3], 4))
