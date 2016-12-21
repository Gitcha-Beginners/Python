#--*- coding : cp949 -*-
import smtplib
from email.mime.text import MIMEText
#어떤 이메일을 사용할 것인지 정한다
smtpHost = "smtp.naver.com"
#메세지를 MINETEXT에 담아서 보낸다 이때 한글을 쓰려면 인코딩을 넣어줘야 한다
text = "안녕하세요"
msg = MIMEText(text.encode("utf-8"),_charset='UTF-8')
#보내는 사람의 이메일 주소와 비밀번호, 그리고 받는사람의 이메일 주소를 써놓는다
#받는사람의 이메일은 여러개일 수 있다
senderAddr =
password =
recipientAddr =

msg['Subject'] = "Hello world!"
msg['From'] = senderAddr
msg['To']=recipientAddr

#smtp 서버를 이용해 587 포트로 네이버에 연결한다
s=smtplib.SMTP(smtpHost,587)
s.ehlo()
s.starttls()
s.ehlo()
#네이버에 로그인 한다
s.login(senderAddr,password)
#메세지를 받는사람에게 보낸다
s.sendmail(senderAddr,[recipientAddr],msg.as_string())
s.close()

# 부가적인 설정
#naver에서 사용할 경우에는 환경설정에서 IMAP 설정에 들어가서 따로 설정을 해주어야 제대로 발송이 됩니다
#gmail에서 사용할 경우에는 경고 이메일이 오는데 그 메일 안에 링크타고 들어가서 설정을 해주면 됩니다