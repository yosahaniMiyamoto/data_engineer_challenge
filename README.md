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

## Decisiones Técnicas

Implemente el uso de pandas para poder hacer un filtrado y limpieza de datos de forma más sencilla.
Para excluir eventos no requerido especifiqué que "purchase_failed" aunque tiviera las propiedades completas no se considerara
Solo validé "purchase_complete" contaba con todas sus propiedades y validé que el "phone" era válido si iniciaba con "+52" y continaba con 10 dígitos seguidos. 
Así que la longitud total fuera de 13. Para los demás atributos "payment_method" validé que no estuviera vacío o nulo, "amount" que no fuera nulo o < 0
Por último para el evento "search" validé que vinieran sus 3 atributos dentro de las propiedades, pero no puse condiciones si alguno venía vació o nulo ya que consideré
que se podría buscar por uno de los 3 campos, es decir, no los consideré obligatorios para la búsqueda. 

## Si hubiera tenido más tiempo

- Tal vez consultar el que campos eran obligatorios para el evento search y validar de mejor manera. 
- Conectar a BD para el almacenamiento de los resultados y jalar la información obtenida para la API desde ahí.

