import requests
import traceback

try:
    url = "/AltoroJ/search.jsp?query=<script>alert('Ataque XSS')</script>"
    with open("ipCrosside.txt") as my_file:
        url = my_file.read().strip() + url # Elimina espacios y saltos de línea

    # Enviamos la petición GET con la inyección en el parámetro 'query'
    gr = requests.get(url)

    # Recuperamos el texto de la respuesta
    HTMLText = gr.text

    # Comprobamos si nuestra inyección aparece en la respuesta
    if "<script>alert('Ataque XSS')</script>" in HTMLText:
        # No se sanitizó la entrada, el ataque fue exitoso
        print("Paso el ataque")
        exit(1)
    else:
        # La entrada estaba sanitizada, el ataque falló
        print("Fallo el ataque")
        exit(0)
except Exception as e:
    print("Ocurrió una excepción mientras se ejecutaba el script de ataque:")
    traceback.print_exc()

