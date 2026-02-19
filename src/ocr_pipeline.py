import easyocr
import numpy as np

class PipelineOCR:
    def __init__(self):
        print("Cargando motor EasyOCR...")
        # Inicializamos el lector en español. 
        # Ponemos gpu=False por defecto para evitar errores si no tienes tarjeta gráfica configurada.
        self.reader = easyocr.Reader(['es'], gpu=False, verbose=False)

    def extraer_texto(self, imagen_preprocesada):
        """Recibe una imagen (numpy array) y devuelve una lista con las líneas de texto."""
        if imagen_preprocesada is None:
            return []
            
        # EasyOCR lee directamente el numpy array.
        # detail=0 hace que nos devuelva directamente una lista de textos limpios,
        # ignorando las coordenadas de las cajas y los puntajes de confianza.
        textos_extraidos = self.reader.readtext(imagen_preprocesada, detail=0)
                
        return textos_extraidos