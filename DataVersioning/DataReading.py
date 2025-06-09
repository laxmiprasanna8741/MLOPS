import pandas as pd 
import os

data = {'Name':['laxmi','Prasanna',"reddy"],
        'Age':[20,23,25],
        'City':['hyd','bgn','chennai']}

df = pd.DataFrame(data)


data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"csv file save to {file_path}")