void setup() {
  size(80, 80, OPENGL);
  noStroke();
  lights();
  frameRate(300);
}

void draw() {
 background(3);
 translate(10, 10, 0);
 if(frameCount > 0){
   sphere(3); 
 }
 translate(10, 0, 0);
 if(frameCount % 2 == 0){
   sphere(3); 
 }
 translate(10, 0, 0);
 if(frameCount % 4 == 0){
   sphere(3); 
 }
 translate(10, 0, 0);
  if(frameCount % 8 == 0){
   sphere(3); 
 }
 translate(10, 0, 0);
  if(frameCount % 16 == 0){
   sphere(3); 
 }
 translate(10, 0 , 0);
  if(frameCount % 32 == 0){
   sphere(3); 
 }
}
