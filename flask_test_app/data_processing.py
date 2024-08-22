class Email():
    def __init__(self, sender, subject, body):
        self.sender = sender
        self.subject = subject
        self.body = body
        
    def get_sender(self):
        return self.sender
    
    def get_subject(self):
        return self.subject
    
    def get_body(self):
        return self.body
    
    def print(self):
        return "" + self.sender + " " + self.subject 
    
#stac = []
#l = []    
        
def gen_emails():
    #stac = []
    email = Email("Nick Day", "Meeting next week", "Hi John, Can we please talk about the funding meeting next week?")
    #stac[1] = Email("John Smith", "Meeting next week", "Hi John, Can we please talk about the funding meeting next week?")
    #stac[2] = Email("Katriona Lukas", "", "")
    #stac[3] = Email("Sam Wintersmith", "","")
    
    return email

def get_stack():
    
    st = gen_emails()
    l = []

    l = ["Nick Day", "John Smith", "Katriona Lukas", "Sam Wintersmith", st.get_sender()]
    l = [0,1,2,3,4,5,6,7]
    return l

''' 
if __name__ == '__main__':
    main()
'''


''' 
https://raw.githubusercontent.com/OmkarPathak/Playing-with-datasets/master/Email%20Spam%20Filtering/emails.csv
'''