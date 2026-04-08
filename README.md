## Challenge Data Engineer

## Descripción
Pipeline que procesa diferentes eventos desde archivo JSON, genera CSV con los datos filtrados y limpios.
Presenta un API con FastAPI para consultar la cantidad de eventos por día. 

## Tecnologías
- Python
- Pandas
- FastAPI

## Archivos utilizados
Dentro de la carpeta "data" vienen dos archivos:
- events.json que me brindaron en el correo y utilice para prueba
- daily_events.csv que se genera al ejecutar el sistema ETL 


## Cómo ejecutar

1. Crear entorno virtual:
   python -m venv venv

2. Activar entorno:
   venv\Scripts\activate

3. Instalar dependencias:
   pip install -r requirements.txt

4. Ejecutar ETL:
   python src/main.py

5. Levantar API:
   uvicorn src.apis.get_daily_stats:app --reload


