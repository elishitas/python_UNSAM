# 1.5
# rebotes.py
#Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa rebotes.py que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.

altura= 100
salto=3/5
rebotes = 1

while rebotes<=10:
	altura= round(altura*3/5,4) #round para redondear a cuatro dígitos
	print(rebotes,altura )
	rebotes = rebotes + 1
