# Level 1
# A function that returns to the user how many tables are currently available.
# The sole parameter is a 2 dimensional array, containing all the tables and reservations
# Return a List, containing all the ID's where a value in the tables is o
# Iterate throught the list and return every value where the index == 'o'

def find_free_tables(tables):
    # Creating the list of tables that will be returned
    free_tables = []
    # Sets the rows = to 1 so that it can skip over the header row
    row = 1
    # Here I visisted python documentation to find out how to reference the specific rows and columns of a 2d array, and to recall the syntax for the len function
    # A while loop is used to iterate through the length of the tables array, exluding the 
    while row < len(tables):
        # The columns must be reset back to 0 every time the nested while loop iterates so that it checks the columns of every row in tables
        column = 0
        # Iterates through every column in tables. tables[0] refers to the number of rows in a list
        while column < len(tables[0]):
            # Checks if a specific index is o, if it is, then that index is added to the table
            if tables[row][column] == 'o':
                # Adds the table index to the list of free tables
                free_tables.append(row + "" + column)
            # Increments the columns so that every column is checked
            column = column + 1
        # Increments the rows so that every row is checked
        row = row + 1
        
    return free_tables
            
# Level 2
# A function that, depending on the guests party size, tells them which FREE tables can seat their party
# Takes an integer, representing the party size as a parameter
# Takes the list of free_tables as another parameter
# Returns one index from the free_tables list that can seat the party
# Since the previous level has already found all the free, we can iterate through that list to find one table that fits the party

def find_table(party_size, freeTables):
    # Iterate through the freeTables
    for i in range(len(freeTables)):
        # find an index where the header(Number of people seated) = party_size
        # I got stuck here. In the example list of restaurant tables, the number of people sitting at the table doesn't follow any pattern
        # I know that my code will require me to access the number in parentheses following the table number. So my code will need to access T1(#)
        # I do not know how to access this element of the array list.
        # An idea I have, but do not know how to implement is that because the free_tables indices are in the format or rows, space, columns, if I can find a way to split up these words then I could refer to the restaurant tables
        # Then from there, I would need to find out how to access the header of each column.
        if freeTables[i] >= party_size:
            # Returns the table index that is free and fits the groups size
            return freeTables[i]
    # If there were no available seats, return a message informing the user that their are no available seats
    sorry = "Sorry, there are no available seats"
    # If there was a matching table, then this code, which returns the sorry message won't execute
    return sorry
    

# Level 3
# A function that returns all of the possible free tables that fit the groups size
# This function sounds nearly the same as level 2, except it should instead return a LIST of free tables that fit the group, instead of just the first one that fits the criteria.
# Takes the same parameters as level 2, an integer that represents the party size, and a list of free tables

def find_all_tables(party_size, freeTables):
    # Creates a list of tables that are free and fit the group size
    matching_tables = []
    # Iterates through the free tables list
    for i in range(len(freeTables)):
        # Finds every free Table whose size is AT LEAST the party size
        if freeTables[i] >= party_size:
            # Adds the free table index, where the size is at least the party size
            matching_tables.append(freeTables[i])
    return matching_tables
# Level 4
# A function that checks the adjacent values of a selected table in the restaurant_tables list, and return a combination of tables whose added up seats can accomodate the party.
# Takes the matching tables index as a parameter, as well as the group size
# Check the adjacent tabless, which can be done by [row-1][col], [row+1][col], [row][col-1], [row][col+1], which checks all the adjacent indices
# Return a combination of tables whose sizes combined can accomodate the group
def combine_tables(guests_table, party_size):
    # Checks to see if the party_size is indeed less than their table size
    if party_size < table_size:
        # Makes a list of the adjacent tables
        adjacentTables = [[row-1][col], [row+1][col], [row][col-1], [row][col+1]]
        # I do not know how to keep track of the tables size along with its index
        
        #List of all the combinations of tables that accomodate the party
        CombinedTables = []
        # .size() is a placeholder for the size of the table
        for i in range len(adjacentTables)
            # If the adjacent tables size combined with the guests table size can accomodate their full, party, add that combination to the lsit of possible combined tables
            if adjacentTables[i].size() + guests_tables.size() >= party_size:
                #Adds the table to a list of tables that can be combined with the users table
                CombinedTables.append(adjacentTables[i])
            
        return CombinedTables
    
    else:
        return "thanks!"
    
    
    
    
    