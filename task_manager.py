# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

# Red/ green color for error/success output.
OFF = '\033[0m'
FG_RED = '\033[31m'
FG_GREEN = '\033[32m'

# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w", encoding = 'utf-8-sig') as default_file:
        pass

with open("tasks.txt", 'r', encoding = 'utf-8-sig') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [t for t in task_data if t != ""]
    
# Task creation.
task_list = []
for t_str in task_data:
    curr_t = {}

    # Split by semicolon and manually add each component
    task_components = t_str.split(";")
    curr_t['username'] = task_components[0]
    curr_t['title'] = task_components[1]
    curr_t['description'] = task_components[2]
    curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT)
    curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT)
    curr_t['completed'] = True if task_components[5] == "Yes" else False

    task_list.append(curr_t)

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w", encoding = "utf-8-sig") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r', encoding = "utf-8-sig") as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:

    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print(30 * '-')
        print(f"{FG_RED}User does not exist{OFF}")
        print(30 * '-')
        continue
    elif username_password[curr_user] != curr_pass:
        print(30 * '-')
        print(f"{FG_RED}Wrong password{OFF}")
        print(30 * '-')
        continue
    else:
        print(30 * '-')
        print(f"{FG_GREEN}Login Successful!{OFF}")
        print(30 * '-')
        logged_in = True

# --------------------------------------------------
# functions
#---------------------------------------------------
#----------------
# register user.
def reg_user():
    '''Add a new user to the user.txt file'''
    # - Request input of a new username
    user_flag = False
    while user_flag == False:
        new_username = input("New Username: ")
        counter = 0
        for k in username_password:
            if k == new_username:
                print('-' * 30)
                print(f"{FG_RED}User alredy registered!\nChange current name to add a new user.{OFF}")
                print('-' * 30)
                break
            counter += 1
        if counter == len(username_password):
            user_flag = True
        
    # - Request input of a new password
    new_password = input("New Password: ")

    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print('-' * 30)
        print(f"{FG_GREEN}New user added.{OFF}")
        print('-' * 30)
        username_password[new_username] = new_password
        
        with open("user.txt", "w", encoding = "utf-8-sig") as out_file:
            user_data_2 = []
            for k in username_password:
                user_data_2.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data_2))

    # - Otherwise you present a relevant message.
    else:
        print(30 * '-')
        print(f"{FG_RED}Passwords do not match{OFF}")
        print(30 * '-')
# ------------------------------------------------
# add a task
def add_task():
    '''Allow a user to add a new task to task.txt file
        Prompt a user for the following: 
            - A username of the person whom the task is assigned to,
            - A title of a task,
            - A description of the task and 
            - the due date of the task.'''
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print(50 * '-')
            print(f"{FG_RED}User does not exist. Please enter a valid username.{OFF}")
            print(50 * '-')
        else:
            break
        
    task_title = input("Title of Task: ")
    task_description = input("Description of Task: ")
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD): ")
            due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
            break

        except ValueError:
            print(50 * '-')
            print(f"{FG_RED}Invalid datetime format. Please use the format specified{OFF}")
            print(50 * '-')

    # Then get the current date.
    curr_date = date.today()
    
    ''' Add the data to the file task.txt and
        Include 'No' to indicate if the task is complete.
        new_task is a dictionary which represent a new task'''
    new_task = {
        "username": task_username,
        "title": task_title,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": curr_date,
        "completed": False
    }
    # Append the new_task to the list of tasks.
    task_list.append(new_task)
    # Add data to task.txt.
    with open("tasks.txt", "w", encoding = 'utf-8-sig') as task_file_a:
        task_list_to_write_a = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
          
            task_list_to_write_a.append(";".join(str_attrs))
        task_file_a.write("\n".join(task_list_to_write_a))
    print('-' * 30)
    print(f"{FG_GREEN}Task successfully added.{OFF}")
    print('-' * 30)
