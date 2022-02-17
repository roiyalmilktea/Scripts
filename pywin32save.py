import win32com.client as com

app=com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

book = app.Workbook.Add()
sheet = book.ActiveSheet

sheet.Range("B2").Value = "こんにちは"
