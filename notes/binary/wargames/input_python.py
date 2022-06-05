import interact
process = interact.Process()

print process.readuntil('name?')
process.sendline('Bob')

print process.readuntil('math problem:\n')
num_one = process.readuntil(' + ')[:-3]
num_two = process.readuntil(' = ?')[:-3]

answer = int(num_one) + int(num_two)
process.sendline(str(answer))
process.interactive()
