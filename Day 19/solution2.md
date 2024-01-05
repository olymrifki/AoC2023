```
In this problem, each label x, m, a, s can have values between [1,4000] (there are total of 4000^4 parts). We need to calculate how many parts will be accepted through the containers

the examples answer will be 167409079868000

I think the overall structure of the code can be the same,
except the representation of the parts

Each part still be dictionary containing its range (ex: {"x":[1:300], ...})

We can imagine each rule is possibly going to be slicing the part into two parts
one part will go the next container and the other will continue
    The part that will go to the next container will be saved in some buffer before being processed later. Initial buffer: [("in",{"x":[1,4000],"m":[1,4000],"a":[1,4000],"s":[1,4000]})]
    we keep processing until the buffer is empty (all parts into A or R)

In combination calculation:
    In a part range, the total part count will be the product if each x,m,a,s possible combination
    Sum all part counts
```
