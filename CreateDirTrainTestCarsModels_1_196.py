import os
import shutil
output_dir="KaggleCarsByModels_1_196"
Num_clases=196
if  os.path.exists(output_dir):shutil.rmtree(output_dir)
os.mkdir(output_dir)
os.mkdir(output_dir + "\\train")
os.mkdir(output_dir+ "\\valid")
os.mkdir(output_dir + "\\test")
for i in range (Num_clases):
    j=i+1
    NameDir=str(j)
    if len(NameDir) < 2: NameDir= "00" + NameDir
    else:
        if len(NameDir) < 3: NameDir= "0" + NameDir
    os.mkdir(output_dir + "\\train\\"+NameDir)
    os.mkdir(output_dir+ "\\valid\\"+NameDir)
