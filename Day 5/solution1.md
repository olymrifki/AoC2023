```
Given:
    1. list of type of initial source category
        "seeds: 79 14 55 13"
    2. many list of convertion from source to destination
        "seed-to-soil map:
        50 98 2
        52 50 48

        soil-to-fertilizer map:
        0 15 37
        37 52 2
        39 0 15"

        Conversion:
        This list consists of *destination start*, *source start*, and *map range*
        If source number is in range, the converted destination number is a 1 to 1 map inside of the range
        otherwise, the sourec number is the same as destination number

Find the smallest value of the final destination number
```

```
To do:
1. Convert initial source line to number
2. Convert map line to number
    2.1 Convert multiple map line to list of map
        detect starting non number line and blank stopping line
    2.2 For each map:
        Conversion will be
        destination = (source-source_start) > map_range? source
                    : destination_start + (source-source_start)
        for all maps
3. Connvert and find smallest destination

```
