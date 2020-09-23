appelbomen = 333
appelbomenInSchaduw = ((appelbomen/3)*2)
appelbomenInZon = appelbomen - appelbomenInSchaduw
appelsInZon = appelbomenInZon * 146
appelsInSchaduw = (appelbomenInSchaduw * 146)* 0.8
aantalAppels = appelsInZon + appelsInSchaduw
mijnAppels = aantalAppels/3
print(mijnAppels)
mijnVerkoopbareAppels = round(mijnAppels)
print(mijnVerkoopbareAppels)