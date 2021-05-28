import win32com.client as win32
 
def send_mail():
    outlook = win32.Dispatch('Outlook.Application')
 
    mail_item = outlook.CreateItem(0) # 0: create mail
 
    mail_item.Recipients.Add('del_fyodis@live.com')
    mail_item.Subject = 'Mail Test'
 
    mail_item.BodyFormat = 2          # 2: Html format
    mail_item.HTMLBody  = '''
        <H2>Hello, This is a test mail.</H2>
        Hello Guys.
        '''
    mail_item.Attachments.Add('C:/Users/Del_F/Desktop/SoSe_2021/Pre-doctoral_Self_Study/Python/辦公相關/material/04_月考勤表.xlsx')   
    mail_item.Send()
 
if __name__ == '__main__':
    send_mail()
