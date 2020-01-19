# import start
import os
import time
import CheckNonet
import Row_Column_Check

# import end


# Global variable start
dict_len=0
sudoku_values = {}  # this will store values of sudoku
sudoku_cache_values = {}  # '''This will store set of  all possible values that an empty value can be filled.
                          # EG: positon 7 can Three possibilities 1,4,6 so,
                          # sudoku_cache_values={7:[1,4,6],4:[1]}
                          # keys  :All enpty boxes to be filled
                          # Value:Set of all possible values that can be filled at the position 'key'
set_of_star_pos={1}
dict_of_count_of_numbe={}
count=1

num_list=[1,2,3,4,5,6,7,8,9]


# Global variable end


# Get sudoku from txt file
def Get_Form_File():
    f = open(os.getcwd() + "\Look_here\sud.txt", 'r')
    lines = f.readlines()
    # print(type(lines))
    # print(type(m[1]))
    return lines

def Prepare_Sudoku():
    k=1
    matt = Get_Form_File()
    #print (matt)
    for i in matt:
        for j in i :
            if j=="\n":
                pass
            else:
            	#print(k)
            	sudoku_values[k]=j
            	k+=1
    
    #return (sudoku_values)



# display in sudoku form
def display_Sudoku():
    #mat=matt()
    new_ln=1
    i=1
    global dict_len,sudoku_values
    dict_len=len(sudoku_values)
    while i<=dict_len:
        print(sudoku_values[i],end=" ")
        #print(i,end=" ")
        if i%9==0:
        	print()
        i+=1
        
    print()    
    #print(sudoku_values[10])    	



# function to find spaces to be filled [spaces are termed as stars]
def Get_pos_of_Spaces():
	global dict_len,set_of_star_pos,sudoku_values
	set_of_star_pos.clear()
	i=1
	while i<=dict_len:
		if sudoku_values[i]=="*":
			set_of_star_pos.add(i)
		else:
			pass
			
		i+=1
	#print(set_of_star_pos)
	
#Generate initial sudoku_cache_values for each round.
#This creats dict with values those pos that have stars and not number, and Value of that key will be 
# an empty set for now in step_One(), this set is filled

def gen_sudoku_cache_values():
	global set_of_star_pos,sudoku_cache_values
	sudoku_cache_values.clear()
	for i in set_of_star_pos:
		sudoku_cache_values[i]=set()

	#print (sudoku_cache_values)


def CheckToFit(pos,num):
	Flag1=Row_Column_Check.CheckRowAndColumn(pos,num,sudoku_values)
	Flag2=CheckNonet.Chech_In_Nonet(pos,num,sudoku_values)
	 
	global  count 
	if Flag1 and Flag2==True:
		sudoku_cache_values[pos].add(num)
		
		count+=1 
		#print(str(num)," at ",str(pos)," passed")#,file=logf)
		#print(sudoku_cache_values)
	else:
		#print(str(num)," at ",str(pos)," Failed")#,file=logf)	
		pass

def step_One():#generates sudoku cache value
	global num_list,set_of_star_pos
	for i in set_of_star_pos:
		for j in num_list:
			CheckToFit(i,j)

def step_Two():
	"""Places having only 1 possibility are sorted and filled by respective no in this function """
	#garbVals=[]
	for i in sudoku_cache_values:
		if (len(sudoku_cache_values[i])==1):
			tempVal=list(sudoku_cache_values[i])
			sudoku_values[i]=tempVal[0]
			#del sudoku_cache_values[i]
			
	
#--code ends 


#--Main function
#--one time run function
#-start
def main():
	Prepare_Sudoku()
	print("unsolved Sudoku")
	print("____________")
	display_Sudoku()
	print("____________")
#-end
 
	round=1
	#print(len(set_of_star_pos))
	while len(set_of_star_pos)>0:
	 
		Get_pos_of_Spaces()
		gen_sudoku_cache_values()
		step_One()
		step_Two() 
		round+=1
		#time.sleep(2)
		
		print(sudoku_cache_values)
		print(len(set_of_star_pos))
		display_Sudoku()
	print("solution")

	print("sudoku solved in ",round,"round(s)")	
	print("____________")
	display_Sudoku()
	print("____________")
	print("adfadsfasdf",file=logf)

	logf.close()
	
#driving code
main()
