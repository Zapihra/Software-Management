This page includes the required class diagram, sequence diagram
and dependency graph. They are based on the project before any 
changes were made to the code

### Class diagram

![alt text](<pictures/Class diagram.png>)

### Sequence diagram

![alt text](<pictures/Sequence diagram.png>)

### Dependency graph

![alt text](<pictures/Dependency graph.png>)


### Discription of the system's architecture

base.py
- defines fonts and colors to be used
- defines the layout of the pages

books.py
- shows books available in the system
- handles the visualization of books-page
- adding, updating or deletion of books

dashboard.py
- shows summary of the system as whole
- handles the visualization of dashboard

database.py
- handles all the communication with database
- initializes database connection

issue_books.py
- calculates fines
- handles the returning and loaning of the book
- visualization of issue books -page

login.py
- handels the login to the page
- visualization of login-page

members.py
- visualization of members-page
- shows the members and their key information
- Searching of a member
- adding, updating or deleting of member

reports.py
- visualization of reports-page
- downloading report to csv-file
- handling the summary of reports

settings.py
- resetting password
- creating backup of database
- visualization of settings-page

users.py
- visualization of users-page
- managing users
- adding, updating or deleting admins and staff members

main.py
- handling sidebar
- handling of showing the different pages

### Main components in modules

all
- _init__() if exists

base.py
- build_heading()
- build_card()

books.py
- _build_ui()
- load_data()
- add_book()
- delete_book()

dashboard.py
- _build_charts()
- _build_cards()

database.py
- _connection()
- hash_password()
- verify_password()

issue_books.py
- _build_ui()
- issue_book()

login.py
- _build_ui() 
- _attempt_login()

members.py
- _build_ui()
- add_member()
- load_data()

reports.py
- _build_ui()
- load_report()

settings.py
- _build_ui()
- change_password()
- backup_database()
- restore_database()

users.py
- _build_ui()
- add_user()
- delete_user()
- load_data()

main.py
- show_module()
- show_login()
- _build_sidebar()