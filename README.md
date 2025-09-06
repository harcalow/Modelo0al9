# Reconocimiento de Dígitos Manuscritos (MNIST)

Este proyecto permite reconocer números manuscritos (0-9) usando un modelo de deep learning entrenado con el dataset MNIST. Incluye un frontend en React para dibujar el número y un backend en Flask que procesa la imagen y devuelve la predicción.

## Estructura del Proyecto

- **Back/**: API en Flask para procesar la imagen y predecir el dígito usando un modelo Keras.
- **Front/app/**: Aplicación React donde el usuario puede dibujar un número y consultar el resultado.
- **modelo/**: Scripts y notebooks para entrenamiento y exportación del modelo MNIST.

## Instalación

### Backend (Flask)
1. Ve a la carpeta `Back`:
   ```bash
   cd Back
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Asegúrate de tener el archivo `modelo_mnist.keras` en la carpeta `Back`.
4. Ejecuta el servidor:
   ```bash
   python app.py
   ```

### Frontend (React)
1. Ve a la carpeta `Front/app`:
   ```bash
   cd Front/app
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Inicia la aplicación:
   ```bash
   npm start
   ```

La app estará disponible en [http://localhost:3000](http://localhost:3000).

## Uso
1. Dibuja un número (0-9) en el recuadro del navegador.
2. Haz clic en el botón para consultar.
3. El backend procesará la imagen y devolverá la predicción del dígito.

## Entrenamiento del Modelo
- El modelo se entrena en el notebook `modelo/entorno_virtual.ipynb` usando Keras y el dataset MNIST.
- El modelo final se exporta como `modelo_mnist.keras` y se utiliza en el backend.

## Requisitos
- Python 3.8+
- Node.js 18+
- Navegador moderno

## Créditos
- Basado en MNIST y tecnologías open source (Flask, React, Keras).

---

Para dudas o mejoras, abre un issue o pull request.
