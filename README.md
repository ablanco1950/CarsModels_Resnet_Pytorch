# CarsModels_Resnet_Pytorch
Project that detects the Model of a car, between 1 and 196 models ( the 196 models of Stanford car file), that appears in a photograph with a success rate of more than 70% (using a test file that has not been involved in the training as a valid or training file, "unseen data") and can be implemented on a personal computer.

The project is an adaptation and simplification of the one presented at https://www.kaggle.com/code/hussnain47/car-object-detection-and-classification to consider the detection of cars models

All used packages, if any are missing, can be installed with a simple pip after de error of missing.

For this, the Stanford car file downloaded from https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset/code?resource=download has been used.

When you download and unzip the download file you will see that it contains the directories
archive\cars_train\cars_train with 8144 numbered images. This folder should be copied to the c: directory so that it is accessible by other projects apart from CarsModels_Resnet_Pytorch and also change the name of the archive folder to archiveKaggle so that there is a folder with C:\\archiveKaggle\\cars_train\ \cars_train

Download all the files that accompany the CarsModels_Resnet_Pytorch project in a single folder.

The director file is cardatasettrain.csv downloaded from:
https://github.com/BotechEngineering/StanfordCarsDatasetCSV/tree/main


For the training, images 1 to 7000 will be considered as train/valid making an internal split of 70% train and 30% valid, and from 8000 to 8144 as an independent test of the training process.

You have to create the folder structure that Resnet requires: a directory with 3 folders: train, valid and test. From train and valid hang as many folders as car models are considered named with the code assigned to each model. This structure is created by running the program in the download folder of the project:

CreateDirTrainTestCarsModelss_1_196.py

Next, the structure created in the previous step is filled in by executing:

FillDirKaggleCarsByModels_1_196.py

As part of the downloaded Stanford file is supposed to be located in C:\\archiveKaggle\\cars_train\\cars_train, if not, modify the FillDirKaggleCarsByModels_1_196.py line 39 so that it points to where the Stanford file is located.

Run the train:

TrainCarsModelss_Resnet_Pytorch.py

which comes ready for 20 epoch, designed so that it can run in a reasonable time on a laptop.

Note:An error may occur when detecting that there are classes in the valid that do not have any image. This can be bypassed by copying any image of the corresponding class from the train to the valid so that all folders in the valid have at least one image. Or by unzipping and copying the attached valid.zip in KaggleCarsByModels_1_196 folder


No. epochs: 2,             Training Loss: 0.122             Valid Loss: 4.928             Valid Accuracy: 0.033

No. epochs: 3,             Training Loss: 0.183             Valid Loss: 4.046             Valid Accuracy: 0.118

No. epochs: 4,             Training Loss: 0.211             Valid Loss: 3.313             Valid Accuracy: 0.237

No. epochs: 5,             Training Loss: 0.19             Valid Loss: 2.726             Valid Accuracy: 0.353

No. epochs: 6,             Training Loss: 0.179             Valid Loss: 2.113             Valid Accuracy: 0.465

No. epochs: 7,             Training Loss: 0.146             Valid Loss: 1.873             Valid Accuracy: 0.517

No. epochs: 8,             Training Loss: 0.121             Valid Loss: 1.624             Valid Accuracy: 0.589

No. epochs: 9,             Training Loss: 0.098             Valid Loss: 1.453             Valid Accuracy: 0.621

No. epochs: 10,             Training Loss: 0.081             Valid Loss: 1.405             Valid Accuracy: 0.621

No. epochs: 11,             Training Loss: 0.062             Valid Loss: 1.061             Valid Accuracy: 0.726

No. epochs: 12,             Training Loss: 0.066             Valid Loss: 1.03             Valid Accuracy: 0.733

No. epochs: 13,             Training Loss: 0.064             Valid Loss: 1.008             Valid Accuracy: 0.738

