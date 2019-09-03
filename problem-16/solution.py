from math import floor, pow

least_sum = 0
num = pow(2, 15)
num = list(str(num))
for i in num:
    least_sum = least_sum + int(i)

def calclulate_power_digit_sum(power):
    multiplier = power / 15
