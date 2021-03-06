import matplotlib.pyplot as plt
import array as ar
import numpy as np

class datas:
    def __init__(self, X1, X2, target):
        self.X1 = X1
        self.X2 = X2
        self.target = target

alpha=1
bias=1

Vectors=[datas(1, 1, 1), datas(1, 0, -1), datas(0, 1, -1), datas(0, 0, -1)]
W1=0
W2=0 
b=0

cont = True
while cont:
	weight_change=0
	cont = False
	for datas in Vectors:
		Yin = b + datas.X1 * W1 + datas.X2 * W2
		if Yin > 0.2:
			y = 1
		elif Yin < -0.2:
			y = -1
		else:
			y = 0
		Delta_W1=alpha * (datas.target - y) * datas.X1
		Delta_W2=alpha * (datas.target - y) * datas.X2
		Delta_b=alpha * (datas.target - y) * 1
		if weight_change< abs(W1 - (W1 + Delta_W1)):
			weight_change = abs(W1 - (W1 + Delta_W1))
		if weight_change < abs(W2 - (W2 + Delta_W2)):
			weight_change = abs(W2 - (W2 + Delta_W2))
		if weight_change < abs(b - (b + Delta_b)):
			weight_change = abs(b - (b + Delta_b))
		cont= True
		W1 += Delta_W1
		W2 += Delta_W2
		b += Delta_b
		if weight_change <= 0.2:
			cont = False
print("X1:",datas.X1)
print("X2: ",datas.X2)
print("Yin: ", Yin)
print("y: ", y)
print("t: ", datas.target)
print("dw1 :", Delta_W1)
print("dw2: ", Delta_W2)
print("db:", Delta_b)
print("w1: ", W1)
print("w2: ", W2)
print("b: ", b)
print("weight change is : ", weight_change <= 0.2)
print("weight_change: ",weight_change)
