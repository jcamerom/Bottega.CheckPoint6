## Checkpoint 6

  

### 1) ¿Para qué usamos clases en Python?

Muchos lenguajes de programación ya presentan un concepto relativamente moderno que es usado para manejar ejemplos más realistas de la vida cotidiana a la hora de programar: **la programación orientada a objetos**.

La programación orientada a objetos ha significado un gran avance que nos ha posibilitado dar con nuevas soluciones para escribir código. Y está basado en el uso de instrumentos de programación denominados: **clases**.

Las clases sirven para **definir** modelos de entidades que poseen una serie de características (o **atributos**) y son capaces de realizar una serie de procedimientos (o **métodos**).

Por ejemplo: manejar un modelo abstracto de coche, cuyos atributos sean: marca, modelo, y color, por ejemplo. Y sus métodos serán los procedimientos que puede ofrecer, como el consumo de gasolina en un tramo de kms, o la emisión de CO2 que realiza. Con esta clase tenemos un patrón básico para definir coches.

Cada uno de los ejemplos que podemos definir, gracias a ese modelo de creación, con atributos y procedimientos, serán llamados **objetos** . Los objetos ya serán ejemplos definidos a partir de ese "molde" de definición, con los que podremos operar y hacer toda una serie de acciones programables. Se dice que un objeto es una **estancia** de la clase, que ya tiene atributos y procedimientos definidos. 

En el ejemplo anterior, un objeto será, un coche de marca "SEAT", de modelo "Ibiza", y color "Rojo", que consumirá unos "7 litros por kilómetro" y emitirá "100 g de CO2 por cada 100 Km". Con este objeto lo tendremos bien definido.

Ejemplo del diseño de una clase en Python:
```python

class Coche:

""" Representa un coche con sus características y un método para calcular el consumo de gasolina.

Atributos:

marca: La marca del coche (str).

modelo: El modelo del coche (str).

color: El color del coche (str).

consumo_por_km: El consumo de gasolina por kilómetro (float, en litros/km).

Métodos:

__init__(self, marca, modelo, color, consumo_por_km): Constructor de la clase.

calcular_consumo(self, distancia): Calcula el consumo de gasolina para una distancia dada.

"""

  

def __init__(self, marca, modelo, color, consumo_por_km):

	self.marca = marca

	self.modelo = modelo

	self.color = color

	self.consumo_por_km = consumo_por_km

  

def calcular_consumo(self, distancia):

	if distancia <= 0:

		raise ValueError("La distancia debe ser un valor positivo.")

	consumo = distancia * self.consumo_por_km return consumo

  

# Ejemplo de uso coche1 = Coche("Toyota", "Corolla", "Azul", 0.06) # 6 litros/100 km

```

En Python se usan objetos continuamente. Ya sean de la generación del desarrollador para un programa que esté desarrollando, o bien por ejemplo a través de las propias clases y objetos que ya tiene definidos el lenguaje para su uso interno. Como por ejemplo, la clase File para leer archivos, la clase Date para definir fechas, o la clase Str para manejar cadenas en Python, y sus métodos que ya hemos utilizado como lower(), replace(), o find().

  

Ejemplos sencillos de uso de la clase `str` de Python y algunos de sus métodos:

  

**Crear una cadena:**

```python

cadena1 = "Hola, mundo!"

cadena2 = 'Este es un texto entre comillas simples.'

cadena3 = """Este es un texto entre comillas triples,

que puede contener varias líneas."""

  

```

  

**Acceder a caracteres por índice:**

```python

cadena = "Python es genial"

  

print(cadena[0]) # Salida: P

print(cadena[5]) # Salida: o

print(cadena[-1]) # Salida: l

  

```

**Convertir a mayúsculas y minúsculas:**

```python

cadena = "Este texto está en mayúsculas y minúsculas."

  

cadena_mayusculas = cadena.upper()

cadena_minusculas = cadena.lower()

  

print(cadena_mayusculas) # Salida: ESTE TEXTO ESTÁ EN MAYÚSCULAS Y MINÚSCULAS.

print(cadena_minusculas) # salida: este texto está en mayúsculas y minúscula

```

  
  

