# Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña. 
# Crea un objeto usando la clase.
class Usuario:
  def __init__(self, nombre, contraseña):
    self.__nombre = nombre
    self.__contraseña = contraseña

# Creamos un objeto usuario
usuario1 = Usuario("Juan", "123456789")

print(usuario1.nombre)  
print(usuario1.contraseña)  

# Resultados:
# Imprime "Juan"
# Imprime "123456789"