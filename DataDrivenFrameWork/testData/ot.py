import os,openpyxl

path=os.path.dirname(os.path.dirname(__file__))
excel=path+r'\testData\126邮箱联系人.xlsx'
wb=openpyxl.load_workbook(excel)
sheet=wb.get_sheet_by_name('126账号')
ab=sheet.columns[4]
print(ab)