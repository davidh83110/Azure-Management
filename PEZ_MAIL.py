import smtplib
from email.mime.text import MIMEText
from email.header import Header


class mail():

    @classmethod
    def send_mail(cls, content, header):

        FROM = 'elephant.sys@gmail.com'
        TO = ['jerry@payeasy.com.tw','jenny_liao@payeasy.com.tw',
              'jc_wang@payeasy.com.tw', 'chris_hsu@payeasy.com.tw',
              'lewis_shui@payeasy.com.tw','tony_tang@payeasy.com.tw',
              'kevin_huang@payeasy.com.tw', 'david_hsu@payeasy.com.tw']
        # MSG = str(error).encode('utf-8')
        MSG = MIMEText(content, 'plain', 'utf-8')
        MSG['From'] = Header(FROM, 'utf-8')
        MSG['To'] = Header('system_service_group@payeasy.com.tw', 'utf-8')
        MSG['Subject'] = Header(header, 'utf-8')

        mailServer = smtplib.SMTP('smtp.gmail.com', 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login('elephant.sys@gmail.com', 'dikmpncqawjambxe')
        mailServer.sendmail(FROM, TO, MSG.as_string())
        mailServer.quit()

