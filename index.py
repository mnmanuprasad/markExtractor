from bs4 import BeautifulSoup
import requests
import re
from xl import wb,MS
def extract(index,payload):
    r=requests.post("https://pareeksha.mgu.ac.in/Pareeksha/index.php/Public/PareekshaResultView_ctrl/index/3",data=payload)

    soup=BeautifulSoup(r.content,'html.parser')

    result={
        'maths':[],
        'digital':[],
        'c':[],
        'se':[],
        'dbms':[],
        'dbms_lab':[],
        'c_lab':[],
        'est':[],   #Employability Skill Training
    }
    count=3
    for sub in result:
        for i in range(3,11):
            m = soup.select_one(f"#mgu_btech_contentholder table table:nth-child(6) tr:nth-child({count}) td:nth-child({i})").get_text().strip()
            result[sub].append(m)
        count=count+1

    name = soup.select_one(f"#mgu_btech_contentholder table table:nth-child(5) tr tr:nth-child(2) td:nth-child(3)").get_text().strip()

    sgpa_str = soup.select_one("#mgu_btech_contentholder table table:nth-child(6)  tr:nth-child(11) td:nth-child(2)").get_text()
    # sgpa_str = re.findall("([0-9]+|[.]+[0-9])", sgpa_str)
    # print(sgpa_str)
    sgpa_str = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", sgpa_str)
    
    sgpa=""
    if(sgpa_str):
        sgpa=sgpa_str[0]
    
    print("SGPA :",sgpa)

    final_result = soup.select_one("#mgu_btech_contentholder table table:nth-child(6)  tr:nth-child(11) td:nth-child(6)").get_text().strip()

    total_mark = soup.select_one("#mgu_btech_contentholder table table:nth-child(6)  tr:nth-child(11) td:nth-child(3)").get_text().strip()


    MS.write(index,0,payload["prn"])
    MS.write(index,1,name)
    MS.write(index,2,result["maths"][0])
    MS.write(index,3,result["maths"][2])
    MS.write(index,4,result["maths"][4])

    MS.write(index,5,result["digital"][0])
    MS.write(index,6,result["digital"][2])
    MS.write(index,7,result["digital"][4])

    MS.write(index,8,result["c"][0])
    MS.write(index,9,result["c"][2])
    MS.write(index,10,result["c"][4])

    MS.write(index,11,result["se"][0])
    MS.write(index,12,result["se"][2])
    MS.write(index,13,result["se"][4])

    MS.write(index,14,result["dbms"][0])
    MS.write(index,15,result["dbms"][2])
    MS.write(index,16,result["dbms"][4])

    MS.write(index,17,result["dbms_lab"][0])
    MS.write(index,18,result["dbms_lab"][2])
    MS.write(index,19,result["dbms_lab"][4])

    MS.write(index,20,result["c_lab"][0])
    MS.write(index,21,result["c_lab"][2])
    MS.write(index,22,result["c_lab"][4])

    MS.write(index,23,result["est"][0])
    MS.write(index,24,result["est"][2])
    MS.write(index,25,result["est"][4])

    MS.write(index,26,sgpa)
    MS.write(index,27,total_mark)
    MS.write(index,28,final_result)


    wb.save("SEM-1 Mark.xls")
    print(result)





