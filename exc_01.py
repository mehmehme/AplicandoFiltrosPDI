import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# a imagem com média fica ainda com bastante ruído de sal
#já a de mediana aparenta ter melhor resultado, mas apresenta ainda muitos ruídos cinza

# Caminho da pasta com as imagens
pasta = "galaxia"

# Lista todos os arquivos da pasta
arquivos = [f for f in os.listdir(pasta) if f.endswith(('.jpg'))]

# Acumula as imagens
soma_media = None
soma_mediana = None
cont = 0

for arquivo in arquivos:
    caminho = os.path.join(pasta, arquivo)
    img = cv2.imread(caminho, cv2.IMREAD_GRAYSCALE)

    # Aplica filtros
    img_media = cv2.blur(img, (5,5))
    img_mediana = cv2.medianBlur(img, 5)

    # Inicializa as somas na primeira rodada
    if soma_media is None:
        soma_media = np.zeros_like(img, dtype=np.float32)
        soma_mediana = np.zeros_like(img, dtype=np.float32)

    # Acumula
    soma_media += img_media
    soma_mediana += img_mediana
    cont += 1

# Faz a média final
media_final = (soma_media / cont).astype(np.uint8)
mediana_final = (soma_mediana / cont).astype(np.uint8)

# Salva as imagens finais
cv2.imwrite("saida_media.jpg", media_final)
cv2.imwrite("saida_mediana.jpg", mediana_final)

# imagem para comparação
img = cv2.imread("galaxia/galaxia_0.jpg", cv2.IMREAD_GRAYSCALE)

# Plota histogramas
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.title("Original")
plt.hist(img.ravel(), bins=256, range=(0,255), color='gray')

plt.subplot(1,3,2)
plt.title("Filtro Média")
plt.hist(media_final.ravel(), bins=256, range=(0,255), color='gray')

plt.subplot(1,3,3)
plt.title("Filtro Mediana")
plt.hist(mediana_final.ravel(), bins=256, range=(0,255), color='gray')

plt.show()
