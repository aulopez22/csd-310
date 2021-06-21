MongoDB: insert_one()
emma = {
    "student_id" : "1007",
    "first_name" : "Emma",
    "last_name" : "Lopez"
},
zoe = {
    "student_id" : "1008",
    "first_name" : "Zoe",
    "last_name" : "Lopez"
}, 
antonio = {
    "student_id" : "1009",
    "first_name" : "Antonio"
    "last_name" : "Lopez"
}
emma_student_id = students.insert_one(emma).inserted_id
zoe_student_id = students.insert_one(zoe).inserted_id
antonio_student_id = students.insert_one(antonio).inserted_id
