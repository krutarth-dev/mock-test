def mySqrt(x):
    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        mid_squared = mid * mid

        if mid_squared == x:
            return mid
        elif mid_squared > x:
            right = mid - 1
        else:
            left = mid + 1

    return left - 1

# Sample inputs
x1 = 4
x2 = 8
x3 = 16

# Calculate square roots using mySqrt()
sqrt1 = mySqrt(x1)
sqrt2 = mySqrt(x2)
sqrt3 = mySqrt(x3)

# Print the results
print("Square root of", x1, "is:", sqrt1)
print("Square root of", x2, "is:", sqrt2)
print("Square root of", x3, "is:", sqrt3)
