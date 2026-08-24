def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


n, m = map(int, input().split())

next_num = n + 1

while not is_prime(next_num):
    next_num += 1

if next_num == m:
    print("YES")
else:
    print("NO")