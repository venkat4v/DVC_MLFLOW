import pandas as pd


Data = [

{"name":"venkat","age":27,"city":"vizag"},
{"name":"venkat1","age":28,"city":"vizay"},
{"name":"venkat2","age":29,"city":"viziag"},
{"name":"venkat3","age":30,"city":"visakah"}

]


df = pd.DataFrame(Data)

df.to_csv("data/data.csv",index = False)