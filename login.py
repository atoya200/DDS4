import requests
import traceback

try:
    # Leer la URL desde el archivo
    url = "/AltoroJ/doLogin"
    with open("ipLogin.txt") as my_file:
        url = my_file.read().strip() + url  # Elimina espacios y saltos de línea

    # PATH a la que se espera redirigir después del login
    pathEsperado = "AltoroJ/bank/main.jsp"

    # Datos del formulario para la inyección SQL
    data = {
        "uid": "'OR 1 = 1 --",
        "passw": "Atacando",
        "btnSubmit": "Login"
    }

    # Envío de la petición POST
    response = requests.post(url, data=data)

    # Verificar si hubo redirección a la URL esperada
    urlResponse = response.url 

    tmp = urlResponse.split("/")
    tmp = tmp[3:]
    pathRecibido = "/".join(tmp)
    
    print(f"Path recibido: {pathRecibido}")
    
    if pathEsperado == pathRecibido:
        print("Paso el ataque")
        exit(1)
    else:
        print("Fallo el ataque")
        exit(0)

except Exception as e:
    print("Ocurrió una excepción mientras se ejecutaba el script de ataque:")
    traceback.print_exc()
