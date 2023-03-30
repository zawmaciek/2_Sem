import cv2
import numpy as np
from keras.models import load_model

# Load the saved model
model = load_model('classifier.h5')

# Define the dimensions of the input image
img_width, img_height = 224, 224

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Capture an image from the webcam
    ret, frame = cap.read()

    # Preprocess the image
    img = cv2.resize(frame, (img_width, img_height))
    img = img.astype('float32') / 255.0

    # Make a prediction on the preprocessed image
    pred = model.predict(np.expand_dims(img, axis=0))

    # Get the predicted probability value
    prob = pred[0][0]

    # Interpret the predictions
    if prob <= 0.5:
        label = "Real"
        color = (0, 255, 0)  # Green color for real images
    else:
        label = "Fake"
        color = (0, 0, 255)  # Red color for fake images

    # Display the captured image
    cv2.imshow("Image", frame)

    # Draw the predicted label on the image
    cv2.putText(frame, label, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 2)

    # Show the image with the predicted label
    cv2.imshow("Predicted Image", frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the windows
cap.release()
cv2.destroyAllWindows()
