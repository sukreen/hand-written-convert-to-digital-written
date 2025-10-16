import cv2
import easyocr
import os
image_path = "test.jpg"
if not os.path.exists(image_path):
    print("❌ Error: Image not found. Check the path:", image_path)
    exit()

img = cv2.imread(image_path)
reader = easyocr.Reader(['en'])  
results = reader.readtext(img)
extracted_text = ""
for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(img, text, (top_left[0], top_left[1]-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)

    extracted_text += text + " "
cv2.imwrite("cnn_processed_output.jpg", img)
print("✅ Processed image saved as 'cnn_processed_output.jpg'")
print("\n📄 Extracted Text:\n")
print(extracted_text.strip())
print("\n✅ Done! (CNN-based OCR)")
