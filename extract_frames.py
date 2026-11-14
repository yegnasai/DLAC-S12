
import cv2
import os

# Create frames folder
os.makedirs("frames", exist_ok=True)

# Load traffic video
video = cv2.VideoCapture("input/traffic.mp4")

if not video.isOpened():
    print("Error: Cannot open traffic video!")
    exit()

frame_count = 0
saved_count = 0

print("Extracting video frames...")

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Save every 30th frame
    if frame_count % 30 == 0:

        filename = f"frames/frame_{saved_count:04d}.jpg"

        cv2.imwrite(filename, frame)

        saved_count += 1

    frame_count += 1

video.release()

print("Frame extraction completed!")
print("Total frames processed:", frame_count)
print("Frames saved:", saved_count)
