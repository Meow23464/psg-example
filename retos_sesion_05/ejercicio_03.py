segundos_totales = 288325

dias = segundos_totales // (24 * 3600)
segundos_restantes = segundos_totales % (24 * 3600)
horas = segundos_restantes // 3600
segundos_restantes %= 3600
minutos = segundos_restantes // 60
segundos = segundos_restantes % 60

print(f"{segundos_totales} segundos corresponden a {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos")