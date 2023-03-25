test_list = [1, 2, 3, 4, 12, 322, 55, 66, 71, 80, 94, 6, 10, 32]
def avg_and_first_above_avg(numbers):
    avg = sum(numbers) / len(numbers)
    first_above_avg = None
    for num in numbers:
        if num > avg:
            first_above_avg = num
            break
    return (avg, first_above_avg)
print(avg_and_first_above_avg(test_list))