No. epochs: 14,             Training Loss: 0.067             Valid Loss: 1.016             Valid Accuracy: 0.731

No. epochs: 15,             Training Loss: 0.07             Valid Loss: 1.003             Valid Accuracy: 0.735

No. epochs: 16,             Training Loss: 0.076             Valid Loss: 1.005             Valid Accuracy: 0.741

No. epochs: 17,             Training Loss: 0.077             Valid Loss: 1.001             Valid Accuracy: 0.74

No. epochs: 18,             Training Loss: 0.083             Valid Loss: 0.997             Valid Accuracy: 0.74

No. epochs: 19,             Training Loss: 0.09             Valid Loss: 1.014             Valid Accuracy: 0.729

No. epochs: 20,             Training Loss: 0.092             Valid Loss: 0.985             Valid Accuracy: 0.745

Test accuracy of model: 69.89%

>>>


Test with unseen data executing

GuessCarsModelss_Resnet_Pytorch.py


=============================== RESTART: C:\CarsModels_Resnet_Pytorch\GuessCarsModels_Resnet_Pytorch.py ==============================


ERROR 07999.jpg is assigned Model 087Dodge Charger SRT-8 2009  True Model 070Chevrolet Silverado 1500 Regular Cab 2012

HIT 08000.jpg is assigned model 162Mercedes-Benz C-Class Sedan 2012

HIT 08001.jpg is assigned model 149Jeep Wrangler SUV 2012

HIT 08002.jpg is assigned model 161Mercedes-Benz 300-Class Convertible 1993

HIT 08003.jpg is assigned model 131Hyundai Azera Sedan 2012

HIT 08004.jpg is assigned model 030BMW 6 Series Convertible 2007

HIT 08005.jpg is assigned model 003Acura RL Sedan 2012

HIT 08006.jpg is assigned model 140Hyundai Veracruz SUV 2012

HIT 08007.jpg is assigned model 036BMW X5 SUV 2007

ERROR 08008.jpg is assigned Model 006Acura TSX Sedan 2012  True Model 066Chevrolet Monte Carlo Coupe 2007

ERROR 08009.jpg is assigned Model 164Mercedes-Benz S-Class Sedan 2012  True Model 162Mercedes-Benz C-Class Sedan 2012

HIT 08010.jpg is assigned model 017Audi S4 Sedan 2007

HIT 08011.jpg is assigned model 001AM General Hummer SUV 2000

HIT 08012.jpg is assigned model 150Lamborghini Aventador Coupe 2012

HIT 08013.jpg is assigned model 119GMC Canyon Extended Cab 2012

HIT 08014.jpg is assigned model 012Audi 100 Sedan 1994

HIT 08015.jpg is assigned model 040Bentley Continental Flying Spur Sedan 2007

ERROR 08016.jpg is assigned Model 003Acura RL Sedan 2012  True Model 005Acura TL Type-S 2008

HIT 08017.jpg is assigned model 065Chevrolet Malibu Sedan 2007

HIT 08018.jpg is assigned model 006Acura TSX Sedan 2012

HIT 08019.jpg is assigned model 138Hyundai Tucson SUV 2012

HIT 08020.jpg is assigned model 087Dodge Charger SRT-8 2009

HIT 08021.jpg is assigned model 028BMW 3 Series Sedan 2012

HIT 08022.jpg is assigned model 152Lamborghini Gallardo LP 570-4 Superleggera 2012

HIT 08023.jpg is assigned model 141Infiniti G Coupe IPL 2012

HIT 08024.jpg is assigned model 159Mazda Tribute SUV 2011

HIT 08025.jpg is assigned model 119GMC Canyon Extended Cab 2012

ERROR 08026.jpg is assigned Model 176Rolls-Royce Phantom Drophead Coupe Convertible 2012  True Model 024Audi TTS Coupe 2012

HIT 08027.jpg is assigned model 013Audi 100 Wagon 1994

