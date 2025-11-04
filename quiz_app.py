import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os


user_data = {} 


def generate_certificate_pdf(score):
    filename = f"Certificate_{user_data['name'].replace(' ', '_')}.pdf"
    filepath = os.path.join(os.getcwd(), filename)

   
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4

    
    c.setLineWidth(4)
    c.setStrokeColorRGB(0.1, 0.5, 0.2)
    c.rect(30, 30, width - 60, height - 60)


    c.setFont("Helvetica-Bold", 24)
    c.setFillColorRGB(0.1, 0.3, 0.6)
    c.drawCentredString(width / 2, height - 100, "Certificate of Achievement")

    
    c.setFont("Helvetica", 14)
    c.setFillColorRGB(0, 0, 0)
    c.drawCentredString(width / 2, height - 150, "This certificate is proudly presented to")

    
    c.setFont("Helvetica-Bold", 20)
    c.setFillColorRGB(0.1, 0.1, 0.5)
    c.drawCentredString(width / 2, height - 190, user_data['name'])

    
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(0, 0, 0.2)
    c.drawCentredString(width / 2, height - 230, f"Email: {user_data['email']}")
    c.drawCentredString(width / 2, height - 250, f"Department: {user_data['department']}")

    
    c.setFont("Helvetica", 13)
    c.drawCentredString(width / 2, height - 300, "For successfully completing the Python Quiz")

    
    c.setFont("Helvetica-Bold", 16)
    c.setFillColorRGB(0.4, 0, 0.4)
    c.drawCentredString(width / 2, height - 340, f"Final Score: {score}/100")

    
    c.setFont("Helvetica-Oblique", 10)
    c.drawRightString(width - 60, 60, f"Date: {datetime.now().strftime('%d-%m-%Y')}")

    
    c.setFont("Helvetica", 10)
    c.drawString(80, 60, "Authorized by: Python Quiz Admin")

    
    c.save()

    messagebox.showinfo("Certificate Generated",
                        f"Certificate saved as:\n{filename}\n\nLocation:\n{filepath}")


def show_certificate(score):
    cert_window = tk.Tk()
    cert_window.title("Certificate of Achievement")
    cert_window.geometry("450x400")
    image = Image.open(r"C:\Users\Lokesh\Downloads\techmaa_org.jpg")
    new_width = 70
    new_height = 70
        

    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

    photo = ImageTk.PhotoImage(resized_image)

    logo_label = tk.Label(cert_window, image=photo)
    logo_label.pack(pady=10)

    tk.Label(cert_window, text="🎓 Certificate of Achievement 🎓",
             font=("Arial", 16, "bold"), fg="darkgreen").pack(pady=20)

    tk.Label(cert_window, text=f"Presented to {user_data['name']}",
             font=("Arial", 14, "bold"), fg="blue").pack(pady=5)

    tk.Label(cert_window, text=f"Email: {user_data['email']}", font=("Arial", 10)).pack(pady=2)
    tk.Label(cert_window, text=f"Department: {user_data['department']}", font=("Arial", 10)).pack(pady=2)

    tk.Label(cert_window, text=f"Score: {score}/10", font=("Arial", 12, "bold"), fg="purple").pack(pady=10)
    tk.Label(cert_window, text="Congratulations on completing the quiz!",
             font=("Arial", 11)).pack(pady=10)

    tk.Button(cert_window, text="Download Certificate (PDF)",
              command=lambda: generate_certificate_pdf(score),
              bg="lightblue").pack(pady=15)

    tk.Button(cert_window, text="Close", command=cert_window.destroy, bg="lightgreen").pack(pady=10)

    cert_window.mainloop()


