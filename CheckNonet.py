"""
Nonet here are refered as  3*3 boxes, Which in total are 9.
this script does following:
1. sudoku
2. number 'n' be to be tested and 
3. Positon 'pos' for which the no is tested.

If 'n' can be placed at 'pos', the function will return True else False. 
"""
nonet1=[1,2,3,10,11,12,19,20,21]
nonet2=[4,5,6,13,14,15,22,23,24]
nonet3=[7,8,9,16,17,18,25,26,27]
nonet4=[28,29,30,37,38,39,46,47,48]
nonet5=[31,32,33,40,41,42,49,50,51]
nonet6=[33,34,36,43,44,45,52,53,54]
nonet7=[55,56,57,64,65,66,73,74,75]
nonet8=[58,59,60,67,68,69,76,77,78]
nonet9=[61,62,63,70,71,72,79,80,81]
Master_nonoet=[nonet1,nonet2,nonet3,nonet4,nonet5,nonet6,nonet7,nonet8,nonet9]


def Chech_In_Nonet(pos,num,sudoku):
	FlagCheckNonet=0 #True: if num can be places at pos,else False 
	#to find nonet 
	#print(file=logf)
	#print("start ","pos:",pos,"num:",num,file=logf)
	sudoku_values=sudoku
	for i in Master_nonoet:
		if pos in i:
			#check in respective nonet						 
			for j in i:

			 	if j==pos or sudoku_values[j]=="*" :
			 		#FlagCheckNonet=True
			 		pass
			 	
			 	elif (str((sudoku_values[j]))==str(num)):
			 		#print("nonet compare:",sudoku_values[j],file=logf)
			 		FlagCheckNonet=False
			 		#logf.write("\n")
			 		break
			 	else:
			 		FlagCheckNonet=True
	
	return FlagCheckNonet




