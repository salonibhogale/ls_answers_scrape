import pandas as pd
from selenium import webdriver
import collections
import os
import time
import csv
import PyPDF2

ls13 = pd.read_csv('/Users/salonibhogale/PycharmProjects/Muslim_Representation/Questions_Data/ls13_Q.csv',encoding='latin1')

browser = webdriver.Chrome()

errors=[]
with open("output.csv",'w') as f:
    writer = csv.writer(f, dialect='excel')
    for i in range(0,len(ls13)):
        try:
            url = ls13.Q_Link.iloc[i]
            browser.get(url)
            elem = browser.find_element_by_xpath('//*[@id="ContentPlaceHolder1_lnkPdfDownload"]')
            elem.click()
            time.sleep(1)
            pdf_file = open('Answer_PDFs/QResult15.pdf', 'rb')
            read_pdf = PyPDF2.PdfFileReader(pdf_file,'rb')
            number_of_pages = read_pdf.getNumPages()
            c = collections.Counter(range(number_of_pages))
            p = ''
            for j in c:
               page = read_pdf.getPage(j)
               page_content = page.extractText()
               p = p + str(page_content.encode('utf-8'))
            answer_text = p.split('ANSWER')[2]
            id = str(ls13.ID.iloc[i])
            writer.writerow([id,answer_text])
            os.remove('Answer_PDFs/QResult15.pdf')
            print(i)
        except:
            errors.append(i)
