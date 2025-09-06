from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import tensorflow as tf
from skimage import morphology

CORS_ORIGINS = ["http://localhost:3000"]
app = Flask(__name__)
CORS(app, origins=CORS_ORIGINS)

last_matrix = None  # Variable global para guardar la última matriz recibida
model = None  # Variable global para el modelo

# Ruta para validar y guardar la matriz
@app.route('/validate', methods=['POST'])
def validate():
    global last_matrix, model
    data = request.get_json()
    matrix = data.get('matrix')
    # Validar que la matriz sea 28x28 y contenga solo 0 y 1
    if not matrix or len(matrix) != 28 or any(len(row) != 28 for row in matrix):
        return jsonify({'error': 'La matriz debe ser de 28x28'}), 400
    if any(cell not in (0, 1) for row in matrix for cell in row):
        return jsonify({'error': 'La matriz solo debe contener 0 y 1'}), 400


    np_matrix = np.array(matrix, dtype=np.uint8)

    # Eliminar puntos aislados o ruido (remover objetos pequeños)
    matrix_clean = morphology.remove_small_objects(np_matrix.astype(bool), min_size=5, connectivity=2)
    matrix_clean = matrix_clean.astype(np.uint8)
    # Unir los píxeles 1 usando dilatación morfológica
    matrix = morphology.dilation(matrix_clean, morphology.square(1))

    # Centrar el dígito usando el centro de masa
    from scipy.ndimage import center_of_mass, shift
    digit = matrix.astype(np.float32)
    cy, cx = center_of_mass(digit)
    center_y, center_x = 13.5, 13.5
    shift_y, shift_x = center_y - cy, center_x - cx
    digit_centered = shift(digit, shift=(shift_y, shift_x), order=1, mode='constant', cval=0.0)
    matrix = digit_centered


    # Cargar el modelo solo una vez
    if model is None:
        model = tf.keras.models.load_model('modelo_mnist.keras')

    # Preprocesar la matriz para el modelo
    input_matrix = matrix.astype(np.float32)
    input_matrix = input_matrix.reshape(1, 28, 28, 1)
    prediction = model.predict(input_matrix)
    predicted_class = int(np.argmax(prediction))
    return jsonify(predicted_class)

if __name__ == '__main__':
    app.run(debug=True)
