import  urllib3
import requests
lists = list()
host=urllib3.get_host("http://127.0.0.1:8099/")
status = requests.get("http://127.0.0.1:8099/").status_code
charset = requests.get("http://127.0.0.1:8099/").encoding
cookies = requests.get("http://127.0.0.1:8099/").cookies
headers = requests.get("http://127.0.0.1:8099/").headers
url = requests.get("http://127.0.0.1:8099/").url
codes = requests.codes
history = requests.get("http://127.0.0.1:8099/").history
elapsed = requests.get("http://127.0.0.1:8099/").elapsed
