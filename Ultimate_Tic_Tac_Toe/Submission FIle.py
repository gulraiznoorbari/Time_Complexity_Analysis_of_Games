##MUQADDAS AMAN 231454590
## CLASS GAME PROJECT
class Table():            ##THE BUILDING BLOCK OF THE ENTIRE PROJECT. THIS CLASS IS THE BASIC TICTACTOE 
    def __init__(self):
        self.win = "N" ##WIN STATUS
        self.corners = [["A1","B2","C3"],["C1","B2","A3"]]

        self.available = 9

        self.vertical =   [['A1','A2','A3'],
                           ['B1','B2','B3'],
                           ['C1','C2','C3']]

        self.horizontal= [['A1','B1','C1'],
                         ['A2','B2','C2'],
                         ['A3','B3','C3']]

        self.mid = "B2"

        ###THESE ARE THE AVIALABLE CELLS
        self.cells = {'A1':0,           
                      'A2':0,
                      'A3':0,
                      'B1':0,
                      'B2':0,
                      'B3':0,
                      'C1':0,
                      'C2':0,
                      'C3':0,}



    def user_input(self,player,cell):

        if self.available == 0:
            return ('0') ##IF THE TABLE IS FULL
        elif self.available > 0:
            if self.cells[cell] == 0:
                self.cells[cell] = player
                self.available -= 1
                self.win_check()
                if self.win!=0:
                    return ("1") ##IF THE INPUT WAS SUCCESSFUL

            else:
                return ("2") ##IF THE CELL ALREADY HAD AN INPUT
            


    def diagonal_win(self):
        for i in self.corners:
            val1 = self.cells[i[0]]
            val2 = self.cells[i[1]]
            val3 = self.cells[i[2]]

            if val1!= 0 and val2!=0 and val3!=0:
                if val1==val2 and val2==val3:
                    self.win = val1



    def vertical_win(self):
        for i in self.vertical:
            if self.win!='N':
                return
            count = 0
            v_lst = i
            v_check = self.cells[v_lst[count]]
            while v_check!=0 and count<2:
                count+=1
                if v_check != self.cells[v_lst[count]]:
                    v_check = 'N'
                    count = 3

            if count==2:
                self.win = v_check


    def horizontal_win(self):
        for i in self.horizontal:
            if self.win!='N':
                return
            count = 0
            h_lst = i
            h_check = self.cells[h_lst[count]]
            while h_check!=0 and count<2:
                count+=1
                if h_check != self.cells[h_lst[count]]:
                    h_check = 'N'
                    count = 3

            if count==2:
                self.win = h_check


    def win_check(self):

        if self.available == 0:
            self.win = "D"
        if self.win =='N':
            self.diagonal_win()
        if self.win =='N':
            self.vertical_win()
        if self.win == 'N':
            self.horizontal_win()




##########################################
##THESE FUNCTIONS WERE USED IN THE SIMPLE TICTACTOE
## TO PRINT OUT THE TABLE ################
    def X_print(self):   ##DEL
        print("   \       /  ")
        print("     \   /    ")
        print("       X      ")
        print("     /   \    ")
        print("   /       \  ")
    def O_print(self):  ##DEL
        print("       -      ")
        print("     -   -    ")
        print("    -     -   ")
        print("     -   -    ")
        print("       -      ")
    def D_print(self):  ##DEL
        print("      |-      ")
        print("      |   -   ")
        print("      |     - ")
        print("      |   -   ")
        print("      |-      ")
    def table_print(self,table_letters,table_numbers):  ##DEL
        if self.available ==0:
            self.D_print()
        elif self.win == "N":
            self.table(table_letters,table_numbers)
        elif self.win == "X":
            self.X_print()
        elif self.win == "O":
            self.O_print()
    def table(self,table_letters,table_numbers):
        length = len(table_letters)
        #grid1 = 0
        #grid_print = 0
        #grid_count = 0
        #grid_check = False
        #while grid_check == False:
        #    if grid1 == 12:
        #        grid_check =True
        #    else:
        #        if grid1 % 4 != 0:
        #            if grid1 % 2==0:
        #                print(table_numbers[grid_print],end = " ")
        #                grid_print+=1
        #            else:
        #                print(" ",end = "")
        #        else:
        #            print(" ",end = "")
        #    grid1 += 1


        grid2= 0
        number_count = -1
        for i in range(5):
            print(end="\n")
            h_dashes=1
            count = 0
            run = 1 

            #if i%2 == 0:
            #    print(table_letters[grid2],end=" ")
            #    grid2+=1
            #else:
            #    print(" ",end = " ")

            if i%2 == 0:
                number_count += 1

            for j in range(10):
                if i%2==0:
                    if j%2 == 0:
                        if h_dashes == 1:
                            letters = self.cells[table_letters[count]+str(table_numbers[number_count])]
                            l_t = table_letters[count]+str(table_numbers[number_count])
                            if letters==0:
                                print(l_t,end ="")
                                count +=1
                                h_dashes +=2
                            else:
                                print(letters,end=" ")
                                count +=1
                                h_dashes +=2
                        else:
                            h_dashes -= 2
                            print("|",end="")
                    else:
                        print(" ",end="")
                else:

                    if h_dashes < 4:
                        print("-",end="")
                        h_dashes +=1
                    elif h_dashes == 4:
                        h_dashes = 0
                        run += 1
                        if run == 3:
                            print("+",end="---")
                            run = 1
                        else:
                            print("+",end="")
        print("")  
