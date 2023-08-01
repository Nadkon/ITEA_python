def find_largest_number(*args):
    max = args[0]
    for num in args[1:]:
        if max < num:
            max = num
    return max

print(find_largest_number(1,2,3,9,5,7))