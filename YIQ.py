import cv2
import numpy as np

# Baca gambar
img = cv2.imread("pic1.jpg")

# Konversi gambar dari RGB ke YIQ
img_yiq = np.zeros_like(img)
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        r, g, b = img[i, j]
        y = 0.299*r + 0.587*g + 0.114*b
        i = 0.596*r - 0.274*g - 0.322*b
        q = 0.211*r - 0.523*g + 0.312*b
        img_yiq[i, j] = [y, i, q]

# Tampilkan gambar asli dan gambar hasil konversi
cv2.imshow("Original", img)
cv2.imshow("YIQ", img_yiq)
cv2.waitKey(0)
cv2.destroyAllWindows()
