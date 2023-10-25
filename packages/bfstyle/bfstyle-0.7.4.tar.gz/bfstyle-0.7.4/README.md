# Brain Food Style Library

This library contains details for using the Brain Food style library with graphics developed using the Seaborn library in Python.

The library includes four functions:

- `set_bf_style`: Function to set the Brain Food style for graphics.
- `set_bf_palette`: Function to set the Brain Food color palette.
- `select_color`: Function to select a color from the color palette.
- `generate_gradient_colors`: Function to generate a list of gradient colors based on a base color.

Additionally, the library allows you to load the color list into `colors`.
## Usage
### Initial Setup

First, you need to install the bfstyle library.

*Apply this step only if the library has not been installed previously.*


```
pip install bfstyle
```

To use the mentioned functions and the Brain Food color list, you only need to use the following code:

```
import bfstyle
from bfstyle.load_bf_style import colors, set_bf_style, set_bf_palette, select_color, generate_gradient_colors
```



*It is recommended to apply this step at the beginning of your notebook. Also, make sure to import the `seaborn` and 
`matplotlib` libraries.*

Next, apply the functions as follows:
```
set_bf_style()
set_bf_palette()
```

*Once these three steps are applied, the graphics created using the seaborn and matplotlib libraries will use the Brain Food style.*

*Note that the graphics will use Python's default fonts.*

### Customize Desired Fonts

The `set_bf_style()` function allows you to use fonts that have been downloaded in `.ttf` format; 
you only need to specify the directory where the font files are located. As an example, here's how to set the [Roboto](https://fonts.google.com/specimen/Roboto) 
font for your graphics. All `.ttf` files should be saved in the same folder.

```
font_path = "User/working_directory/fonts"  # Example
set_bf_style(path_fonts=font_path)
```


This only requires that the `set_bf_style()` function be executed with the `path_fonts` parameter.

### Customize Color Palette

The `set_bf_palette` function allows you to set a custom color palette. 
It only requires a list of colors for the desired palette with values in RGB format. 
To apply a new palette, use the following code:


```
new_color_list = ['#FFFFFF', '#000000', '#F12323']  # Example
set_bf_palette(colors=new_color_list)
```


## Other Functions

Below are the uses of two other functions: `select_color` and `generate_gradient_colors`.

As mentioned, `select_color` makes it easy to select a specific color from a list and save the RGB value as a *string* 
in a variable. The function requires a list of colors and the position of the color. Note that the first position in the list corresponds to `1`.

For example, to select the first color from the colors list of the `bfstyle` library, 
which contains the Brain Food colors in RGB format, you can use the following lines of code:

```
colors  # Brain Food colors list
first_color = select_color(colors, 1)  # Stores the RGB color string in first_color
```


When you run the function, it will display the selected color graphically.

Sometimes, you may need a gradient of colors to expand the color palette. 
For this, you only need a base color and the number of colors to generate.

```
base_color = '#B01515'
degrade_color_list = generate_gradient_colors(base_color, 11)
```



This will generate a list of 11 colors based on base_color.