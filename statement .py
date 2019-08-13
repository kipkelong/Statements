
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#fromaddr = input('enter your email address  \n')
#toaddr = input('enter recipients email address\n')
#Password = input ('Enter your Outlook password \n')
fromaddr="x@gmail.com"
toaddr="t0@gmail.com"
Password="qwse123"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "test email"

body = "If you are reciveing this email it means MVP has been delivered expect 133 emails with attachment for each dealer "
msg.attach(MIMEText(body, 'plain'))

import pandas as pd
df=pd.read_csv("/Users/shadrackkipkelong/Code/sample.csv")
df = df.where(pd.notnull(df), "nan")
df.rename(columns=lambda x: x.strip(" "),inplace=True)
df.columns.str.strip()
names=df.filter(["Dealer Code","Outlet Name"],axis=1)
import csv

for index, row in df.iterrows():
        with open(names.loc[index][1]+".csv", 'w') as csvFile:
            print(names.loc[index][1])
            writer = csv.writer(csvFile)
            writer.writerows(map(lambda x: [x],[df.columns[1],df.loc[index]]))
            csvFile.close()
        filename=names.loc[index][1]+".csv"
        attachment=open(filename)
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)
        server = smtplib.SMTP('smtp.mail.me.com', 587)
        server.starttls()
        server.login(fromaddr, Password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
            
