# Función para simular el inicio de sesión
def iniciar_sesion():
    print("Inicio de sesión exitoso.")
    return True

# Función principal
def main():
    print("Bienvenido a la página web.")
    sesion_iniciada = False
    
    # Intentar iniciar sesión hasta que el usuario lo cancele o inicie sesión correctamente
    while not sesion_iniciada:
        opcion = input("¿Desea iniciar sesión? (s/n): ").lower()
        if opcion == 's':
            sesion_iniciada = iniciar_sesion()
        elif opcion == 'n':
            print("Cancelado. No se ha iniciado sesión.")
            break
        else:
            print("Opción no válida. Por favor, ingrese 's' para iniciar sesión o 'n' para cancelar.")

    # Verificar si el usuario ha iniciado sesión
    if sesion_iniciada:
        print("¡Bienvenido! Ahora puedes acceder a la página web.")
    else:
        print("No has iniciado sesión. No puedes acceder a la página web.")

if __name__ == "__main__":
    main()
