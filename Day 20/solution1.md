```
Given modules that can send *high pulse* or *low pulse* to its *destination modules*

Types of modules:
1. Flip-flop (Prefix %)
    - Initially off
    - If off and receive low pulse: turn on and send a high pulse
    - If on and reveive low pulse: turn off and send a low pulse
2. Conjunction (Prefix &)
    - It can remember last pulse from all its input modules
    - Initially all input remebered as low pulse
    - When a pulse is received:
        - update its memories for that input
        - If this new memories are all high pulses: send a low pulse
            otherwise send a high pulse
3. Broadcast module (there is only one, always named broadcaster)
    - When revieve a pulse: send the same pulse to all of its destination modules
4. Button module
    - Send a low pulse to the broadcaster

We will have to press the button 1000 times, but we have to wait until all pulses are sent by all module before pressing again. During this process, *record* the number of low and high pulses sent (including the button's pulse). After 1000th process are over, multiply the number of high and low pulse, this is the answer needed.

Pulses are always processed in the order they are sent. If a module1 send pulses to module2 and module3, it send it to them first before module2 and module3 process it.

Ex1:

broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a

answer: 32000000

Ex2:

broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output

answer: 11687500

Steps:
0. Read all input and create module dictionary hashed by its name (after prefix)
1. Create class for broadcaster, flip-flop, and conjunction modules
2. Each class can *recieve a pulse* and schedule the broadcasted pulse into a buffer
3. Initially, the buffer will be sending low pulse into broadcaster (this is why we dont create button module)
4. Record each pulse that happen when reading the buffer
5. After the buffer is emptied, one cycle is done. Add low and high pulse count to button push score, reset the pulse count.
6. Calculate score.

Left out:
module name is not in the list, ignore it, but signal still count

```
