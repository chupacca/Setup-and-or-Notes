# GEF
#source /home/test/.gdbinit-gef.py

# PWNDBG
source /home/test/pwndbg/gdbinit.py
source /home/test/pwndbg/splitmind/gdbinit.py

## PWNDBG - Split screen w/ tmux & splitmind
### sudo apt install tmux
### git clone https://github.com/jerdna-regeiz/splitmind

python
import splitmind
(splitmind.Mind()
  .below(display="stack")
  #.right(display="backtrace")
  .right(display="regs")
  .right(of="main", display="disasm")
  .show("legend", on="disasm")
).build()
end
