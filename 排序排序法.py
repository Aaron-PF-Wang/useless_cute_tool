#通过数学里的排序不等式给一个数列排序，时间复杂度是O(n!)

def all_permutations(n):#这里用递归，展示屎山
    if n == 0:return[[0]]
    else:
        last=all_permutations(n-1)
        new=[]
        for arr in last:
            for p in range(len(arr)+1):
                _=arr.copy()
                _.insert(p,n)
                new.append(_)
        return new
def multiply(a,b):
    if len(a)==len(b):
        sum=0
        for i in range(len(a)):
            sum+=a[i]*b[i]
        return sum
    else: return None

lst=[6,5,3,2,8,9,-1,-3,-5,-11]
_len=len(lst)
direct=1#direct的正负决定是从小到大还是从大到小，正表明从小到大

all_per=all_permutations(_len-1)
sum=multiply(range(_len),lst)
target_lst=list(range(_len))

for i in all_per:
    _=multiply(i,lst)
    if _*direct>sum*direct:
        sum=_
        target_lst=i

answer=lst.copy()
for i in range(_len):
    answer[target_lst[i]]=lst[i]

lst=answer
print(answer)

