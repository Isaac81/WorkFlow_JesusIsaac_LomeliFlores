# Universidad de Guadalajara - Centro Universitario de Ciencias Exactas e Ingenierias
## Departamento de ciencias computacionales
Computacion Tolerante a fallas - Seccion D06

Profesor: *Lopez Franco Michel Emanuel*

Alumno: *Lomeli Flores Jesus Isaac*

## Workflow managers

### Introducción

<p align="justify">
  Los workflows como prefect resultan ser bastante utiles cuando se quiere observar el flujo de los procesos de un sistema, ademas de aislar las diferentes funciones 
  de este lo que resulta muy util para informar sobre errores ocurridos en las diferentes tareas al proporcionar información clara sobre el lugar donde ocurrio el fallo.
</p>


</div>

### Desarrollo

<p align="justify">
Para el desarrollo de esta practica se utilizo el lenguaje de programación python en su versión 3.11 para implementar un código capaz de detectar el estado del puerto
que utiliza la pagina realizada con React.js, cuyo código principal es el siguiente.

</p>


```py
def verificar(ip, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        status = sock.connect_ex((ip, puerto))
        if status == 0:
            print(f"Puerto: {port} - Abierto")
        else:
            print(f"Port: {port} - Cerrado")
            os.system("npm run dev --port={puerto}")
        sock.close()
    except socket.error as err:
        print(f"Connection error: {err}")    
        sys.exit()
```


<p align="justify">
El servicio se debe ejecutar indefinidamente, por lo que se implemento dentro de un bucle sin fin dentro del punto de entrada del programa, lugar donde también se
asignan los valores de los argumentos requeridos.
</p>


```py
if __name__ == '__main__':
    ip_address = "192.168.1.75"
    port = 5173
    url = "D:/6to semestre/ComputacionToleranteFallos/Codigos/persistenciaDatos/"
    
    os.chdir(url)
    while(True):
        verificar(ip_address, port)
        time.sleep(300)
```


<p align="justify">
Para convertir el script realizado en un servicio se utilizo nssm.
</p>

![Creación del servicio con nssm](/imagenes/Screenshot_17.png)

<p align="justify">
Posteriormente se inicia el servicio utilizando una terminal con permisos de administrador.
</p>

![Ejecución del servicio](/imagenes/Screenshot_18.png)

<p align="justify">
Una vez iniciado el servicio se comprueba su ejecución con ayuda del administrador de tareas de Windows.
</p>

![Comprobar ejecución del servicio](/imagenes/Screenshot_19.png)


<p align="justify">
Posteriormente la ejecucion de Nodejs en los procesos del sistema.
</p>

### Conclusion

<p align="justify">
Se logró comprender la importancia de los servicios y como es que estos se implementan. Estos tipos de servicios encargados de revisar el estatus de un programa o aplicación
resultan muy utiles si se necesita que dicha aplicación permanezca siempre activa como es el caso de algunas paginas gubernamentales.
</p>


### Bibliografia
* queue — A synchronized queue class. (s. f.). Python documentation. Recuperado el 5 de Marzo de 2023, de https://docs.python.org/3/library/queue.html *
