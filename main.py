import sys
import tkinter as tk
import pandas as pd
import tkinter.ttk as ttk
import smtplib
from email.mime.text import MIMEText
import datetime

# 不具合一覧
# INOPERATION
# WORN OUT
# SUPPLY
# DISCHARGER

file = pd.read_csv('data.csv')
file = file.dropna(how = "all",axis=1)
file = file.dropna(how = "all")
print("不具合情報:")
value = input()
value = value.upper()
inpe = file[file['不具合情報'].str.match('^.*'+value+'.*$')]
inpe_count = len(inpe)


d = datetime.datetime.today()
date = d.strftime("%Y-%m-%d")

# def send_mail():
#     try:
#         print("メールアドレス:")
#         toaddr = input()
#         raw_msg = "「" + value + "」の不具合は" + inpe_count + "件です。"
#         msg = MIMEText(raw_msg.encode(jp), 'plain', jp, )
#         fromaddr = "e185706@ie.u-ryukyu.ac.jp"
#         password = "LCqbEq85UMaE"
#
#         msg['Subject'] = "不具合情報" + date
#         msg['From'] = fromaddr
#         msg['To'] = toaddr
#
#         smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
#         smtpobj.ehlo()
#         smtpobj.starttls()
#         smtpobj.ehlo()
#         smtpobj.login(fromaddr, password)
#         smtpobj.sendmail(fromaddr, toaddr, msg)
#         smtpobj.close()
#         return True
#     except:
#         return False

print(inpe,"\n",inpe_count,"\n",value)

if (inpe_count >= 3):
    inpe.to_csv('to_csv_out'+date+'.csv')
    print("3回以上です")
    # try:
    #     if (send_mail()):
    #         print("Successfully sent email")
    # except Exception:
    #     print("Error: unable to send email")


# file['不具合情報'].str.match('^.*INOPERATION.*$')

# file[file['8'].isna() == False]

# inpe = file[file['不具合情報'].str.match('^.*INOPERATION.*$')]
# print(inpe)


# def search(event):
#     value = EditBox.get()
#     inpe = file[file['不具合情報'].str.match('^.*'+value+'.*$')]
#     inpe_count = len(inpe)
#     pd.set_option("display.max_columns", None)
#     pd.set_option("display.max_rows", None)
#     Static1 = tk.Label(text=inpe)
#     Static1.pack()
#     Static1.place(x=10, y=200)
#
#     Static1 = tk.Label(text=inpe_count)
#     Static1.pack()
#     Static1.place(x=10, y=100)
#
# root = tk.Tk()
# root.title(u"Software Title")
# root.geometry("1200x900")
# EditBox = tk.Entry(width=50)
# EditBox.pack()
#
# # value = EditBox.get()
#
# Button = tk.Button(text=u'button', width=50)
# Button.bind("<Button-1>",search)
# Button.pack()
#
#
# root.mainloop()
