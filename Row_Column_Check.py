"""
This script check in row and column to which the particular positon pos belong.
this script does following:
1. sudoku
2. number 'n' be to be tested and 
3. Positon 'pos' for which the no is tested.
If 'n' can be placed at 'pos', the function will return True else False. 
"""
def CheckInRow(pos,num,sudoku):
	counter=Lower_val=1
	Upper_val=9	
	sudoku_values=sudoku
	#find the row		
	while counter<=9:
		if ((pos>=Lower_val) and (pos<=Upper_val)):
				#if we found the row brake this loop
				break
		else:
			
			Lower_val=Upper_val+1
			Upper_val+=9
			counter+=1
	 
	flagR=True #True: if num can be places at pos,else False
	while Lower_val<=Upper_val:
		#print("row compare:",sudoku_values[Lower_val])
		if Lower_val==pos:
	
			Lower_val+=1
			#print(Lower_val)
				
			continue
		else:
			#print("checking for num",str(num),"at pos:",sudoku_values[Lower_val])
			if ((str(sudoku_values[Lower_val]))==str(num)):
				flagR=False
				break
			else:
				Lower_val+=1
		
	return flagR
	
	#check in the column
	

	 			 

def CheckInColumn(pos,num,sudoku):
	scroll_val=pos
	shift_Val=9
	scroll_count=0
	sudoku_values=sudoku
	FlagC=False
	#print("pos:",pos)
	while scroll_count<9:
		
		if scroll_count!=0:
			scroll_val+=shift_Val
			#scroll_count+=1
		if scroll_val>=81:
			scroll_val=pos
			shift_Val=-9
			#scroll_count+=1
		elif scroll_val<=1:
			scroll_val=pos
			shift_Val=9
			#scroll_count+=1
		else:
			#print("colum ",sudoku_values[scroll_val])
			if(str(sudoku_values[scroll_val])==str(num)):
				#print("column compare:",sudoku_values[scroll_val])
				FlagC=False
				break
			else:	
				FlagC=True
			#scroll_count+=1		
		#print("scroll_count",scroll_count,"current_pos",scroll_val,"val_at_pos",sudoku_values[scroll_val])
		scroll_count+=1

	return FlagC


def CheckRowAndColumn(pos,num,sudoku):
	FlagRowCheck=CheckInRow(pos,num,sudoku)
	FLagColumnCheck=CheckInColumn(pos,num,sudoku)
	return (FlagRowCheck and FLagColumnCheck )
