import cv2
import numpy as np

# Color ranges for each face
color_ranges = {
    'green': ([35, 100, 50], [85, 255, 255]),
    'red': ([0, 100, 100], [10, 255, 255]),
    'blue': ([100, 100, 50], [130, 255, 255]),
    'orange': ([5, 100, 100], [15, 255, 255]),
    'white': ([0, 0, 200], [180, 50, 255]),
    'yellow': ([20, 100, 100], [30, 255, 255]),
}

def detect_colors(image):
    # Convert image to HSV color space
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    detected_colors = {}

    for color, (lower_range, upper_range) in color_ranges.items():
        # Create a mask using color ranges
        mask = cv2.inRange(hsv, np.array(lower_range), np.array(upper_range))

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Get the largest contour as the color region
        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
            detected_colors[color] = largest_contour

    return detected_colors

def manually_correct_colors(detected_colors):
    corrected_colors = detected_colors.copy()

    print("Detected colors:")
    for color, contour in detected_colors.items():
        print(f"{color}: {contour}")

    print("\nDo you want to correct any colors? (yes/no)")
    user_response = input()

    if user_response.lower() == 'yes':
        for color in corrected_colors:
            print(f"Correcting {color} color:")
            new_contour = input(f"Enter new contour values (comma-separated): ")
            corrected_colors[color] = list(map(int, new_contour.split(',')))
    #if user writes no, detected_colors will be the same as corrected_colors, the code continues

    return corrected_colors
class RubiksCube:
    def __init__(self):
        self.faces = {
            #up, down, left,...
            'U': [['w' for _ in range(3)] for _ in range(3)],
            'D': [['y' for _ in range(3)] for _ in range(3)],
            'L': [['g' for _ in range(3)] for _ in range(3)],
            'R': [['b' for _ in range(3)] for _ in range(3)],
            'F': [['r' for _ in range(3)] for _ in range(3)],
            'B': [['o' for _ in range(3)] for _ in range(3)],
        }
        
    def main():
        image_paths = {
            'green': 'green.jpg',
            'red': 'red.jpg',
            'blue': 'blue.jpg',
            'orange': 'orange.jpg',
            'white': 'white.jpg',
            'yellow': 'yellow.jpg',
        }

        detected_colors = {}

#storing user's colors
        for color, path in image_paths.items():
            image = cv2.imread(path)
            detected_colors[color] = detect_colors(image)

        corrected_colors = manually_correct_colors(detected_colors)
        

        cube = RubiksCube()
        cube.set_colors(corrected_colors)

#storing the colors in a string
    def set_colors(self, corrected_colors):
        for color, contour in corrected_colors.items():
            row, col = contour
            self.faces[color][row][col] = color[0]  # Use the first letter of the color as the face label
            
    
#storing the cubes state in a string
    def __str__(self):
        cube_str = ""
        for i in range(3):
            for face in ['U', 'L', 'F', 'R', 'B', 'D']:
                cube_str += ' '.join(self.faces[face][i]) + '   '
            cube_str += '\n'
        return cube_str

