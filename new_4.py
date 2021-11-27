import math
import numpy as np
from numpy import array  
from numpy.linalg import norm

def print_dict(d1):
    for i in d1:
        print(i,d1[i])
    print('\n')
##    for i in d1:
##        print(d1[i])
    
def ex(apoA,apo2):
    for i in apoA:
        print(apo2[i])
def riza(a):
    return round(math.sqrt(a),3)
def eukleidia_apostasi(s1,s2):
    d=0
    for i,j in zip(s1,s2):
        d=d+math.pow((j-i),2)
    d=math.sqrt(d)

    return d

def eukleidia_2(s1,s2,e1,e2):
    d=riza(e1+e2-2*math.sqrt(e1*e2)*np.correlate(s1,s2))
    return d
def find_d(lexiko,E):
    apost={}
    for k in lexiko:
        signal1=lexiko[k]
        for j in lexiko:
            if(j!=k):
                signal2=lexiko[j]
                apost[str(k)+str(j)]=eukleidia_apostasi(signal1,signal2)#,E[k],E[j])
                #apost[str(k)+str(j)]=eukleidia_2(signal1,signal2,E[k],E[j])
                
    return apost
E={'s1':1,'s2':3,'s3':1,'s4':2}
a={'s1':[1,0,0,0],      's2':[1,riza(2),0,0], 's3':[0,0,1,0],                's4':[0,1/riza(2),1,1/riza(2)]}
d={'s4':[riza(2),0,0,0],'s1':[0,1,0,0],       's2':[1/math.sqrt(2),1,math.sqrt(3/2),0],'s3':[1/math.sqrt(2),-1/(2*riza(1.5)),0,math.sqrt(1/3)]}
c={'s3':[1,0,0,0],      's4':[1,1,0,0],       's1':[0,0,1,0],                's2':[0,1,1,1]}
b={'s2':[riza(3),0,0,0],'s3':[0,1,0,0],       's4':[1/riza(3),1,riza(2/3),0],'s1':[1/math.sqrt(3),0,-(1/3)*math.sqrt(3/2),1/math.sqrt(2)]}

apoA=find_d(a,E)
apoB=find_d(b,E)
apoC=find_d(c,E)
apoD=find_d(d,E)
y=2
if(y==1):
    print('apoA \n')
    print_dict(apoA)
    print('\n apoB \n')
    print_dict(apoB)
    print('\n apoC \n')
    print_dict(apoC)
    print('\n apoD \n')
    print_dict(apoD)
else:

    print('apoA \n')
    ex(apoA,apoA)
    print('\n apoB \n')
    ex(apoA,apoB)
    print('\n apoC \n')
    ex(apoA,apoC)
    print('\n apoD \n')
    ex(apoA,apoD)



