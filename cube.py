# cube.py
# DEVELOPER: SYED EBTISAM ALI

# =========================
# CUBE STRUCTURE
# =========================

CUBE = [
    ['W','W','W','W','W','W','W','W','W'],  # 0 - Up
    ['G','G','G','G','G','G','G','G','G'],  # 1 - Front
    ['Y','Y','Y','Y','Y','Y','Y','Y','Y'],  # 2 - Down
    ['B','B','B','B','B','B','B','B','B'],  # 3 - Back
    ['R','R','R','R','R','R','R','R','R'],  # 4 - Right
    ['O','O','O','O','O','O','O','O','O']   # 5 - Left
] 
# NOTE:
""" 0 --> 1 --> 2 --> 3 --> 4 --> 1 --> 5"""
""" W --> G --> Y --> B --> R --> G --> O"""

# =========================
# DISPLAY FUNCTION
# =========================

def display_cube(cube):
    print(f"{    " "   } {    " "   } {    " "   }   {cube[0][0]} {cube[0][1]} {cube[0][2]}   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }")
    print(f"{    " "   } {    " "   } {    " "   }   {cube[0][3]} {cube[0][4]} {cube[0][5]}   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }")
    print(f"{    " "   } {    " "   } {    " "   }   {cube[0][6]} {cube[0][7]} {cube[0][8]}   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }")
    print(f"{    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }")
    print(f"{cube[5][0]} {cube[5][1]} {cube[5][2]}   {cube[1][0]} {cube[1][1]} {cube[1][2]}   {cube[4][0]} {cube[4][1]} {cube[4][2]}   {cube[3][0]} {cube[3][1]} {cube[3][2]}")
    print(f"{cube[5][3]} {cube[5][4]} {cube[5][5]}   {cube[1][3]} {cube[1][4]} {cube[1][5]}   {cube[4][3]} {cube[4][4]} {cube[4][5]}   {cube[3][3]} {cube[3][4]} {cube[3][5]}")
    print(f"{cube[5][6]} {cube[5][7]} {cube[5][8]}   {cube[1][6]} {cube[1][7]} {cube[1][8]}   {cube[4][6]} {cube[4][7]} {cube[4][8]}   {cube[3][6]} {cube[3][7]} {cube[3][8]}")
    print(f"{    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }")
    print(f"{    " "   } {    " "   } {    " "   }   {cube[2][0]} {cube[2][1]} {cube[2][2]}   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }")
    print(f"{    " "   } {    " "   } {    " "   }   {cube[2][3]} {cube[2][4]} {cube[2][5]}   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }")
    print(f"{    " "   } {    " "   } {    " "   }   {cube[2][6]} {cube[2][7]} {cube[2][8]}   {    " "   } {    " "   } {    " "   }   {    " "   } {    " "   } {    " "   }")
    print("\n")


# =========================
# FACE ROTATION
# =========================

def rotate_face(cube, face):

    f = cube[face][:]

    cube[face][0] = f[6]
    cube[face][1] = f[3]
    cube[face][2] = f[0]
    cube[face][3] = f[7]
    cube[face][4] = f[4]
    cube[face][5] = f[1]
    cube[face][6] = f[8]
    cube[face][7] = f[5]
    cube[face][8] = f[2]


# =========================
# MOVES
# =========================

# -------- U --------
def U(cube):
    rotate_face(cube, 0)

    a = cube[1][0]; b = cube[1][1]; c = cube[1][2]
    d = cube[4][0]; e = cube[4][1]; f = cube[4][2]
    g = cube[3][0]; h = cube[3][1]; i = cube[3][2]
    j = cube[5][0]; k = cube[5][1]; l = cube[5][2]

    cube[1][0] = d; cube[1][1] = e; cube[1][2] = f
    cube[4][0] = g; cube[4][1] = h; cube[4][2] = i
    cube[3][0] = j; cube[3][1] = k; cube[3][2] = l
    cube[5][0] = a; cube[5][1] = b; cube[5][2] = c


# -------- D --------
def D(cube):
    rotate_face(cube, 2)

    a = cube[1][6]; b = cube[1][7]; c = cube[1][8]
    d = cube[5][6]; e = cube[5][7]; f = cube[5][8]
    g = cube[3][6]; h = cube[3][7]; i = cube[3][8]
    j = cube[4][6]; k = cube[4][7]; l = cube[4][8]

    cube[1][6] = d; cube[1][7] = e; cube[1][8] = f
    cube[5][6] = g; cube[5][7] = h; cube[5][8] = i
    cube[3][6] = j; cube[3][7] = k; cube[3][8] = l
    cube[4][6] = a; cube[4][7] = b; cube[4][8] = c


# -------- R --------
def R(cube):
    rotate_face(cube, 4)

    a = cube[0][2]; b = cube[0][5]; c = cube[0][8]
    d = cube[1][2]; e = cube[1][5]; f = cube[1][8]
    g = cube[2][2]; h = cube[2][5]; i = cube[2][8]
    j = cube[3][6]; k = cube[3][3]; l = cube[3][0]

    cube[0][2] = d; cube[0][5] = e; cube[0][8] = f
    cube[1][2] = g; cube[1][5] = h; cube[1][8] = i
    cube[2][2] = j; cube[2][5] = k; cube[2][8] = l
    cube[3][6] = a; cube[3][3] = b; cube[3][0] = c


# -------- L --------
def L(cube):
    rotate_face(cube, 5)

    a = cube[0][0]; b = cube[0][3]; c = cube[0][6]
    d = cube[3][8]; e = cube[3][5]; f = cube[3][2]
    g = cube[2][0]; h = cube[2][3]; i = cube[2][6]
    j = cube[1][0]; k = cube[1][3]; l = cube[1][6]

    cube[0][0] = d; cube[0][3] = e; cube[0][6] = f
    cube[3][8] = g; cube[3][5] = h; cube[3][2] = i
    cube[2][0] = j; cube[2][3] = k; cube[2][6] = l
    cube[1][0] = a; cube[1][3] = b; cube[1][6] = c


# -------- F --------
def F(cube):
    rotate_face(cube, 1)

    a = cube[0][6]; b = cube[0][7]; c = cube[0][8]
    d = cube[4][0]; e = cube[4][3]; f = cube[4][6]
    g = cube[2][2]; h = cube[2][1]; i = cube[2][0]
    j = cube[5][8]; k = cube[5][5]; l = cube[5][2]

    cube[0][6] = j; cube[0][7] = k; cube[0][8] = l
    cube[4][0] = a; cube[4][3] = b; cube[4][6] = c
    cube[2][2] = d; cube[2][1] = e; cube[2][0] = f
    cube[5][8] = g; cube[5][5] = h; cube[5][2] = i


# -------- B --------
def B(cube):
    rotate_face(cube, 3)

    a = cube[0][0]; b = cube[0][1]; c = cube[0][2]
    d = cube[5][6]; e = cube[5][3]; f = cube[5][0]
    g = cube[2][8]; h = cube[2][7]; i = cube[2][6]
    j = cube[4][2]; k = cube[4][5]; l = cube[4][8]

    cube[0][0] = j; cube[0][1] = k; cube[0][2] = l
    cube[5][6] = a; cube[5][3] = b; cube[5][0] = c
    cube[2][8] = d; cube[2][7] = e; cube[2][6] = f
    cube[4][2] = g; cube[4][5] = h; cube[4][8] = i


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    display_cube(CUBE)

    F(CUBE)
    R(CUBE)
    U(CUBE)

    display_cube(CUBE)