#These methods provide a way to simulate movements that aren't covered by the basic face rotations and inverses
#By using these twist methods, you can manipulate specific rows, columns, or layers of the cube
#    def horizontal_twist(self, row, direction):
#        if row < len(self.faces[0]):
#            if direction == 0:  # Twist left
#                self.faces[1][row], self.faces[2][row], self.faces[3][row], self.faces[4][row] = (
#                    self.faces[2][row], self.faces[3][row], self.faces[4][row], self.faces[1][row]
#                )
#            elif direction == 1:  # Twist right
#                self.faces[1][row], self.faces[2][row], self.faces[3][row], self.faces[4][row] = (
#                    self.faces[4][row], self.faces[1][row], self.faces[2][row], self.faces[3][row]
#                )
#            else:
#                raise ValueError('ERROR - direction must be 0 (left) or 1 (right)')
#            
#            if direction == 0:  # Twist left
#                if row == 0:
#                    self.faces[0] = [list(x) for x in zip(*reversed(self.faces[0]))]
#                elif row == len(self.faces[0]) - 1:
#                    self.faces[5] = [list(x) for x in zip(*reversed(self.faces[5]))]
#            elif direction == 1:  # Twist right
#                if row == 0:
#                    self.faces[0] = [list(x) for x in zip(*self.faces[0])][::-1]
#                elif row == len(self.faces[0]) - 1:
#                    self.faces[5] = [list(x) for x in zip(*self.faces[5])][::-1]
#        else:
#            raise ValueError(f'ERROR - desired row outside of Rubik\'s cube range. Please select a row between 0-{len(self.faces[0])-1}')
#
#    def vertical_twist(self, col, direction):
#        if col < len(self.faces[0]):
#            if direction == 0:  # Twist up
#                rotated_column = [self.faces[row][col] for row in range(len(self.faces))]
#                rotated_column = rotated_column[1:] + [rotated_column[0]]
#                for row in range(len(self.faces)):
#                    self.faces[row][col] = rotated_column[row]
#            elif direction == 1:  # Twist down
#                rotated_column = [self.faces[row][col] for row in range(len(self.faces))]
#                rotated_column = [rotated_column[-1]] + rotated_column[:-1]
#                for row in range(len(self.faces)):
#                    self.faces[row][col] = rotated_column[row]
#            else:
#                raise ValueError('ERROR - direction must be 0 (up) or 1 (down)')
#        else:
#            raise ValueError(f'ERROR - desired column outside of Rubik\'s cube range. Please select a column between 0-{len(self.faces)-1}')
#
#    def side_twist(self, depth, direction):
#        if depth < len(self.faces):
#            if direction == 0:  # Twist left
#                rotated_layer = self.faces[depth][:]
#                for row in range(len(self.faces)):
#                    self.faces[row][depth] = rotated_layer[row]
#            elif direction == 1:  # Twist right
#                rotated_layer = self.faces[depth][:]
#                for row in range(len(self.faces)):
#                    self.faces[row][depth] = rotated_layer[-1]
#                    rotated_layer = [rotated_layer[-1]] + rotated_layer[:-1]
#            else:
#                raise ValueError('ERROR - direction must be 0 (left) or 1 (right)')
#        else:
#            raise ValueError(f'ERROR - desired depth outside of Rubik\'s cube range. Please select a depth between 0-{len(self.faces)-1}')
#
#    def rotate_face_clockwise(self, face):
#        self.cube[face] = [list(row) for row in zip(*self.cube[face][::-1])]
#
#    def rotate_face_counter_clockwise(self, face):
#        self.cube[face] = [list(row[::-1]) for row in zip(*self.cube[face])]

