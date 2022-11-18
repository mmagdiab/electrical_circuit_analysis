# Electrical Circuit Analysis
Desktop application written in python to analysis any give electrical cirucuit.
## Features
- Analyse any given electrical circuit branches as its input.
  - Current on each branch as output (Jb vector)
  - Voltage on each branch (Vb vector)
  - a graph of the circuit consists of tree and links demonstrating current/voltage on each edge.
## Dependencies
- [numpy](https://numpy.org/)
- [pandas](https://pandas.pydata.org/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [networkx](https://networkx.org/documentation/stable/index.html)
- [matplotlib.pyplot](https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html)
## How to start
1. Clone the project.
2. Make sure you have **python 2 or higher** installed.
3. Open electrical_circuit_analysis folder in **CMD**.
4. Create virtual environment.
      > python -m venv .\venv
5. **Activate the virtual environment** by typing the following command in **CMD**.
      > .\venv\Scripts\activate
6. Install required dependencies
      > pip install numpy, pandas, pyqt5, networkx, matplotlib
7. **Run** the main method
      > python main.py
