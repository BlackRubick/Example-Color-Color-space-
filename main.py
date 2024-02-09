import cv2

# Cargar la imagen
image = cv2.imread('figuras.jpeg')

# Convertir de RGB a HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Convertir de RGB a YUV
yuv_image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)

# Convertir de RGB a LAB
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

# Convertir de RGB a LUV
luv_image = cv2.cvtColor(image, cv2.COLOR_BGR2LUV)

# Convertir de RGB a HLS
hls_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

# Concatenar todas las imágenes en una lista vertical
all_images = cv2.vconcat([image, hsv_image, yuv_image, lab_image, luv_image, hls_image])

# Agregar texto para indicar cada espacio de color
text = "Original\nHSV\nYUV\nLAB\nLUV\nHLS"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(all_images, text, (10, 30), font, 1, (255, 255, 255), 2)

# Mostrar la imagen combinada con texto
cv2.imshow('Todas las conversiones de espacio de color', all_images)
cv2.waitKey(0)
cv2.destroyAllWindows()


