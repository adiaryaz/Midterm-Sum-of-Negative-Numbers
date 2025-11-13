n = input()
if "." in n:
    print("NotProceed")
else:
    n = int(n)
    if n <= 0:
        print("NotProceed")
    else:
        sum_of_negative = 0
        for _ in range(n):
            num = int(input())
            if num < 0: 
                sum_of_negative += num
        print(sum_of_negative)