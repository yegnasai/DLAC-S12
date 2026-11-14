
import cv2
import os

os.makedirs("images", exist_ok=True)

image_url = "https://ultralytics.com/images/bus.jpg"

import urllib.request

urllib.request.urlretrieve(
    image_url,
    "images/traffic_capture.jpg"
)

image = cv2.imread("images/traffic_capture.jpg")

if image is None:
    print("Image loading failed!")
else:
    print("Traffic sample image saved successfully!")
    cv2.imshow("VisionPort - Traffic Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
