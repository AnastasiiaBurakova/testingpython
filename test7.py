def my_reverse(l):
    length = len(l)
    i = length

    rev_list = [None] * length

    for item in l:
        i = i - 1
        rev_list[i] = item
    return rev_list    

l = [1,2,3,4,5]
print(my_reverse(l))