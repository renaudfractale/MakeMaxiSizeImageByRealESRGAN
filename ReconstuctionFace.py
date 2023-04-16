# Importing Image class from PIL module
import face_recognition
import time
import datetime
from pathlib import Path
from os import walk

FolderIn = "./inputs"
ListeFichiers = []
for (repertoire, sousRepertoires, fichiers) in walk(FolderIn):
    ListeFichiers.extend(fichiers)


Fichier = FolderIn+"/"+ListeFichiers[0]
picture_of_me = face_recognition.load_image_file(Fichier)
face_locations = face_recognition.face_locations(picture_of_me)
print(Fichier)
print(face_locations)

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