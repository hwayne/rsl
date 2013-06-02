rsl
=====

Brainfuck with multiple registers. Named after the r-selection evolution.

To run:

1) python orgy.py {your orgy file}
2) python orgy.py, put your code into the input.

Each registry has 300 cells. You can add as many additional registries as you want.

Commands:

'> move position in registry one cell forward.
'< move position in registry one cell back.
'+ increase value of registry by 1.
'- decrease value of registry by 1.
'[ if value of position is 0, jump to matching ].
'] if not jumped to, jump to matching [.
', user input to cell.
'. output unicode value of cell.
'! output raw value of cell. Because I'm lazy.
'\* create a new registry. New registry appears at the end of the registry list.
'^ move to next register, wrapping around to the first one. If you've not been to that register before, you start at cell 0. If you have been, you start at the last location you left it.