########################################


class Meta_Table():
    def __init__(self,table_list):
        self.win = "N"
        
        self.forced_cell = 0

        self.table = {    'A1':[table_list[0],table_list[0].win],
                          'A2':[table_list[3],table_list[3].win],
                          'A3':[table_list[6],table_list[6].win],
                          'B1':[table_list[1],table_list[1].win],
                          'B2':[table_list[4],table_list[4].win],
                          'B3':[table_list[7],table_list[7].win],
                          'C1':[table_list[2],table_list[2].win],
                          'C2':[table_list[5],table_list[5].win],
                          'C3':[table_list[8],table_list[8].win]
                          }

        
        self.minor_cells = [self.table["A1"][0],
                            self.table["B1"][0],
                            self.table["C1"][0],
                            self.table["A2"][0],
                            self.table["B2"][0],
                            self.table["C2"][0],
                            self.table["A3"][0],
                            self.table["B3"][0],
                            self.table["C3"][0]]

        self.avaialbe = 0
        for k in self.minor_cells:##THIS IS DYNAMIC TO MAKE SURE THAT ANY AVIALABLE VALUES ARE PROPERLY CHECKED
            if k.win == "N":
                if k.cells["A1"]==0:
                    self.avaialbe+=1
                if k.cells["B1"]==0:
                    self.avaialbe+=1
                if k.cells["C1"]==0:
                    self.avaialbe+=1
                if k.cells["A2"]==0:
                    self.avaialbe+=1
                if k.cells["B2"]==0:
                    self.avaialbe+=1
                if k.cells["C2"]==0:
                    self.avaialbe+=1
                if k.cells["A3"]==0:
                    self.avaialbe+=1
                if k.cells["B3"]==0:
                    self.avaialbe+=1
                if k.cells["C3"]==0:
                    self.avaialbe+=1


        self.table_wins ={'A1':self.table["A1"][1],
                          'A2':self.table["A2"][1],
                          'A3':self.table["A3"][1],
                          'B1':self.table["B1"][1],
                          'B2':self.table["B2"][1],
                          'B3':self.table["B3"][1],
                          'C1':self.table["C1"][1],
                          'C2':self.table["C2"][1],
                          'C3':self.table["C3"][1]
                          }

        self.cell_reference = {'A1':['A1','A2','A3','B1','B2','B3','C1','C2','C3'],
                              'A2':['A4','A5','A6','B4','B5','B6','C4','C5','C6'],
                              'A3':['A7','A8','A9','B7','B8','B9','C7','C8','C9'],

                              'B1':['D1','D2','D3','E1','E2','E3','F1','F2','F3'],
                              'B2':['D4','D5','D6','E4','E5','E6','F4','F5','F6'],
                              'B3':['D7','D8','D9','E7','E8','E9','F7','F8','F9'],

                              'C1':['G1','G2','G3','H1','H2','H3','I1','I2','I3'],
                              'C2':['G4','G5','G6','H4','H5','H6','I4','I5','I6'],
                              'C3':['G7','G8','G9','H7','H8','H9','I7','I8','I9'] }

        self.corners = [["A1","B2","C3"],["C1","B2","A3"]]

        self.vertical =   [['A1','A2','A3'],
                           ['B1','B2','B3'],
                           ['C1','C2','C3']]

        self.horizontal= [['A1','B1','C1'],
                         ['A2','B2','C2'],
                         ['A3','B3','C3']]

        self.mid = "B2"


    def calculate_avalaible(self): ###THIS FUNCTION  CALCULATES EACH AVIALABE CELL 
        self.avaialbe = 0
        for k in self.minor_cells:##THIS IS DYNAMIC TO MAKE SURE THAT ANY AVIALABLE VALUES ARE PROPERLY CHECKED
            if k.win == "N":
                if k.cells["A1"]==0:
                    self.avaialbe+=1
                if k.cells["B1"]==0:
                    self.avaialbe+=1
                if k.cells["C1"]==0:
                    self.avaialbe+=1
                if k.cells["A2"]==0:
                    self.avaialbe+=1
                if k.cells["B2"]==0:
                    self.avaialbe+=1
                if k.cells["C2"]==0:
                    self.avaialbe+=1
                if k.cells["A3"]==0:
                    self.avaialbe+=1
                if k.cells["B3"]==0:
                    self.avaialbe+=1
                if k.cells["C3"]==0:
                    self.avaialbe+=1

    def user_input(self,player,cell): ##FIX THIS 

        user_cell = 0
        if self.avaialbe == 0:
            #print("TEST 1")
            return ('0') ##IF THE TABLE IS FULL
        
        elif self.avaialbe > 0:
            for i in self.cell_reference:
                if cell in self.cell_reference[i]:
                    #print("TEST 2")
                    user_cell = i
                    i = "C3"
            if user_cell== 0:
                #print("TEST 3")
                return ("3") ##IF THE USER INPUTS A WRONG ADDRESS
            
            ##WE GOT THE META CELL, NOW WE NED TO CHECK IF IT HAS WINS...
            ##STEP 1: CHECK THE WIN AND IF THE PLAYER IS PLAYING IN THE RIGHT TICTACTOE
            if self.table_wins[user_cell] != "N":
                #print("TEST 4")
                return ('4') ##THIS IS IF THE TICTACTOE HAS BEEN WON ALREADY OR DECIDED
            elif user_cell != self.forced_cell and self.forced_cell!=0:
                #print("TEST 5")
                return ('5')##THIS IS IF THE PLAYER IS PLAYING IN THE WRONG TICTACTOE
            
            if user_cell == self.forced_cell or self.forced_cell == 0:
                #print("TEST 6")
                index = self.cell_reference[user_cell].index(cell)
                mini_tac_cell = self.cell_reference["A1"][index]  ##THIS IS THE CELL THAT WE NEED TO PASS INTO THE MINI TIC TAC TOE
                reply = self.table[user_cell][0].user_input(player,mini_tac_cell)


                victory = self.table[user_cell][0].win
                if victory!='N':
                    self.table[user_cell][1] = victory
                    self.table_wins[user_cell] = victory


                if reply == "1": #HERE WE NEED TO UPDATE THE FORCED CELL
                    
                    keys = list(self.cell_reference.keys())
                    self.forced_cell = keys[index]

                    if self.table_wins[self.forced_cell]!="N":
                        self.forced_cell = 0
                    self.calculate_avalaible()
                    self.win_check()

                    if self.win == "N" and self.avaialbe==0:
                        self.win = "D"
                    #print("TEST 7")
                    
                    return ('1') ##SUCCESSFUL INPUT
                elif reply == "2":
                    #print("TEST 8")
                    return ('2')


