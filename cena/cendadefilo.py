# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:19:56 2020

@author: Henry
"""


import threading
num = 5
palillos = [threading.Semaphore(1) for i in range(num)]

def filosofo(id):
    while True:
        piensa(id)
        levanta_palillos(id)
        come(id)
        suelta_palillos(id)

def piensa(id):
  
    print ("El filosofo numero %d - Tiene hambre " % id)

def levanta_palillos(id):
    if (id % 2 == 0):  # Zurdo
        palillo1 = palillos[id]
        palillo2 = palillos[(id + 1) % num]
    else:  # Diestro
        palillo1 = palillos[(id + 1) % num]
        palillo2 = palillos[id]
    palillo1.acquire()
    print ("El filosofo numero %d - Tiene el primer palillo" % id)
    palillo2.acquire()
    print ("El filosofoso numero %d - Tiene ambos palillos" % id)
def suelta_palillos(id):
    palillos[(id + 1) % num].release()
    palillos[id].release()
    print ("El filosofo numero %d - Pasa a el estado pensando " % id)

def come(id):
    print ("El filosofo numero %d - Empieza a comer " % id)
    

filosofos = []
for i in range(num):
    fil = threading.Thread(target=filosofo, args=[i])
    filosofos.append(fil)
    fil.start()