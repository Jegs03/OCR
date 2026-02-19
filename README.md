# proyecto OCR: Extracción de Texto Manuscrito

## 1. Descripción General
Este proyecto implementa un *pipeline* completo de Reconocimiento Óptico de Caracteres (OCR) diseñado específicamente para extraer **texto manuscrito**. 

El principal desafío de este tipo de imágenes son las sombras irregulares y las líneas horizontales del papel, las cuales confunden a los motores de OCR tradicionales. Para solucionarlo, este proyecto utiliza **OpenCV** para aplicar un filtro de escala de grises y **EasyOCR** para la extracción final del texto mediante Inteligencia Artificial.

## 2. Requisitos del Sistema
* **Sistema Operativo:** Linux, Windows o macOS.
* **Python:** Versión 3.8 a 3.12 
* **RAM:** Mínimo 4GB (Se recomiendan 8GB).
* **GPU (Opcional):** El sistema funciona perfectamente en CPU, pero se acelerará considerablemente si cuentas con una tarjeta gráfica NVIDIA compatible con CUDA.

## 3. Instrucciones de Instalación

Sigue estos pasos en tu terminal para configurar el entorno:

**Paso 1: Clonar o descargar el repositorio**
(Si usas git)
```bash
git clone https://github.com/Jegs03/OCR
cd proyecto-ocr
```

**Paso 2: Crear un entorno virtual (Recomendado)**
Esto evitará conflictos con otras librerías de tu sistema.
```bash
python -m venv venv
# Activar en Linux/macOS:
source venv/bin/activate
# Activar en Windows:
venv\Scripts\activate
```

**Paso 3: Instalar dependencias**
Asegúrate de tener tu instalador pip actualizado y luego instala las librerías necesarias:
```bash
pip install --upgrade pip
pip install opencv-python numpy easyocr
```

## 4. Estructura del Repositorio
```
proyecto_ocr/
│
├── README.md            <-- Este archivo de documentación
├── Output/              <-- Carpeta generada automáticamente con los resultados (.txt)
└── src/
    ├── utils.py         <-- Funciones de preprocesamiento (OpenCV)
    ├── ocr_pipeline.py  <-- Lógica del motor OCR (EasyOCR)
    └── inferencia.py    <-- Script principal para ejecución por consola
```

## 5. Instrucciones de Uso

El punto de entrada del programa es el script inferencia.py. Puedes pasarle la ruta de una imagen individual o la ruta de una carpeta entera que contenga varias imágenes.

Para procesar una sola imagen:
Bash
```bash
python src/inferencia.py --imagen /ruta/absoluta/o/relativa/imagen.jpeg
```
Para procesar toda una carpeta (procesamiento por lotes):
```bash
python src/inferencia.py --imagen /ruta/a/la/carpeta/de/imagenes/
```
Los resultados se mostrarán en la consola y se guardarán automáticamente en la carpeta Output/ con el mismo nombre de la imagen original, pero con extensión .txt.


## 7. Limitaciones y Posibles Mejoras

Limitaciones actuales:

    Letras ligadas: EasyOCR puede tener dificultades si la escritura es cursiva y las letras están extremadamente unidas.

    Ángulos extremos: Si la foto se tomó con una perspectiva muy inclinada (no paralela a la hoja), la eliminación de líneas horizontales mediante morfología en utils.py perderá eficacia, ya que asume que las líneas son mayormente rectas y horizontales.

Posibles mejoras futuras:

    Integración de PaddleOCR: Una vez que el entorno o las versiones de Python se estabilicen, migrar a PaddleOCR o TrOCR (Microsoft) podría mejorar la precisión específica en manuscritos.

    Corrección de perspectiva: Añadir un paso en utils.py que detecte los bordes de la hoja y aplique una "transformación de perspectiva" (Deskew) antes de binarizar la imagen.

    Post-procesamiento con LLM: Pasar el texto extraído por un modelo de lenguaje ligero para corregir pequeños errores ortográficos causados por la lectura del OCR.