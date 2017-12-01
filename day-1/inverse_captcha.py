#!/usr/bin/env python3

def inverse_captcha_from_string(string_number):
    return inverse_captcha([int(x) for x in string_number])

def inverse_captcha(numbers):
    sum = 0
    for first, second in zip(numbers[0:], numbers[1:] + numbers[0:1]):
        if first == second:
            sum += first

    return sum