#####################################
## THIS SECTION CHECKS THE WIN STATUS 
## OF THE META TABLE ################

    def diagonal_win(self):
        for i in self.corners:
            val1 = self.table_wins[i[0]]
            val2 = self.table_wins[i[1]]
            val3 = self.table_wins[i[2]]

            if val1!= "N" and val2!="N" and val3!="N":
                if val1==val2 and val2==val3 and val1!="D":
                    self.win = val1

    def vertical_win(self):
        for i in self.vertical:
            if self.win!='N':
                return
            count = 0
            v_lst = i
            v_check = self.table_wins[v_lst[count]]
            while v_check!=0 and count<2:
                count+=1
                if v_check != self.table_wins[v_lst[count]]:
                    v_check = 'N'
                    count = 3

            if count==2 and v_check!="D":
                self.win = v_check  
                

    def horizontal_win(self):
        for i in self.horizontal:
            if self.win!='N':
                return
            count = 0
            h_lst = i
            h_check = self.table_wins[h_lst[count]]
            while h_check!=0 and count<2:
                count+=1
                if h_check != self.table_wins[h_lst[count]]:
                    h_check = 'N'
                    count = 3

            if count==2 and h_check!="D":
                self.win = h_check


    def win_check(self):
        if self.win =='N':
            self.diagonal_win()
        if self.win =='N':
            self.vertical_win()
        if self.win == 'N':
            self.horizontal_win()
        if self.avaialbe==0:
            self.win="D"





#######################################

