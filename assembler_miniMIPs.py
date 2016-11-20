"""
Created on Sun Nov 20 19:19:10 2016

Assembler for miniMIPs

Keywords:
lw rt, offset(rs)
sw rt, offset(rs) 
addi rt, rs, const 
add rd, rs, rt 
sub rd, rs, rt

{opcode; rs; rt; rd/offset/const}
opcode = 4 bits; rs = 2 bits; rt = 2 bits; rd/offset/const = 4 bits

lw : opcode = 0000
sw : opcode = 0001
addi : opcode = 0010
add : opcode = 0011
sub : opcode = 0100

Register Set
$zero, $t0, $t1, $t2

@author: Conor
"""
import re
filename = "instructions.txt"
mode = 'r'

m_in = open(filename, mode)
h_out = open("assembled.txt", 'w')
h_out.write("v2.0 raw\n")

instruction4 = ["add", "sub"]
instruction3 = ["lw", "sw"]

opcode = {"add" : '0011', "addi" : '0010', "sub" : '0100', "lw" : '0000', "sw" : '0001'}
register = {"$zero" : "00", "$t0" : "01", "$t1" : "10", "$t2" : "11"}

for line in m_in:
    if '#' in line:
        line = line[:line.index('#')] #remove comments ->Tenks Keg
    mcode = re.split("[, \n()]+", line)

    print(mcode)
    if (mcode[0] in instruction4):
        op = opcode[mcode[0]]
        rd = '00' + register[mcode[1]]
        rs = register[mcode[2]]
        rt = register[mcode[3]]
    elif(mcode[0] in instruction3):
        op  = opcode[mcode[0]]
        rt = register[mcode[1]]
        rd = format(int(mcode[2]), '04b')
        rs = register[mcode[3]]
    else:
        op = opcode[mcode[0]]
        rt = register[mcode[1]]
        rs = register[mcode[2]]
        rd = format(int(mcode[2]), '04b')
        
    hcode = format(int(op + rs + rt + rd, 2), '03x')
    h_out.write(hcode + '\n')
    
h_out.close()
m_in.close()

    
    