### 2) ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?
Al instanciarse un objeto de la clase, es decir, cuando se crea un ejemplo concreto de esa clase, siempre se ejecuta automáticamente uno de los procedimientos internos que se llama **constructor**. En Python, este método es **"`__init__`"**, y su función principal es inicializar las características internas cuando el objeto es creado. Con él se construyen los objetos de la clase. 
Ejemplo: 
De la clase coche del ejemplo anterior:
```python
def __init__(self, marca, modelo, color, consumo_por_km):

	self.marca = marca

	self.modelo = modelo

	self.color = color

	self.consumo_por_km = consumo_por_km
```
Para que se construya un objeto de esa clase, se utiliza el nombre de la clase y sus parámetros de entrada. 
```python
coche1 = Coche("Toyota", "Corolla", "Rojo", "8")
```



### 3) ¿Cuáles son los tres verbos de API?
Empecemos comentando qué es una API. Una API (Application Programming Interface) es un conjunto de reglas y protocolos que permiten a diferentes aplicaciones interactuar entre sí. En otras palabras, es una interfaz que permite que dos o más sistemas se comuniquen y compartan datos y servicios. 
Las API pueden ser de diferentes tipos, como API de SOAP, API de RPC, API de WebSocket y API de REST, entre otras. Hoy día la más habitual es la API de REST: 

**API de REST**  es una forma de permitir que diferentes aplicaciones se comuniquen entre sí a través de internet utilizando el protocolo HTTP.

El protocolo HTTP define el lenguaje general de la comunicación a través de internet. Que utiliza entre otras cosas los métodos HTTP, que son las palabras específicas que se utilizan para realizar acciones dentro de una solicitud HTTP, como obtener información, enviar información, o eliminar información.

Los métodos HTTP más comunes utilizados en las API, y como tales, los verbos más usados para la comunicación entre componentes de software a través de internet son:

-   **GET:**  utilizado para recuperar información del servidor. Se considera una operación "segura" ya que no modifica ningún dato en el servidor.
    
-   **POST:**  utilizado para enviar información al servidor para que la procese. Esta solicitud puede crear o modificar datos en el servidor y no es considerada una operación "segura".
    
-   **DELETE:**  utilizado para eliminar información del servidor. Esta solicitud es considerada una operación "no segura" ya que elimina información del servidor.
    

Estos métodos no son los únicos pero sí los principales más utilizados, también hay otros métodos HTTP comunes como PUT, y menos comunes como HEAD, OPTIONS, CONNECT, TRACE y PATCH que se utilizan en casos más específicos.

 

### 4) ¿Es MongoDB una base de datos SQL o NoSQL?
MongoDB es una base de datos multiplataforma de código abierto mantenida por MongoDB, Inc. Es una base de datos basada en documentos que tiene como objetivo manejar las demandas de datos de las aplicaciones de software modernas. 
MongoDB no SQL como lenguaje de consulta, sino que usa JavaScript y representa los datos de forma similar a documentos JSON en bloques llamados colecciones. Es por tanto una base de datos NoSQL.
Almacena objetos de datos en colecciones y documentos en lugar de las tablas y filas que se utilizan en las bases de datos relacionales tradicionales. Las colecciones comprenden conjuntos de documentos, que son equivalentes a tablas en una base de datos relacional. Los documentos consisten en pares clave-valor, que son la unidad básica de datos en MongoDB.
MongoDB no requiere un esquema predefinido como con el lenguaje SQL, lo que significa que los documentos (incluso de una misma colección) pueden tener diferentes estructuras. 
Ejemplo:
```python
[
  {
    "_id": "123",
    "nombre": "Camiseta",
    "precio": 20.50,
    "categoria": "ropa"
  },
  {
    "_id": "456",
    "nombre": "Portátil",
    "precio": 599.99,
    "categoria": "electrónica"
  },
  {
    "_id": "789",
    "nombre": "Taza",
    "precio": 7.95,
    "categoria": "hogar"
  }
]
```
MongoDB utiliza MongoDB Query Language (MQL) para recuperar datos de la base de datos. Es fácil de usar y funciona de manera similar a SQL con operaciones CRUD para crear, leer, actualizar y eliminar documentos. Los nombres de las funciones siguen la sintaxis:

**< database > . < collection_name > . < operation >**

