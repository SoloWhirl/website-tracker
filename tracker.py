import urllib.request
import urllib.error

url = "https://www.google.com" # يمكنك تغيير الرابط لاحقاً

try:
    response = urllib.request.urlopen(url)
    if response.getcode() == 200:
        print(f"✅ Success! {url} is UP and running.")
except urllib.error.URLError as e:
    print(f"❌ Alert! {url} is DOWN. Reason: {e.reason}")
