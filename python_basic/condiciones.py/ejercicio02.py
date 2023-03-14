def verificar_contrasena(contrasena_guardada):
    contrasena_usuario = input("Ingresa la contraseña: ")
    if contrasena_guardada.lower() == contrasena_usuario.lower():
        print("La contraseña es correcta")
    else:
        print("La contraseña es incorrecta")

contrasena = "contraseña123"
verificar_contrasena(contrasena)
