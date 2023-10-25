# Brain Food style library

En esta librería se encuentran los detalles para el uso de la librería que le da estilo Brain Food a los gráficos desarrollados con la librería Seaborn de python.





La librería contiene cuatro funciones::
  - `set_bf_style`: Función que establece el estilo Brain Food en los gráficos.
  - `set_bf_palette`: Función que establece la paleta de colores Brain Food.
  - `select_color`: Función que selecciona un color de la paleta de colores.
  - `generate_gradient_colors`: Función que utiliza un color base y genera una lista de colores degradados.

Además, la librería permite cargar la lista de colores en `colors`.


## Usage

### Initial setup



1. Primero, se debe instalar la librería `bfstyle`

    *Aplicar paso solo si la librería no ha sido instalada previamente.*

    ```
    pip install bfstyle
    ```



2. Para cargar las funciones mencionadas y la lista de colores *Brain Food* solo se debe utilizar el siguiente código:

    ```
    import bfstyle
    from bfstyle.load_bf_style import colors, set_bf_style, set_bf_palette, select_color, generate_gradient_colors
    ```
    *Se recomienda aplicar este paso al inicio del notebook. Además, se deben cargar las librerías `seaborn` y `matplotlib`.*

3. Luego se deben aplicar las funciones de la siguiente manera:
    ```
    set_bf_style()
    set_bf_palette()
    ```
Una vez aplicados estos tres pasos, los gráficos que se realicen utilizando la librería `seaborn` y `matplotlib` utilizarán el estilo *Brain Food*.

*Cabe señalar que los gráficos utilizarán las fonts por defecto de python*

### Personalizar la fonts deseada

La función `set_bf_style()` permite utilizar fonts que hayan sido descargadas en formato `.ttf`, solo se necesita indicar el directorio de los archivos.
A modo de ejemplo, se muestra cómo establecer la font [Roboto](https://fonts.google.com/specimen/Roboto) en los gráficos.
Todos los archivos `.ttf` deben estar guardados en la misma carpeta.

```
font_path="User/working_directory/fonts" # Example
set_bf_style(path_fonts=font_path)
```

*Esto último solo requiere que la funcion `set_bf_style()` sea ejecutada utilizando el parametro `path_fonts`*.

### Personalizar paleta de colores

La función `set_bf_palette` permite establecer una paleta de colores personalizada. Solo requiere una lista de los 
colores de la paleta deseada con los valores en formato `RGB`. Para aplicar una nueva paleta se debe aplicar el siguiente 
código:

```
new_color_list =['#FFFFFF', '#000000','#F12323'] # Example
set_bf_palette(colors=new_color_list)
```





## Otras funciones

A continuación, se muestra el uso de otras dos funciones: `select_color` y `generate_gradient_colors`.

Como se mencionó, `select_color` facilita la selección de un determinado color que esté en una lista y guardar el `RGB` 
en formato *string* en alguna variable.

La función requiere de una lista de colores y la posición del color. 
Cabe señalar que la primera posición en la lista corresponde a `1`.

Por ejemplo, si se desea seleccionar el primer color de la lista `colors` de la librería `bfstyle` que contiene
los colores *Brain Food* en formato `RGB` se aplican las siguientes líneas de código:

```
colors # Brain Food colors list
first_color = select_color(colors,1) # Stores the color RGB string in first_color
```

*Al ejecutar la función, la pantalla mostrará gráficamente el color seleccionado*.

En ocasiones se puede necesitar un degrade de colores para ampliar la paleta de colores.
Para ello solo se necesita un color base y la cantidad de colores a generar.

```
base_color = '#B01515'
degrade_color_list = generate_gradient_colors(base_color, 11)
```

*Esto último generará una lista de 11 colores en base a `base_color`*.
