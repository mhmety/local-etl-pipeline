import pandas as pd
import psycopg2
import os

def load_data_to_postgres():
    csv_path = "processed/latest_bitcoin.csv"
    
    if not os.path.exists(csv_path):
        print("❌ Transform edilmiş CSV dosyası bulunamadı! Lütfen önce transform.py çalıştırın.")
        return
        
    # Temizlenmiş CSV Verisini Oku
    df = pd.read_csv(csv_path)
    row = df.iloc[0] # Satırı alıyoruz
    
    # PostgreSQL Bağlantı Bilgileri
    conn_str = "dbname=crypto_db user=postgres password=426245 host=localhost port=5432"
    
    try:
        conn = psycopg2.connect(conn_str)
        cursor = conn.cursor()
        
        # SQL INSERT Sorgusu (Postgres formatında %s kullanılır)
        insert_query = """
            INSERT INTO bitcoin_prices (asset, price_usd, volume_24h, extracted_at)
            VALUES (%s, %s, %s, %s)
        """
        
        cursor.execute(insert_query, (row['asset'], float(row['price_usd']), float(row['volume_24h']), row['extracted_at']))
        
        # Değişiklikleri kaydet (Commit)
        conn.commit()
        print("🚀 SUCCESS: Data successfully loaded into PostgreSQL Database!")
        
        cursor.close()
        conn.close()
        
    except Exception as e:
        print(f"❌ Veritabanına yükleme başarısız oldu: {e}")

if __name__ == "__main__":
    load_data_to_postgres()