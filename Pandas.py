import pandas as pd

mydataset = {
    'cars'  :['Toyota','Ford','Nissan'],
    'passings': [4,5,7]
}
myvar= pd.DataFrame(mydataset)
print(myvar)