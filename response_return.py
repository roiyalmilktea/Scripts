import docx
import datetime

template_file = 'response.docx'
save_file = 'reply.docx'

now = datetime.datetime.now()
commpany = input('会社名')
reculute = input('採用担当者')
# 書き換え
card = {
    '株式会社': commpany,
    '担当者様': reculute,
}


doc = docx.Document(template_file)
doc.save(save_file)
