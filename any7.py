def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE 
    for n in nums:
        if n == 7:
            return True
    return False

print("should be True", any7([1, 2, 7, 4, 5]))
print("should be False", any7([1, 2, 4, 5]))