#This algorithm assumes that the cube's initial state has the white cross already oriented correctly
    def solve_bottom_cross(self):
        # Solve the bottom layer cross
        front_color = self.cube[2][1][1]
        back_color = self.cube[4][1][1]
        left_color = self.cube[3][1][1]
        right_color = self.cube[5][1][1]

        moves = []

        # Find the matching edge pieces and rotate them to the bottom layer
        if self.cube[1][0][1] == front_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        elif self.cube[1][1][0] == left_color:
            self.rotate_face_counter_clockwise(5)
            moves.append("L'")
        elif self.cube[1][1][2] == right_color:
            self.rotate_face_clockwise(5)
            moves.append("R")
        elif self.cube[1][2][1] == back_color:
            self.rotate_face_counter_clockwise(0)
            moves.append("U'")

        # Rotate the bottom face to align the cross
        while self.cube[1][2][1] != front_color:
            self.rotate_face_clockwise(0)
            moves.append("U")

        print("Moves to solve the bottom cross:", " ".join(moves))


    def solve_first_layer(self):
        # Solve the first layer corners
        front_color = self.cube[2][1][1]
        back_color = self.cube[4][1][1]
        left_color = self.cube[3][1][1]
        right_color = self.cube[5][1][1]

        moves = []

        # Solve front-left corner
        while self.cube[0][2][0] != front_color or self.cube[3][0][2] != left_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("R U' R'")

        # Solve front-right corner
        while self.cube[0][2][2] != front_color or self.cube[5][0][0] != right_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("L' U L")

        # Solve back-right corner
        while self.cube[0][0][2] != back_color or self.cube[5][0][2] != right_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("L U' L'")

        # Solve back-left corner
        while self.cube[0][0][0] != back_color or self.cube[3][0][0] != left_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("R' U R")

        print("Moves to solve the first layer:", " ".join(moves))


    def solve_second_layer(self):
        # Solve the second layer edges
        front_color = self.cube[2][1][1]
        left_color = self.cube[3][1][1]
        right_color = self.cube[5][1][1]
        back_color = self.cube[4][1][1]

        moves = []

        # Solve front-left edge
        while self.cube[0][1][0] != front_color or self.cube[3][1][2] != left_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("F U' F'")

        # Solve front-right edge
        while self.cube[0][1][2] != front_color or self.cube[5][1][0] != right_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("F' U F")

        # Solve back-right edge
        while self.cube[0][0][1] != back_color or self.cube[5][2][0] != right_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("B U' B'")

        # Solve back-left edge
        while self.cube[0][2][1] != back_color or self.cube[3][2][0] != left_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("B' U B")

        print("Moves to solve the second layer:", " ".join(moves))

    def solve_top_cross(self):
        # Solve the top layer cross
        front_color = self.cube[2][1][1]
        back_color = self.cube[4][1][1]
        left_color = self.cube[3][1][1]
        right_color = self.cube[5][1][1]

        moves = []

        # Orient front edge
        while self.cube[1][0][1] != front_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("F U R U' R' F'")

        # Orient right edge
        while self.cube[1][1][2] != right_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("R U F U' F' R'")

        # Orient back edge
        while self.cube[1][2][1] != back_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("B U L U' L' B'")

        # Orient left edge
        while self.cube[1][1][0] != left_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("L U B U' B' L'")

        print("Moves to solve the top cross:", " ".join(moves))


    def solve_top_corners(self):
        # Solve the top layer corners
        front_color = self.cube[2][1][1]
        back_color = self.cube[4][1][1]

        moves = []

        # Position and orient front-left corner
        while self.cube[0][2][0] != front_color or self.cube[3][0][2] != back_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("R U R' U' R U U R'")

        # Position and orient front-right corner
        while self.cube[0][2][2] != front_color or self.cube[5][0][0] != back_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("U R U R' U' R U U R' U'")

        # Position and orient back-right corner
        while self.cube[0][0][2] != back_color or self.cube[5][0][2] != front_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("U R U R' U' R U U R' U'")

        # Position and orient back-left corner
        while self.cube[0][0][0] != back_color or self.cube[3][0][0] != front_color:
            self.rotate_face_clockwise(0)
            moves.append("U")
        moves.append("U R U R' U' R U U R' U'")

        print("Moves to solve the top corners:", " ".join(moves))

    def solve_final_layer(self):
        # Solve the final layer permutation
        moves = []

        # Orient the last layer edges
        while self.cube[1][0][1] != self.cube[1][1][1] or \
              self.cube[1][1][0] != self.cube[1][1][1] or \
              self.cube[1][1][2] != self.cube[1][1][1] or \
              self.cube[1][2][1] != self.cube[1][1][1]:
            self.rotate_face_clockwise(0)
            moves.append("U")
        while self.cube[1][0][1] != self.cube[1][1][1]:
            self.rotate_face_clockwise(5)
            moves.append("U")
        moves.append("R U R' U R U U R' U'")

        # Permute the last layer edges
        while self.cube[1][0][2] != self.cube[1][1][1] or \
              self.cube[1][2][2] != self.cube[1][1][1]:
            self.rotate_face_clockwise(0)
            moves.append("U")
        while self.cube[1][0][2] != self.cube[1][1][1]:
            self.rotate_face_clockwise(5)
            moves.append("U")
        moves.append("U R U R' U' R U U R' U'")

        print("Moves to solve the final layer:", " ".join(moves))

    cube = RubiksCube()
    
    cube.set_colors(corrected_colors)
    
    cube.solve_bottom_cross()

    cube.solve_first_layer()

    cube.solve_second_layer()

    cube.solve_top_corners()

    cube.solve_final_layer()


    # Print the state of the cube
    print(cube)

if __name__ == "__main__":
    main()
