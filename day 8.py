#set
#unordered collection and values are unindexed
#it stores values based on hashtable
s={5,7,2,1,4,3}
print(s)
#set not allow duplicate values
se={2,3,4,4,5,5,6}
print(se)
#pop works as first in first out
s.pop()
print(s)
s.add(6)
print(s)
d={7,2,8,5,3,9}
print(d)
r={'b','r','u','a','i'}
print(r)

#dictinary
d = {"brand": "Ford","model": "Mustang","year": 1964,"year": 2005}
print(len(d))
#add new item to dictionary
d['city'] = 'chennai'
d.update({"year1":2011})
print(len(d))
#overwrite key's value with maverick
d['model']='maverick'
print(d)
#overwright key year1 with year2
d['year2']=d.pop('year1')
print(d)







