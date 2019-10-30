import pandas as pd
AtomType={1:'B',2:'H',3:'N'}
Bcutdic={'B':[1.8,1.4,1.8],'H':[1.8,1.2,1.8],'N':[1.8,1.4,1.8]}
Bcutdf=pd.DataFrame(Bcutdic,columns=['B','H','N'],index=['B','H','N'])
print("The distance cut for bond is :")
print(Bcutdf)
#  Bondcut=1.0  #Unit is angstrom
A=0
