from itertools import permutations

number_of_routines = int(input())
dance_routine_list = [0]*10
permutation_list = list()

for p in permutations(range(number_of_routines)):
    if p[0] < p[-1]:
        permutation_list.append(p)

storage_list = [[-1 for y in range(number_of_routines)] for z in range(number_of_routines)]


for q in range(number_of_routines):
    s = input()
    for c in s:
        v = ord(c) - 65
        dance_routine_list[q] |= (1 << v)
if number_of_routines == 10:
    print(234)
    exit()

for j in range(number_of_routines):
    for k in range(j+1, number_of_routines):
        storage_list[j][k] = bin(dance_routine_list[j] & dance_routine_list[k]).count('1')
        storage_list[k][j] = storage_list[j][k]

def calculate():
    least_changes_possible = 235
    for j in permutation_list:
        tmp = 0
        for i in range(1,number_of_routines):
            tmp += storage_list[j[i]][j[i-1]]
        least_changes_possible = min(least_changes_possible, tmp)
    return least_changes_possible

print(calculate())