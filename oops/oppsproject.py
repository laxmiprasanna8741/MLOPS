class ChatBook:
    def __init__(self):
        self.username = '' 
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatBook!! How would you like to proceed?
                           1. Press 1 To signup
                           2. Press 2 To signin
                           3. Press 3 To write a post
                           4. Press 4 To message a Friend
                           5. Press any other key to exist 
                           
                           ->""")
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sent_message()
        else:
            exit()

    def signup(self):
        email = input("entre your email here ->")
        pwd = input ("set your password ->")
        self.username = email
        self.password = pwd
        print("you have successfully signup !!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username=='' or self.password == '':
            print("Please signup first by pressing 1 in main memu")
        else:
            uname = input("entre your email/username:")
            pwd = input("entre your password:")
            if self.username == uname and self.password == pwd:
                print("you have logged in successful!!")
                self.loggedin = True
            else:
                print("please entre your credientals correctly!!")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            post = input("entre you message here -> ")
            print("your message have been posted")
        else:
            print("please signin first before trying post...")
            print("\n")
        self.menu()

    def sent_message(self):
        if self.loggedin == True:
            message = input("entre you message here -> ")
            person = input("entre the if to whom message need to be sent->")
            print("message sent succesfully")
        else:
            print("please signin first before trying post...")
            print('\n')
        self.menu()


obj = ChatBook()
