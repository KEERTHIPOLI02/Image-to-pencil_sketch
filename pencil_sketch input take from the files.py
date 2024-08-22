import cv2
from tkinter import Tk, filedialog

# Function to get the image file from the user
def upload_image():
    # Hide the main tkinter window
    Tk().withdraw()
    
    # Open a file dialog and ask the user to select an image file
    image_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.tiff *.gif")]
    )
    return image_path

# Get the image path from the user
image_path = upload_image()

if image_path:
    # Reading the image
    image = cv2.imread(image_path)
    cv2.imshow("Given Picture", image)
    cv2.waitKey(0)

    # Converting it into grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Step1 : GrayScale", gray_image)
    cv2.waitKey(0)

    # Inverting the image
    inverted_image = 255 - gray_image
    cv2.imshow("Step 2: Invert", inverted_image)
    cv2.waitKey(0)

    # The pencil sketch
    blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
    inverted_blurred = 255 - blurred
    pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)
    cv2.imshow("Step3: Sketch", pencil_sketch)
    cv2.waitKey(0)

    # Final image
    cv2.imshow("Original Image", image)
    cv2.imshow("Pencil Sketch", pencil_sketch)
    cv2.waitKey(0)

    cv2.destroyAllWindows()
else:
    print("No image selected.")