from persona import Persona as P
def main():
    P("Juan perez",32,1.75,True).presentarse()
    P("pedro lerenzini",31,14).presentarse()
    elvi= P("elvira romero",32,1.40)
    P("josue said",40,1.78).presentarse()
    elvi.presentarse()
    
   
if __name__=="__main__":
    main()