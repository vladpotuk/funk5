def product_in_range(start, end):
    if end < start:
        return "Непрвильний діапазон"
    result = 1

    for num in range(start, end+1):
        result *= num
    return result
start_range = 1
end_range = 5
result = product_in_range(start_range, end_range)
print(f"Добуток чисел у діапазоні від {start_range} до {end_range} дорівнює: {result}")
