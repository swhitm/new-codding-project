

assignments = [ {'id' :"HW1",
                 "title" : "Intro to database Design",
                 "description": "basics",
                 "due_date" : "2026-1-20",
                 "score" : 10
                 },
                 {"id": "HW2",
                  "title" : "Homework 2: Normalization",
                  "description" : "learn normalization",
                  "due_date" : "2026-1-26",
                  "score" : 100}
]

new_id_number = 3

# new id generation pattern
new_assignment_id = "HW" + str(new_id_number)
new_id_number += 1

# Create (Add a new Item)
assignments.append(
    {
        "id" : new_assignment_id,
        "title" : "Final project - DB Design",
        "description" : "comprehansive final project" ,
        "due_date" : "2026-03-01",
        "score" : 100
})

# Q1: Displaying all assignments information
# input

# pull assignments

#process

#output
for assignment in assignments:
    print(f"ID: {assignment['id']}, Title: {assignment['title']}, Description: {assignment['description']}")


#Q2:Find an assignment with title : Homework 2: Normalization and display assignmnet info

#input
# pull assignments
input_assignmnet_title = "Homework 2: Normalization"

#process - Find an assignment
exists = False
assignment_details = None

for assignment in assignments:
    if assignment['title'] == input_assignmnet_title:
        exists = True
        assignment_details = assignment
        break


#output
if exists:
    print(f"assignmnet_datails: ", assignment_details)
else:
    print("was not found")

#Q3: Update the description of an assignmnet with an assignment id = HW1 and confirm the update - 
# new description : This assignment is about the basics

#input

search_assignment_id = "HW1"
new_description = "This assignment is about the basics"

#process - Update assignment
found = False
for assignment in assignments:
    if assignment['id'] == search_assignment_id:
        assignment['description'] = new_description
        found = True
        break


#output
if found:
    print("assignmnet was updated!")
else:
    print("assignment not found")
    

#Q3: delete a record - HW1

counter = 0
exists = False
for assignment in assignments:
    if assignment['id'] == "HW1":
        exists = True
        break
    counter +=1

if exists:
    del assignments[counter]

