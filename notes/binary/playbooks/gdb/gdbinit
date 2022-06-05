# 1) Setup Pwndbg and GEF

# GEF
#source /home/test/.gdbinit-gef.py    # change to your directory
# PWNDBG
source /home/test/pwndbg/gdbinit.py   # change to your directory

# 2) Setup tmux & splitmind

## PWNDBG - Split screen w/ tmux & splitmind
### sudo apt install tmux
### git clone https://github.com/jerdna-regeiz/splitmind

source /home/test/pwndbg/splitmind/gdbinit.py    # change to your directory


python
import splitmind
(splitmind.Mind()
  .below(display="disasm")
  #.right(display="backtrace")
  .right(display="stack")
  .right(of="main", display="regs")
  .show("legend", on="disasm")
).build()
end

#python
#import splitmind
#(splitmind.Mind()
#  .below(display="backtrace")
#  .right(display="stack", cmd="grep rax", use_stdin=True)
#  .right(display="regs")
#  .below(cmd='sleep 1; htop')
#  .below(of="stack", cmd='sleep 1; watch ls')
#  .right(of="main", display="disasm")
#  .show("legend", on="disasm")
#).build()
#end


#python
#import splitmind
#(splitmind.Mind()
# # .below(display="backtrace")
#  .below(of="main", display="stack", cmd="grep rax", use_stdin=True)
#  .right(of="main", display="disasm")
#  .below(of="disasm", display="regs")
#  .show("legend", on="disasm")
#).build()
#end
