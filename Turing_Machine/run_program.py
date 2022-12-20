from TM import TuringMachine

N = 1000 # tape length, initialize to a large value if you need it

input_tape = '1101_101'
program = open('sample_TM.txt').read()

tm = TuringMachine(program, input_tape, N)
tm.run()
# 10010 H
