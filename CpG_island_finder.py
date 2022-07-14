# Programming Exercise 1 CpG island
# Luis del Peso, Sep 2022
# Locates the position of a CpG island

"""
Modificaciones (Sergio Alías, 20211003):
- Guardo en una lista, Freq_CpG, las frecuencias de CG de todas las ventanas
- Calculo la desviación estándar, sd
- Compruebo si el %GC de las ventanas supera al valor de
  la media + 2·sd (para un nivel de confianza del 95%), y en tal caso:
    - Cuenta el inicio de la ventana como el inicio de una isla CpG, y mira
      en las siguientes ventanas hasta que el %CG deje de ser superior a la media + 2·sd,
      y en ese momento toma el final de esa ventana como el final de la isla
"""

## Function to count nucleotide frequencies
def NuclFrq(Seq):
    Nucleotides=["A","C","G","T"]
    Nucl_count=[]#Initializes Dictionary for nucleotides
    for Nucl in Nucleotides:
        Nucl_count.append(Seq.count(Nucl))
    # Sequence length (Note that there might be "Ns" in the sequence)
    Nucl_total=sum(Nucl_count)
    Nucl_freq=[Count/Nucl_total for Count in Nucl_count]
    return(dict(zip(Nucleotides,Nucl_freq)))#returns a identifier-null dict

## Function to count dinucleotide frequencies
def diNuclFrq(Seq):
    # Initializes a dictionary for all 16 potential dinucleotides
    diNucl_freq={}#Hash storing observed dinucleotide frecuencies
    for Base1 in ["A","C","G","T"]:
        for Base2 in ["A","C","G","T"]:
            diNucl_freq[Base1+Base2]=0
    # count frequencies
    for pos in range(0,len(Seq)-1):
        if Seq[pos:pos+2] in diNucl_freq.keys():
            diNucl_freq[Seq[pos:pos+2]]=diNucl_freq[Seq[pos:pos+2]]+1
    # Sequence length (Note that there are "N" in Chr22 sequence)
    diNucl_len=sum(diNucl_freq.values())
    absFqList=diNucl_freq.values()
    Frq=[round(absfr/diNucl_len,4) for absfr in absFqList]
    return(dict(zip(diNucl_freq.keys(),Frq)))#returns a identifier-null dict.

## Function to Read FASTA sequence
def ReadFASTA(File):
    Seq="" #initializes variable that will store the sequece
    try:
        MyFile=open(File,"r")
    except:
        print("File ", File," not found")
        exit()
    for Line in MyFile:
        if not(">" in Line):## skips the title line of the FASTA format
            Seq=Seq+Line.strip()
    MyFile.close()
    Seq=Seq.upper()#make sure all symbols are encoded equally
    return(Seq)

## Program main body
from math import sqrt #required to compute sqrt
Seq=ReadFASTA("ACTB_genomic.fa")#Reads FASTA seq


## Count dinucleotide freq in a sliding window
Start_pos=-1#Initial position of the CpG island
WinSize=1000#Sliding window size
pos=0#starting position to search the sequence
Freq_CpG=[] # List for the %CG of all windows

while (pos<len(Seq)-WinSize):
    subSeq=Seq[pos:pos+WinSize]
    Freq_CpG.append(diNuclFrq(subSeq)['CG']) # Getting the %CG
    pos+=1
    print("Calculating %CG of window", pos)

average = sum(Freq_CpG)/len(Freq_CpG) # Calculating the average
numerator = [] # Preparing the numerator of standard deviation formula
for i in Freq_CpG:
    numerator.append(((i-average)**2)) # Calculating (xi - xm)^2
sd = sqrt(sum(numerator)/(len(numerator))) # And here we have the sd

CpG_islands = [] # list that will be storing other lists with the start and end of CpG islands

i = 0 # counter for the next loop
while i < len(Freq_CpG): # loop iterating the list of %GC of the windows
    print("Searching %CG greater than average + 2·sd, window", i, "...")
    if Freq_CpG[i] > average + 2*sd: # "if the %CG is greater than average + 2·sd"
        start_CpG = i + 1 # we found one! we store the start
        end_CpG = i + WinSize + 1 # and we store the provisional end
        final = 1 # variable for the next loop
        while Freq_CpG[i + final] > average + 2*sd: # "while next windows keep having %CG greater than avegare + 2·sd"
            print("CpG island found! Searching the end... (Iteration nº {})".format(final))
            end_CpG = i + final + WinSize + 1 # modify the end of the island, now the final of the next window is the new end
            final += 1
        CpG_islands.append([start_CpG, end_CpG]) # We append our brand new island to the list of islands
        i = i + final + WinSize # Skipping the loop to the final of the CpG island, it doesnt make sense to check windows that starts inside our recently discovered island
    i += 1
print("CpG islands of the sequence are", CpG_islands)


### Results with file "ACTB_genomic.fa" ###
# Moodle solution: 2516, 4047
# My "solution" with 2·sd: 2040, 4469
# My "solution" with 3·sd: 2257, 3262
