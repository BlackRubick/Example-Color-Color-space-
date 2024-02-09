import cv2

# Cargar la imagen
image = cv2.imread('figuras.jpeg')

# Convertir de RGB a HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Mostrar la imagen original y la imagen en el espacio de color HSV
cv2.imshow('Original', image)
cv2.imshow('HSV', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