A continuación se muestran tres ejemplos prácticos:

**INSERT**: Crear o insertar un nuevo documento en una colección. Si la colección no existe, se creará una nueva colección.

***db.collection.insertOne()*** inserta un documento en una colección.

***db.collection.insertMany()*** inserta varios documentos en una colección a la vez.

Así es como se ve la inserción de un documento en la colección del cliente:
```python
db.customer.insertOne (

{

	firstname: “Marta”,

	lastname: “Casas”

	Address: “Calle Petunias 232, Ciempozuelos, Madrid, 28350”

}
```

**FIND**: Esto consulta una colección de documentos. Se pueden aplicar criterios y filtros de consulta para encontrar documentos específicos.

***db.collection.find()***

El siguiente código encuentra todos los documentos en la colección del cliente:
```
db.customer.find()
```

**UPDATE**: Esto modifica los documentos existentes en una colección.

***db.collection.updateOne()
db.collection.updateMany()
db.collection.replaceOne()***

Así es como actualizaría un documento en la colección de clientes:
```python
db.customer.updateOne(

	{ firstname: “Marta” },

	{

	$set: { “address”, “Calle Lavanda 5, Ciempozuelos, Madrid, 28350”}

	}

)
```
### 5) ¿Qué es una API?
Una API (Application Programming Interface) es un conjunto de reglas y protocolos que permiten a diferentes aplicaciones interactuar entre sí. En otras palabras, es una interfaz que permite que dos o más sistemas se comuniquen y compartan datos y servicios.  
Las API pueden ser de diferentes tipos, como API de SOAP, API de RPC, API de WebSocket y API de REST, entre otras. Hoy día la más habitual es la API de REST:

**API de REST**  es una forma de permitir que diferentes aplicaciones se comuniquen entre sí a través de internet utilizando el protocolo HTTP.

El protocolo HTTP define el lenguaje general de la comunicación a través de internet. Que utiliza entre otras cosas los métodos HTTP, que son las palabras específicas que se utilizan para realizar acciones dentro de una solicitud HTTP, como obtener información, enviar información, o eliminar información.


### 6) ¿Qué es Postman?
Postman es una **herramienta de colaboración y desarrollo que permite a los desarrolladores interactuar y probar el funcionamiento de servicios web y aplicaciones**. Consiste en una interfaz gráfica intuitiva y fácil de usar para enviar solicitudes a servidores web y recibir las respuestas correspondientes.
Con esta plataforma se puede gestionar diferentes entornos de desarrollo, organizar las solicitudes en colecciones y realizar pruebas automatizadas para verificar el comportamiento de los sistemas.  
Postman es utilizado para **testear colecciones y catálogos APIs** (tanto a nivel _front-end_ como _back-end_), para gestionar el ciclo de vida de las APIs, mejorar el trabajo colaborativo y mejorar la organización del proceso de diseño y desarrollo.
Todo ello lo hace mediante una GUI que facilita a los desarrolladores el envío de solicitudes HTTP y HTTPS a una API y gestionar las respuestas recibidas.

Las principales características y funcionalidades de Postman son:

-   **Envío de solicitudes**. Permite enviar solicitudes GET, POST, PUT, DELETE y otros métodos HTTP a una API especificando los parámetros, encabezados y cuerpo de la solicitud.
-   **Gestión de entornos**. Facilita la configuración para diferentes entornos (por ejemplo, desarrollo, prueba, producción) y el cambio sencillo entre ellos (para realizar pruebas y desarrollo en diferentes contextos).
-   **Colecciones de solicitudes**. Agrupa las solicitudes relacionadas en colecciones, lo que facilita la organización y ejecución de pruebas automatizadas.
-   **Pruebas automatizadas**. Es ideal para crear y ejecutar pruebas automatizadas para verificar el comportamiento de una API (detectar errores e incrementar la calidad del software).
-   **Documentación de API**. Genera de forma automatizada, documentación detallada de la API a partir de las solicitudes y respuestas realizadas, lo que facilita su comprensión y uso por parte de otros desarrolladores.
  
### 7) ¿Qué es el polimorfismo?
En Python, la herencia es una característica clave que nos permite crear clases hijas a partir de una clase padre.

