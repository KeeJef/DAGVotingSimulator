import time
import json

votepernode = 2 
votesforconfrimation = 4 

def countlinks(array):
    counter = 0 
    counter2 = 0
    votetallyarray = {}
    oddarray = []
    normalarray = []

    while len(array) != counter:

        lastnum = array[counter][1]
        oddarray.append(array[counter][1])
        normalarray.append(array[counter][0])

        try:
            var = votetallyarray[str(array[counter][0])]
            var += 1 
            votetallyarray[str(array[counter][0])] = var
            pass
        except:
            votetallyarray[str(array[counter][0])] = 1 
            pass
        
        if array[counter][0]:
            pass

        counter += 1 
        pass

    main_list = list(set(oddarray) - set(normalarray))

    while len(main_list) != counter2:

        number = int(main_list[counter2])

        votetallyarray[str(number)] = 0 

        counter2 +=1 
        pass

    return votetallyarray, lastnum

def decidevote(votetally):
    counter = 1 
    votesthreshold = 0
    voteon = []

    while len(votetally) != counter - 1:

        if votetally[str(counter)] < votesforconfrimation:
            voteon.append(counter)
            votesthreshold += 1 
            pass
        if votesthreshold == votepernode:

            return voteon
        
        counter += 1 

        pass

    pass

def constructVote(voteon, lastnumber):
    counter = 0 
    lastnumber = int(lastnumber) + 1 
    while len(voteon) != counter:
        
        votetuple = (str(voteon[counter]),str(lastnumber))
        array.append(votetuple)

        counter += 1 

        pass


array = []

tupletest = ("1","2")
array.append(tupletest)

interations = 10
counter = 0 

while True:
    linkarray = countlinks(array)
    proposedvotes = decidevote(linkarray[0])
    constructVote(proposedvotes,linkarray[1])
    counter += 1
    time.sleep(2)
    print(str(counter) + " Iteration")

    with open('listfile.txt', 'w') as filehandle:
        json.dump(array, filehandle)

    pass

#with open('listfile.txt', 'w') as filehandle:
   # json.dump(array, filehandle)

pass




