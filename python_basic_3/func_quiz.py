# 최댓값 최솟값 구하기

def max_min_search(*number):
    max_num = number[0]
    min_num = number[0]
    for num in number:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num, min_num
    # return max(number),min(number)

print(max_min_search(15,30,4,6,7,89,32))
