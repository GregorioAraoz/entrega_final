# Proyecto Django - Tercera Pre-entrega

Este proyecto es una pequeña aplicación hecha con Django donde se pueden agregar animales a una lista de animales y revisar los precios del alimento en una lista de alimento para los animales.

Además cuenta con algunas otras ventanas que estuvimos viendo en el curso

## ¿Qué se puede hacer?

**EXTRA**

- Para acceder a la totalidad de las funciones se debe tener un usuario y estar logueado.
- Se puede crear un usuario facilmente tocando en "Registrarse"
- Una vez que el usuario se registra pasa automáticamente a la ventana de "login" donde deberá hacer el login con el usuario y contraseña registrados para acceder a todas las funciones.
- Si por alguna razon el usuario quiere hacer un logout, podrá hacerlo con el boton de "logout"

1. **Ver una página de inicio**
   - Muestra un mensaje de bienvenida.

2. **Ver un ejemplo de condicional y bucle**
   - Aparece una lista de números y se muestra en color rojo si es par, azul si es impar.

3. **Agregar Animal**
   - Podés cargar una especie de animal (por ejemplo: elefante) y decir si es herbívoro o carnívoro.
   - Luego de enviar el formulario, aparece un mensaje confirmando que el animal fue agregado con exito.

4. **Lista de Animales**

   - Dentro de la lista aparecen los animales que fueron registrados 
   - Junto con el nombre y la alimentación del animal registrado aparecen las opciones de "Ver Detalle, Actualizar y Eliminar"
   - Si vamos a ver detalle podemos acceder a una nueva pestaña donde vemos también el numero de ID. 
   - Tocando en actualizar podemos hacer modificaciones al registro
   - Tocando eliminar se elimina el animal de la lista 

5. **Precios de Alimento**

   - Entrando en la ventana precios de alimento podrá ver los diferentes alimentos disponibles para los animales
   - Puede agregar un nuevo alimento tocando en "Agregar nuevo alimento" dentro de la misma ventana. Para agregar un nuevo alimento deberá completar: Nombre, Precio, Unidad y Descripción
   - Para leer la descripción de un alimento deberá entrar en "Ver Detalle" a la derecha del alimento
   - Puede actualizar cualquier campo del alimento con el boton de actualizar, también a la derecha del alimento
   - Puede eliminar cualquier alimento con el boton de "eliminar" y con previa confirmación.
