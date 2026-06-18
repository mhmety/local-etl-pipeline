import requests
import json
import os
from datetime import datetime

def extract_bitcoin_data():
    # Canlı Bitcoin fiyatını veren ücretsiz API
    URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_vol=true"
    
    try:
        response = requests.get(URL)
        response.raise_for_status() # HTTP hatası varsa yakalar
        data = response.json()
        
        # Verinin çekildiği anın zaman damgasını ekliyoruz
        data['bitcoin']['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Ham veriyi 'raw' klasörüne JSON olarak kaydet
        os.makedirs('raw', exist_ok=True)
        file_path = f"raw/bitcoin_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(file_path, 'w') as f:
            json.dump(data, f)
            
        print(f" SUCCESS: Raw data extracted and saved to {file_path}")
        return data
        
    except Exception as e:
        print(f" FAILED to extract data: {e}")
        return None

if __name__ == "__main__":
    extract_bitcoin_data()