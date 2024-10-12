import requests

# Hacemos una request y le colocamos la inyeccion en el param query
gr = requests.get("http://localhost:8080/AltoroJ/search.jsp?query=<script>alert('Ataque XSS')</script>")

# Recuperamos el texto de la respuesta
HTMLText = gr.text

# Comprobamos si el texto que nos devolvió Altoro con nuestra injección
if("<script>alert('Ataque XSS')</script>" in HTMLText):
	
	# No se sanitizo la entrada, por lo cual nuestra injección fue un exito
	print("Paso el ataque")
	exit(1)

else:
	
	# La entrada estaba sanitizada y por ende no fue exitoso nuestro ataque
	print("Fallo el ataque")
	exit(0)

	