HIT 08028.jpg is assigned model 013Audi 100 Wagon 1994

HIT 08029.jpg is assigned model 106Ford E-Series Wagon Van 2012

ERROR 08030.jpg is assigned Model 173Porsche Panamera Sedan 2012  True Model 099FIAT 500 Abarth 2012

HIT 08031.jpg is assigned model 001AM General Hummer SUV 2000

HIT 08032.jpg is assigned model 034BMW M6 Convertible 2010

HIT 08033.jpg is assigned model 036BMW X5 SUV 2007

HIT 08034.jpg is assigned model 138Hyundai Tucson SUV 2012

HIT 08035.jpg is assigned model 073Chevrolet Tahoe Hybrid SUV 2012

ERROR 08036.jpg is assigned Model 135Hyundai Santa Fe SUV 2012  True Model 187Toyota Camry Sedan 2012

HIT 08037.jpg is assigned model 071Chevrolet Silverado 2500HD Regular Cab 2012

HIT 08038.jpg is assigned model 080Chrysler Sebring Convertible 2010

ERROR 08039.jpg is assigned Model 076Chrysler 300 SRT-8 2010  True Model 147Jeep Liberty SUV 2012

HIT 08040.jpg is assigned model 057Chevrolet Corvette Convertible 2012

HIT 08041.jpg is assigned model 165Mercedes-Benz SL-Class Coupe 2009

HIT 08042.jpg is assigned model 050Buick Verano Sedan 2012

ERROR 08043.jpg is assigned Model 018Audi S4 Sedan 2012  True Model 017Audi S4 Sedan 2007

ERROR 08044.jpg is assigned Model 036BMW X5 SUV 2007  True Model 010Aston Martin Virage Convertible 2012

HIT 08045.jpg is assigned model 139Hyundai Veloster Hatchback 2012

ERROR 08046.jpg is assigned Model 139Hyundai Veloster Hatchback 2012  True Model 188Toyota Corolla Sedan 2012

HIT 08047.jpg is assigned model 079Chrysler PT Cruiser Convertible 2008

ERROR 08048.jpg is assigned Model 059Chevrolet Corvette ZR1 2012  True Model 036BMW X5 SUV 2007

ERROR 08049.jpg is assigned Model 071Chevrolet Silverado 2500HD Regular Cab 2012  True Model 064Chevrolet Malibu Hybrid Sedan 2010

ERROR 08050.jpg is assigned Model 186Toyota 4Runner SUV 2012  True Model 094Dodge Magnum Wagon 2008

HIT 08051.jpg is assigned model 011Aston Martin Virage Coupe 2012

HIT 08052.jpg is assigned model 154Land Rover LR2 SUV 2012

ERROR 08053.jpg is assigned Model 020Audi S5 Coupe 2012  True Model 024Audi TTS Coupe 2012

HIT 08054.jpg is assigned model 117Ford Ranger SuperCab 2011

ERROR 08055.jpg is assigned Model 160McLaren MP4-12C Coupe 2012  True Model 022Audi TT Hatchback 2011

HIT 08056.jpg is assigned model 119GMC Canyon Extended Cab 2012

HIT 08057.jpg is assigned model 143Isuzu Ascender SUV 2008

ERROR 08058.jpg is assigned Model 063Chevrolet Impala Sedan 2007  True Model 032BMW M3 Coupe 2012

HIT 08059.jpg is assigned model 121GMC Terrain SUV 2012

ERROR 08060.jpg is assigned Model 120GMC Savana Van 2012  True Model 145Jeep Compass SUV 2012

HIT 08061.jpg is assigned model 166Mercedes-Benz Sprinter Van 2012

HIT 08062.jpg is assigned model 054Chevrolet Avalanche Crew Cab 2012

ERROR 08063.jpg is assigned Model 159Mazda Tribute SUV 2011  True Model 121GMC Terrain SUV 2012

