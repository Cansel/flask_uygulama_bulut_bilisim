
# Resmi Python imajını kullanarak temel imaj belirle
FROM python:3.8-slim

# Çalışma dizetini belirle
WORKDIR /app

# Bağımlılıkları kopyala
COPY requirements.txt .

# requirements.txt dosyasındaki paketleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# Mevcut dizindeki tüm dosyaları /app dizinine kopyala
COPY . /app

# Flask'ın çalışacağı port'u aç
EXPOSE 5002

# Çalışma dosyasını belirle
ENV FLASK_APP=uygulama_adınız_uzantısı_olmadan.py

# Container başladığında çalıştırılacak komutu belirle
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5002"]