La  **herencia en Python**  se logra por medio de una sintaxis sencilla que involucra la creación de una nueva clase que hereda atributos y métodos de la clase padre. Para crear una clase hija en Python, simplemente agregamos el nombre de la clase padre en paréntesis después del nombre de la clase hija.

**El polimorfismo**, por otro lado, es una característica que nos permite utilizar objetos de diferentes clases de manera intercambiable. Esto significa que el mismo método o función puede ser utilizado en diferentes tipos de objetos, sin preocuparnos por conocer los detalles exactos de cada uno de ellos. En Python, el polimorfismo está estrechamente relacionado con la herencia y la superposición de métodos.

La  **superposición de métodos**  es una técnica que nos permite modificar el comportamiento de los métodos heredados de la clase padre en la clase hija. Esto se logra al definir un método con el mismo nombre en la clase hija como en la clase padre. Cuando se llama al método en la clase hija, el intérprete de Python buscará la definición del método en la clase hija primero y, si no la encuentra, lo buscará en la clase padre.

En Python, también podemos acceder a los métodos heredados de la clase padre utilizando la función  `super()`. Esto nos permite llamar al método de la clase padre directamente desde la clase hija, ahorrándonos tiempo y esfuerzo en la reescritura de código.

>La herencia y el polimorfismo en Python nos permiten crear clases con una mayor flexibilidad y versatilidad. Esto nos permite reutilizar código y diseñar sistemas más eficientes y escalables. 

Por ejemplo, si tenemos una clase ‘Animal’ con algunas propiedades y métodos, podemos crear una clase ‘Perro’ que hereda estas propiedades y métodos. Además, podemos agregar propiedades y métodos adicionales específicos de la clase de ‘Perro’.

```python
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Este animal hace algún sonido")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        print("El perro hace guau guau")

```

En este ejemplo, la clase ‘Perro’ hereda las propiedades de la clase ‘Animal’ mediante la declaración de ‘(Animal)’ en su definición. Además, sobre escribe el método ‘hacer_sonido’, para que este método ahora muestre “El perro hace guau guau” en lugar de “Este animal hace algún sonido”.

Esto significa que, al  **crear una instancia**  de la clase ‘Perro’, podemos acceder a las propiedades y métodos de la clase ‘Animal’ y también a las nuevas propiedades y métodos de la clase ‘Perro’.

```python
mi_perro = Perro("Scottie", 3, "Terrier")
print(mi_perro.nombre) # Scottie
print(mi_perro.edad) # 3
print(mi_perro.raza) # Terrier
mi_perro.hacer_sonido() # El perro hace guau guau

```
Con el  **polimorfismo**  se permite a distintos objetos responder de manera diferente a un mismo llamado de método. Por ejemplo imagina que tienes una clase padre denominada  **Mascota**  con un método  **saludar()**. Y luego escribimos dos clases que heredan de Mascota, como  **Perro**  y  **Gato**, donde cada una puede definir su propia implementación del método  **saludar()**. Entonces, cuando llames a  **saludar()**  en un objeto de tipo Perro, la implementación de Perro se ejecutará, mientras que en un objeto de tipo Gato, la implementación de Gato se ejecutará. 
Ejemplo:
```python
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        print("Este animal hace algún sonido")

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        print("El perro hace guau guau")
        
class Gato(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        print("El gato hace miau miau")
```
Vamos a invocar los atributos y métodos de estas clases:
```python
mi_perro = Perro("Scottie", 3, "Terrier")
print(mi_perro.nombre) # Scottie
print(mi_perro.edad) # 3
print(mi_perro.raza) # Terrier
mi_perro.hacer_sonido() # El perro hace guau guau

mi_gato = Gato("Garfield", 2, "Siamés")
print(mi_gato.nombre) # Garfield
print(mi_gato.edad) # 2
print(mi_gato.raza) # Siamés
mi_gato.hacer_sonido() # El gato hace miau miau
```

### 8) ¿Qué es un método dunder?

En Python, los métodos dunder (abreviatura de «double underscore methods», también conocidos como «métodos mágicos» o «métodos especiales») son métodos especiales que tienen un doble guion bajo (**__**) al principio y al final de su nombre. Se emplean para definir el comportamiento especial de las clases y sus instancias, y son llamados automáticamente por el intérprete de Python en respuesta a ciertas operaciones.

