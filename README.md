<p align="center">
  <h1>  Análise e Redução de Ruído em Imagens Coloridas  </h1>
</p>

<p align="center">
  <img src="https://i.pinimg.com/originals/57/29/bf/5729bf63e3627f5b664016036d6a81c3.gif" alt="GIF Animado" width="400"/>
</p>

---

## 🚀 Descrição do Projeto

Este projeto implementa filtros de **redução de ruído** em imagens coloridas, permitindo comparar diferentes técnicas de suavização e preservação de bordas.  

1. **Exercício 1 - Galáxias com ruído**
    - Pasta: `galaxia/` com várias imagens.  
    - Aplicação de filtros acumulativos:
      - **Filtro de média** → ainda mantém ruído de sal.  
      - **Filtro de mediana** → melhora a suavização, mas ainda aparecem ruídos cinza.  
    - Criação de imagens finais combinando todas as imagens filtradas, para análise comparativa.  
2. **Exercício 2 - Capivara com ruído**  
   - Imagem: `capivara_r.jpg`  
   - Análise dos canais RGB e histograma.  
   - Aplicação de filtros:
     - **Filtro adaptativo (NL Means)** → remove quase todo o ruído, preservando texturas.  
     - **Filtro bilateral** → suaviza mantendo bordas.  
     - **Filtro gaussiano** → suaviza toda a imagem, perdendo detalhes.
3. **Exercício 3 - Filtros adaptativo de mediana, mediana simples e média alpha-cortada**  
   - Imagem: colorida (RGB)  
   - Filtros aplicados:
     - **Mediana adaptativa** → ajusta a vizinhança para cada pixel, removendo ruído tipo sal e pimenta.  
     - **Mediana simples** → substitui pixel pela mediana da vizinhança.  
     - **Média alpha-cortada** → ignora os valores extremos antes de calcular a média, reduzindo outliers.  
   - Observação: cada filtro foi aplicado em **cada canal separadamente**, mantendo cores coerentes.  

---
🔹 Filtros Implementados

O projeto aplica uma série de filtros para redução de ruído, distribuídos nos três exercícios:

1. **Exercício 1 – Galáxias (grayscale, várias imagens)**

- Filtro Adaptativo (NL Means): remove quase todo o ruído, preservando texturas.
- Filtro Bilateral: suaviza a imagem mantendo bordas.
- Filtro Gaussiano: suaviza toda a imagem, perdendo detalhes.

2. **Exercício 2 – Capivara com ruído**

- Filtro de Média: suaviza, mas ainda mantém ruído tipo “sal”.
- Filtro de Mediana: reduz ruído, melhor que média, mas ainda há ruídos residuais.

3. **Exercício 3 – Capivara colorida com ruído**

- Filtro Adaptativo de Mediana: ajusta a vizinhança do pixel adaptativamente para remover ruído tipo sal e pimenta.
- Filtro de Mediana Simples: substitui cada pixel pela mediana da vizinhança.
- Filtro de Média Alpha-Cortada: ignora os valores extremos na vizinhança antes de calcular a média, reduzindo outliers.

Além disso, o projeto gera histogramas dos canais RGB ou grayscale, permitindo comparar visualmente o efeito de cada filtro e identificar padrões de ruído.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- OpenCV  
- NumPy  
- Matplotlib   

---

## 📁 Estrutura do Projeto
```yaml
├── capivara_r2.jpg # Imagem com ruído
├── exc_01.py
├── exc_02.py
├── exc_03.py 
├── capivara_r.jpg # Imagem do exercício 1
├── galaxia/ # Pasta com imagens do exercício 2
├── saida_media.jpg # Resultado final do filtro de média
├── saida_mediana.jpg # Resultado final do filtro de mediana
├── READ.me
```

## ⚡ Como Usar

1. Clone este repositório:
```bash
git clone <URL_DO_REPOSITORIO>
```
Instale as dependências:

```bash
pip install opencv-python numpy matplotlib
```
Execute o script principal:

```bash
exc_01.py
exc_02.py
exc_03.py
```
O script exibirá:

Histogramas dos canais RGB

🎯 Objetivo
Comparar visualmente e estatisticamente o efeito de diferentes filtros na remoção de ruído.

Fornecer uma base para estudos de processamento de imagens coloridas e técnicas de redução de ruído adaptativa.

<p align="center">✨ Projeto criado com 💜 por [Seu Nome] ✨</p> ```
