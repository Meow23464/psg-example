def puerta_abierta(luz1, luz2):
    return (luz1 and luz2) or (not luz1 and not luz2)

print("Tabla de verdad para la afirmación:")
print("La puerta sólo debe abrirse cuando las dos luces están apagadas o las dos están encendidas.")
print("Luz1 | Luz2 | Puerta Abierta")
for luz1 in [0, 1]:
    for luz2 in [0, 1]:
        print(f"  {luz1}   |  {luz2}  |     {puerta_abierta(luz1, luz2)}")
