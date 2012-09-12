import processing.opengl.*;

class Txyz {
 float t;
 float x;
 float y; 
 float z;
 // 1 parameter functions
 float tw;
 float xw;
 float yw;
 float zw;
 
 Txyz(float tPos, float xPos, float yPos, float zPos) {
   t = tPos;
   x = xPos;
   y = yPos;
   z = zPos;
 }
 Txyz(float tPos) {
   t = tPos;
   x = 0;
   y = 0;
   z = 0;
 }
}
