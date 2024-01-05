```
Given parts labeled x, m, a, and s
{x=787,m=2655,a=1222,s=2876}
and given container of rules which contain condition to send the parts either to next rules, accepted, or rejected.
ex{x>10:one,m<20:two,a>30:R,A}
here, if x > 10, send parts to rule container labeled "one"
R and A will be rejected or accepted

All parts has to enter from container named "in"

Example:
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}

then add all parts number in the accepted container

Answer will be 19114

Steps:
1. Read input
    1.1 Create dictionary of rules and its container
        1.1.1 Each rule container can be initialized by the conditions inside {}
        1.1.2 There is a function that accept parts and a single rule and return true or false
        1.1.3 There is a function that can runs through the entire container rule and return the next container
        1.1.4 There is a function that accept parts and pass it to "in" container untill it reaches accepted or rejected
        1.1.5 There is one accepted and rejected container
    1.2 Create list of parts dictionary
2. Run parts through containers and sum all values inside accepted container

```
