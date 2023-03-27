import cv2

# Load the image
img = cv2.imread('pic1.jpg')

# Convert YIQ to RGB
yiq_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
rgb_img = cv2.cvtColor(yiq_img, cv2.COLOR_YCrCb2RGB)

# Save the output image
cv2.imwrite('output_image.png', rgb_img)
cv2.imshow('yiq image', yiq_img)
cv2.imshow('rgb image', rgb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()