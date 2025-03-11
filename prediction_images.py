import os
from ultralytics import YOLO
import cv2

# Specify the path to your sample images directory
sample_images_dir = 'C:/Users/PDL Local User/Pictures/images1.jpg'  # Update with the correct path

# Check if the directory exists
if not os.path.exists(sample_images_dir):
    print(f"Error: Directory '{sample_images_dir}' does not exist.")
    exit()

# Initialize YOLO model
model_path = os.path.join('.', 'runs', 'detect', 'train2', 'weights', 'last.pt')
model = YOLO(model_path)

threshold = 0.5

# Iterate over each image in the directory
for filename in os.listdir(sample_images_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):  # Adjust for the types of images you have
        image_path = os.path.join(sample_images_dir, filename)
        frame = cv2.imread(image_path)
        if frame is None:
            print(f"Error: Could not read image '{image_path}'.")
            continue

        H, W, _ = frame.shape

        # Perform object detection
        results = model(frame)[0]

        # Process results and draw bounding boxes
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
                cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 5, cv2.LINE_AA)

        # Display or save annotated image (optional)
        cv2.imshow('Object Detection Result', frame)
        cv2.waitKey(0)  # Wait for any key to be pressed to continue to the next image

cv2.destroyAllWindows()
