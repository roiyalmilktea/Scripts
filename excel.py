import openpyxl as excel

book = excel.Workbook()

sheet = book.active

sheet['A1'] = "hello!"

book.save("hello.xlsx")
