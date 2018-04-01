import re

def convertDNA(DNA):
    dnaLen = int(len(DNA))
    if (re.match('[ATGC]', DNA)) and ((dnaLen % 3) == 0):
        RNA_LIST = []
        RNA = ""
        codonList = []
        codonListChar = []
        global aminoAcidList
        aminoAcidList = []
        for x in DNA:  # Convert to RNA
            if x is "A":
                RNA_LIST.append("U")
            elif x is "T":
                RNA_LIST.append("A")
            elif x is "G":
                RNA_LIST.append("C")
            elif x is "C":
                RNA_LIST.append("G")
        RNA = RNA.join(RNA_LIST)
        print("")
        print("RNA:", RNA)
        print("")

        list(RNA)
        tempStr = ""

        for y in range(int((dnaLen/3 + 1))):
            if y > 0:
                codonListChar.append([RNA[(3 * y - 3)], RNA[(3 * y - 2)], RNA[(3 * y - 1)]])
                codonList.append(tempStr.join(codonListChar[y-1]))
        print("Codon List:", codonList)
        print("")

        for z in range(len(codonList)):
            if codonListChar[z][0] is "A":
                runA(codonListChar[z])
            elif codonListChar[z][0] is "U":
                runU(codonListChar[z])
            elif codonListChar[z][0] is "G":
                runG(codonListChar[z])
            elif codonListChar[z][0] is "C":
                runC(codonListChar[z])
        print("Amino Acids:", aminoAcidList)

    else:
        print("Invalid input. \nPlease input a string that only contains 'ATGC' and has a length that is a multiple of three.")


def runA(codon):
    if codon[1] is "G":
        if codon[2] is ("G" or "A"):
            aminoAcidList.append("Arginine")
        else:
            aminoAcidList.append("Serine")
    elif codon[1] is "A":
        if codon[2] is ("G" or "A"):
            aminoAcidList.append("Lysine")
        else:
            aminoAcidList.append("Asparagine")
    elif codon[1] is "C":
        aminoAcidList.append("Threonine")
    else:
        if codon[2] is "G":
            aminoAcidList.append("Methionine")
        else:
            aminoAcidList.append("Isoleucine")

def runU(codon):
    if codon[1] is "U":
        if codon[2] is ("U" or "C"):
            aminoAcidList.append("Phenylalanine")
        else:
            aminoAcidList.append("Leucine")
    elif codon[1] is "C":
        aminoAcidList.append("Serine")
    elif codon[1] is "A":
        if codon[2] is ("U" or "C"):
            aminoAcidList.append("Tyrosine")
        else:
            aminoAcidList.append("Stop")
    else:
        if codon[2] is ("U" or "C"):
            aminoAcidList.append("Cysteine")
        elif codon[2] is "A":
            aminoAcidList.append("Stop")
        else:
            aminoAcidList.append("Tryptophan")

def runG(codon):
    if codon[1] is "U":
        aminoAcidList.append("Valine")
    elif codon[1] is "C":
        aminoAcidList.append("Alanine")
    elif codon[1] is "G":
        aminoAcidList.append("Glycine")
    else:
        if codon[2] is ("U" or "C"):
            aminoAcidList.append("Aspartic acid")
        else:
            aminoAcidList.append("Glutamic acid")

def runC(codon):
    if codon[1] is "U":
        aminoAcidList.append("Leucine")
    elif codon[1] is "C":
        aminoAcidList.append("Proline")
    elif codon[1] is "G":
        aminoAcidList.append("Arginine")
    else:
        if codon[2] is ("U" or "C"):
            aminoAcidList.append("Histidine")
        else:
            aminoAcidList.append("Glutamine")

convertDNA(input("Type the DNA..."))