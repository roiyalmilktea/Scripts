import openpyxl as excel
import os


file = excel.Workbook()
sheet = file.active


array = [
        ["学生番号", "名前"],
        ["BM20026", "奥平　泰基"],
        ["BM20034", "川上　琉弥"],
        ["BM20039", "神崎　悠衣"],
        ["BM20049", "坂手　柊斗"],
        ["BM20053", "重本　悠貴"],
        ["BM20062", "洲濱　拓弥"],
        ["BM20100", "藤原　望  "],
        ["BM20120", "宗久　和樹"],
        ["BM20124", "森重　嘉優"],
        ["BM20141", "頼本　康  "],
        ["BL19002", "安部　穂  "],
        ["BL19009", "今井　健太"],
        ["BL19036", "木村　蒼輝"],
        ["BL19067", "永井　弘輝"],
        ["BL19073", "西村　伊織"],
        ["BL19076", "浜本　奏太"],
        ["BL19103", "森　俊介"],
        ["BL19114", "横山　廉"],
        ["BL19115", "吉田　龍矢"],
        ["BL18058", "田添　春樹"],
        ["BL18064", "谷口　順哉"],
        ["BL18092", "東川　尊人"],
        ["BL17006", "安部　貴弘"]
]
for i in range(23):
    for j in range(23):
        for k in range(2):
            sheet.cell(row=j+1, column=k+1, value=array[j][k])

sheet["A24"] = "教員"
sheet["B24"] = "松本慎平"

file.save("list.xlsx")
