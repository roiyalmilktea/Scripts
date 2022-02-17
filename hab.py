import openpyxl as excel


book = excel.Workbook()
sheet = book.active

sheet["A1"] = '家計簿リスト'

for i range(31):
    sheet.cell(row=(i+1), column=1, value=i)
book.save("hab.xlsx")
