import requests

# Agregamos un try - except por si no se llega a hacer la rquest
try:
   # URL del endpoint de la API al a cual atacaremos
	url = "http://localhost:8080/AltoroJ/doLogin"

	# URL a la que la API redirige una vez que el usuario se loguea corrctamente
	urlEsperada = "http://localhost:8080/AltoroJ/bank/main.jsp"

	# Cargamos los datos que se enviarán en la petición POST
	data = {
		"uid": "'OR 1 = 1 --",
		"passw": "Atacando",
		"btnSubmit": "Login"
	}

	# Enviamos la petición POST
	response = requests.post(url, data=data)

	# Comprobamos si la API nos devolvió la URL esperada tras un logeuo correcto
	if(urlEsperada == response.url):

		# La consulta no esta parametrizada o no se sanitizo la entrada, por ende nuestra injección es exitosa
		print("Paso el ataque")
		exit(1)
	else:

		# Se sanitizo la entrada o se menejo una consulta parametrizada, por ende no logramos la injección
		print("Fallo el ataque")
		exit(0)
except:
  print("Ocurrio una excepción mientras se ejecutaba el script de ataque")
	
