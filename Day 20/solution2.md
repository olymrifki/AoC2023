```
The question of this problem is:
what is the fewest number of button presses required to deliver a single low pulse to the module named rx?

I dont know the right algorithm
But after manual inspection
rx will be low if xd, ts, pf, and vr is all low

somehow a least common multiplier
of  3877 3769 3833 3917
is equal to the right answer
219388737656593


3877 3769 3833 3917
is like a sub problem in a way,

i can calculate when xd is low. There are 7 input to xd, somehow it can get low until the 6th low at 3877 pressings. And never seems to reach low again (or calculation is too high for my time)

then this is the same for ts with 8 input, 3769 is the 7th low.
and pf with 9 input
and vr in 8 input

my guess was that this next high computational low will be the lcm of the last low computational low
and it just works.



Note:
People said these are four separate binary shift register

```
