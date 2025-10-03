def fizzbuzz(n):
    # n: upper limit of values to test (inclusive)
    # Returns: NONE
    # Prints: appropriate response for each value i in ascending order
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:  # multiple of both 3 and 5
            print("FizzBuzz")
        elif i % 3 == 0:  # multiple of 3 (but not 5)
            print("Fizz")
        elif i % 5 == 0:  # multiple of 5 (but not 3)
            print("Buzz")
        else:  # not a multiple of 3 or 5
            print(i)

# 입력값 검증 (0 < n < 2 x 10^5)
n = int(input())
if 0 < n < 2 * 10**5:
    fizzbuzz(n)
else:
    print("입력값은 0보다 크고 2x10^5보다 작아야 합니다.")
