def almostIncreasingSequence(sequence, recurs=False):
    for i in range(len(sequence)-1):
        if sequence[i] >= sequence[i+1] and recurs == False: # Base Run 
            seq1 = sequence[:]
            seq2 = sequence[:]

            seq1.pop(i)
            ireturn = almostIncreasingSequence(seq1, True)

            seq2.pop(i+1)
            i1return = almostIncreasingSequence(seq2, True)

            return ireturn or i1return

        elif sequence[i] >= sequence[i+1] and recurs == True: # Recursive Run
            return False
    return True
