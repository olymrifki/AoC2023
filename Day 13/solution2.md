```
In this problem, there is no perfect mirror,. The mirrored image will have exactly one smudge, where # is reflected by .

The rest of the problem is still the same

The answer will be 400

Then, a match can be correct if it is exact match or one smudge
Smudge detector function to detect if two row are matching, and also return smudge:
Get row, mirrored row, and boolean containing is smudge ever happen:
    If exact match:
        return true
    If only one smudge and smudge never happen:
        return true
    return false
```
