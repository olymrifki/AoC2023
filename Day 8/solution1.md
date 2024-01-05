```
Given sequence of steps and nodes

LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)

count how many steps needed to go from AAA to ZZZ.
Here, from AAA we take L to BBB then L to AAA then R to BBB then the steps loop with L to AAA then L to BBB then R to ZZZ with total of 6 steps


Steps:
1. Read input to store sequence of steps and nodes
    1.1 Each node will have L and R nodes
    1.2 Save node AAA
2. starting from node AAA:
    2.1 Follow each step. In each step, add step count,
    2.2 then check if this next node is ZZZ. If so, end follow




```
