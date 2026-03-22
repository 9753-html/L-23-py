list1 = {10,20,30,40}
list2 = {'a', 'b','c', 'd'}
res = list(zip(list1, list2))
print(res)

l1 = [10,20,30]
l2 = [100,200,300]
for a, b in zip(l1,l2[::-1]):
    print(a,b)

stud = ['rishi', 'kiri', 'shanu']
roll = [1,2,3]
dict1 = {stud: roll for stud, roll in zip(stud, roll)}
print(dict1)