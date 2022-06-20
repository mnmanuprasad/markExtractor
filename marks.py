from index import extract
for i in range(0,117):
    reg=203242210158+i
    payload={
        'exam_id':58,
        'prn':reg,
        'btnresult':'Get Result'
    }
    extract(i+1,payload)


