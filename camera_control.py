import cv2
import datetime
import os

#* Initialize the camera
def initialize_camera():
    cap = cv2.VideoCapture(0)  # 0 default
    if not cap.isOpened():
        print("Error: Could not open camera")
        return None
    return cap

#* Capture image and save it to a path
def capture_image(cap, save_path):
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image")
        return False
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"image_{timestamp}.png"
    cv2.imwrite(os.path.join(save_path, filename), frame)
    return filename

def main():
    save_path = './history/'
    os.makedirs(save_path, exist_ok=True)
    
    # Initialize the camera
    cap = initialize_camera()
    if cap is None:
        return
    
    try:
        # Capture image
        filename = capture_image(cap, save_path)
        print(f"Captured image saved as {filename}")
        if filename:
            return os.path.join(save_path, filename)
    finally:
        # Release the camera
        cap.release()

if __name__ == "__main__":
    main()
