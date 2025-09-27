import pymysql

def connect_db():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="123456789",  
        database="chronic_disease_registry"
    )

#Patient
def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    phone = input("Enter phone: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Patient (name, age, gender, phone) VALUES (%s, %s, %s, %s)", 
                   (name, age, gender, phone))
    conn.commit()
    print("Patient added successfully")
    cursor.close()
    conn.close()

def view_patients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Patient")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def update_patient():
    patient_id = int(input("Enter patient ID to update: "))
    new_phone = input("Enter new phone: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Patient SET phone=%s WHERE patient_id=%s", 
                   (new_phone, patient_id))
    conn.commit()
    print("Patient updated successfully")
    cursor.close()
    conn.close()

def delete_patient():
    patient_id = int(input("Enter patient ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Patient WHERE patient_id=%s", (patient_id,))
    conn.commit()
    print("Patient deleted successfully")
    cursor.close()
    conn.close()

def search_patient():
    print("\n--- Search Patient ---")
    print("1. By ID")
    print("2. By Name")
    print("3. By Age")
    print("4. By Gender")
    print("5. By Phone")

    choice = input("Enter search option: ")

    conn = connect_db()
    cursor = conn.cursor()

    if choice == "1":
        patient_id = input("Enter patient ID: ")
        cursor.execute("SELECT * FROM Patient WHERE patient_id=%s", (patient_id,))
    elif choice == "2":
        name = input("Enter patient name: ")
        cursor.execute("SELECT * FROM Patient WHERE name LIKE %s", ("%" + name + "%",))
    elif choice == "3":
        age = input("Enter patient age: ")
        cursor.execute("SELECT * FROM Patient WHERE age=%s", (age,))
    elif choice == "4":
        gender = input("Enter gender: ")
        cursor.execute("SELECT * FROM Patient WHERE gender=%s", (gender,))
    elif choice == "5":
        phone = input("Enter phone: ")
        cursor.execute("SELECT * FROM Patient WHERE phone=%s", (phone,))
    else:
        print("Invalid option")
        cursor.close()
        conn.close()
        return

    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No patient found.")

    cursor.close()
    conn.close()

#Doctor
def add_doctor():
    name = input("Enter doctor name: ")
    specialization = input("Enter specialization: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Doctor (name, specialization) VALUES (%s, %s)", 
                   (name, specialization))
    conn.commit()
    print("Doctor added successfully")
    cursor.close()
    conn.close()

def view_doctors():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Doctor")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def update_doctor():
    doctor_id = int(input("Enter doctor ID to update: "))
    new_specialization = input("Enter new specialization: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Doctor SET specialization=%s WHERE doctor_id=%s", 
                   (new_specialization, doctor_id))
    conn.commit()
    print("Doctor updated successfully")
    cursor.close()
    conn.close()

def delete_doctor():
    doctor_id = int(input("Enter doctor ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Doctor WHERE doctor_id=%s", (doctor_id,))
    conn.commit()
    print("Doctor deleted successfully")
    cursor.close()
    conn.close()

def search_doctor():
    print("\n--- Search Doctor ---")
    print("1. By ID")
    print("2. By Name")
    print("3. By Specialization")

    choice = input("Enter search option: ")

    conn = connect_db()
    cursor = conn.cursor()

    if choice == "1":
        doctor_id = input("Enter doctor ID: ")
        cursor.execute("SELECT * FROM Doctor WHERE doctor_id=%s", (doctor_id,))
    elif choice == "2":
        name = input("Enter doctor name: ")
        cursor.execute("SELECT * FROM Doctor WHERE name LIKE %s", ("%" + name + "%",))
    elif choice == "3":
        specialization = input("Enter specialization: ")
        cursor.execute("SELECT * FROM Doctor WHERE specialization LIKE %s", ("%" + specialization + "%",))
    else:
        print("Invalid option")
        cursor.close()
        conn.close()
        return

    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No doctor found.")

    cursor.close()
    conn.close()

#Disease
def add_disease():
    name = input("Enter disease name: ")
    description = input("Enter description: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Disease (name, description) VALUES (%s, %s)", 
                   (name, description))
    conn.commit()
    print("Disease added successfully")
    cursor.close()
    conn.close()

def view_diseases():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Disease")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def update_disease():
    disease_id = int(input("Enter disease ID to update: "))
    new_description = input("Enter new description: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Disease SET description=%s WHERE disease_id=%s", 
                   (new_description, disease_id))
    conn.commit()
    print("Disease updated successfully")
    cursor.close()
    conn.close()

def delete_disease():
    disease_id = int(input("Enter disease ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Disease WHERE disease_id=%s", (disease_id,))
    conn.commit()
    print("Disease deleted successfully")
    cursor.close()
    conn.close()

#Treatment
def add_treatment():
    patient_id = int(input("Enter patient ID: "))
    disease_id = int(input("Enter disease ID: "))
    medication = input("Enter medication: ")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Treatment 
                      (patient_id, disease_id, medication, start_date, end_date) 
                      VALUES (%s, %s, %s, %s, %s)""", 
                   (patient_id, disease_id, medication, start_date, end_date))
    conn.commit()
    print("Treatment added successfully")
    cursor.close()
    conn.close()

def view_treatments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT t.treatment_id, p.name, d.name, t.medication, t.start_date, t.end_date
                      FROM Treatment t
                      JOIN Patient p ON t.patient_id = p.patient_id
                      JOIN Disease d ON t.disease_id = d.disease_id""")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def update_treatment():
    treatment_id = int(input("Enter treatment ID to update: "))
    new_medication = input("Enter new medication: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Treatment SET medication=%s WHERE treatment_id=%s", 
                   (new_medication, treatment_id))
    conn.commit()
    print("Treatment updated successfully")
    cursor.close()
    conn.close()

def delete_treatment():
    treatment_id = int(input("Enter treatment ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Treatment WHERE treatment_id=%s", (treatment_id,))
    conn.commit()
    print("Treatment deleted successfully")
    cursor.close()
    conn.close()

#Appointment
def add_appointment():
    patient_id = int(input("Enter patient ID: "))
    doctor_id = int(input("Enter doctor ID: "))
    date = input("Enter date (YYYY-MM-DD): ")
    notes = input("Enter notes: ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO Appointment (patient_id, doctor_id, date, notes) 
                      VALUES (%s, %s, %s, %s)""", 
                   (patient_id, doctor_id, date, notes))
    conn.commit()
    print("Appointment added successfully")
    cursor.close()
    conn.close()

def view_appointments():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""SELECT a.appointment_id, p.name, d.name, a.date, a.notes
                      FROM Appointment a
                      JOIN Patient p ON a.patient_id = p.patient_id
                      JOIN Doctor d ON a.doctor_id = d.doctor_id""")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conn.close()

def update_appointment():
    appointment_id = int(input("Enter appointment ID to update: "))
    new_date = input("Enter new date (YYYY-MM-DD): ")

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Appointment SET date=%s WHERE appointment_id=%s", 
                   (new_date, appointment_id))
    conn.commit()
    print("Appointment updated successfully")
    cursor.close()
    conn.close()

def delete_appointment():
    appointment_id = int(input("Enter appointment ID to delete: "))

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Appointment WHERE appointment_id=%s", (appointment_id,))
    conn.commit()
    print("Appointment deleted successfully")
    cursor.close()
    conn.close()

#Main Menu
def main_menu():
    while True:
        print("\n===== Chronic Disease Registry System =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Update Patient")
        print("4. Delete Patient")
        print("5. Add Doctor")
        print("6. View Doctors")
        print("7. Update Doctor")
        print("8. Delete Doctor")
        print("9. Add Disease")
        print("10. View Diseases")
        print("11. Update Disease")
        print("12. Delete Disease")
        print("13. Add Treatment")
        print("14. View Treatments")
        print("15. Update Treatment")
        print("16. Delete Treatment")
        print("17. Add Appointment")
        print("18. View Appointments")
        print("19. Update Appointment")
        print("20. Delete Appointment")
        print("21. Search Patient")
        print("22. Search Doctor")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1": add_patient()
        elif choice == "2": view_patients()
        elif choice == "3": update_patient()
        elif choice == "4": delete_patient()
        elif choice == "5": add_doctor()
        elif choice == "6": view_doctors()
        elif choice == "7": update_doctor()
        elif choice == "8": delete_doctor()
        elif choice == "9": add_disease()
        elif choice == "10": view_diseases()
        elif choice == "11": update_disease()
        elif choice == "12": delete_disease()
        elif choice == "13": add_treatment()
        elif choice == "14": view_treatments()
        elif choice == "15": update_treatment()
        elif choice == "16": delete_treatment()
        elif choice == "17": add_appointment()
        elif choice == "18": view_appointments()
        elif choice == "19": update_appointment()
        elif choice == "20": delete_appointment()
        elif choice == "21": search_patient()
        elif choice == "22": search_doctor()
        elif choice == "0":
            print("Exiting program")
            break
        else:
            print("Invalid choice, try again.")

# Run
if __name__ == "__main__":
    main_menu()
