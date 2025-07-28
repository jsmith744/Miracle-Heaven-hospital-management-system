import uuid

# Generate a unique ID with a prefix
def generate_id(prefix):
    return f"{prefix}{str(uuid.uuid4())[:4]}"

# Base Person class
class Person:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def display_information(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")

# Patient class
class Patient(Person):
    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.patient_id = generate_id("patient")
        self.appointment_list = []

    def view_person(self):
        print(f"\nPatient ID: {self.patient_id}")
        self.display_information()

# Doctor class
class Doctor(Person):
    def __init__(self, first_name, last_name, age, gender, speciality):
        super().__init__(first_name, last_name, age, gender)
        self.doctor_id = generate_id("doctor")
        self.speciality = speciality
        self.schedule = []

    def is_available(self, date, time):
        return (date, time) not in self.schedule

    def view_schedule(self):
        print(f"\nDoctor ID: {self.doctor_id}")
        self.display_information()
        print(f"Speciality: {self.speciality}")
        if self.schedule:
            print("Appointments:")
            for date, time in self.schedule:
                print(f"{date} at {time}")
        else:
            print("No Appointments")

# Appointment class
class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.appointment_id = generate_id("appointment")
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = "Scheduled"

    def cancel_appointment(self):
        self.status = "Cancelled"

# Hospital System class
class Hospital_System:
    def __init__(self):
        self.patients = {}
        self.doctors = {}
        self.appointments = {}

    def add_patient(self):
        try:
            name = input("Enter patient first and last name: ")
            first_name, last_name = name.strip().split(" ", 1)
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            patient = Patient(first_name, last_name, age, gender)
            self.patients[patient.patient_id] = patient
            print(f"Patient added with ID: {patient.patient_id}")
        except ValueError:
            print("Invalid input. Please provide full name and numeric age.")

    def add_doctor(self):
        try:
            name = input("Enter doctor first and last name: ")
            first_name, last_name = name.strip().split(" ", 1)
            age = int(input("Enter doctor age: "))
            gender = input("Enter doctor gender: ")
            speciality = input("Enter doctor speciality: ")
            doctor = Doctor(first_name, last_name, age, gender, speciality)
            self.doctors[doctor.doctor_id] = doctor
            print(f"Doctor added with ID: {doctor.doctor_id}")
        except ValueError:
            print("Invalid input. Please provide full name and numeric age.")

    def add_appointment(self):
        patient_id = input("Enter patient ID: ")
        doctor_id = input("Enter doctor ID: ")
        date = input("Enter date of appointment (YYYY/MM/DD): ")
        time = input("Enter time of appointment (HH:MM): ")

        if patient_id not in self.patients:
            print("No patient found.")
            return
        if doctor_id not in self.doctors:
            print("No doctor found.")
            return

        doctor = self.doctors[doctor_id]
        if not doctor.is_available(date, time):
            print("The doctor is not available at that time.")
            return

        appointment = Appointment(self.patients[patient_id], doctor, date, time)
        doctor.schedule.append((date, time))
        self.patients[patient_id].appointment_list.append(appointment)
        self.appointments[appointment.appointment_id] = appointment
        print(f"Appointment added with ID: {appointment.appointment_id}")

    def cancel_appointment(self):
        appointment_id = input("Enter appointment ID to cancel: ")
        if appointment_id in self.appointments:
            self.appointments[appointment_id].cancel_appointment()
            print("Appointment cancelled.")
        else:
            print("No appointment found.")

    def reschedule_appointment(self):
        appointment_id = input("Enter appointment ID to reschedule: ")
        if appointment_id not in self.appointments:
            print("Appointment not found.")
            return
        new_date = input("Enter new date of appointment (YYYY/MM/DD): ")
        new_time = input("Enter new time of appointment (HH:MM): ")

        appointment = self.appointments[appointment_id]
        doctor= appointment.doctor

        if not doctor.is_available(new_date, new_time):
            print("The doctor is not available at that time.")

# Replace old time with new one
        doctor.schedule.remove((appointment.date, appointment.time))
        doctor.schedule.append((new_date, new_time))

        appointment.date = new_date
        appointment.time = new_time
        print("Appointment scheduled.")


    def generate_bill(self):
        appointment_id = input("Enter appointment ID: ")
        patient_id = input("Enter patient ID: ")

        if patient_id not in self.patients or appointment_id not in self.appointments:
            print("Invalid ID(s).")
            return

        try:
            base_cost = 3000
            extra = int(input("Enter extra cost (if any): "))
            description = input("What is the extra cost for?")
            total = base_cost + extra

            patient = self.patients[patient_id]
            print("\n--- Miracle Haven Hospital Bill ---")
            print(f"Patient: {patient.first_name} {patient.last_name} (ID: {patient_id})")
            print(f"Appointment ID: {appointment_id}")
            print("-----------------------------------")
            print(f"Service Charge: ${base_cost}")
            if extra > 0:
                print(f"{description} ({extra} ")
            print(f"Surcharge:      ${extra}")
            print("-----------------------------------")
            print(f"Total Cost:     ${total}")
        except ValueError:
            print("Please enter a valid number for the cost.")

    def show_patient_details(self):
        patient_id = input("Enter patient ID: ")
        if patient_id in self.patients:
            self.patients[patient_id].view_person()
        else:
            print("No patient found.")

    def show_doctor_schedule(self):
        doctor_id = input("Enter doctor ID: ")
        if doctor_id in self.doctors:
            self.doctors[doctor_id].view_schedule()
        else:
            print("No doctor found.")

    def menu(self):
        while True:
            print("\n--- Miracle Haven Hospital Menu ---")
            print("1. Register new patient")
            print("2. Register new doctor")
            print("3. Make appointment")
            print("4. Cancel appointment")
            print("5. Re-schedule appointment")
            print("6. See patient details")
            print("7. See doctor schedule")
            print("8. Generate bill")
            print("9. Exit")
            print("-----------------------------------")

            choice = input("Enter your choice (1-9): ")

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.add_doctor()
            elif choice == "3":
                self.add_appointment()
            elif choice == "4":
                self.cancel_appointment()
            elif choice == "5":
                self.reschedule_appointment()
            elif choice == "6":
                self.show_patient_details()
            elif choice == "7":
                self.show_doctor_schedule()
            elif choice == "8":
                self.generate_bill()
            elif choice == "9":
                print("Thank you for using Miracle Haven Hospital System")
                break
            else:
                print("Invalid choice. Please try again.")







# Run the program
if __name__ == "__main__":
    hospital = Hospital_System()
    hospital.menu()
