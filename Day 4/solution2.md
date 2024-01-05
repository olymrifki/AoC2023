Given list of _original card_:
Calculate total owned cards if each matching number, n, in a card will give _copy card_ from n next cards that each also give copy cards

````
```
    Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53
    Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    Card 3: 1 21 53 59 44 | 69 82 63 72 16 21 14 1
    Card 4: 41 92 73 84 69 | 59 84 76 51 58 5 54 83
    Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
```

Each _line_
```Card 1: 41 48 83 86 17 | 83 86 6 31 17 9 48 53```
Consists of _winning numbers_ and _random numbers_ to be match


We need to be able to
Get list of winning numbers and the right is list of random
Calculate _match score_:
    Compare list of _winning numbers_ to some _random numbers_ of numbers.
    For each number in _random numbers_, if the number is in the _winning numbers_, add _match score_

Main algorithm:
1.
Because this is a possibly deep recursion problem, we are using memo
To calculate _added card_ in a line:
    If line is already calculated:
        Get _added card_ from memo
    Otherwise:
        Calculate _added card_ from current line count (1)
        and add it with each next line _added card_ if _match score_ is positive, say n,
            (recursion) Add calcuate extra _added card_ from next n _copy card_ from n _line index_ below current one as if there are still lines
        Add _added card_ to memo
2.
Add each line in reversed to queue:
(Line queue is reversed so that the next line's added card value already calculated, preventing more than 2 level of recursions)
while line_queue is not empty
    pop queue for next line
    calculate added cards from poped line

after all lines get memod, add all memod card, this will be the total owned cards

*Total card*s in the example above are 30
````
