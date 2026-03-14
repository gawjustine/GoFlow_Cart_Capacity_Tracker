# # V1. PPL COUNTER
# from ultralytics import YOLO
# import cv2

# # load model
# # model = YOLO("yolov8n.pt")
# model = YOLO("nano.pt")
# print(model.names)

# # load image
# image = cv2.imread("frame.jpg")

# # run detection
# results = model(image)

# count = 0

# for result in results:
#     for box in result.boxes:
#         cls = int(box.cls[0])

#         if model.names[cls] == "person":
#             count += 1

#             x1, y1, x2, y2 = map(int, box.xyxy[0])
#             cv2.rectangle(image,(x1,y1),(x2,y2),(0,255,0),2)

# print("People detected:", count)

# cv2.imshow("result", image)
# cv2.waitKey(0)

# ==============================
# V2. HEAD COUNTER
from ultralytics import YOLO
import cv2

model = YOLO("nano.pt")
# model = YOLO("crowdhuman_yolov5m.pt")

image = cv2.imread("frame.jpg")

results = model(image)

head_count = 0

for result in results:
    for box in result.boxes:
        head_count += 1

        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(image, (x1,y1), (x2,y2), (0,255,0), 2)

print("Heads detected:", head_count)

cv2.putText(image, f"Heads: {head_count}",
            (20,40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0,0,255),
            2)

cv2.imshow("Head Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()