import cv2
import os

# Set person name and directory to save
person_name = "luttfa"
save_dir = f"dataset/{person_name}"
os.makedirs(save_dir, exist_ok=True)

# Start video capture
cap = cv2.VideoCapture(0)

# Try to increase the resolution (optional, may depend on your webcam)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

count = 1
print(" Press 's' to save an image, 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width = frame.shape[:2]

    # Make the rectangle guide larger (cover more face area)
    top = height // 5
    bottom = height - height // 5
    left = width // 4
    right = width - width // 4

    # Draw rectangle on screen
    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    cv2.imshow("Capture Face", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        face_crop = frame[top:bottom, left:right]
        img_path = os.path.join(save_dir, f"{person_name}{count}.jpg")
        cv2.imwrite(img_path, face_crop)
        print(f"[INFO] Saved: {img_path}")
        count += 1

    elif key == ord('q') or count > 5:
        break

cap.release()
cv2.destroyAllWindows()
