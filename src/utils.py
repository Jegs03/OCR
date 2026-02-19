import cv2
import numpy as np

def preprocesar_para_ocr(ruta_imagen):
    img = cv2.imread(ruta_imagen)
    if img is None:
        print(f"Error: No se pudo cargar la imagen en {ruta_imagen}")
        return None
    
    # 1. Escala de grises
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    return gris