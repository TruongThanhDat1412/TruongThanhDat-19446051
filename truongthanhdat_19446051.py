# -*- coding: utf-8 -*-
"""TruongThanhDat-19446051.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zHTwpuZ_NHTUdZbkVrIFe_h2384z9xQV
"""

if 2**2==4:
  print("Cấu trúc if")

a=10
if a==1:
  print(1)
elif a==2:   
  print(2)
else:
  print("a lot")

for i in range(4):
    print(i)

x=range(3,20,2)
for n in x:
  print(n)

t = 12345, 54321, 'hello!'

t[0]

t[0:2]

for word in('cool','powerful','readable'):
  print('python is %s' % word)

z=1+1j
while abs(z)<100:
  if z.imag ==0:
    break
  z=z**2+1
z

a=[1,0,2,4]
for el in a: 
  if el==0:
    continue
  print (1./el)

vowels="aeiouy"
for i in 'powerful':
  if i in vowels:
    print(i)

message="hello how are you?"
for word in message.split():
  print(word)

word=('cool','powerful','readable')
for i in range(0, len(word)):
  print((i, word[i]))

for index, item in enumerate(word):
  print((index,item))

tel={'emanuelle': 5752,'sebastian': 5578}
tel['francis']= 5915
tel

tel['sebastian']

tel.keys()

tel.values()

'francis' in tel

d={'a':1,'b':1.2,'c':1j}
for key, val in sorted(d.items()):
  print('key: %s has value: %r' %(key,val))

[i**2 for i in range(4)]

[i**2 for i in range(4) if i%2==1 ]

fruits=['apple','banana','cherry','kiwi','mango']
new_fruits = [i for i in fruits if 'a' in i]
new_fruits

bi=1
for t in range(1, 100):
  bi *= 4* t **2/(4* t** 2-1)
bi *=2
print(bi)