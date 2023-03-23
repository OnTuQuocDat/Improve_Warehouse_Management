import win32com.client as win32

outlook = win32.Dispatch('outlook.application')

mail = outlook.CreateItem(0)
# mail.To = 'DAQ@sonion.com'
mail.To = 'DAQ@sonion.com ; TUMNG@sonion.com'
mail.Subject = 'EE Warehouse Controller Notifications'
mail.Body = 'Hi. This is a test email to get part for engineer. Sorry for this uncomfortable'
# mail.HTMLBody = '<h2>GET part for engineer</h2>'

mail.Display()
mail.Send()