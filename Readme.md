# Assigment 35


# 1. Color Recognition
+ Write a program with webcam like Assignment 27 - 4 to recognize these colors:

  Red - Green - Blue - Yellow - Orange - Purple - White - Black

## How to Install
Run following commend :
```
pip install -r requirments.txt
```
## How to Run
Execute this command in terminal :
```
python Color_Recognition.py
```

## Results

<img src="Output\Color_Recognition.png" width="350">

-----------------------------------------

# 2. MediaPipe ( Pose landmark detection ) 🏃🏻‍♀️🚶🏻‍♂️🕺🏻
+ The MediaPipe Pose Landmarker task lets you detect landmarks of human bodies in an image or video.

## How to Install
Run following commend :
```
pip install -r requirments.txt
```
## How to Run
Execute this command in terminal :
```
python MediaPipe.py
```

## Results

<img src="Output\MediaPipe.png" width="350">

-----------------------------------------
 
# 3. Convert jpg image to png Transparent Background 

+ Transparent Microsoft logo and remove it's background.Save result with .png format.

## How to Install
Run following commend :
```
pip install -r requirments.txt
```
## How to Run
Execute this command in terminal :
```
python Microsoft_logo_Transparent.py
```

## Input

<img src="Input\Microsoft_logo.jpg" width="350">

## Results

<img src="Output\Microsoft_Transparent.png" width="350">


-----------------------------------------

# 4. Python Imaging Library (PIL)

+ In this exercise we used the pillow library. its a useful library and has some capability that opencv hasn't their.


## -Read a color image with PIL.

### Input
<img src="Input\Rainbow.jpg" width="350">

## -Write a متن فارسی on image.
### Results

<img src="Output\Persian_Text.png" width="350">


## -Calculate 3 histograms and show with plt.
### Results

<img src="Output\Calculate 3 histograms.png" width="350">

## -Equalizes the image histogram.
### Results

<img src="Output\Equalizes.png" width="350">

## -Convert image to gray.
### Results

<img src="Output\Gray.png" width="350">

## -Calculate histogram and show with plt.
### Results

<img src="Output\Calculate histogram and show with plt.png" width="350">

## -Equalizes the gray image histogram.
### Results

<img src="Output\Equalizes the gray image histogram.png" width="350">


## How to Install
Run following commend :
```
pip install -r requirments.txt
```
## How to Run
Execute this command in terminal :
``` 
jupyter nbconvert --to script PIL.ipynb
``` 

-----------------------------------------
 
# 5. Image Encryption and Decryption 🔐 

+ **Image Encryption** is the process of converting a normal image into a cipher image using a secret key in such a way that unauthorized users can't access it.

**Image Decryption** is the process of converting the cipher image into the original image by employing the secret key. Mainly, decryption operation is like encryption operation but applies in reverse order.

* Write `encryptor.py` to get an image, then generate a random secret key and encrypt the image using secret key. Finally save the encrypted image as a `.bmp` file and save the secret key as a `.npy` file.

* Write `decryptor.py` to get a cipher image and a secret key, then convert the cipher image into the original image. Finally save the decrypted image as a `.jpg` file.

* Write `main.py` using PySide6 (Qt for Python) to show input and output in GUI.

## How to Install
Run following commend :
```
pip install -r requirments.txt
```
## How to Run
Execute this command in terminal :
```
python main.py
```

## Input

<img src="Image Encryption and Decryption\Decrypted_image.jpg" width="350">

## Results

<img src="Image Encryption and Decryption\Encrypted_image.png" width="350">


<img src="Image Encryption and Decryption\Decrypted_image.jpg" width="350">
-----------------------------------------










