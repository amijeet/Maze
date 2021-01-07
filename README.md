[![HitCount](http://hits.dwyl.com/amijeet/Maze.svg)](http://hits.dwyl.com/amijeet/Maze)
<!-- PROJECT LOGO -->
<p align="center">
  <a href="https://en.wikipedia.org/wiki/Maze_generation_algorithm">
    <img src="images/mazeLogo.jpg" alt="Logo" width="100" height="100">
  </a>

  <h1 align="center">Visualization of maze generating algorithms</h1>

  <p align="center">
    A pathfinding visualizer project to generate random mazes!
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

In this project I have implemented a small visualization of how random mazes can be generated using a recursive depth first search. I have made this project using only python3. 
Starting from a random cell, the computer then selects a random neighbouring cell that has not yet been visited. The computer removes the wall between the two cells and marks the new cell as visited, and adds it to the stack to facilitate backtracking. The computer continues this process, with a cell that has no unvisited neighbours being considered a dead-end. When at a dead-end it backtracks through the path until it reaches a cell with an unvisited neighbour, continuing the path generation by visiting this new, unvisited cell (creating a new junction). This process continues until every cell has been visited, causing the computer to backtrack all the way back to the beginning cell. We can be sure every cell is visited.
Pseudo code:
1. Given a current cell as a parameter,
2. Mark the current cell as visited
3. While the current cell has any unvisited neighbour cells
    1. Choose one of the unvisited neighbours
    2. Remove the wall between the current cell and the chosen cell
    3. Invoke the routine recursively for a chosen cell

[![Product GIF][product-GIF]](https://en.wikipedia.org/wiki/Maze_generation_algorithm)

<!-- USAGE EXAMPLES -->
## How to use

Just run the python script to see the visualization of a random maze using recursive depth first search.

<!-- CONTACT -->
## Contact

Amijeet Thakur - [amijeetthakur@gmail.com](mailto:amijeetthakur@gmail.com)

Project Link: [https://github.com/amijeet/Maze](https://github.com/amijeet/Maze)

<!-- MARKDOWN LINKS & IMAGES -->

[product-GIF]: images/generatingMazeGIF.gif
