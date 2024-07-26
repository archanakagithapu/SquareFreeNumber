num = int(input("Enter a number: "))
count = 0
for i in range(2, num + 1):  
    if num % i == 0:
        sqrt_i = int(i ** 0.5)
        is_square_free = True
        for j in range(2, sqrt_i + 1):
            if i % (j ** 2) == 0:
                is_square_free = False
                break
        if is_square_free:
            count += 1
print("Number of square-free divisors:", count)
