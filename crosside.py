import requests

# Hacemos una request y le colocamos la inyeccion
gr = requests.get("http://localhost:8080/AltoroJ/search.jsp?query=<script>alert('Ataque XSS')</script>")

# Recuperamos el texto y deberia de contener el texto que pasamos
HTMLText = gr.text

success = "<script>alert('Ataque XSS')</script>" in HTMLText

if(success):
	print("Paso el ataque")
	exit(1)

else:
	print("Fallo el ataque")
	exit(0)

	