HIT 08064.jpg is assigned model 132Hyundai Elantra Sedan 2007

ERROR 08065.jpg is assigned Model 149Jeep Wrangler SUV 2012  True Model 148Jeep Patriot SUV 2012

HIT 08066.jpg is assigned model 115Ford GT Coupe 2006

HIT 08067.jpg is assigned model 150Lamborghini Aventador Coupe 2012

HIT 08068.jpg is assigned model 037BMW X6 SUV 2012

HIT 08069.jpg is assigned model 155Land Rover Range Rover SUV 2012

HIT 08070.jpg is assigned model 062Chevrolet HHR SS 2010

ERROR 08071.jpg is assigned Model 182Suzuki Kizashi Sedan 2012  True Model 193Volvo 240 Sedan 1993

HIT 08072.jpg is assigned model 126Honda Accord Coupe 2012

ERROR 08073.jpg is assigned Model 043Bentley Continental Supersports Conv. Convertible 2012  True Model 042Bentley Continental GT Coupe 2012

HIT 08074.jpg is assigned model 063Chevrolet Impala Sedan 2007

HIT 08075.jpg is assigned model 063Chevrolet Impala Sedan 2007

HIT 08076.jpg is assigned model 105Fisker Karma Sedan 2012

ERROR 08077.jpg is assigned Model 184Suzuki SX4 Sedan 2012  True Model 066Chevrolet Monte Carlo Coupe 2007

HIT 08078.jpg is assigned model 182Suzuki Kizashi Sedan 2012

HIT 08079.jpg is assigned model 114Ford Freestar Minivan 2007

HIT 08080.jpg is assigned model 075Chevrolet Traverse SUV 2012

HIT 08081.jpg is assigned model 023Audi TT RS Coupe 2012

HIT 08082.jpg is assigned model 037BMW X6 SUV 2012

HIT 08083.jpg is assigned model 164Mercedes-Benz S-Class Sedan 2012

HIT 08084.jpg is assigned model 130Hyundai Accent Sedan 2012

HIT 08085.jpg is assigned model 010Aston Martin Virage Convertible 2012

HIT 08086.jpg is assigned model 012Audi 100 Sedan 1994

HIT 08087.jpg is assigned model 123Geo Metro Convertible 1993

HIT 08088.jpg is assigned model 190Volkswagen Beetle Hatchback 2012

HIT 08089.jpg is assigned model 129Honda Odyssey Minivan 2012

ERROR 08090.jpg is assigned Model 091Dodge Durango SUV 2007  True Model 090Dodge Dakota Crew Cab 2010

HIT 08091.jpg is assigned model 095Dodge Ram Pickup 3500 Crew Cab 2010

HIT 08092.jpg is assigned model 087Dodge Charger SRT-8 2009

HIT 08093.jpg is assigned model 102Ferrari 458 Italia Coupe 2012

HIT 08094.jpg is assigned model 054Chevrolet Avalanche Crew Cab 2012

HIT 08095.jpg is assigned model 045Bugatti Veyron 16.4 Convertible 2009

HIT 08096.jpg is assigned model 008Aston Martin V8 Vantage Convertible 2012

HIT 08097.jpg is assigned model 055Chevrolet Camaro Convertible 2012

ERROR 08098.jpg is assigned Model 127Honda Accord Sedan 2012  True Model 181Suzuki Aerio Sedan 2007

HIT 08099.jpg is assigned model 116Ford Mustang Convertible 2007

HIT 08100.jpg is assigned model 081Chrysler Town and Country Minivan 2012

HIT 08101.jpg is assigned model 168Nissan 240SX Coupe 1998

HIT 08102.jpg is assigned model 164Mercedes-Benz S-Class Sedan 2012

ERROR 08103.jpg is assigned Model 159Mazda Tribute SUV 2011  True Model 189Toyota Sequoia SUV 2012

HIT 08104.jpg is assigned model 187Toyota Camry Sedan 2012

