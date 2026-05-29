import streamlit as st
import os
import pandas as pd
def studentresult(student_name,roll_number,marks,subject):
    try:
        
        file_pathc = r"C:\Users\Admin\Documents\Python ClassNotes\report_card.txt"
        
        #Totals
        total = sum(marks)

        #average
        avg = total/ len(marks)

        #Grades
        if avg >= 90 and avg <= 100:
            grade = 'A+'
        elif avg >= 80 and avg < 90:
            grade = 'A'
        elif avg >= 70 and avg < 80:
            grade = 'B'
        elif avg >= 60 and avg < 70:
            grade = 'C'
        elif avg >= 50 and avg < 60:
            grade = 'D'
        elif avg < 50:
            grade = 'Fail'

        result = {'Name':student_name,'RollNumber':roll_number,'Subjects':subject,'Marks':marks,'Total':total,'Average':avg,'Grade':grade}
        tot = int(total)
        df1 = pd.DataFrame(result, columns=['Subjects', 'Marks'])
        df1.index = range(1, len(df1) + 1)
        df1 = df1.reset_index()
        df1.rename(columns={'index': 'Sno'}, inplace=True)
        
        st.write('====================Student Result=======================')
        st.write('Student Name: ',result['Name'])
        st.write('Student Name: ',result['RollNumber'])
        st.write(df1.to_string(index=False))
        st.write('Total Marks: ',result['Total'],' out of 500')
        st.write('Average Marks: ',result['Average'])
        st.write('Grade: ',result['Grade'])
        try:
            if os.path.exists(file_pathc):
                with open(file_pathc, "a",encoding="utf-8") as file:
                    file.write(f"====================Student Result=======================\n")
                    file.write(f"Student Name: {result['Name']}\n")
                    file.write(f"Roll Number: {result['RollNumber']}\n")
                    file.write(df1.to_string(index=False))
                    file.write(f"\nTotal Marks: {result['Total']} out of 500\n")
                    file.write(f"Average Marks: {result['Average']}\n")
                    file.write(f"Grade: {result['Grade']}\n")

                st.write("\nReport saved successfully in 'report_card.txt'")
            else:
                with open(file_pathc, "x",encoding="utf-8") as file:
                    file.write(f"====================Student Result=======================\n")
                    file.write(f"Student Name: {result['Name']}\n")
                    file.write(f"Roll Number: {result['RollNumber']}\n")
                    file.write(df1.to_string(index=False))
                    file.write(f"\nTotal Marks: {result['Total']} out of 500\n")
                    file.write(f"Average Marks: {result['Average']}\n")
                    file.write(f"Grade: {result['Grade']}\n")

                st.write("\nReport saved successfully in 'report_card.txt'")
        except Exception as e:
            st.write("Exception: \n", e)
    except Exception as ex:
        st.write('Enter the valid details')
        st.write("Exception: \n", ex)

# Main Program

#Student Name
student_name = st.text_input("Student Name", key="student_name")
roll_number = st.text_input("Roll Number", key="roll_number")

#Subjects and Marks
marks = []
subject =['English','Maths','Computer Science','Physics','Chemistry']
for i in subject:
    mark = st.number_input(f"Enter mark for {i}",min_value=0.0,max_value=100.0,value=0.0,key=f"mark_{i}")
    marks.append(mark)

if st.button("Generate Result 🎯"):            
    studentresult(student_name,roll_number,marks,subject)


if st.button("Check Report Card File 📝"):
    file_path = r"C:\Users\Admin\Documents\Python ClassNotes\report_card.txt"
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    st.text_area("Report Card", content, height=400)
