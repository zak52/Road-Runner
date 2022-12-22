# Road-Runner

Welcome to the Road Runner project!

This project is designed to take in a map and use AI techniques to find the shortest path from one point on the map to another. The solution is then outputted as a series of steps that can be followed to navigate from the starting point to the destination.

To use the Road Runner, you will need to have Python 3 and the following dependencies installed:

    *NumPy
    *OpenCV (optional, if you want to use the map visualization feature)


Once you have these dependencies installed, you can clone the repository and navigate to the root directory. From there, you can run the Road Runner by using the following command:


    python main.py <path_to_map> <start_x> <start_y> <end_x> <end_y>

The Road Runner will then process the map and output the solution in the form of a series of steps. If you want to visualize the map and the solution, you can pass the --visualize flag to the command:

    python main.py <path_to_map> <start_x> <start_y> <end_x> <end_y> --visualize

We hope you find this project helpful and enjoyable to use! If you have any issues or suggestions for improvement, please don't hesitate to open an issue on the GitHub page.