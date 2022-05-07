# Planetarium

A simulation of the solar system using Python and Panda3D.

![GIF of the application window showing the sun and planets](docs/demo.gif)

## Installation

Create a virtual environment and use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies.

```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
.\venv\Scripts\activate.bat # on Windows
. venv/bin/activate # on macOS/Linux

# Install the dependencies
pip3 install -r requirements.txt
```

## Usage

Simply run the main file:

```bash
python solar_system.py
```

# Backlog / Future improvement ideas
- Realistic lighting: Self-shadowing, day-night cycle, sun occlusion.
- Animated cloud textures.

## License
The code is licensed as [MIT](https://choosealicense.com/licenses/mit/). For the assets, please see the respective license notices in the models folder.