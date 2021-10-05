import random
import math

# generating  board positions fpr N-Queens Problem
def initiate_board(n):
    board=[[0 for i in range(n)] for j in range(n)]
    # place each queen randomly in each column of board
    for i in range(n):
        queen_Initial=random.randrange(0,n,1)
        board[queen_Initial][i]=1
    return board

# to get the positions of queens from the current configuration
def get_Queen_Position(board,n,i):
    for j in range(n):
        if board[j][i]==1:
            return j

# Printing Board Configuration
def print_board(message,board):
    print(message)
    for i in range(n):
        print("\n", board[i])





# to calculate the heuristic value of all n*(n-1) possible configurations reachable from the current configuration - returns a 2D-array with heuristic costs in each cell
def find_all_heuristics(board,n):
    heuristic_all=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        a_index=get_Queen_Position(board,n,i)
        b_index=i
        for j in range(n):
            temp_board=[row[ : ] for row in board]
            if j==a_index:
                heuristic_all[j][i]=math.inf
            else:
                temp_board[j][i]=1
                temp_board[a_index][b_index]=0
                heuristic_all[j][i]=calculate_heuristic(temp_board, n)
    return heuristic_all

#Finding the minimum heuristic move to make to go the next board configuartion
def find_minimum_heuristic_move(board, n):
    heuristic_all=find_all_heuristics(board,n)
    min_heuristic=math.inf
    a_min=0
    b_min=0
    rand_arr = [] #to store the indices of minimum heuristic valued configurations : 1st index is row no. and 2nd index is column no.
    mbmin = min([min(r) for r in heuristic_all])
    for i in range(n):
        for j in range(n):
            if heuristic_all[j][i] == mbmin:
                min_heuristic = heuristic_all[j][i]
                rand_arr.append([j, i])
    min_index = random.randint(0,len(rand_arr)-1)
    a_min = rand_arr[min_index][0]
    b_min = rand_arr[min_index][1]
    return(a_min,b_min,min_heuristic)


# Calculating heuristic value of a particular configuration
def calculate_heuristic(board,n):
    heuristic=0
    for i in range(n):
        a_index=get_Queen_Position(board,n,i)
        b_index=i
        for j in range(n):
            if j==i:
                continue
            else:
                a_pair=get_Queen_Position(board,n,j)
                b_pair=j
                if a_index==a_pair or abs(a_index-a_pair)== abs(b_index-b_pair):
                   heuristic+=1
    return int((heuristic)/2)




# Approach 1 - traditional hill climbing
def hill_climbing(heuristic_current,min_heuristic):
    if heuristic_current > min_heuristic:
        return True
    return False

# Approach 2 - hill climbing with sideways move, the limit set on the number of consecutive sideways move is 100
def hill_climbing_sideways(heuristic_current,min_heuristic):
    global counter
    if heuristic_current == min_heuristic:
        counter+= 1
    else:
        counter = 0
    if heuristic_current >= min_heuristic and counter < counter_value:
        return True
    return False

no_of_instances = 500
rand_print_counter = 0
rand_print = [random.randint(0,no_of_instances) for i in range (4)]
rand_print.sort()



#Main Function/ Driver Function

