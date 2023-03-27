# Fungsi untuk konversi CMYK ke CMY
def cmyk_to_cmy(c, m, y, k):
    cmy_c = c * (1 - k) + k
    cmy_m = m * (1 - k) + k
    cmy_y = y * (1 - k) + k
    return cmy_c, cmy_m, cmy_y

# Contoh warna CMYK
cmyk_c = 0.4
cmyk_m = 0.2
cmyk_y = 0.0
cmyk_k = 0.1

# Konversi ke CMY
cmy_c, cmy_m, cmy_y = cmyk_to_cmy(cmyk_c, cmyk_m, cmyk_y, cmyk_k)

# Cetak nilai CM
cv2('Image')
print("Cyan: ", cmy_c)
print("Magenta: ", cmy_m)
print("Yellow: ", cmy_y)
