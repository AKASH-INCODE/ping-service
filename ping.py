import requests

URLS = [
    "https://fraud-frontend-5ag2.onrender.com",
    "https://fraud-detection-backend-zvxe.onrender.com/docs",
]

for url in URLS:
    try:
        r = requests.get(url, timeout=5)
        print(f"[OK] {url}: {r.status_code}")
    except Exception as e:
        print(f"[ERROR] {url}: {e}")
