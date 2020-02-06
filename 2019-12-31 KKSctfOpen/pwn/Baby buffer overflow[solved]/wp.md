Baby buffer overflow题目描述：
We received new message from kackers. They laugh at us being sure that no one will ever be able to break them and even left a description of what needs to be done. Show them what happens to overly confident people!

$ checksec baby_bof
[*] '/home/ubuntu/Desktop/baby_bof'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)

checksec发现只有栈不可执行保护
输入超长字符串后溢出，判断应该为栈溢出漏洞。

反编译后得到
unsigned int __cdecl read_wrapper(char *input_name)
{
  size_t name_len; // edx
  unsigned int result; // eax
  unsigned int i; // [esp+0h] [ebp-8h]

  gets(input_name);
  for ( i = 0; ; ++i )
  {
    name_len = strlen(input_name);
    result = i;
    if ( name_len <= i )
      break;
    if ( input_name[i] > 64 && input_name[i] <= 90 )// A-Z
      input_name[i] += 32;                      // 大写转小写
  }
  return result;
}

使用pattern检测栈大小为260.

因此思路为通过输入260个字符溢出覆盖read_wrapper地址后控制程序执行流程到win函数的0x080485F6。

int __cdecl win(int hello)
{
  char s; // [esp+3h] [ebp-25h]
  FILE *stream; // [esp+20h] [ebp-8h]

  stream = fopen("flag.txt", (const char *)&unk_8048830);
  if ( !stream )
    return puts("flag not found");
  fgets(&s, 29, stream);
  if ( hello != 0xCAFEBABE )
  {
    puts("Almost there :)");
    exit(0);
  }
  return printf("Here it comes: %s\n", &s);
}
随后发现win函数需要有一个以0xCAFEBABE为参数的输入，因此在payload后面加上随机4字节组成的返回地址加上0xCAFEBABE即可。



tips:
pwn.cyclic(num):生成num字长的随机数
pwn.cyclic_find(pattern):找到该字符所在位置，类似pattern.py
pwn.checksec

gdb
info founctions:查看所有函数及其地址信息
