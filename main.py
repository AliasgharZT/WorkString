
name='Ali'
family='Zarrin'

print(name)

print(name[0])
print(name[-1])
print(name[len(name)-1])

print(name[:2])
print(name[-1::-1])

print(family)

print(name+family)

f=family.find('i')
print(f)
print(family[f])

print(family.upper())
print(family.lower())
#//////////////////////////////////
s='Majid.Salehy'

print(s)

ts=s.split('.')
print(ts)
print(len(ts))

ta=''
for a in ts:
    ta+=a+' '
print(ta)
# /////////////////////////////////
s2='/.,/Ali/'

print(s2)

print(s2.strip('/.,'))

s3='/!@A#$%Z^&*()T_+='

print(s3)

print(s3.strip('/!@#$%^&*()_+='))

ts3=''
for z in s3:
    if z>='A' and z<='Z':
        ts3+=z 
print(ts3)
