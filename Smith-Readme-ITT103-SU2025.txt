Authors: Johan Smith  
Date Created: July 27, 2025  
Course: ITT103  
GitHub Public URL to Code: https://github.com/jsmith744/Miracle-Heaven-hospital-management-system


Hospital Management System - README


Purpose of the Program:

This console-based Hospital Management System is designed to simulate a basic hospital workflow. It allows users to register patients and doctors, manage appointments (including making, cancelling, and rescheduling them), and generate billing for patients.

The program is written in Python and follows object-oriented programming principles. It uses custom classes like Person, Patient, Doctor, Appointment, and a central Hospital_System class to handle operations.

How to Run the Program:

1. Ensure Python 3 is installed on your computer.
2. Open a terminal or command prompt.
3. Navigate to the directory where the 'hospital_system.py' file is saved.
4. Run the program using:
   'python hospital_system.py'
5. Follow the on-screen menu to perform tasks such as:
   - Register new patient or doctor
   - Book or cancel an appointment
   - Reschedule an appointment
   - View doctor schedule or patient details
   - Generate a medical bill

Required Modifications:

The current version stores all data in memory (temporary). To improve or extend the system, consider the following enhancements:
 Add file storage (e.g., saving patient or appointment data to a file).
 Implement login/authentication for staff.
 Add error handling for invalid date/time formats.
 Support for multiple departments or hospital branches.
 Develop a graphical interface or web-based version.

Assumptions and Limitations:

 All data is lost once the program is closed (no database or file storage).
 Users must input names in "First Last" format when prompted.
 Dates and times must be entered in 'YYYY/MM/DD' and 'HH:MM' formats.
 A base bill charge is fixed at $3000 JMD. Any extra cost must be entered manually.
 Only one appointment can be made per doctor at a specific date and time.
 Doctor availability is checked against their current schedule.
 No validations are done for overlapping appointments for patients.


Thank you for using Miracle Haven Hospital System