## THE TABLE PRINTING GOES LINE BY LINE;
## AS EACH LINE CONSISTS OF 3 TICTACTOES

    def print_line1(self):
        count = 0
        run = 0  
        win1 = self.table['A1']    
        win2 = self.table['B1']    
        win3 = self.table['C1']    

        tables = ["A1","B1","C1"] 

        wins = [win1,win2,win3]
        while count < 3:
            temp = self.cell_reference[tables[count]]
            current = wins[count]


            if current[0].available == 0:
                print("      |-      ",end=" ") 


            elif current[1] == "N":

                cells = current[0].cells

                if cells["A1"] != 0:
                    A1 = cells["A1"]
                    run+=3
                    print(A1,end = "  | ")
                else:
                    A1 = temp[run]
                    run+=3
                    print(A1,end = " | ")
                

                if cells["B1"] != 0:
                    B1 = cells["B1"]
                    run+=3
                    print(B1,end = "  | ")
                else:
                    B1 = temp[run]
                    run+=3
                    print(B1,end = " | ")


                if cells["C1"] != 0:
                    C1 = cells["C1"]
                    run = 0
                    print(C1,end = "    ")
                else:
                    C1 = temp[run]
                    run = 0  
                    print(C1,end = "   ")
                                                 
                    
            elif current[1] == "X":                       
                print("   \       /  ",end = " ")         
            elif current[1] == "O":                       
                print("       -      ",end = " ")         

            count += 1
            if count < 3:
                print("|",end = "  ")

        if win1[1] == "D" or win1[0].available==0:
            first = "\n      |   -    "
        elif  win1[1] == "N" and win1[0].available!=0:
            first = "\n---+----+------"                                      
        elif win1[1] == "X":                                                
            first ="\n     \   /     "                                      
        elif win1[1] == "O":                                                
            first = "\n     -   -     "                                     
                                                                            
        if win2[1] == "D" or win2[0].available==0:                         
            second = "         |   -    "                                       
        elif  win2[1] == "N" and win2[0].available!=0:                      
            second = "+-----+----+------"                                   
        elif win2[1] == "X":                                                
            second ="        \   /     "                                        
        elif win2[1] == "O":                                                
            second = "        -   -     "                                       
                                                                            
        if win3[1] == "D" or win3[0].available==0:                         
            third = "         |   -    "                                      
        elif  win3[1] == "N" and win3[0].available!=0:                      
            third = "+-----+----+----"                                      
        elif win3[1] == "X":                                                
            third = "        \   /     "
        elif win3[1] == "O":
            third = "        -   -     "

        final_line = first+second+third
        print(final_line)
    def print_line2(self):
        count = 0
        run = 1
        win1 = self.table['A1']   
        win2 = self.table['B1']   
        win3 = self.table['C1']   

        tables = ["A1","B1","C1"] 

        wins = [win1,win2,win3]
        while count < 3:
            temp = self.cell_reference[tables[count]]
            current = wins[count]

            if current[0].available == 0:
                print("      |     - ",end=" ")  


            elif current[1] == "N":
                cells = current[0].cells


                if cells["A2"] != 0:
                    A1 = cells["A2"]
                    run+=3
                    print(A1,end = "  | ")
                else:
                    A1 = temp[run]
                    run+=3
                    print(A1,end = " | ")
                

                if cells["B2"] != 0:
                    B1 = cells["B2"]
                    run+=3
                    print(B1,end = "  | ")
                else:
                    B1 = temp[run]
                    run+=3
                    print(B1,end = " | ")

                if cells["C2"] != 0:
                    C1 = cells["C2"]
                    run = 1
                    print(C1,end = "    ")
                else:
                    C1 = temp[run]
                    run = 1 
                    print(C1,end = "   ")

                    
            elif current[1] == "X":                      
                print("       X      ",end = " ")        
            elif current[1] == "O":                      
                print("    -     -   ",end = " ")        

            count += 1
            if count < 3:
                print("|",end = "  ")





        if win1[1] == "D" or win1[0].available==0:
            first = "\n      |   -    "
        elif  win1[1] == "N" and win1[0].available!=0:
            first = "\n---+----+------"                   
        elif win1[1] == "X":                             
            first ="\n     /   \     "                   
        elif win1[1] == "O":                             
            first = "\n     -   -     "                  
                                                         
        if win2[1] == "D" or win2[0].available==0:      
            second = "         |   -    "                    
        elif  win2[1] == "N" and win2[0].available!=0:   
            second = "+-----+----+------"                
        elif win2[1] == "X":                             
            second ="        /   \     "                     
        elif win2[1] == "O":                             
            second = "        -   -     "                    
                                                         
        if win3[1] == "D" or win3[0].available==0:      
            third = "         |   -    "                   
        elif  win3[1] == "N" and win3[0].available!=0:   
            third = "+-----+----+----"                   
        elif win3[1] == "X":                             
            third ="        /   \      "
        elif win3[1] == "O":
            third = "        -   -     "

        final_line = first+second+third
        print(final_line)
    def print_line3(self):
        count = 0
        run = 2
        win1 = self.table['A1']   
        win2 = self.table['B1']   
        win3 = self.table['C1']   

        tables = ["A1","B1","C1"] 

        wins = [win1,win2,win3]
        while count < 3:
            temp = self.cell_reference[tables[count]]
            current = wins[count]

            if current[0].available == 0:
                print("      |-      ",end=" ")  


            elif current[1] == "N":
                cells = current[0].cells ##CELLS


                if cells["A3"] != 0:
                    A1 = cells["A3"]
                    run+=3
                    print(A1,end = "  | ")
                else:
                    A1 = temp[run]
                    run+=3
                    print(A1,end = " | ")
                

                if cells["B3"] != 0:
                    B1 = cells["B3"]
                    run+=3
                    print(B1,end = "  | ")
                else:
                    B1 = temp[run]
                    run+=3
                    print(B1,end = " | ")

                if cells["C3"] != 0:
                    C1 = cells["C3"]
                    run = 2
                    print(C1,end = "    ")
                else:
                    C1 = temp[run]
                    run = 2  
                    print(C1,end = "   ")





                                                         
            elif current[1] == "X":                    
                print("   /       \  ",end = " ")     
            elif current[1] == "O":                       
                print("       -      ",end = " ")      



            count += 1
            if count < 3:
                print("|",end = "  ")
        #print("\n   |    |      |     |    |      |     |    |   ")
        print("\n")
        print("---|----|------|-----|----|------|-----|----|---")
        print("")



    def print_line4(self):
        count = 0
        run = 0  
        win1 = self.table['A2']    
        win2 = self.table['B2']    
        win3 = self.table['C2']    

        tables = ["A2","B2","C2"] 

        wins = [win1,win2,win3]
        while count < 3:
            temp = self.cell_reference[tables[count]]
            current = wins[count]

            if current[0].available == 0:
                print("      |-      ",end=" ") 


            elif current[1] == "N":
                cells = current[0].cells


                if cells["A1"] != 0:
                    A1 = cells["A1"]
                    run+=3
                    print(A1,end = "  | ")
                else:
                    A1 = temp[run]
                    run+=3
                    print(A1,end = " | ")
                

                if cells["B1"] != 0:
                    B1 = cells["B1"]
                    run+=3
                    print(B1,end = "  | ")
                else:
                    B1 = temp[run]
                    run+=3
                    print(B1,end = " | ")


                if cells["C1"] != 0:
                    C1 = cells["C1"]
                    run = 0
                    print(C1,end = "    ")
                else:
                    C1 = temp[run]
                    run = 0  
                    print(C1,end = "   ")
                                                 
                    
            elif current[1] == "X":                       
                print("   \       /  ",end = " ")         
            elif current[1] == "O":                       
                print("       -      ",end = " ")         

            count += 1
            if count < 3:
                print("|",end = "  ")

        if win1[1] == "D" or win1[0].available==0:
            first = "\n      |   -    "
        elif  win1[1] == "N" and win1[0].available!=0:
            first = "\n---+----+------"                                      
        elif win1[1] == "X":                                                
            first ="\n     \   /     "                                      
        elif win1[1] == "O":                                                
            first = "\n     -   -     "                                     
                               
        if win2[1] == "D" or win2[0].available==0:                         
            second = "         |   -    "                                       
        elif  win2[1] == "N" and win2[0].available!=0:                      
            second = "+-----+----+------"                                   
        elif win2[1] == "X":                                                
            second ="        \   /     "                                        
        elif win2[1] == "O":                                                
            second = "        -   -     "                                       
                                                                            
        if win3[1] == "D" or win3[0].available==0:                         
            third = "         |   -    "                                      
        elif  win3[1] == "N" and win3[0].available!=0:                      
            third = "+-----+----+----"                                      
        elif win3[1] == "X":                                                
            third = "        \   /     "
        elif win3[1] == "O":
            third = "        -   -     "

        final_line = first+second+third
        print(final_line)
    def print_line5(self):
        count = 0
        run = 1
        win1 = self.table['A2']   
        win2 = self.table['B2']   
        win3 = self.table['C2']   

        tables = ["A2","B2","C2"] 

        wins = [win1,win2,win3]
        while count < 3:
            temp = self.cell_reference[tables[count]]
            current = wins[count]

            if current[0].available == 0:
                print("      |     - ",end=" ")  


            elif current[1] == "N":
                cells = current[0].cells


                if cells["A2"] != 0:
                    A1 = cells["A2"]
                    run+=3
                    print(A1,end = "  | ")
                else:
                    A1 = temp[run]
                    run+=3
                    print(A1,end = " | ")
                

                if cells["B2"] != 0:
                    B1 = cells["B2"]
                    run+=3
                    print(B1,end = "  | ")
                else:
                    B1 = temp[run]
                    run+=3
                    print(B1,end = " | ")

                if cells["C2"] != 0:
                    C1 = cells["C2"]
                    run = 1
                    print(C1,end = "    ")
                else:
                    C1 = temp[run]
                    run = 1 
                    print(C1,end = "   ")

                    
            elif current[1] == "X":                      
                print("       X      ",end = " ")        
            elif current[1] == "O":                      
                print("    -     -   ",end = " ")        

            count += 1
            if count < 3:
                print("|",end = "  ")





        if win1[1] == "D" or win1[0].available==0:
            first = "\n      |   -    "
        elif  win1[1] == "N" and win1[0].available!=0:
            first = "\n---+----+------"                   
        elif win1[1] == "X":                             
            first ="\n     /   \     "                   
        elif win1[1] == "O":                             
            first = "\n     -   -     "                  
                                                         
        if win2[1] == "D" or win2[0].available==0:      
            second = "         |   -    "                    
        elif  win2[1] == "N" and win2[0].available!=0:   
            second = "+-----+----+------"                
        elif win2[1] == "X":                             
            second ="        /   \     "                     
        elif win2[1] == "O":                             
            second = "        -   -     "                    
                                                         
        if win3[1] == "D" or win3[0].available==0:      
            third = "         |   -    "                   
        elif  win3[1] == "N" and win3[0].available!=0:   
            third = "+-----+----+----"                   
        elif win3[1] == "X":                             
            third ="        /   \      "
        elif win3[1] == "O":
            third = "        -   -     "

        final_line = first+second+third
        print(final_line)
    def print_line6(self):
        count = 0
        run = 2
        win1 = self.table['A2']   
        win2 = self.table['B2']   
        win3 = self.table['C2']   

        tables = ["A2","B2","C2"] 

        wins = [win1,win2,win3]
        while count < 3:
            temp = self.cell_reference[tables[count]]
            current = wins[count]

            if current[0].available == 0:
                print("      |-      ",end=" ")  


            elif current[1] == "N":
                cells = current[0].cells ##CELLS


                if cells["A3"] != 0:
                    A1 = cells["A3"]
                    run+=3
                    print(A1,end = "  | ")
                else:
                    A1 = temp[run]
                    run+=3
                    print(A1,end = " | ")
                

                if cells["B3"] != 0:
                    B1 = cells["B3"]
                    run+=3
                    print(B1,end = "  | ")
                else:
                    B1 = temp[run]
                    run+=3
                    print(B1,end = " | ")

                if cells["C3"] != 0:
                    C1 = cells["C3"]
                    run = 2
                    print(C1,end = "    ")
                else:
                    C1 = temp[run]
                    run = 2  
                    print(C1,end = "   ")





                                                         
            elif current[1] == "X":                    
                print("   /       \  ",end = " ")     
            elif current[1] == "O":                       
                print("       -      ",end = " ")      











            count += 1
            if count < 3:
                print("|",end = "  ")
        #print("\n   |    |      |     |    |      |     |    |   ")
        print("\n")
        print("---|----|------|-----|----|------|-----|----|---")
        print("")

    def print_line7(self):
        count = 0
        run = 0  
        win1 = self.table['A3']    
        win2 = self.table['B3']    
        win3 = self.table['C3']    

        tables = ["A3","B3","C3"] 

        wins = [win1,win2,win3]
        while count < 3:
            temp = self.cell_reference[tables[count]]
            current = wins[count]

            if current[0].available == 0:
                print("      |-      ",end=" ") 


            elif current[1] == "N":
                cells = current[0].cells


                if cells["A1"] != 0:
                    A1 = cells["A1"]
                    run+=3
                    print(A1,end = "  | ")
                else:
                    A1 = temp[run]
                    run+=3
                    print(A1,end = " | ")
                

                if cells["B1"] != 0:
                    B1 = cells["B1"]
                    run+=3
                    print(B1,end = "  | ")
                else:
                    B1 = temp[run]
                    run+=3
                    print(B1,end = " | ")


                if cells["C1"] != 0:
                    C1 = cells["C1"]
                    run = 0
                    print(C1,end = "    ")
                else:
                    C1 = temp[run]
                    run = 0  
                    print(C1,end = "   ")
                                                 
                    
            elif current[1] == "X":                       
                print("   \       /  ",end = " ")         
            elif current[1] == "O":                       
                print("       -      ",end = " ")         

            count += 1
            if count < 3:
                print("|",end = "  ")

        if win1[1] == "D" or win1[0].available==0:
            first = "\n      |   -    "
        elif  win1[1] == "N" and win1[0].available!=0:
            first = "\n---+----+------"                                      
        elif win1[1] == "X":                                                
            first ="\n     \   /     "                                      
        elif win1[1] == "O":                                                
            first = "\n     -   -     "                                     
                                                                            
        if win2[1] == "D" or win2[0].available==0:                         
            second = "         |   -    "                                       
        elif  win2[1] == "N" and win2[0].available!=0:                      
            second = "+-----+----+------"                                   
        elif win2[1] == "X":                                                
            second ="        \   /     "                                        
        elif win2[1] == "O":                                                
            second = "        -   -     "                                       
                                                                            
        if win3[1] == "D" or win3[0].available==0:                         
            third = "         |   -    "                                      
        elif  win3[1] == "N" and win3[0].available!=0:                      
            third = "+-----+----+----"                                      
        elif win3[1] == "X":                                                
            third = "        \   /     "
        elif win3[1] == "O":
            third = "        -   -     "

        final_line = first+second+third
        print(final_line)
    def print_line8(self):
        count = 0
        run = 1
        win1 = self.table['A3']   
        win2 = self.table['B3']   
        win3 = self.table['C3']   

        tables = ["A3","B3","C3"] 

        wins = [win1,win2,win3]
        while count < 3:
            temp = self.cell_reference[tables[count]]
            current = wins[count]

            if current[0].available == 0:
                print("      |     - ",end=" ")  


            elif current[1] == "N":
                cells = current[0].cells


                if cells["A2"] != 0:
                    A1 = cells["A2"]
                    run+=3
                    print(A1,end = "  | ")
                else:
                    A1 = temp[run]
                    run+=3
                    print(A1,end = " | ")
                

                if cells["B2"] != 0:
                    B1 = cells["B2"]
                    run+=3
                    print(B1,end = "  | ")
                else:
                    B1 = temp[run]
                    run+=3
                    print(B1,end = " | ")

                if cells["C2"] != 0:
                    C1 = cells["C2"]
                    run = 1
                    print(C1,end = "    ")
                else:
                    C1 = temp[run]
                    run = 1 
                    print(C1,end = "   ")

                    
            elif current[1] == "X":                      
                print("       X      ",end = " ")        
            elif current[1] == "O":                      
                print("    -     -   ",end = " ")        

            count += 1
            if count < 3:
                print("|",end = "  ")





        if win1[1] == "D" or win1[0].available==0:
            first = "\n      |   -    "
        elif  win1[1] == "N" and win1[0].available!=0:
            first = "\n---+----+------"                   
        elif win1[1] == "X":                             
            first ="\n     /   \     "                   
        elif win1[1] == "O":                             
            first = "\n     -   -     "                  
                                                         
        if win2[1] == "D" or win2[0].available==0:      
            second = "         |   -    "                    
        elif  win2[1] == "N" and win2[0].available!=0:   
            second = "+-----+----+------"                
        elif win2[1] == "X":                             
            second ="        /   \     "                     
        elif win2[1] == "O":                             
            second = "        -   -     "                    
                                                         
        if win3[1] == "D" or win3[0].available==0:      
            third = "         |   -    "                   
        elif  win3[1] == "N" and win3[0].available!=0:   
            third = "+-----+----+----"                   
        elif win3[1] == "X":                             
            third ="        /   \      "
        elif win3[1] == "O":
            third = "        -   -     "

        final_line = first+second+third
        print(final_line)
    def print_line9(self):
        count = 0
        run = 2
        win1 = self.table['A3']   
        win2 = self.table['B3']   
        win3 = self.table['C3']   

        tables = ["A3","B3","C3"] 

        wins = [win1,win2,win3]
        while count < 3:
            temp = self.cell_reference[tables[count]]
            current = wins[count]

            if current[0].available == 0:
                print("      |-      ",end=" ")  


            elif current[1] == "N":
                cells = current[0].cells ##CELLS


                if cells["A3"] != 0:
                    A1 = cells["A3"]
                    run+=3
                    print(A1,end = "  | ")
                else:
                    A1 = temp[run]
                    run+=3
                    print(A1,end = " | ")
                

                if cells["B3"] != 0:
                    B1 = cells["B3"]
                    run+=3
                    print(B1,end = "  | ")
                else:
                    B1 = temp[run]
                    run+=3
                    print(B1,end = " | ")

                if cells["C3"] != 0:
                    C1 = cells["C3"]
                    run = 2
                    print(C1,end = "    ")
                else:
                    C1 = temp[run]
                    run = 2  
                    print(C1,end = "   ")





                                                         
            elif current[1] == "X":                    
                print("   /       \  ",end = " ")     
            elif current[1] == "O":                       
                print("       -      ",end = " ")      











            count += 1
            if count < 3:
                print("|",end = "  ")
        #print("\n   |    |      |     |    |      |     |    |   ")
        print("\n ")

