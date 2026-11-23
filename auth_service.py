def validar_credenciales(usuario, clave):
    return usuario == "admin" and clave == "1234"

print(validar_credenciales("admin", "1234"))
