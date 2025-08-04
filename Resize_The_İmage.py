resized = cv2.resize(image, (300, 300))  # Width, Height
cv2.imshow("Resized", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