Los métodos dunder pueden utilizarse para implementar características como **la inicialización de objetos, la representación en forma de cadena, la sobrecarga de operadores, la comparación**, entre otras.

A continuación se muestra algunos de los métodos dunder más comunes en Python:

#### "__ init __( )"

Es un método especial en Python que se utiliza para inicializar una instancia de una clase. Cuando se crea una instancia de una clase, el método __ init __ es llamado automáticamente por el intérprete de Python y se utiliza para realizar cualquier inicialización que sea necesaria para la instancia.

Por ejemplo, supongamos que queremos crear una clase llamada Persona con dos atributos: nombre y edad. Podríamos definir la clase de la siguiente manera:
```python
class persona:

	def __init__(self, nombre, edad): 
		self.nombre = nombre 
		self.edad = edad
```
En este ejemplo, el método __init__ toma dos parámetros: nombre y edad. Estos se utilizan para inicializar los atributos nombre y edad de la instancia de la clase.

#### " __ str __ ( )"

Es otro método especial (dunder) en Python que se utiliza para devolver una representación de cadena (string) de una instancia de una clase.  **Este método se llama cuando se usa la función str() para convertir un objeto en una cadena de caracteres.**

En otras palabras, el método __str__ se emplea para definir cómo se debe imprimir una instancia de la clase cuando se llama la función str() o cuando se utiliza la interpolación de cadenas (f-strings).

Por ejemplo, supongamos que tenemos una clase  **Persona** con los atributos nombre y edad. Podemos definir el método __ str __ de la siguiente manera:
```python
class persona:

	def __init__(self, nombre, edad): 
		self.nombre = nombre 
		self.edad = edad
		
	def __str__(self):
		return f"{self.nombre} tiene {self.edad} años"
```
### Encapsulación

Python soporta la encapsulación mediante el uso de métodos y atributos privados. Los métodos y atributos privados se definen mediante el uso del doble guion bajo (**__**). Solo puede accederse a los métodos privados por otros métodos dentro de la misma clase; no se puede acceder directamente a los atributos privados desde fuera de la clase.

```python
class automovil:
	def __init__(self, marca, modelo, color):
		self.__marca = marca
		self.__modelo = modelo
		self.__color = color
```


### 9) ¿Qué es un decorador de python?
Los decoradores son funciones que **utilizan otras funciones ya definidas y les añaden nuevos comportamientos **, evitándose así sobreescribir el mismo código, reutilizándolo, y al mismo tiempo, que sea más fácil de testear y mantener. 
Si alguna vez has visto  **"@"** sobre una función, estás ante un decorador o decorator, bien sea uno que Python ofrece por defecto o uno que pudo haber sido creado por interés del programador.

Veamos un ejemplo muy sencillo. Tenemos una función  `suma()`  que vamos a decorar usando  `mi_decorador()`. Para ello, antes de la declaración de la función suma, hacemos uso de  `@mi_decorador`.

```python
def mi_decorador(funcion): 
	def wrapper(): 
		print("Antes de la función") 
		funcion() 
		print("Después de la función") 
	return wrapper 
@mi_decorador 
def saludar(): 
	print("Hola!") 

saludar()

"""
Salida:
Antes de la función 
Hola! 
Después de la función
"""
```

Lo que realiza  `mi_decorador()`  es definir una nueva función que encapsula o envuelve la función que se pasa como entrada, `saludar( )`. Concretamente lo que hace es hace uso de dos  `print()`, uno antes y otro después de la llamada la función.
Si además queremos integrar argumentos, podemos seguir este ejemplo: 
```python
def mi_decorador(suma):
    def wrapper(*args, **kwargs):
        print('Antes de la ejecución de la función a decorar')
        result = suma(*args, **kwargs)
        print('Después de la ejecución de la función a decorar')    

        return result

    return wrapper

@mi_decorador
def suma(a, b):
    return a + b
"""
Lo iniciamos:
>>> suma(10, 20)  
En lugar de retornar sólo la suma, ahora retorna los mensajes agregados:

Antes de la ejecución de la función a decorar
Después de la ejecución de la función a decorar
30
"""
```

