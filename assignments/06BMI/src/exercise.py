def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg: "))
    altura = float(input("Altura en m: "))
    indice = peso / altura**2

    if peso<=0 or altura<=0:
        print("Revisa tus datos, alguno de ellos es erróneo.")
    elif indice<20:
        print("PESO BAJO")
    elif 20<=indice and indice<25:
        print("NORMAL")
    elif 25<=indice and indice<30:
        print("SOBREPESO")
    elif 30<=indice and indice<40:
        print("OBESIDAD")
    elif 40<=indice:
        print("OBESIDAD MORBIDA")
    else:
        print("Revisa tus datos, alguno de ellos es erróneo.")

if __name__=='__main__':
    main()