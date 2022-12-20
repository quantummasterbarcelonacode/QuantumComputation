We shall assume that the tape alphabet can contain only the symbols  {0,1,⊔}, the head on the Turing machine moves in left (L) / right (R) direction (D) or doesn’t move (\*), upon reading a symbol on the tape (i.,e., D can be one of {L,R,*}). Also, given a program along with a valid input, the Turing machine just halts (goes to the state halt) after writing the desired output on its tape.

The program is loaded as a text file (.txt) where each line represents a transition function of the form 𝛿(𝑝,𝑋)=(𝑞,𝑌,D), where the 5 tuples are strictly in the order p, X, Y, D, q (the character _ represents a blank symbol on the tape).

You will find detailed information on the original article about this implementation [here](https://sandipanweb.wordpress.com/2020/08/08/simulating-a-turing-machine-with-python-and-executing-programs/).
