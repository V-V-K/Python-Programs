string=input()
char=input()
l=len(string)
def last_index(string,char,li):
    z=0
    if len(string)==0 or li==-1:
        return -1
    if string[li]==char:
        z=1
    if z:
        return li
    else:
        return 0+last_index(string,char,li-1)
print(last_index(string,char,l-1))
