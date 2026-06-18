# Crypto ETL Pipeline (Local)

Bu projenin amacı, CoinGecko API'sini kullanarak canlı Bitcoin fiyat verilerini otomatik olarak çekmek, Pandas kütüphanesi ile temizleyip yapılandırmak ve ardından yerel bir PostgreSQL veritabanına kaydederek kalıcı hale getirmektir. Proje; veri mühendisliğinin en temel süreçleri olan Extract (Veri Çekme), Transform (Veri Dönüştürme) ve Load (Veri Yükleme) adımlarını uçtan uca simüle eder.

### Gerekli Kütüphaneler

Projenin çalışması için Python ortamına yüklenmesi gereken kütüphaneler:

```bash
pip install requests pandas psycopg2-binary

```

### Veritabanı Hedef Tablo Sorgusu

PostgreSQL (pgAdmin) üzerinde crypto_db veritabanını oluşturduktan sonra verilerin yazılacağı tabloyu hazırlamak için çalıştırılması gereken SQL kodu:

```sql
CREATE TABLE IF NOT EXISTS bitcoin_prices (
    id SERIAL PRIMARY KEY,
    asset VARCHAR(50),
    price_usd NUMERIC(12, 2),
    volume_24h NUMERIC(18, 2),
    extracted_at TIMESTAMP
);

```

### Projeyi Çalıştırma Adımları

Veri hattını başlatmak için proje klasöründe sırasıyla şu komutları çalıştırın:

```bash
python extract.py
python transform.py
python load.py

```

### Veri Kontrol Sorgusu

Verilerin başarıyla yüklenip yüklenmediğini doğrulamak için pgAdmin üzerinde çalıştırabileceğiniz SQL kodu:

```sql
SELECT * FROM bitcoin_prices;

```
