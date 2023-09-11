# ExeChecker
El programa "ExeChecker" es una aplicación de Python que tiene la función de listar todos los ejecutables (programas) que se han ejecutado en las últimas 12 horas en un sistema Windows. El programa proporciona información sobre cada ejecutable, incluyendo su nombre, ruta de ubicación y la fecha en que se ejecutó.

**1.-**
Importación de módulos: El programa comienza importando varios módulos de Python que serán utilizados en el desarrollo de la aplicación. Estos módulos incluyen os, psutil, datetime, tkinter (para la interfaz gráfica de usuario), y otros módulos relacionados con la GUI.

**2.-**
Definición de la función obtener_ejecutables: Esta función se encarga de obtener la lista de ejecutables ejecutados en las últimas 12 horas. Utiliza el módulo psutil para iterar a través de todos los procesos en ejecución y recopila información sobre el nombre del proceso, la ubicación del archivo ejecutable y la fecha de creación del proceso. Luego, compara la fecha de creación con el tiempo actual menos 12 horas para determinar si el proceso se ejecutó en las últimas 12 horas. Los datos recopilados se almacenan en una lista y se devuelven.

**3.-**
Definición de la función actualizar_resultados: Esta función se utiliza para actualizar la interfaz de usuario con la lista de ejecutables obtenidos a través de la función obtener_ejecutables. Limpia el área de texto en la interfaz y luego agrega la información sobre los ejecutables (nombre, fecha y ubicación) en el área de texto con formato adecuado.

**4.-**
Definición de la función guardar_resultados: Esta función permite al usuario guardar la lista de ejecutables en un archivo de texto (.txt). Utiliza un cuadro de diálogo de archivo para que el usuario seleccione la ubicación y el nombre del archivo de destino. Luego, escribe la información de los ejecutables en el archivo .txt.

**5.-**
Configuración de la interfaz de usuario: El programa utiliza el módulo tkinter para crear una interfaz gráfica de usuario (GUI). Se crea una ventana principal que contiene un título, botones de "Actualizar" y "Guardar en archivo .txt", y un área de texto con una barra de desplazamiento. Los botones están vinculados a las funciones actualizar_resultados y guardar_resultados.

**6.-**
Función iniciar y ejecución de la GUI: La función iniciar se utiliza para cargar los resultados iniciales al iniciar la aplicación. Luego, se ejecuta la interfaz gráfica utilizando ventana.mainloop().

# Modulos/Librerias usadas
**psutil**
**tkinter**
**os**
**datetime**
