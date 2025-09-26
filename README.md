<p align="center">
  <h1>🖼️ Análise e Redução de Ruído em Imagens Coloridas 🖼️</h1>
</p>

<p align="center">
  <img src="https://i.pinimg.com/originals/57/29/bf/5729bf63e3627f5b664016036d6a81c3.gif" alt="GIF Animado" width="400"/>
</p>

---

## 🚀 Descrição do Projeto

Este projeto implementa filtros de **redução de ruído** em imagens coloridas, permitindo comparar diferentes técnicas de suavização e preservação de bordas.  

Os filtros implementados incluem:  

- **Filtro Adaptativo de Mediana**: ajusta a vizinhança do pixel adaptativamente para remover ruído tipo sal e pimenta.  
- **Filtro de Mediana Simples**: substitui cada pixel pela mediana da vizinhança.  
- **Filtro de Média Alpha-Cortada**: ignora os valores extremos na vizinhança antes de calcular a média, reduzindo outliers.  

O projeto também gera **histogramas dos canais RGB** para analisar visualmente os padrões de ruído antes e depois da filtragem.  

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
├── filtros.py # Código principal com os filtros
├── resultados/ # Pasta para salvar imagens filtradas (opcional)
└── README.md
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
python filtros.py
```
O script exibirá:

A imagem original

Imagens filtradas: Adaptativa, Mediana, Alpha-Cortada

Histogramas dos canais RGB

🎯 Objetivo
Comparar visualmente e estatisticamente o efeito de diferentes filtros na remoção de ruído.

Fornecer uma base para estudos de processamento de imagens coloridas e técnicas de redução de ruído adaptativa.

<p align="center">✨ Projeto criado com 💜 por [Seu Nome] ✨</p> ```
