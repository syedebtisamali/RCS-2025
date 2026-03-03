/* cube.c */
/* DEVELOPER: SYED EBTISAM ALI */

/* =========================
   CUBE STRUCTURE
   ========================= */

#include <stdio.h>

char CUBE[6][9] = {
    {'W','W','W','W','W','W','W','W','W'},  /* 0 - Up */
    {'G','G','G','G','G','G','G','G','G'},  /* 1 - Front */
    {'Y','Y','Y','Y','Y','Y','Y','Y','Y'},  /* 2 - Down */
    {'B','B','B','B','B','B','B','B','B'},  /* 3 - Back */
    {'R','R','R','R','R','R','R','R','R'},  /* 4 - Right */
    {'O','O','O','O','O','O','O','O','O'}   /* 5 - Left */
};

/* NOTE:
   0 --> 1 --> 2 --> 3 --> 4 --> 1 --> 5
   W --> G --> Y --> B --> R --> G --> O
*/


/* =========================
   DISPLAY FUNCTION
   ========================= */

void display_cube() {

    printf("            %c %c %c\n", CUBE[0][0], CUBE[0][1], CUBE[0][2]);
    printf("            %c %c %c\n", CUBE[0][3], CUBE[0][4], CUBE[0][5]);
    printf("            %c %c %c\n\n", CUBE[0][6], CUBE[0][7], CUBE[0][8]);

    printf("%c %c %c   %c %c %c   %c %c %c   %c %c %c\n",
        CUBE[5][0], CUBE[5][1], CUBE[5][2],
        CUBE[1][0], CUBE[1][1], CUBE[1][2],
        CUBE[4][0], CUBE[4][1], CUBE[4][2],
        CUBE[3][0], CUBE[3][1], CUBE[3][2]);

    printf("%c %c %c   %c %c %c   %c %c %c   %c %c %c\n",
        CUBE[5][3], CUBE[5][4], CUBE[5][5],
        CUBE[1][3], CUBE[1][4], CUBE[1][5],
        CUBE[4][3], CUBE[4][4], CUBE[4][5],
        CUBE[3][3], CUBE[3][4], CUBE[3][5]);

    printf("%c %c %c   %c %c %c   %c %c %c   %c %c %c\n\n",
        CUBE[5][6], CUBE[5][7], CUBE[5][8],
        CUBE[1][6], CUBE[1][7], CUBE[1][8],
        CUBE[4][6], CUBE[4][7], CUBE[4][8],
        CUBE[3][6], CUBE[3][7], CUBE[3][8]);

    printf("            %c %c %c\n", CUBE[2][0], CUBE[2][1], CUBE[2][2]);
    printf("            %c %c %c\n", CUBE[2][3], CUBE[2][4], CUBE[2][5]);
    printf("            %c %c %c\n\n", CUBE[2][6], CUBE[2][7], CUBE[2][8]);
}


/* =========================
   FACE ROTATION
   ========================= */

void rotate_face(int face) {

    char f[9];

    for(int i = 0; i < 9; i++)
        f[i] = CUBE[face][i];

    CUBE[face][0] = f[6];
    CUBE[face][1] = f[3];
    CUBE[face][2] = f[0];
    CUBE[face][3] = f[7];
    CUBE[face][4] = f[4];
    CUBE[face][5] = f[1];
    CUBE[face][6] = f[8];
    CUBE[face][7] = f[5];
    CUBE[face][8] = f[2];
}


/* =========================
   MOVES
   ========================= */


/* -------- U -------- */
void U() {

    rotate_face(0);

    char a = CUBE[1][0], b = CUBE[1][1], c = CUBE[1][2];
    char d = CUBE[4][0], e = CUBE[4][1], f = CUBE[4][2];
    char g = CUBE[3][0], h = CUBE[3][1], i = CUBE[3][2];
    char j = CUBE[5][0], k = CUBE[5][1], l = CUBE[5][2];

    CUBE[1][0]=d; CUBE[1][1]=e; CUBE[1][2]=f;
    CUBE[4][0]=g; CUBE[4][1]=h; CUBE[4][2]=i;
    CUBE[3][0]=j; CUBE[3][1]=k; CUBE[3][2]=l;
    CUBE[5][0]=a; CUBE[5][1]=b; CUBE[5][2]=c;
}


