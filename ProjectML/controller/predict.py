import tensorflow as tf
import tensorflow_hub as hub
from keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
from flask import request
import numpy as np

def predict():
    model = load_model('Model.h5',
       custom_objects = {
           'KerasLayer': hub.KerasLayer
        }
    )
    # Mengambil file gambar dari request
    gambar = request.files['gambar']
    
    # Membuka gambar menggunakan PIL
    img = Image.open(gambar)
    
    # Mengubah ukuran gambar sesuai dengan input yang diharapkan model 
    # (misalnya 224x224 untuk beberapa arsitektur model)
    img = img.resize((224, 224))
    
    # Mengkonversi gambar ke array dan normalisasi
    img_array = img_to_array(img)
    img_array = img_array / 255.0  # Normalisasi ke rentang 0-1
    img_array = np.expand_dims(img_array, axis=0)  # Menambahkan dimensi batch
    
    # Melakukan prediksi
    prediksi = model.predict(img_array)
    
    # Mendapatkan kelas dengan probabilitas tertinggi
    kelas_prediksi = np.argmax(prediksi, axis=1)[0]
    
    # Opsional: Anda bisa menambahkan mapping kelas jika diperlukan
    # misalnya: 
    label_kelas = [
        'Actinic keratosis',
        'Atopic Dermatitis',
        'Benign keratosis',
        'Dermatofibroma',
        'Melanocytic nevus',
        'Melanoma',
        'Squamous cell carcinoma',
        'Tinea Ringworm Candidiasis',
        'Vascular lesion',
    ]
    nama_kelas = label_kelas[kelas_prediksi]
    
    return {
        'status': 'success', 
        'prediksi': int(kelas_prediksi),
        'nama_kelas': nama_kelas,  # Tambahkan ini jika Anda memiliki mapping kelas
        'probabilitas': float(np.max(prediksi))
    }