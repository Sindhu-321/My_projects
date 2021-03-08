# -*- coding: utf-8 -*-
import numpy as np
one=np.array(["[-----------]",
              "[           ]",
              "[     0     ]",
              "[           ]",
              "[-----------]"])
two=np.array(["[-----------]",
              "[           ]",
              "[   0   0   ]",
              "[           ]",
              "[-----------]"])
three=np.array(["[-----------]",
                "[     0     ]",
                "[     0     ]",
                "[     0     ]",
                "[-----------]"])
four=np.array(["[-----------]",
               "[  0    0   ]",
               "[           ]",
               "[  0    0   ]",
               "[-----------]"])
five=np.array(["[-----------]",
               "[  0    0   ]",
               "[  0    0   ]",
               "[    0      ]",
               "[-----------]"])
six=np.array(["[-----------]",
              "[   0    0  ]",
              "[   0    0  ]",
              "[   0    0  ]",
              "[-----------]"])


def pmat(array):
    x=len(array)
    for i in range(x):
        print(array[i])

def rolldice(n):
    if n==1:
        pmat(one)
    elif n==2:
        pmat(two)
    elif n==3:
        pmat(three)
    elif n==4:
        pmat(four)
    elif n==5:
        pmat(five)
    elif n==6:
        pmat(six)
    else:
        print("Number {} not available".format(n))
        
import random
n=random.randint(1,6)

print("This is a dice simulator.")

rolldice(n)

y=input("Enter y to roll again: ")


while(y=='y'):
    n=random.randint(1,6)
    rolldice(n)
    y=input("Enter y to roll again: ")

print("Simulation complete!")


        
