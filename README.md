# Project2
# Student Grade Management System
A simple Python program to manage student information, calculate grades, and generate a comprehensive student report with marks, averages, and letter grades.

## Features

- Load student datasets
- Data organization and structuring  
- Modular functions for each task
- Print data in readable format

## How to Run

```bash
python Project2.py
```

It will load the student data and show it on the screen.

## What I Learned

- **File handling** - Reading files and loading data
- **Data structures** - How to organize data from files
- **Functions** - Breaking down data processing into steps
- **Loops** - Processing multiple records
- **Data organization** - Why organizing data properly is important
- **Dictionary and list usage** - Storing structured information

## How It Works

```
1. User Input Phase: Program prompts user to enter name,age,and marks.
2. Data Storage: Information is stored in a dictionary structure.
3. Calculation Phase: Total and average are automatically calculated.
4. Grade Assignment: Grade is determined based on average marks.
5. Display Phase: Formatted report is printed to console.
```

## How to run
```python
python Project2.py
```

## Example
```python

Enter your name: John Doe
Enter your age: 18
Enter your Maths marks: 85
Enter your Science marks: 92
Enter your English marks: 78
Enter your History marks: 88
Enter your Geography marks: 95
                    Student Report                       
=======================================================
-------------------------------------------------------
                    John Doe                          
-------------------------------------------------------
|Name                : John Doe                       |                             
|Age                 : 18                             |                              
-------------------------------------------------------
|Maths               : 85                             |                              
|Science             : 92                             |                              
|English             : 78                             |                              
|History             : 88                             |                              
|Geography           : 95                             |                              
-------------------------------------------------------
|Average Marks       : 87.6                           |                            
|Total Marks         : 438                            |                            
|Grade               : B                              |       

```

## Code Structure
Funtcions Overview

Student_info()
- Collects student name, age, and marks for all subjects
- Returns a dictionary containing student data
calculate_total(marks)
- Takes marks dictionary as input
- Returns the sum of all marks
calculate_average(marks)
- Calculates the average of all marks
- Returns average as a float
display_student_info(student)
- Formats and displays the complete student report
- Shows name, age, marks, total, average, and grade
grade(average)
- Assigns a letter grade based on average marks
- Returns grade from A to Fail
main()
- Entry point of the program
- Calls functions in sequence


## Example Data Structure

```python
student = [
    {
        'name': 'John Doe',
        'age': 18,
        'subjects': ['Maths', 'Science','English', 'History', 'Geography'],
        'marks': {'Maths': 85, 'Science': 92, 'English': 78, 'History': 88, 'Geography': 95}
    },
    {
        'name': 'Snow', 
        'age': 18, 
        'subjects': ['Maths', 'Science', 'English', 'History', 'Geography'], 
        'marks': {'Maths': 87, 'Science': 82, 'English': 96, 'History': 75,'Geography': 89}
    }
]
```

## Things I Could Learn Next

- How to validate data (check for missing or incorrect values)
- Sorting and filtering data
- SQL databases for larger datasets
- Data analysis techniques

## Challenges I Faced

- Understanding how to structure data for analysis
- Reading and parsing files correctly
- Handling multiple records efficiently
- Organizing large amounts of information

## Why This Matters

This project teaches how to organize information properly. When you have good data structure, everything else becomes easier!