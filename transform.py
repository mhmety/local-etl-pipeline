import pandas as pd
import json
import glob
import os

def transform_latest_data():
    # 'raw' klasöründeki en son oluşturulan JSON dosyasını otomatik bulur
    list_of_files = glob.glob('raw/*.json')
    if not list_of_files:
        print(" No raw data found to transform.")
        return None
        
    latest_file = max(list_of_files, key=os.path.getctime)
    
    with open(latest_file, 'r') as f:
        raw_data = json.load(f)
        
    # Karmaşık JSON yapısını düzleştirip temiz bir satır haline getiriyoruz
    bitcoin_info = raw_data['bitcoin']
    
    df = pd.DataFrame([{
        'asset': 'Bitcoin',
        'price_usd': float(bitcoin_info['usd']),
        'volume_24h': float(bitcoin_info['usd_24h_vol']),
        'extracted_at': bitcoin_info['timestamp']
    }])
    
    # Temizlenmiş veriyi 'processed' klasörüne CSV olarak kaydet
    os.makedirs('processed', exist_ok=True)
    processed_path = "processed/latest_bitcoin.csv"
    df.to_csv(processed_path, index=False)
    
    print(f" SUCCESS: Data transformed and saved to {processed_path}")
    print(df) # Ekranda tabloyu görelim
    return df

if __name__ == "__main__":
    transform_latest_data()