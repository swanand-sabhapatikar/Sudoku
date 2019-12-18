
This is a command line tool-game devloped to solve sudoku for now this tool can solve only sudoku of easy level Later updates will be made to solve meduim and hard level sudoku also.
@How This work
We need to save the sudoku as below in text file "sud.txt":

659*1*28*
1***5**3*
2**8***1*
***135*7*
8**9****2
**3*7864*
3*2**9**4
*****18**
**876****

Here * denotes the empty spaces in the sudoku.
After this, execute the "SolveSudoku.py" script. For each empty space, it will check each number (1-9) to check if can be placed or not.
If yes, the number is placed if no, it is passed.
At last when all the spaces are filled (the script checks this by keeping count of spaces after each itteration), it stops and saves the solution "solution.txt".
NOTE: currently the script is in verbos mode that shows for each itteration :
        1.The sudoku
        2.For each empty space, all possible numbers that can be fitted. 
 
