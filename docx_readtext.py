import docx

doc = docx.Document('little.docx')
for p in doc.paragraphs:
    print(p.text)
