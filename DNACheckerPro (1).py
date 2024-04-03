import re
import os
import Bio

os.chdir ('E:')         
def DNACheck(file):
    file=open(file,'r')
    file=file.read()
    file=file.upper()
    file=file.replace('\n','') 

    for m in re.finditer(r'NNNN(.*)NNNN',file):
        DNAn=len(m.group(1))
        if DNAn<500:     
            print("Sequence is less than 500 nuleotides. Please Check for 'N'within the sequence")
        else:               
            seq=m.group(1)
            seq_count=(seq.count('N')/DNAn)
            print("Percentage of 'N' per sequence =",(seq_count)*100,"%")
            print("Number of 'N' present =",seq.count('N')," base pairs")
            print("Total length of sequence identified =",DNAn,"base pairs")
            if seq_count<0.05 :         
                print("The sequence is BEAUTIFUL")
           
            if 0.05<seq_count<0.20 :   
                print('The sequence is FINE')
                
            if 0.21<seq_count<0.39 :
                print('The sequence is OKAY')
            
            if seq_count>0.40 :
                print('The is sequence is UGLY')
