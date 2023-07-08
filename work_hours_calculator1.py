import pandas as pd
from datetime import datetime, timedelta

df=pd.read_excel("test_1.xlsx" ,na_values=[""])

in_list=list(df['in']) #excel column called in
out_list=list(df['out']) #excel_column called out 
#List3=[]
start_time=""
end_time=""
total=0
hourly_wage=180 #change as you wish 

for i in range(len(in_list)):
    #calculate delta time 
    delta_time=((datetime.strptime(str(out_list[i]), "%H.%M")-datetime.strptime(str(in_list[i]),"%H.%M")))
    seconds_diff=int(delta_time.total_seconds())

    if seconds_diff<0:
        seconds_diff+=86400
    
    time=seconds_diff/3600
    total=round(total+time,2)
    bruto=round(total*hourly_wage,3)
net=0.85*bruto

contract_percentage=round((total/160)*100,2) #since in norway monthly work hours are 160 /m

total_string=f"""
total hours:{total}
bruto      :{bruto}
netto      :{net}
Contract %  :{contract_percentage}"""

print(total_string)
