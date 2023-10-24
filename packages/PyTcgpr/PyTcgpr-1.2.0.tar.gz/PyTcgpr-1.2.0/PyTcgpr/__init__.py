import datetime
now = datetime.datetime.now()
formatted_date_time = now.strftime('%Y-%m-%d %H:%M:%S')

art = '''
████████╗ ██████╗ ██████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔════╝██╔════╝ ██╔══██╗██╔══██╗
   ██║   ██║     ██║  ███╗██████╔╝██████╔╝
   ██║   ██║     ██║   ██║██╔═══╝ ██╔══██╗
   ██║   ╚██████╗╚██████╔╝██║     ██║  ██║
   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝
'''                                          

print(art)
print('Screening Abnormal Data and Important features for Small DataSet')
print('TCGPR, Bin Cao, Advanced Materials Thrust, HKUST(GZ)')
print('Intro : https://github.com/Bin-Cao/TCGPR/blob/main/Intro/TCGPR.pdf')
print('URL : https://github.com/Bin-Cao/TCGPR')
print('DOI : https://doi.org/10.1038/s41524-023-01150-0 (npj Comput Mater)')
print('Executed on :',formatted_date_time, ' | Have a great day.')  
print('\n')
