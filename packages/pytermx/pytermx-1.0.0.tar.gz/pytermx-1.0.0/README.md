# PyTermX

PyTermX is a Python package for creating colorful text-based animations and effects in your terminal. It provides a variety of features to make your command-line applications more visually appealing.

## Features

- Text animation with color and style options
- Center text in your terminal
- Gradient text effects
- Hide and show the cursor
- Easy-to-use and customizable

## Installation

You can install PyTermX via `pip`:

```shell
pip install pytermx
```

## Usage

Here is a simple example of how to use PyTermX in your Python code:

```python
from pytermx import Anim, Color, Center

# Create an animated banner
banner = "Hello, PyTermX!"
Anim.show_n_hide(banner, 10)

# Create centered text
centered_text = Center.center("This text is centered.")
print(centered_text)

# Apply a gradient effect
gradient_text = Fade.in_blue("This text has a blue gradient.", 255, 0)
print(gradient_text)
```

## Credits

Made with <3 by Seka

For questions or support, you can reach me on Discord: @sekateur

And remember, cats are world! 🐱