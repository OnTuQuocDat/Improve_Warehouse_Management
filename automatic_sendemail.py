import win32com.client as win32


def send_email_to_admin():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'DAQ@sonion.com'
    mail.Subject = '[EE Warehouse Software] Request reset password'
    mail.Body = 'Hi admin, I forgot my password. Please help me to reset.'
    mail.Display()
    mail.Send()
