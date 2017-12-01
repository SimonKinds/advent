#!/usr/bin/env python3

def inverse_captcha_from_string(string_number, step=1):
    return inverse_captcha([int(x) for x in string_number], step)

def inverse_captcha(numbers, step=1):
    sum = 0
    for first, second in zip(numbers[0:], numbers[step:] + numbers[0:step]):
        if first == second:
            sum += first

    return sum
