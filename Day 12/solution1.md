```
Given lines with . and # and list of number that tells number of consecutive # in each respective line. And given ? that can be filled with . or #. Count how many arrangement of . and # that satisfy the number beside each. Then add all of them

???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1

answer here is 21


Steps:
1. Real line, separate . and #s with its group number
2. For each line,
    Add . at both sides of the line
    2.1 Get first group number
        Say group number of n: Create window of size n+2 containing ".#*n."
        If window length is more than inserted line:
            return 0
        If group number is empty:
            If no # in line return 1
            otherwise return 0
        Set result to 0
        Read from left to right:
            If line slot has any #:
                stop search after that first # disappear
            If Window can fits that line slot:
                Add result with Step2 with line starting from left_index + n+2
        return result
    2.2 To compare window:
        For each string in window and cropped line:
            if ith crpped element is ? or ith cropped element equals ith elementof window:
                continue
            else return false
        return true
3. Add the result


Comment:
I missed a step (or edge case) in this day:
    # stop searching after the 1st "#" disappear from the searched line
So i had to see other people's solution and try to match the result to mine, i didnt copy the logic, just finding cases where i have different answer figuring out the logic from there
```
