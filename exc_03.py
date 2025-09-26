import cv2
import numpy as np
import matplotlib.pyplot as plt

# novamente após 250 há um pulo enorme de cores 
# nesse caso a mediana foi melhor para desfocar o ruído, mas com isso
# desfocou também a imagem

img = cv2.imread("capivara_r2.jpg")  
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # converte pra RGB


cores = ['R', 'G', 'B']

#para o histograma fazer do canal de cores
plt.figure(figsize=(12,4))
for i, cor in enumerate(cores):
    plt.subplot(1, 3, i+1)
    plt.title(f"Histograma {cor}")
    plt.hist(img_rgb[..., i].ravel(), bins=256, range=(0,255), color=cor.lower())
plt.show()


def mediana_adaptativa(img, max_kernel=7):
    img_out = img.copy()
    h, w, c = img.shape
    
    for ch in range(c):  # percorre cada canal
        canal = img[..., ch]
        out = canal.copy()
        for i in range(h):
            for j in range(w):
                k = 3
                while k <= max_kernel:
                    # define vizinhança
                    i_min, i_max = max(i - k//2, 0), min(i + k//2 + 1, h)
                    j_min, j_max = max(j - k//2, 0), min(j + k//2 + 1, w)
                    viz = canal[i_min:i_max, j_min:j_max]
                    
                    med = np.median(viz)
                    min_val = viz.min()
                    max_val = viz.max()
                    
                    if min_val < canal[i,j] < max_val:
                        out[i,j] = canal[i,j]  # pixel ok
                        break
                    else:
                        out[i,j] = med
                        k += 2
        img_out[..., ch] = out
    return img_out.astype(np.uint8)

img_adaptativa = mediana_adaptativa(img_rgb)

img_mediana = cv2.medianBlur(img_rgb, 5)

def media_alpha_cortada(img, k=3, alpha=1):
    pad = k//2
    img_pad = np.pad(img, ((pad,pad),(pad,pad),(0,0)), mode='edge')
    h, w, c = img.shape
    out = np.zeros_like(img, dtype=np.float32)
    
    for ch in range(c):
        canal = img_pad[..., ch]
        for i in range(h):
            for j in range(w):
                viz = canal[i:i+k, j:j+k].flatten()
                viz.sort()
                viz_cortada = viz[alpha:-alpha] if alpha < len(viz)//2 else viz
                out[i,j,ch] = viz_cortada.mean()
    return out.astype(np.uint8)

img_alpha = media_alpha_cortada(img_rgb, k=5, alpha=2)


filtros = [img_rgb, img_adaptativa, img_mediana, img_alpha]
titulos = ['Original', 'Adaptativo', 'Mediana', 'Alpha']

plt.figure(figsize=(16,8))
for i, (f, t) in enumerate(zip(filtros, titulos)):
    plt.subplot(2, 2, i+1)
    plt.imshow(f)
    plt.title(t)
    plt.axis('off')
plt.show()
