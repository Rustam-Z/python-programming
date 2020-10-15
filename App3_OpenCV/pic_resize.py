import cv2
import glob

images = glob.glob("*.jpg")

for image in images:
    img = cv2.imread(image, 1)  # 0=grey pic, 1=rgb normal pic
    re = cv2.resize(img, (int(img.shape[1]/5), int(img.shape[1]/5)))  # giving the new dimensions for the picture
    cv2.imshow("The new image", re)
    cv2.waitKey(500)  # the time for showing the new pictures
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image, re)

# DELETE PICS



