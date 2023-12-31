# BMC Via Simulation

BMC Via Simulation is a project that aims to simulate a system using the BMC (Bounded Model Checking) approach. It provides a graphical user interface (GUI) for interacting with the simulation.

## Project Hierarchy

The project consists of the following files and folders:

- `MainWindow.py`: Contains the main GUI window that starts the entire project.

### Folders

1. `Utils`: Contains utility classes used in the simulation.
   - `SystemFactory.py`: Implements a system factory for creating system instances.
   - `SystemUtils.py`: Includes utility functions for managing system operations.
   - `T_Matrix.py`: Defines a matrix utility class for system simulation.
   - `VisualUtils.py`: Contains visual utility functions for displaying system information.

2. `KripkeStructureFramework`: Contains files related to the Kripke structure framework.
   - `Node.py`: Implements the Node class for representing nodes in the Kripke structure.
   - `KripkeStructure.py`: Provides the KripkeStructure class for managing the Kripke structure.

3. `GUI`: Contains files related to the graphical user interface.
   - `Screens`: Contains classes for the sub-screens of the GUI.
   - `UI`: Includes all the UI files for the GUI.

## Getting Started

To run the BMC Via Simulation project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/BMC-Via-Simulation.git`
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Open `MainWindow.py` and run it to start the GUI.

