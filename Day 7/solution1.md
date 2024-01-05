```
Given hands and bids:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

Rank each hand based on a rule (highest hand get highest rank number)
Then multiply the rank with its bid and sum them

The answer here is 6440

Rule:
Hands will be compared based on type:
    from strongest to weakest:
        five of a kind, four of a kind, full house, three of a kind, two pair, one pair, and high card
if hands have equal type strength:
    compare from left to right:
        compare each card, hand with bigger card will win right away

Steps:
1. Read each line into hand and bid
2. Add comparison to card:
    2.1 Determine type strength of a card
    2.2 Determine ordered card strength
3. Sort card, sum the multiplied index+1 with its bids

```
