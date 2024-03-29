# TASK MANAGER

  - Add users and assign tasks to each one of them (admin is automatically generated).
  - Check statistics for each user or for all of them.
  - Generate reports (admin only)
  - The program will automatically generate users.txt and tasks.txt files. Each time a change or an update is done the .txt files will be re-written.

### LOGIN
  ![Screenshot 2024-03-09 103754](https://github.com/MassimilianoCattani/finalCapstone/assets/52679658/5a3f6faf-c936-4fc8-9d63-498075854676)
  - The first step is a login panel.
  - If the credentials are fine, a successful message will appear.

### REGISTER A NEW USER
  ![Screenshot 2024-03-09 104452](https://github.com/MassimilianoCattani/finalCapstone/assets/52679658/7cfd8df1-72d1-4b79-ae05-55b27de64cb9)
  - Add a name and a password, which will have to be confirmend.

### ADD A TASK
  ![Screenshot 2024-03-09 104901](https://github.com/MassimilianoCattani/finalCapstone/assets/52679658/91218a75-dac3-4167-a600-caa5844d61ac)
  - Select user to add the task.
  - Give a title to the task.
  - Add a description.
  - Insert due date in the correct format.

### VIEW ALL TASKS
  ![Screenshot 2024-03-09 105626](https://github.com/MassimilianoCattani/finalCapstone/assets/52679658/3b8d4109-84ed-4ef2-a8ac-3d6d660df32b)
  - A full  overview of all the task for all the users.

### VIEW MY TASKS
  - View and modify sigle user task.
  - Change user for a specific task.
  - Change due date for the selected task.

### GENERATE REPORTS
  ![Screenshot 2024-03-09 105705](https://github.com/MassimilianoCattani/finalCapstone/assets/52679658/6f3a8c24-9f37-435c-b9a3-4c9e335e75f1)
  - General view:
      - Total tasks
      - Total tasks completed and uncompleted.
  - Single user:
      - Total tasks
      - % of assigned tasks vs total tasks
      - Completed user tasks
      - Uncompleted user tasks.
      - Uncompleted and overdue tasks.
        
### DISPLAY STATISTICS
  ![Screenshot 2024-03-09 105722](https://github.com/MassimilianoCattani/finalCapstone/assets/52679658/87979af5-58af-47bc-ada0-1155e90f051d)
  - Admin access only.


## PROCESS
Each user task is a dictionary stored into a list.
It is from and to the list of dictionaries that we can access, visualise and modify user task data (change user for the task or change due date).
- When data gets written on the external .txt file, is transformed into a string, where each element is separated by ';'.
- When data gets retrieved from the .txt file, passes from the string type to the dictionary type. In this way we can access clearly to each element and create a custom layout to display the info. 



