#To run it --> python3 main.py -p perfectImage.jpg -n nextImage.jpg

#Imports
import cv2
from skimage.metrics import structural_similarity as ssim
import argparse # --> Will be replaced.
import glob

#Link to [argparse] docs: https://docs.python.org/3/library/argparse.html
argumentParser = argparse.ArgumentParser()
#The image that we will compare the others to.
argumentParser.add_argument("-p", "--perfect", required=True, help="Pass in a perfect product image!")
args = vars(argumentParser.parse_args())

#Link to [cv2] docs: https://docs.opencv.org/4.5.2/index.html
#Store benchmark image and turn to grayscale
perfectImage = cv2.imread(args["perfect"])
grayPerfect = cv2.cvtColor(perfectImage, cv2.COLOR_BGR2GRAY)

#Load images from compare folder and turn to grayscale
#Reference: https://stackoverflow.com/questions/33369832/read-multiple-images-on-a-folder-in-opencv-python/33371454
nextImages = []
for file in glob.glob("./compare/*.jpg"):
    img = cv2.imread(file)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    nextImages.append(img)

#Calculate ISSM [-1;1] (Difference between the images)
# -1 --> 100% different
# 1 -->  100% match
print("The score is between 1 and -1")
print("-1 --> 100% different")
print("1 --> 100% match")
print("")
for img in nextImages:
    score = 0
    diff = 0
    (score, diff) = ssim(grayPerfect, img, full=True)
    diff = (diff * 255).astype("uint8")
    print(score)

