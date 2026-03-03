import requests
import sys

try:
    response = requests.get("https://example.com")
    if response.status_code == 200:
        print("CHECK PASSED")
        sys.exit(0)
    else:
        print("CHECK FAILED")
        sys.exit(1)

except Exception as e:
    print("ERROR:", e)
    sys.exit(1)