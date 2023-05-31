import cv2

img = cv2.imread(
    "C:/Users/raiss/Desktop/code_gamesss/PRO_1-1_C104_AtividadeDaProfessora2-main/butterfly.jpg"
)

cv2.imshow("Image de exibição", img)

cv2.waitKey(0)


img2 = cv2.imread(
    "C:/Users/raiss/Desktop/code_gamesss/PRO_1-1_C104_AtividadeDaProfessora2-main/poster.jpg"
)

cv2.imshow("Imagem", img2)

cv2.waitKey(0)
