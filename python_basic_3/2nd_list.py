# 2차원 리스트
# list_2nd = [[1,2,3],["a","b","c"]]

# for i in list_2nd:
#     print(i)
#     for j in i:
#         print(j)

# for i in range(1,3):
#     for j in range(1,3):
#         print("첫번째 for문의 반복 {}번, 두번째 for문을 반복 {}번".format(i,j))

#구구단
# 2단부터 9단부터 = 8번 반복
# 1부터 9까지 = 9번 반복

print("2단부터 9단까지 구구단 출력")
for i in range(2, 9+1):
    for j in range(1, 9+1):
        print(f"{i} X {j} = {i*j}", end = "\t")
    print()

# 3차원 리스트
list_3rd = [[[1,2,3],[4,5,6]],[[11,12,13],[14,15,16]]]


cnt1=0
cnt2=0
cnt3=0
for i in list_3rd:
    cnt1 += 1
    print("i의 {}번째 반복입니다.".format(cnt1))
    print(i)
    for j in i:
        cnt2 += 1
        print("j의 {}번째 반복입니다.".format(cnt2))
        print(j)
        for k in j:
            cnt3 += 1
            print("k의 {}번째 반복입니다.".format(cnt3))
            print(k)
print('i는 {}번 반복, j는 {}번 반복, k는 {}번 반복'.format(cnt1, cnt2, cnt3))

