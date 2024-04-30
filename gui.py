import tkinter as tk
from PIL import Image, ImageTk

class ImageClassificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Classification Viewer")
        
        # Label to display the image
        self.image_label = tk.Label(root)
        self.image_label.pack()
        
        # Label to display the classification result
        self.result_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.result_label.pack()

    def update_display(self, image_path, classification):
        try:
            # Load the latest image
            img = Image.open(image_path)
            img = img.resize((500, 500), Image.ANTIALIAS)  # Resize for display purposes
            img_tk = ImageTk.PhotoImage(img)
            
            # Update the image in the label
            self.image_label.config(image=img_tk)
            self.image_label.image = img_tk
            
            # Update the result label
            self.result_label.config(text=f"Classification: {classification}")
            
        except Exception as e:
            print("Failed to update image or result:", str(e))
