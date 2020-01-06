import numpy as np
import pandas as pd
dictionary_teams={
    'Duke':1,
    'MichiganState':2,
    'LSU':3,
    'VirginiaTech':4,
    'MississippiState':5,
    'Maryland':6,
    'Louisville':7,
    'VCU':8,
    'UCF':9,
    'Minnesota':10,
    'Bellmont/Temple':11,
    'Liberty':12,
    'SaintLouis':13,
    'Yale':14,
    'Bradley':15,
    'NC Central/NorthDokotaState':16
    
    
    
}
print(dictionary_teams)

for i in range(20):
    x= np.random.randint(1,16,1)
    a=np.random.randint(16,32,1)
    b=np.random.randint(32,48,1)
    c=np.random.randint(48,64,1)
    e=pd.Series([x,a,b,c], index=[1,2,3,4])
    print(e)
    y=e[np.random.randint(1,4,1)]
    print(y)
   
