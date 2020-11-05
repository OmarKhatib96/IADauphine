



import math

 

w1 = 0.4
w2 = 0.6
w3 = 0.1
i1 = 0.1
i2 = 0.5
out1 = 1
out2 = 0

eta = 0.5

w4=0.5

from math import log
def cross_entropy(outputin,yin,total_i,n):
    sum=0
    for j in range(1,n):
        for i in range(1,total_i):
            sum=sum+log(outputin)+(1-yin)*log(1-outputin)
    return -sum



def sigmoid (x):
    s = 1.0  / (1.0 + math.exp (-x))
    return s



def softmax(i, output,outputs):#i number of class
    from math import exp
    return exp(output)/(1+exp(outputs[0])+exp(outputs[1]))

    # forward
neth = w1 * i1 + w2 * i2
#outh = sigmoid (neth)

neto1 = w3 * neth
neto2=w4*neth
o1 = softmax(2,neto1,[neto1,neto2])
o2=softmax(2,neto2,[neto1,neto2])

for i in range (1000):
    neth = w1 * i1 + w2 * i2
   # outh = sigmoid (neth)
    #neto = w3 * outh
    neto1=w3*neth
    neto2=w4*neth
    o1 =softmax(2,neto1,[neto1,neto2])
    o2=softmax(2,neto2,[neto1,neto2])
    #err = 0.5 * (out - o) ** 2
     #-yin / oin + (1 - yin) / (1 - oin)
    err1=cross_entropy(o1,out1,2,1)#2 classes, 50 exemples
    err2=cross_entropy(o2,out2,2,1)
    print (err1+err2, o1,o2)
    '''
    if(1-o==0):
        multi=0
    else:
        multi=1
    '''

    dw3 =  (-out1/o1)* o1 * (1.0 - o1)* neth
    dw2 = (-out1/o1)* o1 * (1.0 - o1) * w3 * neth * (1.0 - neth) * i2
    dw1=(-out1/o1)*o1 * (1.0 - o1) * w3 * neth * (1.0 - neth) * i1
    #for MSE
    #dw3 = (o - out) * o * (1.0 - o) * outh
    #dw2 = (o - out) * o * (1.0 - o) * w3 * outh * (1.0 - outh) * i2
    #dw1 = (o - out) * o * (1.0 - o) * w3 * outh * (1.0 - outh) * i1
    w3 = w3 - eta * dw3
    w2 = w2 - eta * dw2
    w1 = w1 - eta * dw1

    dw4 =  (-out2/o2)* o2 * (1.0 - o2)* neth
    dw2 = (-out2/o2)* o2 * (1.0 - o2) * w3 * neth * (1.0 - neth) * i2
    dw1=(-out2/o1)*o2 * (1.0 - o1) * w3 * neth * (1.0 - neth) * i1
    #for MSE
    #dw3 = (o - out) * o * (1.0 - o) * outh
    #dw2 = (o - out) * o * (1.0 - o) * w3 * outh * (1.0 - outh) * i2
    #dw1 = (o - out) * o * (1.0 - o) * w3 * outh * (1.0 - outh) * i1
    w4 = w4 - eta * dw4
    w2 = w2 - eta * dw2
    w1 = w1 - eta * dw1





'''


#2 inputs , one input, one hidden layer of one neuron

inputs=[0.1, 0.5]
weights= [0.4,0.6,0.1]
eta=0.5
true_out=0.2
#desired output =0.2
import numpy as np




def hidden_layer(weights,input):
    return np.dot(weights,input)


def  output_layer(weights, hidden):
    return  hidden*weights[0:2]


def forward_pass(input,weights):

    return  weights[2]*sigmoid(hidden_layer(weights[0:2],input))  



import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def error_calc(out,true_out):
    return 0.5*(true_out-out)*(true_out-out)

def output_layer1(output,target):
        return -(target-output)


def output_layer2(output):
        return output*(1-output)

def output_layer3(output):
        return output

def output_layer4(output,target):
    return output_layer1(output,target)* output_layer2(output)*output_layer3(output)

def update_weights(weight,output,target):
    return weight-eta*output_layer4(output,target)





#print(forward_pass(inputs,weights))
#print(error_calc(forward_pass(inputs,weights),2))
#print(update_weights(weights[2],forward_pass(inputs,weights),true_out))
for iteration in range(0,800):
    for i in range(0,len(weights)):
       weights[i]=update_weights(weights[0],forward_pass(inputs,weights),true_out)
       print(error_calc(forward_pass(inputs,weights),true_out))
print(weights)
'''