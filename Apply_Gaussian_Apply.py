blur = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow("Blurred", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
