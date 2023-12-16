# -*- coding: utf-8 -*-
"""


@author: Alfonso Blanco
"""

import numpy as np
import cv2
import time


      
inicio=time.time()

dir="KaggleCarsByModels_1_196"
f=open("cardatasettrain.csv","r")
ContTraining=0
ContValid=0
ContTest=0
Conta=0;
for linea in f:
    Conta=Conta+1
    if Conta==1: continue
    
    lineadelTrain =linea.split(",")
    NameImg=lineadelTrain[6]
    # OJO LLEVA UN CR AL FINAL
    NameImg=NameImg[0:9]
    #print(NameImg)
    Model =int(lineadelTrain[5])
    
 
    StrModel=str(Model)
    if len(StrModel) < 2 : StrModel="00"+StrModel
    else:
        if len(StrModel) < 3 : StrModel="0"+StrModel
        
    img=cv2.imread('C:\\archiveKaggle\\cars_train\\cars_train' + '\\'+ NameImg) 
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img, (224,224), interpolation = cv2.INTER_AREA)
   
    if Conta > 8000:
        cv2.imwrite(dir +"\\test\\"+ NameImg,img)
        ContTest=ContTest+1
    else:
        if Conta > 7000:
            cv2.imwrite(dir +"\\valid\\"+ StrModel +"\\"+NameImg,img)
            ContValid=ContValid+1
            
        else: 
            Sitio=dir +"\\train\\"+ StrModel+"\\"+NameImg
            
            cv2.imwrite(Sitio,img)
            ContTraining=ContTraining+1
        
print("")         
print("Records to train = "+str(ContTraining))
print("Records to valid = "+str(ContValid))
print("Records to test = "+str(ContTest))
print("time in seconds = " + str(time.time()- inicio))
