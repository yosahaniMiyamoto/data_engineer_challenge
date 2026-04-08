import pandas as pd
import json 

def clean_data():
    with open('data/events.json', 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    filtered_data = df.dropna(subset=['user_id'])
    filtered_data = filtered_data[filtered_data['user_id'] != '']

    filtered_data = filtered_data[filtered_data['timestamp'].apply(lambda x: pd.to_datetime(x, errors='coerce')).notnull()]

    print("1er Filtro de datos: Eliminación de registros con user_id nulo o vacío y timestamp no válido")

    purchase_complete_required_keys = {'amount','payment_method','phone'}
    search_required_keys = {'origin','destination','date'}

    normalized_data = filtered_data[filtered_data['event'].isin(['purchase_complete', 'search'])]

    print("2do Filtro de datos: Filtrado de eventos para incluir solo 'purchase_complete' y 'search'")

    def validate_event(row):
        if row['event'] == 'purchase_complete':
            purchase_props = row['properties'] or {}
            if purchase_props is None or {}: return False
            phoneValue = purchase_props.get('phone')
            if purchase_props.get('payment_method') is None or purchase_props.get('payment_method') == '': return False
            if purchase_props.get('amount') is None or purchase_props.get('amount') == -0 : return False
            return purchase_complete_required_keys.issubset(purchase_props.keys()) and phoneValue and phoneValue.startswith('+52') and len(phoneValue) == 13 and phoneValue[3:].isdigit()
        elif row['event'] == 'search':  
            search_props = row['properties'] or {}
            if search_props is None or {}: return False
            return search_required_keys.issubset(search_props.keys())
    


    normalized_data = normalized_data[normalized_data.apply(validate_event, axis=1)]
    print("3er Filtro de datos: Validación de eventos 'purchase_complete' y 'search' para asegurar que tengan las propiedades requeridas y que el número de teléfono en 'purchase_complete' sea válido")

    normalized_data['user_id'] = normalized_data['user_id'].str.lower()
    normalized_data['event'] = normalized_data['event'].str.lower()


    normalized_data['purchse_amount'] = normalized_data['properties'].apply(lambda x: x.get('amount', 0) if x and isinstance(x, dict) else 0)

    daily_list = normalized_data.groupby(['user_id','event','timestamp']
    ).agg( 
        total_amount = ('purchse_amount', 'sum'),
        total_events = ('event', 'size')
    ).reset_index().sort_values(by='timestamp', ascending=True).sort_values(by='user_id', ascending=True)

    print("Lista de eventos diarios lista para exportar a CSV")

    daily_list.to_csv('data/daily_events.csv', index=False)

    print("Archivo CSV 'daily_events.csv' generado con éxito en la carpeta 'data'")