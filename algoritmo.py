"busquedad en anchura "

"importar librerias a utilizar"


# accion 
class Accion:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre
 # CLASE ESTADO
class Estado:
    def __init__(self, nombre , acciones):
        self.nombre = nombre
        self.acciones = acciones

    def __str__(self): 
        return self.nombre

#clase problema 

class Problema:
    def __init__(self, estado_inicial, estados_objetivos, acciones):
        self.esatdo_inicial = estado_inicial
        self.estados_objetivos = estados_objetivos
        self.acciones = acciones

    def __str__(self):
        msg = "ESATDO INICIAL: {0}--> Objetivos: {1}"
        return msg.fromat(self.esatdo_inicial.nombre,
                          self.estados_objetivos)

    def es_objetivos(self, estado):   
        return estado in self.estados_objetivos

    def resultado(self, estado , accion):
        if estado.nombre not in self.acciones.keys():
            return None
        acciones_estado = self.acciones[estado.nombre]
        if accion.nombre not in acciones_estado.keys():
            return None
        return acciones_estado[accion.nombre] 

        
# clase nodo 
class Nodo:
    def __init__(self, estado ,accion=None, acciones=None, padre=None):
        self.estado =estado
        self.accion = accion
        self.acciones = acciones
        self.padre = padre
        self.hijo =[]

    def __str__(self):
        return self.estado.nombre

    def expandir(self, problema):
        self.hijos = []
        if not self.acciones:
            if self.estado.nombre not in problema.acciones.keys():
                return self.hijos                                  
            self.acciones = problema.acciones[self.estado.nombre]
        for accion in self.acciones.keys():
            accion_hijo = Accion(accion)
            nuevo_estado = problema.resultado(self.estado, accion_hijo)
            acciones_nuevo ={}
            if nuevo_estado.nombre in problema.acciones.keys():
                acciones_nuevo = problema.accione[nuevo_estado.nombre]
            hijo = Nodo(nuevo_estado,accion_hijo, acciones_nuevo, self)
            self.hijos.append(hijo)
        return self.hijos    


def anchura(problema):
    raiz = crea_nodo_raiz(problema)
    if problema.es_objetivo(raiz.estado):
        return raiz 
    frontera = [raiz,]
    explorados = set()  
    while True:
        if not frontera:
            return None
        nodo = frontera.pop(0)    
        explorados.add(nodo.estado)
        if not nodo.acciones:
           continue
        for nombre_accion in nodo.acciones.keys():
            accion = Accion(nombre_accion)
            hijo = crea_nodo_hijo(problema, nodo, accion)   
            estados_frontera =[nodo.estado for nodo in frontera]
            if(hijo.estado not in explorados and
               hijo.estado not in estados_frontera):
                 if problema.es_objetivo(hijo.estado):
                     return hijo
                 frontera.append(hijo)

" metodo "

def crea_nodo_raiz(problema):
    estado_raiz = problema.estado_inicial
    acciones_raiz ={}
    if estado_raiz.nombre in problema.acciones.keys():
        acciones_raiz = problema.acciones[estado_raiz.nombre]
    raiz = Nodo(estado_raiz, None, acciones_raiz, None)
    return raiz    


def crea_nodo_hijo(problema, padre , accion):
    nuevo_estado = problema.resultado(padre.estado, accion)
    acciones_nuevo = {}
    if nuevo_estado.nombre in problema.acciones.keys():
        acciones_nuevo = problema.acciones[nuevo_estado.nombre]
    hijo = Nodo(nuevo_estado, accion , acciones_nuevo, padre)
    padre.hijos.append(hijo)
    return hijo    


def muestra_solucion(objetivo=None):
    if not objetivo:
        print("no hay solucion")
        return
    nodo = objetivo
    while nodo:
        msg ="estado: {0}"
        print(msg.format(nodo.estado.nombre))
        if nodo.accion:
           msg = "<----------{0}-------"
           print(msg.format(nodo.accion.nombre)) 
        nodo = nodo.padre


if __name__== '__main__':
    accN = Accion('N')
    accS = Accion('S')
    accE = Accion('E')
    accO = Accion('O')
    accNe = Accion('Ne')
    accNo = Accion('No')
    accSe = Accion('Se')
    accSo = Accion('So')


    lanoi = Estado('lanoi'),[accNe]
    nahoi= Estado('Nahoi'),[accNe,accN]
    run = Estado('run'),[accNe,accN]
    milos = Estado('milos'),[accNe,accN]
    gido = Estado('gido'),[accNe,accN]
    kuart = Estado('kuart'),[accNe,accN]
    boom = Estado('boom'),[accNe,accN]
    gorun = Estado('gorun'),[accNe,accN]
    shipos = Estado('shipos'),[accNe,accN]
    nookos = Estado('nokos'),[accNe,accN]
    paris = Estado('paris'),[accNe,accN]
    kamin= Estado('kamin'),[accNe,accN]
    tarios = Estado('tarios'),[accNe,accN]
    perana = Estado('perana'),[accNe,accN]
    kadan = Estado('kadan'),[accNe,accN]
    tawa = Estado('tawa'),[accSo,accSe]
    teer = Estado('teer'),[accSo,accSe]
    noria = Estado('roria'),[accNo,accSo,accE]
    kokos = Estado('kokos'),[accO]

    acciones = {'lanoi':{'Ne':nahoi},
                'nahoi':{'so':lanoi,
                         'no':run,
                         'ne':milos},
                'run':{'No':gido,
                        'ne':kuart,
                        'e':milos,
                        'se':nahoi},
                'milos':{'0':run,
                        'so':nahoi,
                        'n':kadan },
                'gido':{ 'n':nookos,
                          'e':kuart,
                          'se':run},
                'kuart':{ '0':gido,
                          'so':run,
                          'ne':boom},

                'bom':{ 'n':gorun,
                          'so':kuart},

                'gorun':{ 'o':shipos,
                          's':boom},         

                'shipos':{ 'o':shipos,
                          'e':boom},    

                'nokos':{ 'no':paris,
                           's':gido,
                          'e':shipos},
                          
                'paris':{ 'no':kamin,
                           's0':nookos},
                
                'kamin':{ 'se':paris,
                           's0':tawa,
                          '0':tarios}, 
                                                                    
                'tarios':{ 'o':kamin,
                           'n0':tawa,
                           'ne':noria,
                          'e':perana}, 

                 'perana':{ 'o':tarios,
                           's':kadan},

                 'kadan':{ 'o':perana,
                           's':milos},
                                                                                  
                 'tawa':{ 'so': kamin,
                           'se':tarios,
                          'ne':teer},  

                 'theer':{ 'so':tawa,
                           'se':noria},         

                  'roria':{ 'no': teer,
                           'so':tarios,
                          'e': kokos}, 
                  'kokos':{'o':noria}}            
               
                           
        
    objetivo_1 = [kokos]
    problema_1 = Problema(lanoi, objetivo_1)