def open_quiz_page():
    login_window.destroy()

    quiz_window = tk.Tk()
    quiz_window.title("Quiz Page")
    quiz_window.geometry("400x500")

    tk.Label(quiz_window, text=f"Welcome {user_data['name']}!", font=("Arial", 14, "bold")).pack(pady=10)
    tk.Label(quiz_window, text=f"Department: {user_data['department']}", font=("Arial", 10)).pack(pady=5)
    tk.Label(quiz_window, text=f"Email: {user_data['email']}", font=("Arial", 10)).pack(pady=5)

    
    questions = [
        ("1. Python is a ______ language?", ["Compiled", "Interpreted", "Assembly", "Machine"]),
        ("2. Which keyword defines a function?", ["func", "define", "def", "lambda"]),
        ("3. What is the output of 2**3?", ["5", "6", "8", "9"]),
        ("4. Which data type is immutable?", ["List", "Set", "Dict", "Tuple"]),
        ("5. What does 'len()' return?", ["Type", "Length", "Sum", "Size"]),
        ("6. Python files have which extension?", [".py", ".pt", ".pyt", ".python"]),
        ("7. What is used to import a module?", ["import", "include", "require", "load"]),
        ("8. Which loop executes at least once?", ["for", "while", "do-while", "none"]),
        ("9. Python is developed by ______?", ["Google", "Microsoft", "Guido van Rossum", "Elon Musk"]),
        ("10. Lists are enclosed in ______?", ["{}", "()", "[]", "<>"]),
    ]

    answers = ["Interpreted", "def", "8", "Tuple", "Length", ".py", "import", "do-while", "Guido van Rossum", "[]"]

    score = tk.IntVar(value=0)
    current_q = tk.IntVar(value=0)
    selected = tk.StringVar(value="")

    def next_question():
        q_index = current_q.get()
        if selected.get() == answers[q_index]:
            score.set(score.get() + 1)

        if q_index + 1 < len(questions):
            current_q.set(q_index + 1)
            load_question()
        else:
            messagebox.showinfo("Quiz Complete", f"Your Score: {score.get()}/10")
            quiz_window.destroy()
            show_certificate(score.get())

    def load_question():
        q_index = current_q.get()
        question_label.config(text=questions[q_index][0])
        selected.set("")
        for i in range(4):
            options[i].config(text=questions[q_index][1][i], value=questions[q_index][1][i])

    question_label = tk.Label(quiz_window, text="", font=("Arial", 12))
    question_label.pack(pady=10)

    for_frame = tk.Frame(quiz_window)
    for_frame.pack()

    options = []
    for i in range(4):
        rb = tk.Radiobutton(for_frame, text="", variable=selected, value="", font=("Arial", 10))
        rb.pack(anchor="w")
        options.append(rb)

    next_btn = tk.Button(quiz_window, text="Next", command=next_question, bg="lightblue")
    next_btn.pack(pady=10)

    load_question()
    quiz_window.mainloop()



def login():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    dept = department_selected.get().strip()

    if not name or not email or not dept:
        messagebox.showerror("Error", "All fields are required!")
        return

    user_data["name"] = name
    user_data["email"] = email
    user_data["department"] = dept

    open_quiz_page()





login_window = tk.Tk()
title_label = tk.Label(
    login_window,
    text="Quiz by Techmaa Org.",
    font=("Helvetica", 18, "bold"),
    fg="white",           # text color
    bg="#4A90E2",         # blue background
    padx=10,              # inner padding (x)
    pady=10               # inner padding (y)
)
title_label.pack(fill="x", pady=20)

image = Image.open(r"C:\Users\Lokesh\Downloads\techmaa_org.jpg")
new_width = 70
new_height = 70
        
        # Resize using a high-quality filter
resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)

photo = ImageTk.PhotoImage(resized_image)

# Create a Label widget to display the image
logo_label = tk.Label(login_window, image=photo)
logo_label.pack(pady=10)

login_window.geometry("600x600")

tk.Label(login_window, text="User Login", font=("Arial", 16, "bold")).pack(pady=20)

tk.Label(login_window, text="Name:").pack()
name_entry = tk.Entry(login_window, width=30)
name_entry.pack()

tk.Label(login_window, text="Email:").pack()
email_entry = tk.Entry(login_window, width=30)
email_entry.pack()

department_selected = tk.StringVar(login_window)

options = ["Python", "PowerBi", "MS excel"]
department_selected.set(options[0])  # Set the first option as default

dropdown = tk.OptionMenu(login_window, department_selected, *options)
dropdown.pack()

tk.Button(login_window, text="Login", command=login, bg="lightblue", width=10).pack(pady=15)

login_window.mainloop()