#----------------------------------------------------
def view_all():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling) 
    '''

    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(50 * '-')
        print(disp_str)
#------------------------------------------------------
# View the task of the current logged user.
def view_mine():
    '''Reads the task from task.txt file and prints to the console in the 
        format of Output 2 presented in the task pdf (i.e. includes spacing
        and labelling)
    '''
    c = 1 # This counter will provide the id number to each task related to the logged user.
    dict_task_holder = {}
    list_dict_holder = []
    for t in task_list:
        
        if t['username'] == curr_user:
            t["id"] = c
            disp_str = f"Task id: \t {t['id']}\n"
            disp_str += f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(50 * '-')
            print(disp_str)
            dict_task_holder = {
                'id': t['id'],
                'title': t['title'],
                'username': t['username'],
                'assigned_date':t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                'due_date': t['due_date'].strftime(DATETIME_STRING_FORMAT),
                'description': t['description']
            }
            list_dict_holder.append(dict_task_holder)
            c += 1
    
    # Select task.
    flag_task = False
    selected_task = ''
    while flag_task is False:
        # If user has 0 assigned tasks.
        if not list_dict_holder:
            print(30 * '-')
            print(f"{FG_RED}No tasks to display!{OFF}")
            print(30 * '-')
            return
        
        # User select task.
        print(50 * '-')
        user_task_pick = input("Select task by digiting its id number or -1 to quit: ")
        if user_task_pick == '-1':
            return
        
        # Input validation check: input must be a number.
        if user_task_pick.isnumeric():
            user_task_pick = int(user_task_pick)
            
            # Once the input is an integer, it must respect the following conditions.
            if user_task_pick < -1 or user_task_pick == 0 or user_task_pick > len(list_dict_holder):
                print(f"{FG_RED}Please, enter the correct id task!{OFF}")
            else:
                for i in range(len(list_dict_holder)):
                    if user_task_pick == list_dict_holder[i]['id']:
                        selected_task = list_dict_holder[i]
                        print(50 * '-')
                        print(f"You have selected: {FG_GREEN}{selected_task['title']}{OFF} task.")
                        flag_task = True
        else:
            print(50 * '-')
            print(f"{FG_RED}Please enter correct task id!{OFF}")    
            print(50 * '-')
    
    flag_action = False
    while not flag_action:
        print(50 * '-')
        print("Select option number:\n1. Mark task as completed.")
        print("2. Edit task.\n\n-1. To quit menu.")
        user_task_action = input(":")
        if user_task_action == '-1':
            return
        # Input validation. It has to be a numeric value.
        if user_task_action.isnumeric():
            user_task_action = int(user_task_action) 
            #----------------------------------------------------------------
            # Mark task as completed.
            if user_task_action == 1:
                for ele in task_list:
                    
                    # Identify selected_task in task_list.
                    if ele['username'] == selected_task['username'] and ele['title'] == selected_task['title']:
                        
                        # The value of 'completed' gets modified.
                        ele['completed'] = True 
                print(50 * '-')
                print(f"{FG_GREEN}Task succesfully marked as completed.{OFF}")     
                print(50 * '-')  
                # Re-write tasks.txt file.
                with open("tasks.txt", "w", encoding = 'utf-8-sig') as task_file_2:
                    task_list_to_write_2 = []
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                        ]
                        task_list_to_write_2.append(";".join(str_attrs))
                    task_file_2.write("\n".join(task_list_to_write_2))
                        
                flag_action = True
            #-------------------------------------------------------------
            # change selected task's user or due date.    
            elif user_task_action == 2:
                
                for ele2 in task_list:
                    if ele2['username'] == selected_task['username'] and ele2['title'] == selected_task['title']:
                        # If the task is already marked as completed.
                        # the program will not proceed.
                        if ele2['completed'] is True:
                            print(50 * '-')
                            print(f"{FG_RED}Task already completed!\nImpossible apply any change!{OFF}")
                            print(50 * '-')
                            return
                        flag_edit = False
                        while not flag_edit:
                            print(50 * '-')
                            print("Select one of the following options by digiting its number:")
                            print("1. Change the task's user.")
                            print("2. Change the due date.")
                            print("-1. To quit.")
                            sele_options = input(":")
                            # quit
                            if sele_options == '-1':
                                return
                            # Check if input is numeric.
                            if sele_options.isnumeric():
                                sele_options = int(sele_options)
                                # Change user --------
                                if sele_options == 1: 
                                    new_user_name = input("Enter the new user name: ")
                                    if new_user_name in username_password.keys():
                                        ele2['username'] = new_user_name
                                        print(50 * '-')
                                        print(f"{FG_GREEN}User changed successfully!{OFF}")
                                        print(50 * '-')
                                        flag_edit = True
                                    else:
                                        print(50 * '-')
                                        print(f"{FG_RED}Please enter valid user name{OFF}")
                                        print(50 * '-')
                                        
                                # change due date --------
                                elif sele_options == 2:
                                    while True:
                                        try:
                                            new_due_date = input("Due date of task (YYYY-MM-DD): ")
                                            new_due_date = datetime.strptime(new_due_date, DATETIME_STRING_FORMAT)
                                            break
                                        except ValueError:
                                            print(50 * '-')
                                            print(f"{FG_RED}Invalid datetime format! Please use the format specified!{OFF}")
                                            print(50 * '-')
                                    
                                    ele2['due_date'] = new_due_date
                                    print(50 * '-')
                                    print(f"{FG_GREEN}Due date successfully updated.{OFF}")
                                    print(50 * '-')
                                    flag_edit = True
                                else:
                                    print(50 * '-')
                                    print(f"{FG_RED}Invalid entry! Please select the available options to modify the task.{OFF}")
                            else:
                                print(50 * '-')
                                print(f"{FG_RED}Please enter correct digit!{OFF}")
                # Re-write the updated file tasks.txt.
                with open("tasks.txt", "w", encoding = 'utf-8-sig') as task_file_b:
                    task_list_to_write_b = []
                    for t in task_list:
                        str_attrs = [
                            t['username'],
                            t['title'],
                            t['description'],
                            t['due_date'].strftime(DATETIME_STRING_FORMAT),
                            t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                            "Yes" if t['completed'] else "No"
                        ]
                   
                        task_list_to_write_b.append(";".join(str_attrs))
                    task_file_b.write("\n".join(task_list_to_write_b))
                flag_action = True
            else:
                print(50 * '-')
                print(f"{FG_RED}Please, enter valid input!{OFF}")
        else:
            print(50 * '-')
            print(f"{FG_RED}Please, enter a valid number!{OFF}") 

# -----------------------------------------------------

def generate_rep():
    # data for task_overview.txt.
    data_holder = []
    tot_tasks = 0
    tot_comp_tasks = 0
    tot_uncomp_tasks = 0
    tot_overdue_tasks = 0
    uncomp_percent = 0
    over_due_percent = 0
    for x in task_list:
        tot_tasks += 1
        if x['completed'] is True:
            # Total completed tasks.
            tot_comp_tasks += 1
        else:
            # Total uncompleted tasks.
            tot_uncomp_tasks += 1
        if x['due_date'].strftime(DATETIME_STRING_FORMAT) < date.today().strftime(DATETIME_STRING_FORMAT):
            # Total overdue tasks.
            tot_overdue_tasks += 1
    # Calculate percentages.
    # Test to chatch zero division error.
    # If zero div error, assign derfault value of float(0).
    while True:
        try:
            uncomp_percent = (tot_uncomp_tasks / tot_tasks) * 100
            over_due_percent = (tot_overdue_tasks / tot_tasks) * 100
            break
        except ZeroDivisionError:
            uncomp_percent = float(0)
            over_due_percent = float(0)
            break
    data_holder.append(str(tot_tasks)) 
    data_holder.append(str(tot_comp_tasks)) 
    data_holder.append(str(tot_uncomp_tasks))
    data_holder.append(str(tot_overdue_tasks))
    data_holder.append(str(uncomp_percent))
    data_holder.append(str(over_due_percent))
    # Write and update task_overview.txt. 
    with open("task_overview.txt", "w", encoding= "utf-8-sig") as report_file:
        report_file.write(';'.join(data_holder))
    # Catch data from task_overview.txt
    # Format data output in a readable manner.
    with open("task_overview.txt", "r", encoding= "utf-8-sig") as display_report_file:
        report_data = display_report_file.read().split(';')
    print(30 * '=')
    print("GLOBAL DATA.\n")
    print(30 * '-')
    print(f"Total tasks: {report_data[0]:>19}\nTotal completed tasks: {report_data[1]:>9}")
    print(f"Total uncompleted tasks: {report_data[2]:>7}\nTotal overdue tasks: {report_data[3]:>11}")
    print("Uncompleted tasks:", f"{float(report_data[4]):.2f} %".rjust(15))
    print("Total overdue tasks:", f"{float(report_data[5]):.2f} %".rjust(13))
       
    # data for user_overview.txt
    arr = []
    for i in username_password.keys():
        tot_user_tasks = 0
        completed = 0
        uncompleted = 0
        user_tasks_uncomp_overdue = 0
        # Dictionary holds labels and values.
        dict_labels = {}
        dict_labels['user'] = i
        for j in task_list:
            if j['username'] == i:
                # Total user tasks.
                tot_user_tasks += 1
                if j['completed'] is True:
                    # Completed user tasks.
                    completed += 1
                else:
                    # Uncompleted user tasks.
                    uncompleted += 1
                    if j['due_date'].strftime(DATETIME_STRING_FORMAT) < date.today().strftime(DATETIME_STRING_FORMAT):
                        # User uncomp and overdue tasks.
                        user_tasks_uncomp_overdue += 1
        # Void zero division error.
        # Calculate percentages.
        # Test to chatch zero division error.
        # If zero div error, assign default value of float(0).
        while True:
            try:
                user_tasks_per = (tot_user_tasks / tot_tasks) * 100 
                user_tasks_comp_per = (completed / tot_user_tasks) * 100
                user_tasks_uncomp_per = (uncompleted / tot_user_tasks) * 100 
                user_task_uncomp_overdue_per = (user_tasks_uncomp_overdue / tot_user_tasks) * 100
                break
            except ZeroDivisionError:
                user_tasks_per = float(0)
                user_tasks_comp_per = float(0)
                user_tasks_uncomp_per = float(0)
                user_task_uncomp_overdue_per = float(0)
                break
        # The try/except block keeps the code shorter.
        
        # Populate the dictionary.
        dict_labels['user'] = i               
        dict_labels['user_tot_tasks'] = tot_user_tasks 
        dict_labels['user_perc_share_tasks'] = f"{float(user_tasks_per):.2f}"
        dict_labels['user_perc_completed_tasks'] = f"{float(user_tasks_comp_per):.2f}"
        dict_labels['user_perc_uncompleted_tasks'] = f"{float(user_tasks_uncomp_per):.2f}"
        dict_labels['user_perc_uncompleted_tasks_overdue'] = f"{float(user_task_uncomp_overdue_per):.2f}"
        arr.append(dict_labels)  
    # Write and update user_overview.txt.    
    with open("user_overview.txt", "w", encoding= "utf-8-sig") as user_report_file:
        outer_holder = []
        for c in arr:
            temp_holder = [
                str(c['user']),
                str(c['user_tot_tasks']),
                str(c['user_perc_share_tasks']),
                str(c['user_perc_completed_tasks']),
                str(c['user_perc_uncompleted_tasks']),
                str(c['user_perc_uncompleted_tasks_overdue'])
            ]
            outer_holder.append(';'.join(temp_holder))     
        user_report_file.write('\n'.join(outer_holder))
    # Catch data from user_overview.txt
    # Format data output in a readable manner.    
    with open("user_overview.txt", "r", encoding= "utf-8-sig") as display_user_report_file:
        user_report_data = display_user_report_file.readlines()
        each_user_data = [ele.split() for ele in user_report_data]
        print(50 * '=')
        print("SINGLE USERS.\n")
        print(50 * '=')
        for single_user_data in each_user_data:
            single_user = [ i.split(';') for i in single_user_data]
            print(f"Username: {single_user[0][0]}\nUser total tasks: {single_user[0][1]}")
            print('-' * 20)
            print(f"Assigned tasks vs total: {single_user[0][2]:>14} %")
            print(f"Completed user tasks: {single_user[0][3]:>17} %")
            print(f"Uncompleted user tasks: {single_user[0][4]:>15} %")
            print(f"Uncompleted overdue user tasks: {single_user[0][5]:>7} %")
            print(50 * '=')
            
            
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r  - Registering a user
a  - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e  - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()          
    elif menu == 'gr':
        generate_rep()
    elif menu == 'ds' and curr_user == 'admin': 
        # If the user is an admin they can display statistics about number of users
        # and tasks.'''
        if not os.path.exists("user.txt"):
            with open("user.txt", "w", encoding = "utf-8-sig"):
                pass
        if not os.path.exists("tasks.txt"):
            with open("tasks.txt", "w", encoding = "utf-8-sig"):
                pass
        num_users = len(username_password.keys())
        num_tasks = len(task_list)

        print("-----------------------------------")
        print(f"Number of users: \t\t {num_users}")
        print(f"Number of tasks: \t\t {num_tasks}")
        print("-----------------------------------")    

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print(50 * '-')
        print(f"{FG_RED}You have made a wrong choice, Please Try again{OFF}")
        print(50 * '-')