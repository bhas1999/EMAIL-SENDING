import yagmail
import os
receiver ='bhaskar9591009339@gmail.com'
sender ='636bhaskar@gmail.com'
subject='hi you have done this great'
contents="""it is great to see u complete this email sending task thank yuou """
yag=yagmail.SMTP(user=sender,password= os.getenv('PASSWORDS'))
yag.send(to = receiver,subject=subject ,contents=contents)
print("email sent")
