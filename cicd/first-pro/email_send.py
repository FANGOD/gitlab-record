# coding:utf-8
"""
User Name: Johnny@main.com.cn
Date Time: 2020-05-18 11:35:17
File Name: email_send.py @v1.0
"""
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


# 发件人邮箱账号
my_sender = 'ci@main.com'
# 发件人邮箱密码
my_pass = '12345'
# 收件人邮箱账号
to_list = ['c1@main.com']
cc_list = ['c3@main.com']


def mail():
    ret = True
    try:
        v1 = build_tags.split("-")[0]
        path = '//file4.main.com/Release-build/itms/{}/{}/'.format(v1, build_tags)
        email_text = '\n    DEBS build debs is ready in {}\n'.format(path)
        msg = MIMEText(email_text, 'plain', 'utf-8')
        msg['From'] = formataddr(["ci", my_sender])
        msg['To'] = ";".join([formataddr([i.split("@")[0], i]) for i in to_list])
        msg['Cc'] = ";".join([formataddr([i.split("@")[0], i]) for i in cc_list])
        msg['Subject'] = "main " + build_tags
        server = smtplib.SMTP("mailx.main.com", 587)
        server.ehlo()
        server.starttls()
        server.login(my_sender, my_pass)
        server.sendmail(my_sender, to_list + cc_list, msg.as_string())
        server.quit()
    except Exception:
        import traceback
        traceback.print_exc()
        ret = False
    return ret


if len(sys.argv) == 2:
    build_tags = str(sys.argv[1])
    ret = mail()


if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)
    # import pydoc
    # pydoc.doc(SomeClass)
