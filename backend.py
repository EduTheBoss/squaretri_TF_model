import os
import time
from PIL import Image
import model_inference
import camera_control
import tkinter as tk
from gui import ImageClassificationApp

def simulate_sensor_trigger():
    # This function simulates the sensor being triggered
    time.sleep(0.5)  # Wait for 5 seconds to simulate sensor delay
    print("Sensor triggered...")
    return True

def display_image_and_classification(image_path, classification):
    # This function displays the image and the classification result
    image = Image.open(image_path)
    image.show()
    print("Classification:", classification)

def main():
    save_path = './data2'
    os.makedirs(save_path, exist_ok=True)
    root = tk.Tk()
    app = ImageClassificationApp(root)
    
    def update_gui():
        # Function to update the GUI with new images and classifications
        triggered = simulate_sensor_trigger()
        if triggered:
            # Capture image
            image_path = camera_control.main()
            if image_path:
                # Classify image
                _, classification = model_inference.process_and_predict(image_path)
                # Update the GUI with the new image and classification
                app.update_display(image_path, classification)

        # Schedule the next update
        root.after(1000, update_gui)  # in milliseconds

    # Start the GUI update loop
    root.after(1000, update_gui)  # Delay start 
    root.mainloop()
if __name__ == "__main__":
    main()
