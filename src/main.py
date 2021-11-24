import CYK_blockbased as CYK

lang=False
while lang==False:
    s=str(input("Masukkan nama file: "))
    s="test/"+s
    lang=CYK.readFile(s)
    
if (CYK.blockParse(lang)):
    print("Compile Success!")
else:
    print(f"Error in line {CYK.lineNumber[CYK.lineError]}!")
    print(f"Error in : {(CYK.lineError)}")