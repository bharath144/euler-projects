from math import floor, pow


def square_of_sum(num):
    # (n * (n + 1)) / 2
    sum = floor(pow(((num * (num + 1)) / 2), 2))
    return sum


def sum_of_squares(num):
    # (n * (n + 1) * (2n + 1)) / 6
    sum = floor(num * (num + 1) * (2 * num + 1) / 6)
    return sum


print("Difference between square of sums of numbers until 10 and sum of squares "
      "of numbers until 10 is: " + str(square_of_sum(10) - sum_of_squares(10)))

print("Difference between square of sums of numbers until 10 and sum of squares "
      "of numbers until 10 is: " + str(square_of_sum(100) - sum_of_squares(100)))
