def readTxtFile():
    with open ("laptop.txt",'r') as file:
        laptop_ID=1
        laptops_dictionary={}
        for line in file:
            line=line.replace('\n',' ')
            laptops_dictionary[laptop_ID]= (line.split(","))
            laptop_ID += 1
    return(laptops_dictionary)

laptop = readTxtFile()