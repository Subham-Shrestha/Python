# a = ['ram', 'shyam', 'hari']
# a.append('sita')
# print(a)
# a.insert(0,'rita')
# print(a)
# a.pop()
# print(a)
# a.pop(3)
# print(a)
# a.append("Marco")
# print(a)
# a.append("Lazer")
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)

# # Empty Tuple
# a = ()
# b = tuple()
# print(type[a])
# print(type[b])

# value can't be changed; immiutable
# a = ('sun', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat')
# print(a)
# print(a[0])
# print(a[-1])
# print(a[::2])
# print(len(a))
# print('sun' in a)
# print('Sun' in a)
# print('Sun'.lower() in a)

# tuple with 1 element
# comma must be given after 1 element in tuple
# a = [1,]
# print(a)

# a,i,j = (1,2,3)
# print(a)
# print(i)
# print(j)

# collection of value that consist of pair dictionary. dictionary stores collection of key value pairs.
# empty dictionary 
# a = {}
# b = dict()
# print(type[a])
# print(type[b]) 
# student_grade = {'ram':25 , 'shyam':35 , 'hari':80}
# print(type[student_grade])

# dictionary is heterogenous. It is muitable. Key and value comes together. value can be accessed by using key. 
# if key is removed then value also gets removed.
# info = {'fname':'umesh' , 'lname':'regmi' , 'age':29 , 'ismarried':False , 'salary':5.01}
# print(type[info])

# key should be unique in dictionary.
# if keys are repeated, the repeated key replaces the original value.

# grades = {'ram':25 , 'shyam':28 , 'rita':52 , 'ram' : 36}
# print(len(grades))
# print('ram' in grades)
# print('Ram' in grades)
# print('RaM'.lower() in grades)
# print(grades['ram'])
# print(grades['rita'])
# print(grades['madan'])
# grades['ram'] = 52
# grades['shyam'] = 82
# print(grades['ram'])
# print(grades['shyam'])
# # grades['rama'] = 53
# print(grades)
# del grades['shyam']
# print(grades)
# grades.clear()
# print(grades)
# print(grades.keys())
# print(grades.values())
# print(grades.items())
# info = {'name':'umesh regmi' , 'salary':50.01 , 'address':{'city':'balaju' , 'district':'Kathmandu'}} #nested dictionary.
# print(info)
# print(info['name'])
# print(info['salary'])
# print(info['address']['city'])
# print(info['address']['district'])