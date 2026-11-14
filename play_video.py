
import cv2

# Load traffic video
video = cv2.VideoCapture("input/traffic.mp4")

if not video.isOpened():
    print("Error: Could not open video!")
    exit()

print("Traffic video loaded successfully!")

# Get video information
fps = video.get(cv2.CAP_PROP_FPS)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("FPS:", fps)
print("Resolution:", width, "x", height)

delay = max(1, int(1000 / fps)) if fps > 0 else 25

while True:
    ret, frame = video.read()

    if not ret:
        print("Video playback completed!")
        break

    cv2.imshow("VisionPort - Traffic Video", frame)

    # Press Q to stop
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        print("Video stopped by user.")
        break

video.release()
cv2.destroyAllWindows()
