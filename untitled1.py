# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h3_d08KDy142_bUH4bt13wJKkGO8AGYu
"""

name="ngoc"
name.capitalize()

name.replace("c","n")

import numpy as np
import matplotlib.pyplot as plt

X= np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S=np.cos(X), np.sin(X)
plt.plot(X,C)
plt.plot(X,S)
plt.show()

height=[1.73, 1.68, 1.71, 1.89, 1.79]
weight=[65.4, 59.2, 63.6, 88.4, 68.7]
np_height=np.array(height)
np_weight=np.array(weight)
np_weight/np_height**2

q=9.87048
print(round(q,0))

x=[6,2,7,19,7,14]
print(x[-3]+x[-4])



import numpy as np
z = np.array([[5,0,2],[3,1,1]])
print(z[0:, 2:])

import numpy as np
z = np.array([[8,14,21],[5,16,20]])
print(z[1][2])

import numpy as np
p = np.array ([15,2,18,15,7,8])
print(p[0])

q=[36]
print(len(q))

import numpy as np
z = np.array([[2,3,3],[4,6,9]])
print(z[0:, 2:])

a= [9.93,5.29,5.44]
b= ['k','j','k']
c= [1,1,7]
print(c,b,a)

import numpy as np
m = np.array ([2,4,6])
n = 2 
print (m-n)

"""
Các giá trị mảng m trừ lần lượt cho 2

"""

p= ['l','f','x','o','e','q']
p.remove(p[4])
print(p)