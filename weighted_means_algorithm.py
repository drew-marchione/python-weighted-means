from texttable import Texttable

# Group Adjust Method
# The algorithm needs to do the following:
# 1.) For each group-list provided, calculate the means of the values for each
# unique group.
#
#   For example:
#   vals       = [  1  ,   2  ,   3  ]
#   ctry_grp   = ['USA', 'USA', 'USA']
#   state_grp  = ['MA' , 'MA' ,  'CT' ]
#
#   There is only 1 country in the ctry_grp list.  So to get the means:
#     USA_mean == mean(vals) == 2
#     ctry_means = [2, 2, 2]
#   There are 2 states, so to get the means for each state:
#     MA_mean == mean(vals[0], vals[1]) == 1.5
#     CT_mean == mean(vals[2]) == 3
#     state_means = [1.5, 1.5, 3]
#
# 2.) Using the weights, calculate a weighted average of those group means
#   Continuing from our example:
#   weights = [.35, .65]
#   35% weighted on country, 65% weighted on state
#   ctry_means  = [2  , 2  , 2]
#   state_means = [1.5, 1.5, 3]
#   weighted_means = [2*.35 + .65*1.5, 2*.35 + .65*1.5, 2*.35 + .65*3]
#
# 3.) Subtract the weighted average group means from each original value
#   Continuing from our example:
#   val[0] = 1
#   ctry[0] = 'USA' --> 'USA' mean == 2, ctry weight = .35
#   state[0] = 'MA' --> 'MA'  mean == 1.5, state weight = .65
#   weighted_mean = 2*.35 + .65*1.5 = 1.675
#   demeaned = 1 - 1.675 = -0.675
#   Do this for all values in the original list.
#
# 4.) Return the demeaned values

# Hint: See the test cases below for how the calculation should work.

def group_adjust(vals, groups, weights):
    """ 
    group_adjust will restructure vals, groups, and weights into one list that consists of dictionaries
    in order to keep track of each element's number of occurences and values.
    The structure of the dictionary looks like this:
        {Key : {Key : {Key : Value}}}
    If we pass in three groups consisting of country, state, and city our data will look like:
        {'Country': {'USA': {'Occurences': 5, 'Value': 19 }}}
        {'State': {'MA': {'Occurences': 3, 'Value': 6}, 'RI': {'Occurences: 2, 'Value': 13}}}
        {'City': {'Boston': {'Occurences': 2, 'Value': 5}, 'Providence':  {'Occurences': 2, 'Value': 13}, 'Weymouth': {'Occurences': 1, 'Value': 1}}}
    To get this data structured in a dictionary, the code iterates 3 times.  The first iteration
    handles country, the second handles state, and the third handles city.
    Each iteration overwrites the dictionary, so at the end of each iteration I append the dictionary to a list.
    The list is then passed into the find_mean() function which in turn after a few more function calls
    returns the demeaned values.
    """

    # Step 1A (Restructure Data)
    keepTrackList = []
    list1 = []
    switch = True
    for i in xrange(len(groups)):
        if i == 0: groupType = 'Country'
        elif i == 1: groupType = 'State'
        elif i == 2: groupType = 'City'
        for j in xrange(len(groups[i])):
            checkVar = groups[i][j]
            if checkVar not in keepTrackList:
                value = 0
                count = 0
                keepTrackList.append(checkVar)
                for k in xrange(len(groups[i])):
                    if checkVar == groups[i][k]:
                        if vals[k] is not None:
                            if switch is True:
                                # Dictionary declarations
                                dic = {}
                                dic[groupType] = {}
                                switch = False
                            count += 1
                            dic[groupType][groups[i][k]] = {}
                            dic[groupType][groups[i][k]]['Occurences'] = count
                            value = value + vals[k]
                            dic[groupType][groups[i][k]]['Value'] = value
                            if k == len(groups[i]) - 1:
                                list1.append(dic) # Adds dic to list1 before dic gets reinitialized to empty on next iteration
        keepTrackList = []
        switch = True
        #print list1 # What the list looks like
    find_mean(vals, groups, weights, list1)

