```
Given 2d map that contains empty space (.), mirrors (/ and \), and splitters (| and -) and beam that enters the map from top left to the right direction

>>>>.|...\....
    |.-.\.....
    .....|-...
    ........|.
    ..........
    .........\
    ..../.\\..
    .-.-/..|..
    .|....-|.\
    ..//.|....
mirror will reflect beam at 90 degree
and splitter split beam that enters its flat side into two beam at each pointy directions

calculate number of tile (including mirror and splitter) that passed through by the beam

answer : 46

Steps:
1. Read inputs and set outputs to all 0s with the same size as input map
2. Create list of beam with first element at top left to the right. Each beam will know its position and direction
    2.1 Beam creation will mark output map to 1  at its position
    2.2 To move the beam:
        remove beam from list
        for each beam:
            get tile in its position
            if position is possible:
                create new tile(s) with its direction and position
            add it to list of beam
3. Add all output map
```
