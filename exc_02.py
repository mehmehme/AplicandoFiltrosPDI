import cv2
import numpy as np
import matplotlib.pyplot as plt

# o histograma de cores aparenta ter uma subida enorme após o 250
# e com as aplicações dos filtros o filtro adaptativo teve o melhor resultado
# tendo removido quase todo o ruído

img = cv2.imread("capivara_r.jpg")  
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converte pra RGB


cores = ['R', 'G', 'B']

#para o histograma fazer do canal de cores
plt.figure(figsize=(12,4))
for i, cor in enumerate(cores):
    plt.subplot(1, 3, i+1)
    plt.title(f"Histograma {cor}")
    plt.hist(img_rgb[..., i].ravel(), bins=256, range=(0,255), color=cor.lower())
plt.show()

# suaviza, mas preserva
img_adapt = cv2.fastNlMeansDenoisingColored(img, None, h=10, hColor=10, templateWindowSize=7, searchWindowSize=21)
# src, dst, altura, cor, tamanho da janela, tamanho da janela de procura

#preserva as bordas, suaviza o resto
img_bilateral = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

#CONTASSSSSSSSSSSSS, suavizar tudo é perder tudo
img_gauss = cv2.GaussianBlur(img, (5,5), 0)

#compara para nós no histograma as imagens bunitinhas uma de cada canto
filtros = [img, img_adapt, img_bilateral, img_gauss]
titulos = ['Original', 'Adaptativo', 'Bilateral', 'Gaussiano']

plt.figure(figsize=(16,8))
for i, (f, t) in enumerate(zip(filtros, titulos)):
    plt.subplot(2, 2, i+1)
    plt.imshow(cv2.cvtColor(f, cv2.COLOR_BGR2RGB))
    plt.title(t)
    plt.axis('off')
plt.show()
