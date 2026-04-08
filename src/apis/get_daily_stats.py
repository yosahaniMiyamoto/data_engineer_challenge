import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df = pd.read_csv('data/daily_events.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')


@app.get("/hello")
def get_hello():
    return {"message": "¡Hola! Esto es una prueba."}

@app.get("/daily_stats/")
def get_daily_stats(date: str):
    try:
        date = pd.to_datetime(date, errors='coerce')
        if pd.isna(date):
            return {"error": "Fecha no válida. Asegúrate de usar el formato YYYY-MM-DD."}
        
        daily_stats = df[df['timestamp'].dt.date == date.date()]
        
        if daily_stats.empty:
            return {"message": f"No se encontraron eventos para la fecha {date.date()}."}
        
        data_daily_stats = {
            'total_users': daily_stats['user_id'].nunique(),
            'total_searches': daily_stats[daily_stats['event'] == 'search'].shape[0],
            'total_purchases': daily_stats[daily_stats['event'] == 'purchase_complete'].shape[0],
            'total_purchase_amount': daily_stats[daily_stats['event'] == 'purchase_complete']['total_amount'].sum() 
        }
        df_daily_stats = pd.DataFrame([data_daily_stats])
                
        return df_daily_stats.to_dict(orient='records')
    
    except Exception as e:
        return {"error": str(e)}
