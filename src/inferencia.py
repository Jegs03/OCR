import argparse
from pathlib import Path

# Importamos nuestras propias herramientas
from utils import preprocesar_para_ocr
from ocr_pipeline import PipelineOCR

def main():
    # 1. Configurar los argumentos de consola
    parser = argparse.ArgumentParser(description="Script para ejecutar OCR sobre imágenes.")
    parser.add_argument("--imagen", type=str, required=True, 
                        help="Ruta de la imagen o de la carpeta con imágenes.")
    args = parser.parse_args()

    ruta_entrada = Path(args.imagen)
    
    if not ruta_entrada.exists():
        print(f"Error: La ruta proporcionada no existe -> {ruta_entrada}")
        return

    # 2. Inicializar el Pipeline y crear carpeta de salida
    motor_ocr = PipelineOCR()
    
    carpeta_salida = Path("Output")
    carpeta_salida.mkdir(parents=True, exist_ok=True)
    
    # 3. Determinar si es un archivo o una carpeta
    extensiones = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    archivos_a_procesar = []
    
    if ruta_entrada.is_dir():
        archivos_a_procesar = [f for f in ruta_entrada.iterdir() if f.suffix.lower() in extensiones]
        print(f"Se encontraron {len(archivos_a_procesar)} imágenes en la carpeta.")
    elif ruta_entrada.suffix.lower() in extensiones:
        archivos_a_procesar = [ruta_entrada]
    else:
        print("El archivo no tiene una extensión de imagen válida.")
        return

    # 4. Procesar cada imagen
    for archivo in archivos_a_procesar:
        print(f"\n--- Procesando: {archivo.name} ---")
        
        # A. Preprocesar
        img_limpia = preprocesar_para_ocr(archivo)
        
        if img_limpia is None:
            print(f"Fallo al leer la imagen {archivo.name}")
            continue
            
        # B. Extraer Texto
        lineas_texto = motor_ocr.extraer_texto(img_limpia)
        texto_final = "\n".join(lineas_texto)
        
        # C. Mostrar por consola
        print("Texto Extraído:")
        print(texto_final)
        
        # D. Guardar en TXT
        ruta_txt = carpeta_salida / f"{archivo.stem}.txt"
        with open(ruta_txt, "w", encoding="utf-8") as f:
            f.write(texto_final)
        print(f"✅ Guardado en: {ruta_txt}")

if __name__ == "__main__":
    main()