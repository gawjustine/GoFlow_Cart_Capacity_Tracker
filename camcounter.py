from ultralytics import YOLO
import cv2
import time

# Load your YOLOv8 head model
model = YOLO("nano.pt")  # or "medium.pt"

# Open webcam
cap = cv2.VideoCapture(0)  # 0 = default webcam

fps = 2  # how many frames per second to process
interval = 1 / fps  # seconds between frames
last_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Limit frame rate
    if time.time() - last_time < interval:
        continue
    last_time = time.time()

    # Run head detection
    results = model(frame, conf=0.5)  # optional threshold tweak
    head_count = 0

    for r in results:
        for box in r.boxes:
            head_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # Send/update head count
    print(f"Heads detected this frame: {head_count}")

    # Optional: show the frame
    cv2.imshow("Head Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()