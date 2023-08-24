class Inbox:
    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)
        print('Email added successfully')

    def display_emails(self):
        if len(self.emails):
            for em in self.emails:
                n = 'New - '
                o = '      '
                print(f'{self.emails.index(em)+1}: {n if em.is_new else o}From: {em.sender} Subject: {em.title}')
                print('-' * 40)
        else:
            print('No Emails Found')
    def open_email(self, email_index):
            if (email_index - 1) in range(len(self.emails)):            
                print(f'Sender: {self.emails[email_index-1].sender}')
                print(f'Recipient: {self.emails[email_index-1].recipient}')
                print(f'Subject: {self.emails[email_index-1].title}')
                print(f'Content: {self.emails[email_index-1].body}')
                self.emails[email_index-1].is_new = False
            else:
                print(f'Email with index "{email_index}" NOT found')                


class Email:
    def __init__(self, sender, recipient, title, body, is_new= True):
        self.sender = sender
        self.recipient = recipient
        self.title = title
        self.body = body
        self.is_new = is_new

    def display_details(self):
        return f'Email Details:\nSender: {self.sender}\nRecipient: {self.recipient}\nSubject: {self.title}\nContent: {self.body}'                 
    



inbox1 = Inbox()

menu = f'''
{'-'*30}
The Menu For Inbox:
    1- Add Email
    2- Show Emails
    3- Open Email
    4- Exit
'''

while True:
    print(menu)
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        sender = input('Enter Sender: ')
        check_sen = 1 if '@' in sender else 0
        recipient = input('Enter Recipient: ')
        check_rec = 1 if '@' in recipient else 0
        title = input('Enter Subject: ')
        body = input('Enter Content: ')
        if check_sen and check_rec and sender != recipient:
            email = Email(sender, recipient, title, body)
            inbox1.add_email(email)
            # print(email.display_details())
        elif sender == recipient:
            print('The email sender is the same email recipient')            
        else:
            print(f'Either email sender or recipient or both NOT valid, Email MUST contain "@"')            

    elif choice == 2:
        inbox1.display_emails()

    elif choice == 3:
        index = int(input('Enter the Index of the email to open: '))
        inbox1.open_email(index)

    elif choice == 4:
        break

    else:
        print('Invalid Choice')