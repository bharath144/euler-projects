from math import floor, pow

def calculate_sum(power):
    sum = 0
    num = floor(pow(2, power))
    num = list(str(num))
    for i in num:
        sum = sum + int(i)
    
    return sum

def calclulate_power_digit_sum(power):
    smallest = 15
    least_sum = calculate_sum(smallest)
    
    multiplier = floor(power / smallest)
    fractional_multiplier = floor(power % smallest)

    pd_sum = least_sum * multiplier
    pd_sum = pd_sum * floor(calculate_sum(fractional_multiplier))

    print(least_sum)
    print(pd_sum)

print(calculate_sum(1000))
