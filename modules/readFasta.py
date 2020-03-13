import os
 
def readRnaFastaFile(fileName):
 
    if not os.path.exists(fileName):
        print("Error: File {} not available!".format(fileName))
        return (None,None,None)

    fconnect = open(fileName)
    lines = fconnect.readlines()
    fconnect.close()

    sequenceInfo = []
    moleculeName = None
    description = None

    # Get information from the first line - ignore the >
    firstLine = lines[0]
    firstLineCols = firstLine[1:].split()
    moleculeName = firstLineCols[0]
    description = firstLine[1:].replace(moleculeName,'').strip()

    # Now get the full sequence out
    fullSequence = ""
    for line in lines[1:]:

        line = line.strip()
        fullSequence += line

    # Divide up the sequence depending on type (amino acid or nucleic acid)
    for seqIndex in range(0,len(fullSequence),3):
        sequenceInfo.append(fullSequence[seqIndex:seqIndex+3])

    return (moleculeName,description,sequenceInfo)

#if __name__ == '__main__':
#    print(readRnaFastaFile("data/rnaSeq.txt"))