if __name__ == "__main__":
    success_rate = 0  #This denotes number of successful instances, not percentage
    steps_success = 0
    steps_failure = 0
    no_of_rand_restart = 0

    #Getting the User Input
    n = int(input("Enter the value of N : "))
    #Selecting among the various types of Hill Climbing Search
    m = int(input("Enter the variants of hill climbing search to use:\n 1 --> hill climbing classic; 2 --> hill climbing with sideways moves; 3 --> random restart without sideways moves; 4 --> random restart with sideways moves\n"))



    for k in range(no_of_instances):
        counter = 0
        if(m == 2):
            counter_value = 100 # limit on consecutive sideways move for hill climbing
        else:
            counter_value = 10  # limit on consecutive sideways move for random restart hill climbing
        board=initiate_board(n)
        heuristic_all=[[0 for i in range(n)] for j in range(n)]
        heuristic_current=calculate_heuristic(board, n)

        if ((m == 1 or m == 2) and rand_print_counter < 4 and k == rand_print[rand_print_counter]):
            print("\n Random Initial Configuration :", rand_print_counter+1)
            print_board("\n Initial state ",board)
        min_heuristic=math.inf
        success_local = 0
        failure_local = 0
        no_of_rand_restart_local = 0
        while heuristic_current>0:
            a_min,b_min,min_heuristic = find_minimum_heuristic_move(board, n)
            if (m == 1 and hill_climbing(heuristic_current,min_heuristic) == True): # approach 1 - do not change any hard coded numbers
                a_temp=get_Queen_Position(board,n,b_min)
                board[a_temp][b_min]=0
                board[a_min][b_min]=1
                heuristic_current=min_heuristic
                success_local = success_local + 1
                if (rand_print_counter < 4 and k == rand_print[rand_print_counter]):
                    print_board("\n Next state ",board)
                if heuristic_current==0:
                    success_rate+=1
                    if (rand_print_counter < 4 and k == rand_print[rand_print_counter]):
                        print("\n This was a successful instance.")
                        print("*****************************************")

            elif (m == 2 and hill_climbing_sideways(heuristic_current,min_heuristic) == True): # approach 2 - do not change any hard coded numbers
                a_temp=get_Queen_Position(board,n,b_min)
                board[a_temp][b_min]=0
                board[a_min][b_min]=1
                heuristic_current=min_heuristic
                success_local = success_local + 1
                if (rand_print_counter < 4 and k == rand_print[rand_print_counter]):
                    print_board("\n Next state ",board)
                if heuristic_current==0:
                    success_rate+=1
                    if (rand_print_counter < 4 and k == rand_print[rand_print_counter]):
                        print("\n This was a successful instance.")
                        print("*****************************************")

            elif (m == 3 and k < 50): #approach 3 - do not change any hard coded numbers
                if(hill_climbing(heuristic_current,min_heuristic) == True):
                    a_temp=get_Queen_Position(board,n,b_min)
                    board[a_temp][b_min]=0
                    board[a_min][b_min]=1
                    heuristic_current=calculate_heuristic(board, n)
                    success_local += 1
                    if heuristic_current==0:
                        break
                else:
                    no_of_rand_restart_local = no_of_rand_restart_local + 1
                    board = initiate_board(n)
                    heuristic_current=calculate_heuristic(board, n)

            elif (m == 4 and k < 50): # approach 4 - do not change any hard coded numbers
                if(hill_climbing_sideways(heuristic_current,min_heuristic) == True):
                    a_temp=get_Queen_Position(board,n,b_min)
                    board[a_temp][b_min]=0
                    board[a_min][b_min]=1
                    heuristic_current=calculate_heuristic(board, n)
                    success_local += 1
                    if heuristic_current==0:
                        break
                else:
                    no_of_rand_restart_local = no_of_rand_restart_local + 1
                    board = initiate_board(n)
                    heuristic_current = calculate_heuristic(board, n)

            else:
                failure_local = success_local
                if ((m == 1 or m == 2) and rand_print_counter < 4 and k == rand_print[rand_print_counter]):
                    print("\nThis was a failure instance.")
                    print("*************************************")
                success_local = 0
                break

        steps_success      += success_local
        steps_failure      += failure_local
        no_of_rand_restart += no_of_rand_restart_local
        if ((m == 1 or m == 2) and rand_print_counter < 4 and k == rand_print[rand_print_counter]):
            rand_print_counter = rand_print_counter + 1

    #Calculation of Success Rate and Failure Rate
    if m == 1 or m == 2:
        print("\n \n Success rate is : ", (success_rate*100)/no_of_instances, "%")
        print("\n \n Failure rate is :", ((no_of_instances - success_rate)*100)/no_of_instances, "%")

        if success_rate != 0:
            print('\n Average No. of steps required for success is ', round(steps_success/success_rate,2), 'which is approximately', math.ceil(steps_success/success_rate),'steps. ') #Rounding up using Ceil Function
        if success_rate != no_of_instances:
            print("\n Average No. of steps required for failure is ",round(steps_failure/(no_of_instances - success_rate),2), 'which is approximately',math.ceil(steps_failure/(no_of_instances - success_rate)),'steps. ')


    if m == 3 or m == 4:
        print("\n Average Number of random restarts required is ", no_of_rand_restart/50, 'which is approximately',math.ceil(no_of_rand_restart/50), 'restarts.')
        print('\n Average No. of steps required for random restart is ',steps_success/50, 'which is approximately',math.ceil(steps_success/50),'steps.')

