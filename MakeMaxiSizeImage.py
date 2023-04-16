# Importing Image class from PIL module
from PIL import Image
from PIL import ImageChops
import torch
import numpy as np
from RealESRGAN import RealESRGAN
import time
import datetime
import ModulePython
from os import listdir
from os.path import isfile, join
from pathlib import Path
from os import walk

FileA = "./Exemples/A.jpeg"
FileB = "./Exemples/B.jpeg"
FileC = "./Exemples/C.png"
FileD = "./Exemples/D.jpg"

FolderIn = "./inputs"

ListeFichiers = []
for (repertoire, sousRepertoires, fichiers) in walk(FolderIn):
    ListeFichiers.extend(fichiers)
for i in ListeFichiers:
    print(i)
TaillesInCm=(100,200,400)#60,
def MakeTimestamp():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d_%H-%M-%S")

def PxToCm(PxSize,Dpi):
    return float(PxSize)*2.56/Dpi

def MakeSuperSize(pathImag,V,MaxSizeInCm,Dpi):
    print("*************************************************************")
    print("Path File In : "+pathImag)
    print("Version de l'ago : "+str(V))
    print("DPI : "+str(Dpi))
    print("Taille min : "+str(MaxSizeInCm)+" cm")
    # Opens a image in RGB mode
    im = Image.open(pathImag).convert('RGB')
    widthMaster, heightMaster = im.size

    print("widthMaster = "+str(widthMaster))
    print("heightMaster = "+str(heightMaster))
    
    if(widthMaster != heightMaster):
        return ""
    
    if(PxToCm(widthMaster,Dpi)>=MaxSizeInCm):
        return "" 

    imF = Image.open("./Assets/Filtre.png").convert('RGBA')
    imF2 = Image.open("./Assets/Filtre2.png").convert('RGBA')

    stepMaster = (2048,1792,1536,1280,1024,960,896,832,768,704,640,576,512,448,384,320,256,192,128)
    step=0
    for stepl in stepMaster:
        if(widthMaster % stepl ==0):
            step=stepl
            break

    print("step = "+str(step))
    if step==0:
        return""

    factor = 4
    Mstep = step*factor
    imF= imF.resize((Mstep,Mstep))
    imF2=imF2.resize((Mstep,Mstep))

    #Init torch + cuda
    print(torch.cuda.is_available())
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = RealESRGAN(device, scale=factor)
    model.load_weights('weights/RealESRGAN_x'+str(factor)+'.pth', download=True)


    width, height = im.size
    while(PxToCm(width,Dpi)<MaxSizeInCm):
        start = time.time()
        if V==0:
            im = ModulePython.X4v0(im,imF,step,factor,V,model,Image,ImageChops)
        elif V==1:
            im = ModulePython.X4v1(im,imF,step,factor,V,model,Image,ImageChops)
        elif V==2:
            im = ModulePython.X4v2(im,imF,step,factor,V,model,Image,ImageChops)
        elif V==3:
            im = ModulePython.X4v3(im,imF2,step,factor,V,model,Image,ImageChops)
        elif V==4:
            im = ModulePython.X4v4(im,imF2,step,factor,V,model,Image,ImageChops)

        end = time.time()
        elapsed = end - start
        width1, height1 = im.size
        strTexte = MakeTimestamp()+"_V"+ str(V)+"_"+str(width)+"x"+str(height)+"_to_"+str(width1)+"x"+str(height1)+".txt"
        f = open(strTexte, "w")
        f.write(str(elapsed) +" ==> "+ pathImag)
        f.close()
        print(strTexte+"==>"+str(elapsed))
        width, height = im.size

    im = im.convert("RGB")
    widthFinal, heightFinal = im.size
    # si len < 65500 ==> Jpg possible
    strName = MakeTimestamp()+"_V"+ str(V)+"_"+Path(pathImag).stem+"_"+str(widthFinal)+"x"+str(heightFinal)
    if height<65500:
        strName+=".jpg"
        im.save(strName,quality=85)
    else :
        strName+=".tif"
        im.save(strName,compression='tiff_lzw')
    return strName

for TailleInCm in TaillesInCm:
    for Fichier in ListeFichiers:
        MakeSuperSize(FolderIn+"/"+Fichier,4,TailleInCm,300)

#MakeSuperSize(FileB,0,100,300)
#MakeSuperSize(FileB,1,100,300)
#MakeSuperSize(FileB,2,100,300)
#MakeSuperSize(FileB,3,100,300)
#MakeSuperSize(FileB,4,100,300)

#MakeSuperSize(FileB,0,200,300)
#MakeSuperSize(FileB,1,200,300)
#MakeSuperSize(FileB,2,200,300)
#MakeSuperSize(FileB,3,200,300)
#MakeSuperSize(FileB,4,200,300)