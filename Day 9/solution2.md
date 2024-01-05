```
This time, we predict the previous element, the 0th element (assuming starting from 1st element)

from
diff = next - current
to get next element
next = diff+current

and this next element will be used as diff for its generator sequence (parent sequence)
next = (diff' + current') + current
where ' in current' represent current from the child sequence
this was used in solution 1

from
diff = curernt - prev
to get previous elemet
prev = current - diff

by doing the same
prev = current - (current' - diff')

therefore, we will save the first element and alternating + and - from the next sequence

the rest of the steps are the same
```
