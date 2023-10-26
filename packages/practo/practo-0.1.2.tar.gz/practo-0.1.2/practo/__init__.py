#Bankers Algorithm
class BankersAlgorithm:
    def __init__(self, allocation, max_resources, available_resources):
        self.allocation = allocation  
        self.max_resources = max_resources 
        self.available_resources = available_resources  
        self.num_processes = len(allocation)
        self.num_resources = len(available_resources)

    def is_safe_state(self):
        work = self.available_resources.copy()
        finish = [False] * self.num_processes

        safe_sequence = []

        for _ in range(self.num_processes):
            for process in range(self.num_processes):
                if not finish[process]:
                    if all(work[i] >= self.max_resources[process][i] - self.allocation[process][i] for i in range(self.num_resources)):
                        safe_sequence.append(process)
                        work = [work[i] + self.allocation[process][i] for i in range(self.num_resources)]
                        finish[process] = True
                        break

        if all(finish):
            print("Safe Sequence:", safe_sequence)
            return True
        else:
            print("Unsafe State")
            return False
        
#Bully Algorithm
class bully:
    def __init__(self,st,prio,co,n):
        self.st=st
        self.prio=prio
        self.co=co
        self.n=n
    
    def getval(self):
        for i in range(0, self.n):
            print("Enter Status of the system",i+1,":")
            self.st.append(int(input()))
            print("Enter Priority of the system")
            self.prio.append(int(input())) 
        

    def elect(self,ele):
        ele=ele-1
        self.co=ele+1
        for i in range(0, self.n):
            if(self.prio[ele]<self.prio[i]):
                print("Election message is sent from ",(ele+1)," to ",(i+1),)
                if(self.st[i]==1):
                    self.elect(i+1)
        return self.co

    def startelect(self):
        ele=int(input("Which process will initiate election?"))
        print("Final coordinator is ",self.elect(ele))


#Flask helloWorld program

#from flask import Flask
#app = Flask(__name__)
#@app.route('/')
#def hello_world():
#    return 'Hello World'

#if __name__ == '__main__':
#    app.run()

#Simple Implementation of REST protocal

#from flask import Flask, jsonify

#app = Flask(__name__)

# Sample data
#books = [
#    {"id": 1, "title": "Book 1", "author": "Author 1"},
#    {"id": 2, "title": "Book 2", "author": "Author 2"},
#]

#@app.route('/', methods=['GET'])
#def get_books():
#    return jsonify({"books": books})

#@app.route('/books/<int:book_id>', methods=['GET'])
#def get_book(book_id):
#    book = next((book for book in books if book['id'] == book_id), None)
#    if book is None:
#        return jsonify({"error": "Book not found"}), 404
#    return jsonify({"book": book})

#if __name__ == '__main__':
#    app.run(debug=True)


#Login Page Using Flask

# from flask import Flask, render_template, request, redirect, url_for
# myapp = Flask(__name__)
         
# users = {         
# "user1": "password1",        
# "user2": "password2",         
# }         
# @myapp.route('/', methods=['GET', 'POST'])          
# def index():
#     return render_template('login.html')

# @myapp.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']
#     if username in users and users[username] == password:
#           return "Login successful!"
#     else:
#           return "Login failed. Check your username and password."

# @myapp.route('/register', methods=['POST'])
# def register():
#     new_username = request.form['new_username']
#     new_password = request.form['new_password']
#     if new_username in users:
#         return "Username already exists. Choose a different one."
#     else:
#         users[new_username] = new_password
#         return "Registration successful!"

# if __name__ == '__main__':
#     myapp.run(debug=True)

#login.html file

# <!DOCTYPE html>
# <html>
# <head>
# <title>Login</title>
# </head>
# <body> 
# <h1>Login</h1>
# <form method="POST" action="/login">      
# <label for="username">Username:</label>      
# <input type="text" name="username" required><br><br>   
# <label for="password">Password:</label>  
# <input type="password" name="password" required><br><br>    
# <input type="submit" value="Login">     
# </form>    
# <h2>Register</h2>     
# <form method="POST" action="/register">     
# <label for="new_username">New Username:</label>      
# <input type="text" name="new_username" required><br><br>     
# <label for="new_password">New Password:</label>      
# <input type="password" name="new_password" required><br><br>      
# <input type="submit" value="Register">      
# </form>       
# </body>       
# </html>





