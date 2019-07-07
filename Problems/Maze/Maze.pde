import java.util.ArrayDeque;
//import java.util.Iterator;


int cols = 40;  // width
int rows_ = 20;  // height
int [][] maze = new int[cols][rows_];
float sparseness = 0.2;  // how many walls?
Cell startCell = new Cell(0, 0);
Cell endCell = new Cell(cols-1, rows_-1);
int cellSize = 10;
int brown = color(210, 105, 30);
int black = color(0, 0, 0);
int green_ = color(100, 255, 50);
int white = color(255, 255, 255);
int fill_with;
int wait = 100;
boolean solved = false;
ArrayDeque<Cell> stack = new ArrayDeque<Cell>();


class Cell {
  int x, y;
  public Cell (int _x, int _y) {
    x = _x;
    y = _y;
  }}


void random_maze() {
  for (int i = 0; i < cols; i++) {
    for (int j = 0; j < rows_; j++) {
      if (random(1) > sparseness) {maze[i][j] = 0;}
      else {maze[i][j] = 1;}
    }}}


void get_neighbours(Cell cell) {
  if (cell.x - 1 >= 0 &&
      maze[cell.x-1][cell.y] != 1 &&
      maze[cell.x-1][cell.y] != 4) {
    stack.addLast(new Cell(cell.x - 1, cell.y));
    maze[cell.x-1][cell.y] = 4;
  }
  if (cell.y - 1 >= 0 &&
      maze[cell.x][cell.y-1] != 1 &&
      maze[cell.x][cell.y-1] != 4) {
    stack.addLast(new Cell(cell.x, cell.y - 1));
    maze[cell.x][cell.y-1] = 4;
  }
  if (cell.x + 1 < cols &&
      maze[cell.x+1][cell.y] != 1 &&
      maze[cell.x+1][cell.y] != 4) {
    stack.addLast(new Cell(cell.x + 1, cell.y));
    maze[cell.x+1][cell.y] = 4;
  }
  if (cell.y + 1 < rows_ &&
      maze[cell.x][cell.y+1] != 1 &&
      maze[cell.x][cell.y+1] != 4) {
    stack.addLast(new Cell(cell.x, cell.y + 1));
    maze[cell.x][cell.y+1] = 4;
  }
}


void settings() {
  size(cols*cellSize, rows_*cellSize);
}


void setup() {
  random_maze();
  maze[startCell.x][startCell.y] = 2;
  maze[endCell.x][endCell.y] = 3;
  for (int i = 0; i < cols; i++) {
    for (int j = 0; j < rows_; j++) {
      if (maze[i][j] == 0) {
        fill_with = black;
      }
      else if (maze[i][j] == 1) {
        fill_with = brown;
      }
      else if (maze[i][j] == 2 || maze[i][j] == 3) {
        fill_with = white;
      }
      fill(fill_with);
      rect(i*cellSize, j*cellSize, cellSize, cellSize);
    }}
  stack.addFirst(startCell);
  maze[startCell.x][startCell.y] = 4;
}


void draw() {

  if (stack.size() > 0) {
    //Cell currCell = stack.removeLast();  // depth first
    Cell currCell = stack.removeFirst();  // breadth first

    //println(currCell.x, currCell.y);

    get_neighbours(currCell);
    //Iterator<Cell> itr = stack.iterator();
    //while (itr.hasNext()) {
      //Cell c = itr.next();
      //print(c.x, ",", c.y, "    ");
    //}
    //println("\n");

    fill(solved ? green_ : white);
    rect(currCell.x*cellSize, currCell.y*cellSize, cellSize, cellSize);

    if (currCell.x == endCell.x && currCell.y == endCell.y) {
      solved = true;
    }
    //saveFrame("frames/####.png");
    delay(wait);
  }
  else {
    exit();
  }
}
