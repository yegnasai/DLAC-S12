
import cv2
from ultralytics import YOLO

print("Loading YOLO model...")

model = YOLO("yolov8n.pt")

video = cv2.VideoCapture("input/traffic.mp4")

if not video.isOpened():
    print("Error opening video!")
    exit()

vehicle_classes = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck"
}

print("Starting traffic density analysis...")

total_frames = 0
max_vehicles = 0

while True:

    ret, frame = video.read()

    if not ret:
        break

    results = model(frame, verbose=False)

    vehicle_count = 0

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            if class_id in vehicle_classes and confidence > 0.35:

                vehicle_count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                name = vehicle_classes[class_id]

                label = f"{name} {confidence * 100:.1f}%"

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                cv2.putText(
                    frame,
                    label,
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    # Calculate traffic density
    if vehicle_count <= 5:
        density = "LOW"
        color = (0, 255, 0)

    elif vehicle_count <= 12:
        density = "MEDIUM"
        color = (0, 255, 255)

    else:
        density = "HIGH"
        color = (0, 0, 255)

    total_frames += 1
    max_vehicles = max(max_vehicles, vehicle_count)

    # Display vehicle count
    cv2.putText(
        frame,
        f"Vehicle Count: {vehicle_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (255, 255, 255),
        2
    )

    # Display traffic density
    cv2.putText(
        frame,
        f"Traffic Density: {density}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        color,
        2
    )

    cv2.imshow(
        "VisionPort - Traffic Density Monitoring",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

print("\nTraffic Density Analysis Completed!")
print("Total frames processed:", total_frames)
print("Maximum vehicles in one frame:", max_vehicles)

if max_vehicles <= 5:
    print("Maximum observed traffic density: LOW")
elif max_vehicles <= 12:
    print("Maximum observed traffic density: MEDIUM")
else:
    print("Maximum observed traffic density: HIGH")