##THIS IS THE META PRINT COMMAND TO PRINT ALL THE LINES
    def print_table(self):
        self.print_line1()
        self.print_line2()
        self.print_line3()
        self.print_line4()
        self.print_line5()
        self.print_line6()
        self.print_line7()
        self.print_line8()
        self.print_line9() 
######################################

    

    



def main():

    condition = True
    current_player = "X"
    other_player = "O"

    #################################
    # TABLE FORMATION & INITILIZATION
    top_left = Table()
    top = Table()
    top_right = Table()

     
    centre_left = Table()
    centre = Table()
    centre_right = Table()


    bottom_left = Table()
    bottom = Table()
    bottom_right = Table()





    ######################################
    # THESE VALUES ARE FOR EXPERIMENTATION
    ## AND TESTING. JUST UNCOMMENT AND 
    ## CHANGE POSITIONS AND PLAYERS
    ######################################
    
    ##################################
    ## UNCOMMEND THIS REGION FOR DRAW#
    #centre.user_input("O",'A1')
    #centre.user_input("X",'B1')
    #centre.user_input("O",'C1')
    #centre.user_input("X",'A2')
    #centre.user_input("O",'B2')
    #centre.user_input("X",'C2')
    #centre.user_input("X",'A3')
    #centre.user_input("O",'B3')
    #centre.user_input("X",'C3')
    ##
    #centre_left.user_input("O",'A1')
    #centre_left.user_input("X",'B1')
    #centre_left.user_input("O",'C1')
    #centre_left.user_input("X",'A2')
    #centre_left.user_input("O",'B2')
    #centre_left.user_input("X",'C2')
    #centre_left.user_input("X",'A3')
    #centre_left.user_input("O",'B3')
    #centre_left.user_input("X",'C3')
    ##
    #centre_right.user_input("O",'A1')
    #centre_right.user_input("X",'B1')
    #centre_right.user_input("O",'C1')
    #centre_right.user_input("X",'A2')
    #centre_right.user_input("O",'B2')
    #centre_right.user_input("X",'C2')
    #centre_right.user_input("X",'A3')
    #centre_right.user_input("O",'B3')
    #centre_right.user_input("X",'C3')
    ##
    #top.user_input("O",'A1')
    #top.user_input("X",'B1')
    #top.user_input("O",'C1')
    #top.user_input("X",'A2')
    #top.user_input("O",'B2')
    #top.user_input("X",'C2')
    #top.user_input("X",'A3')
    #top.user_input("O",'B3')
    #top.user_input("X",'C3')
    ##
    #top_right.user_input("O",'A1')
    #top_right.user_input("X",'B1')
    #top_right.user_input("O",'C1')
    #top_right.user_input("X",'A2')
    #top_right.user_input("O",'B2')
    #top_right.user_input("X",'C2')
    #top_right.user_input("X",'A3')
    #top_right.user_input("O",'B3')
    #top_right.user_input("X",'C3')
    ##
    #top_left.user_input("O",'A1')
    #top_left.user_input("X",'B1')
    #top_left.user_input("O",'C1')
    #top_left.user_input("X",'A2')
    #top_left.user_input("O",'B2')
    #top_left.user_input("X",'C2')
    #top_left.user_input("X",'A3')
    #top_left.user_input("O",'B3')
    #top_left.user_input("X",'C3')
    ##
    #bottom_right.user_input("O",'A1')
    #bottom_right.user_input("X",'B1')
    #bottom_right.user_input("O",'C1')
    #bottom_right.user_input("X",'A2')
    #bottom_right.user_input("O",'B2')
    #bottom_right.user_input("X",'C2')
    #bottom_right.user_input("X",'A3')
    #bottom_right.user_input("O",'B3')
    #bottom_right.user_input("X",'C3')
    ##
    #bottom_left.user_input("O",'A1')
    #bottom_left.user_input("X",'B1')
    #bottom_left.user_input("O",'C1')
    #bottom_left.user_input("X",'A2')
    #bottom_left.user_input("O",'B2')
    #bottom_left.user_input("X",'C2')
    #bottom_left.user_input("X",'A3')
    #bottom_left.user_input("O",'B3')
    #bottom_left.user_input("X",'C3')
    ##
    #bottom.user_input("O",'A1')
    #bottom.user_input("X",'B1')
    #bottom.user_input("O",'C1')
    #bottom.user_input("X",'A2')
    #bottom.user_input("O",'B2')
    #bottom.user_input("X",'C2')
    #bottom.user_input("X",'A3')
    #bottom.user_input("O",'B3')
    


    ########################################
    ## UNCHECK THIS AND RUN TO SIMULATE A WIN
    #centre.user_input("X",'A1')
    #centre.user_input("X",'B1')
    #centre.user_input("X",'C1')
    #
    #centre_right.user_input("X",'A1')
    #centre_right.user_input("X",'B1')
    #centre_right.user_input("X",'C1')
    #
    #centre_left.user_input("X",'A1')
    #centre_left.user_input("X",'B1')





    table_list = [top_left,top,top_right,centre_left,centre,centre_right,bottom_left,bottom,bottom_right]
    U_Table = Meta_Table(table_list)
    
    ##################################
    print("WELCOME TO THE ULTIMATE TICTACTOE\n")
    print("PLAYERS WILL PLAY IN TURN. EACH PLAYER WILL CHOOSE 1 CELL BY TYPING CELL NAME")
    print("THE SECOND PLAYER WILL THEN PLAY IN THE TICTACTOE CORRESPONDING TO THE PREVIOUSLY PLAYED CELL")
    print("THE GAME WILL FINISH IF 1 PLAYER IS ABLE TO WIN THE META TICTACTOE")
    print("GOODLUCK...PLAYER X TO SERVE!")
   # print("\nAvailable: ",U_Table.avaialbe,"\n")#### THESE ARE TO CHECK HOW MANY CELLS ARE AVIALABLE STEPS 

    ##### THE INITIAL PRINT STATEMENTS#

    while condition == True:
        print()
        U_Table.print_table()
        message = "Player " + current_player +" Please Type Cell Name: "
        cell = input(message)
        reply = U_Table.user_input(current_player,cell)
        if reply == "1":   ##THIS REPLY SIMULATES SUCCESFULL INPUT
           #print("\nAvailable: ",U_Table.avaialbe)#### THESE ARE TO CHECK HOW MANY CELLS ARE AVIALABLE STEPS 
            temp = current_player
            current_player = other_player
            other_player = temp

            if U_Table.win != "N":
                condition = False
                if U_Table!= "D":
                    print()
                    U_Table.print_table()
                    print("\nThe Match Belongs To: ",U_Table.win)
                else:
                    print()
                    U_Table.print_table()
                    print("\nTHE MATCH WAS A DRAW")
            else:
                if U_Table.forced_cell != 0:
                    print("\nPlayer ",current_player," Must Choose From The Following:")
                    print(U_Table.cell_reference[U_Table.forced_cell])
                else:
                    print("Player ",current_player," Can Play In Any Availabe Cell")

        elif reply == "2":
            print("\nWRONG!  The Cell You Entered Was Already Occpied, please try again!\nPlease Select from the following cells: ")
            if len(U_Table.forced_cell)>0:
                print(U_Table.cell_reference[U_Table.forced_cell])
        elif reply == "3":
            print("\nERROR! The Entered Cell Does Not Exist. Make Sure To Input In Uppercase.\nPlease Select from the following cells: ")
            if len(U_Table.forced_cell)>0:
                print(U_Table.cell_reference[U_Table.forced_cell])
        elif reply == "4":
            print("\nTRY AGAIN! The Cell You Chose Belongs To A TicTacToe That Has Already Been Decided. Please Select Some other TicTacToe: ")
            if len(U_Table.forced_cell)>0:
                print(U_Table.cell_reference[U_Table.forced_cell])
        elif reply == "5":
            print("\nMISTAKE!  You Must Choose A Cell From The Appropriate TicTacToe: ")
            print(U_Table.cell_reference[U_Table.forced_cell])

main()