/* -------- D -------- */
void D() {

    rotate_face(2);

    char a=CUBE[1][6], b=CUBE[1][7], c=CUBE[1][8];
    char d=CUBE[5][6], e=CUBE[5][7], f=CUBE[5][8];
    char g=CUBE[3][6], h=CUBE[3][7], i=CUBE[3][8];
    char j=CUBE[4][6], k=CUBE[4][7], l=CUBE[4][8];

    CUBE[1][6]=d; CUBE[1][7]=e; CUBE[1][8]=f;
    CUBE[5][6]=g; CUBE[5][7]=h; CUBE[5][8]=i;
    CUBE[3][6]=j; CUBE[3][7]=k; CUBE[3][8]=l;
    CUBE[4][6]=a; CUBE[4][7]=b; CUBE[4][8]=c;
}


/* -------- R -------- */
void R() {

    rotate_face(4);

    char a=CUBE[0][2], b=CUBE[0][5], c=CUBE[0][8];
    char d=CUBE[1][2], e=CUBE[1][5], f=CUBE[1][8];
    char g=CUBE[2][2], h=CUBE[2][5], i=CUBE[2][8];
    char j=CUBE[3][6], k=CUBE[3][3], l=CUBE[3][0];

    CUBE[0][2]=d; CUBE[0][5]=e; CUBE[0][8]=f;
    CUBE[1][2]=g; CUBE[1][5]=h; CUBE[1][8]=i;
    CUBE[2][2]=j; CUBE[2][5]=k; CUBE[2][8]=l;
    CUBE[3][6]=a; CUBE[3][3]=b; CUBE[3][0]=c;
}


/* -------- L -------- */
void L() {

    rotate_face(5);

    char a=CUBE[0][0], b=CUBE[0][3], c=CUBE[0][6];
    char d=CUBE[3][8], e=CUBE[3][5], f=CUBE[3][2];
    char g=CUBE[2][0], h=CUBE[2][3], i=CUBE[2][6];
    char j=CUBE[1][0], k=CUBE[1][3], l=CUBE[1][6];

    CUBE[0][0]=d; CUBE[0][3]=e; CUBE[0][6]=f;
    CUBE[3][8]=g; CUBE[3][5]=h; CUBE[3][2]=i;
    CUBE[2][0]=j; CUBE[2][3]=k; CUBE[2][6]=l;
    CUBE[1][0]=a; CUBE[1][3]=b; CUBE[1][6]=c;
}


/* -------- F -------- */
void F() {

    rotate_face(1);

    char a=CUBE[0][6], b=CUBE[0][7], c=CUBE[0][8];
    char d=CUBE[4][0], e=CUBE[4][3], f=CUBE[4][6];
    char g=CUBE[2][2], h=CUBE[2][1], i=CUBE[2][0];
    char j=CUBE[5][8], k=CUBE[5][5], l=CUBE[5][2];

    CUBE[0][6]=j; CUBE[0][7]=k; CUBE[0][8]=l;
    CUBE[4][0]=a; CUBE[4][3]=b; CUBE[4][6]=c;
    CUBE[2][2]=d; CUBE[2][1]=e; CUBE[2][0]=f;
    CUBE[5][8]=g; CUBE[5][5]=h; CUBE[5][2]=i;
}


/* -------- B -------- */
void B() {

    rotate_face(3);

    char a=CUBE[0][0], b=CUBE[0][1], c=CUBE[0][2];
    char d=CUBE[5][6], e=CUBE[5][3], f=CUBE[5][0];
    char g=CUBE[2][8], h=CUBE[2][7], i=CUBE[2][6];
    char j=CUBE[4][2], k=CUBE[4][5], l=CUBE[4][8];

    CUBE[0][0]=j; CUBE[0][1]=k; CUBE[0][2]=l;
    CUBE[5][6]=a; CUBE[5][3]=b; CUBE[5][0]=c;
    CUBE[2][8]=d; CUBE[2][7]=e; CUBE[2][6]=f;
    CUBE[4][2]=g; CUBE[4][5]=h; CUBE[4][8]=i;
}


/* =========================
   MAIN
   ========================= */

int main() {

    display_cube();

    F();
    R();
    U();

    display_cube();

    return 0;
}