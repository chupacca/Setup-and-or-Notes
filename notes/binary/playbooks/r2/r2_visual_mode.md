# VISUAL MODE
    
[Visual Mode]: V
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> V

* Hit `q` twice to go back to terminal mode
* Hit `Space` to toggle to graph mode
```

[Graph Mode]: VV
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> VV

* Hit `q` TWICE to go back to terminal mode
* Hit `Space` to toggle to visual mode
```

[Visual Debugger]: Vpp
```TODO
Haven't tested this yet
```

[Panel Mode]: V!
```
[]> aaaa    ; analyze
[]> s main  ; seek to main
[]> V!

* you can  use `TAB` to switch among panels
* when in another panel, hit `"` to choose what that panel shows
* you can hit `-` to split a panel
* you can hit `X` to close a panel
* hit `z` to make the current window to the top left panel
* There's a tollbar on the top you can use your mouse on
   (then use arrow keys and Enter)
```

+ Switching _decompiler_ in a pane
 - Set a window to `Decompiler` with the `"` command
 - Then hit `e` and you should be prompted with `[Status] New command:`
 - Enter either `pddo` or `pdgo`
 
 
 
[Notes]:

1. When in VISUAL mode, hit `q` to go BACK TO TERMINAL MODE!!!!!
   [Quit]: q -> to go back to command window
   * may need to hit `q` twice if VV is used!!!!!!!!!!!!!!!!!!!!

2. You can change what type of visual mode by hitting `p`
[Change mode]: p
   - p  ; changes go one way
   - P  ; changes go the other way

3. Move from block to block with
   * `TAB`
   * `Shift+TAB`
   
4. Note that you can click the colon `:` to enter
    commands while in visual mode


5. In Visual Mode you can:
  + Regular move: `mouse` or `arrow keys`
   - For faster movement, hold `Shift` while doing this

  + Move like VIM:
   - `j` for down
   - `k` for up
   - `h`for left
   - `l` for right

   - For faster movement, hold `Shift` while doing this


6. Go from vertical view to horizontal view:
   `Shift+V`

7. I can use h and l to shift what address I'm looking at `one byte at a time`
  + This way I can look at different types of instructions (google geometry of instructions)

```Other
 ascii flow graph (analyse: df, af, move: hjkl, resize: +-0, chg mode: pP, highlight: /)
```

