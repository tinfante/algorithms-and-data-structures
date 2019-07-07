# Depth-first & Breadth-first Search on a Random Maze

Comment/uncomment lines 97-98 for depth-first or breadth-first.

Uncomment line 116 to save frames. Then, in the `frames/` directory run
`ffmpeg -i %04d.png output.gif` to make an animated gif.

With a sparseness value of 0.2 it's likely that there is a path between the
starting position and the goal.

Note that breadth-first, although slower, always includes the shortest path
between the starting cell and the goal. Here depth-first is especially
effective because it goes south-east (the direction to the goal from the
starting position). It wouldn't preform as well if the starting and goal
positions were switched.

## Depth-first

![Depth-first Random Maze](https://github.com/tinfante/algorithms-and-data-structures/blob/master/Problems/Maze/depth-first.gif)

## Breadth-first

![Breadth-first Random Maze](https://github.com/tinfante/algorithms-and-data-structures/blob/master/Problems/Maze/breadth-first.gif)
