from ultralytics import YOLO
import cv2
import time

# Load your YOLOv8 head model
model = YOLO("nano.pt")  # or "medium.pt"

# Open webcam
cap = cv2.VideoCapture(0)  # 0 = default webcam

def get_count():
    ret, frame = cap.read()
    if not ret:
        return 0

    # Run head detection
    results = model(frame, conf=0.5)  # optional threshold tweak
    head_count = 0

    for r in results:
        for box in r.boxes:
            head_count += 1
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return head_count
    # Send/update head count
    # print(f"Heads detected this frame: {head_count}")
    # Optional: show the frame
    # cv2.imshow("Head Detection", frame)


def cleanup():
    cap.release()
    cv2.destroyAllWindows()
