import xlwt
from xlwt import Workbook


wb = Workbook()
MS = wb.add_sheet('SEM-1 MARKLIST 2020 BATCH')
MS.write(0,0,"Register Number")
MS.write(0,1,"Name")
MS.write(0,2,"Maths(External)")
MS.write(0,3,"Maths(Internal)")
MS.write(0,4,"Maths(Total)")
MS.write(0,5,"Digital(External)")
MS.write(0,6,"Digital(Internal)")
MS.write(0,7,"Digital(Total)")
MS.write(0,8,"C(External)")
MS.write(0,9,"C(Internal)")
MS.write(0,10,"C(Total)")
MS.write(0,11,"SE(External)")
MS.write(0,12,"SE(Internal)")
MS.write(0,13,"SE(Total)")
MS.write(0,14,"DBMS(External)")
MS.write(0,15,"DBMS(Internal)")
MS.write(0,16,"DBMS(Total)")
MS.write(0,17,"DBMS_LAB(External)")
MS.write(0,18,"DBMS_LAB(Internal)")
MS.write(0,19,"DBMS_LAB(Total)")
MS.write(0,20,"C_LAB(External)")
MS.write(0,21,"C_LAB(Internal)")
MS.write(0,22,"C_LAB(Total)")
MS.write(0,23,"EST(External)")
MS.write(0,24,"EST(Internal)")
MS.write(0,25,"EST(Total)")
MS.write(0,26,"SGPA")
MS.write(0,27,"Total")
MS.write(0,28,"Final Result")
wb.save("SEM-1 Mark.xls")


