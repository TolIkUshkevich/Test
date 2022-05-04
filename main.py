def find_expection(lisst):
    od = 0
    even = 0
    result = 0
    for i in lisst:
        if i % 2 == 0:
            even += 1
        else:
            od += 1

    for i in lisst:
        if od > even:
            if i % 2 == 0:
                result = i
        else:
            if i % 2 != 0:
                result = i
    return result

print(find_expection([1, 2, 3, 5, 7]))