# Step 1B (Find Mean Values)
def find_mean(vals, groups, weights, list1):
    """
    Finding The Mean Value

    The code iterates through list1 and accesses the first key which is either
    the string 'Country', 'State', or 'City'.
    This is achieved by list1[i].items)[0][0].
    To find the mean we must destructure list1 and access each elements value 
    and divide it by the number of times it occurs.
    Example:
        list1[0] --> Accesses the first element of list1
        list1[0][countryOrStateorCity] --> Destructures the list and accesses the Country dictionary
        list1[0][countryOrStateorCity][countryName]['Value'] --> Continues destructuring all the way down 
        to a specific country names value.
        Assign the value and number of occurences to variables and divide the two to get the mean value.
        Store it in the countryMean dictionary.
        The next iteration will do the same with the State dictionary and so on for as many groups the program is given.
    """

    countryMean = {}
    stateMean = {}
    cityMean = {}
    keepTrackList = []
    for i in xrange(len(groups)):
        countryOrStateOrCity = list1[i].items()[0][0]
        #print countryOrStateOrCity
        if countryOrStateOrCity == 'Country':
            for x in xrange(len(groups[0])):
                countryName = groups[0][x]
                if countryName not in keepTrackList:
                    #print countryName
                    if list1[0][countryOrStateOrCity][countryName]['Value'] is None:
                        countryMean[countryName] = None
                        keepTrackList.append(countryName)
                    else:
                        #print list1[0][countryOrStateOrCity][countryName]['Value']
                        value = float(list1[0][countryOrStateOrCity][countryName]['Value'])
                        occurences = float(list1[0][countryOrStateOrCity][countryName]['Occurences'])
                        mean = value / occurences
                        countryMean[countryName] = mean
                        keepTrackList.append(countryName)
        elif countryOrStateOrCity == 'State':
            for x in xrange(len(groups[1])):
                stateName = groups[1][x]
                if stateName not in keepTrackList:
                    #print stateName
                    if list1[1][countryOrStateOrCity][stateName]['Value'] is None:
                        stateMean[stateName] = None
                        keepTrackList.append(stateName)
                    else:
                        #print list1[0][countryOrStateOrCity][countryName]['Value']
                        value = float(list1[1][countryOrStateOrCity][stateName]['Value'])
                        occurences = float(list1[1][countryOrStateOrCity][stateName]['Occurences'])
                        mean = value / occurences
                        stateMean[stateName] = mean
                        keepTrackList.append(stateName)
        elif countryOrStateOrCity == 'City':
            for x in xrange(len(groups[2])):
                cityName = groups[2][x]
                if cityName not in keepTrackList:
                    #print cityName
                    if list1[2][countryOrStateOrCity][cityName]['Value'] is None:
                        cityMean[cityName] = None
                        keepTrackList.append(cityName)
                    else:
                        #print list1[0][countryOrStateOrCity][countryName]['Value']
                        value = float(list1[2][countryOrStateOrCity][cityName]['Value'])
                        occurences = float(list1[2][countryOrStateOrCity][cityName]['Occurences'])
                        mean = value / occurences
                        cityMean[cityName] = mean
                        keepTrackList.append(cityName)
        keepTrackList = []
    return find_weighted_means(vals, groups, weights, countryMean, stateMean, cityMean)

# Step 2 (Calculate Weighted Means)
def find_weighted_means(vals, groups, weights, countryMean, stateMean, cityMean):
    """ 
    Find Weighted Means 
    
    Use the countryMean, stateMean, and cityMean dictionaries to access the mean values.
    If length of groups is equal to 2 then we know we are working with 2 groups which are Country and State
    If length of groups is equal to 3 then the third group is city.
    We must test for that first.
    Use variables countryVar, stateVar, and cityVar to access mean values
    """

    weightedMeansList = []
    if len(groups) == 2: # Country and State
        for i in xrange(len(groups[0])):
            isNone = vals[i]
            countryVar = groups[0][i]
            stateVar = groups[1][i]
            #print countryVar, stateVar
            if isNone is not None:
                weightedMeansVar = (countryMean[countryVar] * weights[0]) + (stateMean[stateVar] * weights[1])
                weightedMeansList.append(weightedMeansVar)
            else:
                weightedMeansList.append(isNone)
    if len(groups) == 3: # Country, State, City
        for i in xrange(len(groups[0])):
            isNone = vals[i]
            countryVar = groups[0][i]
            stateVar = groups[1][i]
            cityVar = groups[2][i]
            #print countryVar, stateVar, cityVar
            if isNone is not None:
                weightedMeansVar = (countryMean[countryVar] * weights[0]) + (stateMean[stateVar] * weights[1]) + (cityMean[cityVar] * weights[2])
                weightedMeansList.append(weightedMeansVar)
            else:
                weightedMeansList.append(isNone)
    #print "Weighted Means: ", weightedMeansList
    return find_demeaned_values(vals, groups, weightedMeansList)

# Step 3 (Calculate Demeaned Values)
def find_demeaned_values(vals, groups, weightedMeansList):
    """ 
    Find Demeaned Values
    
    Subtract the weighted mean by the original value.

    Texttable displays the data in a nice looking table.
    """
    demeanedValuesList = []
    for x in xrange(len(weightedMeansList)):
        if weightedMeansList[x] is not None:
            demeanedVar = vals[x] - weightedMeansList[x]
            demeanedValuesList.append(demeanedVar)
        else:
            demeanedValuesList.append(None)
    #print "Demeaned Values: ", demeanedValuesList
    t = Texttable()
    if len(groups) == 2:
        t.add_row(['Location', 'Demeaned Value'])
        for x in xrange(len(demeanedValuesList)):
            t.add_row([str(groups[0][x]) + ", " + str(groups[1][x]), demeanedValuesList[x]])
        print t.draw()
        print "\n"
    if len(groups) == 3:
        t.add_row(['Location', 'Demeaned Value'])
        for x in xrange(len(demeanedValuesList)):
            t.add_row([str(groups[0][x]) + ", " + str(groups[1][x]) + ", " + str(groups[2][x]), demeanedValuesList[x]])
        print t.draw()
        print "\n"
    # Step 4 (Return Demeaned Values)
    return demeanedValuesList