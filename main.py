# main.py
import cube

def main():
    # Initialize the cube
    my_cube = cube.CUBE
    # Display the Cube
    cube.display_cube(my_cube)
    # Apply some moves
    cube.R(my_cube)
    cube.U(my_cube)
    cube.F(my_cube)
    # Display the Cube after moves
    cube.display_cube(my_cube)

if __name__ == "__main__":
    main()