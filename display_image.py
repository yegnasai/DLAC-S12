
import cv2

# Read traffic image
image = cv2.imread("images/traffic_capture.jpg")

# Check whether image loaded
if image is None:
    print("Error: Image not found!")
    exit()

print("Image loaded successfully!")
print("Image dimensions:", image.shape)

# Display image
cv2.imshow("VisionPort - Traffic Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image display completed!")
