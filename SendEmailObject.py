#####
# Contains the class that handles sending out email alerts when an item is in stock
# Due to gmail needing 2FA, this uses yahoo mail. I would suggest making a bum email address just to send the alerts
#####

# Importing my Scraped Object Class to input the stock for emailing purposes
from NeweggScrapeObject import NeweggStock

# Import of SMTP Library to be able to send emails, and getpass for hidden password input prompts
import smtplib
# Importing getpass for hidden password entry
import getpass

class EmailAlert:

    def __init__(self,stocklist,fromAddress,fromPassword,toAddress):
        self.stocklist = stocklist
        self.fromAddress = fromAddress
        self.fromPassword = fromPassword
        self.toAddress = toAddress

    def sendemail(self):

        #Connecting to email address
        smtpObject = smtplib.SMTP('smtp.mail.yahoo.com',587)
        smtpObject.ehlo()
        smtpObject.starttls()
        smtpObject.login(self.fromAddress,self.fromPassword)
        
        #Creating the Message
        subject = "Hello," + '\n' + "At the time of sending this email, here are the items in stock: "
        stockMsg = ''
        for item,url,promo in self.stocklist:
            stockMsg = stockMsg + (f'{item} is in stock. The website is: {url}  and the promos available are: {promo}.') + '\n'
        fullMsg = subject + stockMsg

        #sending email
        smtpObject.sendmail(self.fromAddress,self.toAddress,fullMsg)

        #ending email session
        smtpObject.quit()

        

            
        