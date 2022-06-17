
# Este realiza varias funciones como son lavar centrifugar y secar previo a eso se definio varias
# reglas que cumplas las funciones de una lavadora 

def Animales():
     # 'Casa' es las locaciones en donde se encuentran la lavadora 
    locacion = input("Casa donde de encuentra la lavadora : \n  zoologico, Campo, Cuidad , Calle\n")
    #Se pide el estado de la lavadora 
    Estado = int(input("Ingrese estado de 1 a 5 : "))
    #Se le asigana un numero a cada estado de la lavadora 
    Perro = 1
    Gato = 2
    Conejo = 3
    Gallina = 4 


    if Perro == 1 : # si la PERrO es igual a 0Ca
        print(" Desea reconocer el animal   " + locacion) #imprima si desea lavar la ropa 
        decide = input(" si / no\n") #decide Si o No 
        if decide == 'si': # si decide si entonces del estado aumentara un cost 
            cost = str(Estado + Perro) # aumenta un costo 
            print("Se reconocio que es un perro: "+locacion) # finaliza e imprime que la ropa se lavo 
            print("su costo aumento y termina en :"+cost)#proceso de lavado termina 
        else: # caso contrario
            cost = str(Estado - Perro) 
            print("no se reconocio que es un perro :"+ locacion) # no se lava la ropa y concatenamos el nombre de la casa 
            print(" su costo se mantiene :"+cost) #proceso finaliza y suma el cost

    if Gato == 2 : # si la gato es igual a 0Ca
        print(" Desea reconocer el animal   " + locacion) #imprima si desea reconocer el animal 
        decide = input(" si / no\n") #decide Si o No 
        if decide == 'si': # si decide si entonces del estado aumentara un cost 
            cost = str(Estado + Gato) # aumenta un costo 
            print("Se reconocio que es un gato: "+locacion) # finaliza e imprime
            print("su costo aumento y termina en :"+cost)#proceso de reconocimeinto termina 
        else: # caso contrario
            cost = str(Estado - Gato) 
            print("no se reconocio que es un gato :"+ locacion) # no reconoce la imagen  
            print(" su costo se mantiene :"+cost) #proceso finaliza y mantiene el costo 


    if Conejo == 3 : # si la Conejo es igual a 0Ca
        print(" Desea reconocer el animal   " + locacion) #imprima si desea reconocer el animal 
        decide = input(" si / no\n") #decide Si o No 
        if decide == 'si': # si decide si entonces del estado aumentara un cost 
            cost = str(Estado + Conejo) # aumenta un costo 
            print("Se reconocio que es un conejo: "+locacion) # finaliza e imprime
            print("su costo aumento y termina en :"+cost)#proceso de reconocimeinto termina 
        else: # caso contrario
            cost = str(Estado - Conejo) 
            print("no se reconocio que es un conejo :"+ locacion) # no reconoce la imagen  
            print(" su costo se mantiene :"+cost) #proceso finaliza y mantiene el costo 

    if Gallina == 4 : # si la galllina es igual a 0Ca
        print(" Desea reconocer el animal   " + locacion) #imprima si desea reconocer el animal 
        decide = input(" si / no\n") #decide Si o No 
        if decide == 'si': # si decide si entonces del estado aumentara un cost 
            cost = str(Estado + Gallina) # aumenta un costo 
            print("Se reconocio que es un gallina: "+locacion) # finaliza e imprime
            print("su costo aumento y termina en :"+cost)#proceso de reconocimeinto termina 
        else: # caso contrario
            cost = str(Estado - Gallina) 
            print("no se reconocio que es un gallina :"+ locacion) # no reconoce la imagen  
            print(" su costo se mantiene :"+cost) #proceso finaliza y mantiene el costo         
        
    
      
Animales()