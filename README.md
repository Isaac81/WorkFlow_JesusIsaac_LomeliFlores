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
Para el desarrollo de esta practica se utilizo el lenguaje de programación python en su versión 3.11. para simular la creación y ejecución de procesos. Lo primero que se realizo fue una función que marcara del flujo de trabajo utilizando el decorador flow.

</p>


```py
@flow
def main_flow():
    p = create_process()
    result = execute(p)
    print(f"Process completed in {p['tme']} seconds. Result: {result}")
```


<p align="justify">
El lo primero que hace el flujo es crear un proceso llamando a una función con el decorador task.
</p>


```py
@task
def create_process():
    process  =  {
        "num1": random.randint(0, 100),
        "num2": random.randint(0, 100),
        "tme": random.randint(1, 2)
    }

    return process
```


<p align="justify">
Posteriormente el flujo llama a otra tarea para ejecutar el proceso creado en la tarea anterior, en este caso una división.
</p>

```py
@task
def execute(process):
    result = process['num1'] / process['num2']
    sleep(process['tme'])

    return result
```

<p align="justify">
Debido a que los números son generados aleatoreamente y que el rango dado permite que alguno de los operandos sea un cero, puede ocurrir un error, pues se estaria tratando de dividir entre cero. Dicho error es capturado por prefect y mostrara el "modulo" que presento el error.
</p>

![Ejecución del servicio](/Imagenes/Screenshot_26.png)

<p align="justify">
Si por el contrario, el programa se ejecuto correctamente finalizara el proceso mostrando las salidas de las diferentes tareas del flujo.
</p>

![Comprobar ejecución del servicio](/Imagenes/Screenshot_25.png)

### Conclusión

<p align="justify">
Se logró comprender la utilidad que tienen las herramientas cómo prefect para el desarrollo de aplicaciones mas seguras y de facil depuración, pues al mostrar exactamente en que parte de flujo del sistema ocurrio el error se ahorra tiempo al no tener que buscar la ubicación del problema y centrarse en la posible solución.
</p>


### Bibliografia
* queue — A synchronized queue class. (s. f.). Python documentation. Recuperado el 5 de Marzo de 2023, de https://docs.python.org/3/library/queue.html *