HIT 08105.jpg is assigned model 085Dodge Caravan Minivan 1997

HIT 08106.jpg is assigned model 151Lamborghini Diablo Coupe 2001

HIT 08107.jpg is assigned model 079Chrysler PT Cruiser Convertible 2008

HIT 08108.jpg is assigned model 060Chevrolet Express Cargo Van 2007

HIT 08109.jpg is assigned model 155Land Rover Range Rover SUV 2012

HIT 08110.jpg is assigned model 186Toyota 4Runner SUV 2012

HIT 08111.jpg is assigned model 170Nissan Leaf Hatchback 2012

HIT 08112.jpg is assigned model 097Dodge Sprinter Cargo Van 2009

HIT 08113.jpg is assigned model 117Ford Ranger SuperCab 2011

ERROR 08114.jpg is assigned Model 088Dodge Charger Sedan 2012  True Model 166Mercedes-Benz Sprinter Van 2012

HIT 08115.jpg is assigned model 160McLaren MP4-12C Coupe 2012

HIT 08116.jpg is assigned model 163Mercedes-Benz E-Class Sedan 2012

HIT 08117.jpg is assigned model 075Chevrolet Traverse SUV 2012

HIT 08118.jpg is assigned model 032BMW M3 Coupe 2012

ERROR 08119.jpg is assigned Model 014Audi A5 Coupe 2012  True Model 067Chevrolet Silverado 1500 Classic Extended Cab 2007

HIT 08120.jpg is assigned model 128Honda Odyssey Minivan 2007

ERROR 08121.jpg is assigned Model 001AM General Hummer SUV 2000  True Model 153Lamborghini Reventon Coupe 2008

HIT 08122.jpg is assigned model 052Cadillac Escalade EXT Crew Cab 2007

ERROR 08123.jpg is assigned Model 058Chevrolet Corvette Ron Fellows Edition Z06 2007  True Model 178Scion xD Hatchback 2012

HIT 08124.jpg is assigned model 040Bentley Continental Flying Spur Sedan 2007

ERROR 08125.jpg is assigned Model 056Chevrolet Cobalt SS 2010  True Model 055Chevrolet Camaro Convertible 2012

ERROR 08126.jpg is assigned Model 132Hyundai Elantra Sedan 2007  True Model 117Ford Ranger SuperCab 2011

HIT 08127.jpg is assigned model 005Acura TL Type-S 2008

HIT 08128.jpg is assigned model 112Ford Fiesta Sedan 2012

HIT 08129.jpg is assigned model 046Bugatti Veyron 16.4 Coupe 2009

HIT 08130.jpg is assigned model 046Bugatti Veyron 16.4 Coupe 2009

HIT 08131.jpg is assigned model 119GMC Canyon Extended Cab 2012

HIT 08132.jpg is assigned model 153Lamborghini Reventon Coupe 2008

ERROR 08133.jpg is assigned Model 007Acura ZDX Hatchback 2012  True Model 003Acura RL Sedan 2012

HIT 08134.jpg is assigned model 124HUMMER H2 SUT Crew Cab 2009


Total hits = 103

Total failures = 33

Accuracy = 75.73529411764706%

References:

https://www.kaggle.com/code/hussnain47/car-object-detection-and-classification

https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset/code?resource=download

https://github.com/BotechEngineering/StanfordCarsDatasetCSV/blob/main/cardatasettest.csv

https://medium.com/analytics-vidhya/top-4-pre-trained-models-for-image-classification-with-python-code-a3cb5846248b

https://github.com/afaq-ahmad/Car-Models-and-Make-Classification-Standford_Car_dataset-mobilenetv2-imagenet-93-percent-accuracy/blob/master/Car_classification.ipynb

https://github.com/ablanco1950/CarsBrands_Inceptionv3
Comparing with this project, there is a similar success rate but now is detailed to model instead a simple brand or make.
