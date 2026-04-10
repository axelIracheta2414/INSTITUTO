def main():
    enteros = [8,20,6,98,7,32,93,-11]
    acumulador = 0
    
    for entero in enteros:
        acumulador += entero
        #acumulador = acumulador + entero
        promedio = acumulador / len(enteros)
        print(promedio)
if __name__=="__main__":
    main()