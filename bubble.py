def bubble_sort(li):
    for i in range(size-1):
        for j in range(size-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
    return li


size = int(input())
li = [int(x) for x in input().split()]
li=bubble_sort(li)
print(li,end="")
