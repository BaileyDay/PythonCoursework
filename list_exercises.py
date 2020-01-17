
# Sum of numbers in a list---------------------------------

sumlist = [ 1, 2, 3, 4, 5]

total = sum(sumlist)

print(total)

# Largest Number ---------------------------------

large = [10, 15, 9, 5]

largest = max(large)

print(largest)

# Smallest Number ---------------------------------

small = [5, 7, 9, 10]

smallest = min(small)

print(smallest)

# Even numbers ---------------------------------

even = [2, 4, 5, 7, 8, 9]

for num in even:
    if num % 2 == 0:
        print(num, end = " ")
    
# positive numbers ---------------------------------

positive_nums = [4, -5, 6, 7, -8, 9]

for nums in positive_nums:
    if nums > 0: 
     print(nums)

# Positive numbers II ----------------------------

neglis = [1, -3, 10, 7, -6, -8 ]
poslis = []

for x in range(len(neglis)):
    if x > 0:
        poslis.append(x)
    print(poslis)









# Multiply a list ---------------------------------

mult = [3, 6, 7, 4, 8]

mult = [i * 2 for i in mult]

print(mult)

# Multiply vectors -------------------------------

lst1 = [1, 2, 3]
lst2 = [1, 2, 3]

answer = [x * y for x, y in zip(lst1,lst2)]

print(answer)

# Matrix addition --------------------------------


matrice1 = [[2,2],
        [3,4]]
matrice2 = [[2,3],
        [4,4]]
matrice_sum = [[0, 0],
        [0, 0]]

for x in range(len(matrice1)):
    for y in range(len(matrice1[0])):
        matrice_sum[x][y] = matrice1[x][y] + matrice2[x][y]
for s in matrice_sum:
    print(matrice_sum)

# De-duplicate, removes duplicates from a list -------------

dupes = [2, 2, 3, 6, 7, 8, 8, 9]

dedupe = []

for num in dupes:
    if num not in dedupe:
        dedupe.append(num)
    print(dedupe)




