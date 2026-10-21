# from openpyxl import load_workbook
import  requests
# wb  = load_workbook(r"D:\Desktop\demo.xlsx")
# ws = wb["Sheet1"]
# print(ws.max_row)
# for row in range(2, ws.max_row+1):
#     usernames = ws.cell(row=row, column=1).value
#     passwords = ws.cell(row=row, column=2).value
#     if not (usernames and passwords):
#         continue
#     print(usernames, passwords)
resp = requests.post(url='http://47.237.80.205:9091/api/auth/login',
                 json={"userkey":"+8617692684850","password":"Aa123456"}, timeout=5,)

print(resp.status_code)
print(resp.content.decode('utf-8', 'replace'))
