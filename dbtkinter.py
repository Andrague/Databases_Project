import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import mysql.connector
from tkinter import messagebox
import matplotlib.pyplot as plt
import datetime 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
canvas_widget = None
import mysql.connector
import tkinter as tk

def database_connection():
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1', 
            port=3306,  
            user='root',  
            password='fNSf9P74NRa6qt',
            database='mainproject',  
        )
        return conn
    except mysql.connector.Error as e:
        tk.messagebox.showinfo(title='Database Connection Error', message=f"Problems with connection to the database: {str(e)}")
        return None


window = tk.Tk()
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)
window.state('zoomed')

my_font = font.Font(family="Helvetica", size=12, underline=True)

page1, page2, page3, page4 = (tk.Frame(window) for _ in range(4))
for page in (page1, page2, page3, page4):
    page.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    if frame == page1:
        page1_entry.delete(0, 'end')
        page1_entry2.delete(0, 'end')
        page2_username_entry.delete(0, 'end')
        page2_password_entry.delete(0, 'end')
    frame.tkraise()

#page1 Login
page1_reg_label = Label(page1, text="If you haven't the account choose the registration option", font=('Arial', 14, 'bold'))
page1_reg_label.place(x=10, y=25)

page1_label = Label(page1, text='Username', font=('Arial', 14), fg='red', bg='blue')
page1_label.place(x=50, y=100)
page1_entry = Entry(page1)
page1_entry.place(x=160, y=105)

page1_label2 = Label(page1, text='Password', font=('Arial', 14), fg='red', bg='blue')
page1_label2.place(x=50, y=150)
page1_entry2 = Entry(page1, show='*')
page1_entry2.place(x=160, y=155)

login_button = Button(page1, text='LOGIN', font=('Arial', 14), command=lambda: login())
login_button.place(x=100, y=200)
tk.Button(page1, text='Register', font=my_font, command=lambda: show_frame(page2), relief='flat', fg='blue', highlightthickness=0).place(x=450, y=55)

# Page 2: Registration
page2.config(background='gray')
page2_label = Label(page2, text='Welcome to Registration', font=('Arial', 14, 'bold'))
page2_label.place(x=50, y=50)

page2_username_label = Label(page2, text='Username:', font=('Arial', 12))
page2_username_label.place(x=50, y=100)
page2_username_entry = Entry(page2)
page2_username_entry.place(x=200, y=100)

page2_password_label = Label(page2, text='Password:', font=('Arial', 12))
page2_password_label.place(x=50, y=150)
page2_password_entry = Entry(page2, show='*')
page2_password_entry.place(x=200, y=150)

page2_company_id_label = Label(page2, text='Company ID:', font=('Arial', 12))
page2_company_id_label.place(x=50, y=200)
page2_company_id_entry = Entry(page2)
page2_company_id_entry.place(x=200, y=200)

page2_first_name_label = Label(page2, text='First Name:', font=('Arial', 12))
page2_first_name_label.place(x=50, y=250)
page2_first_name_entry = Entry(page2)
page2_first_name_entry.place(x=200, y=250)

page2_last_name_label = Label(page2, text='Last Name:', font=('Arial', 12))
page2_last_name_label.place(x=50, y=300)
page2_last_name_entry = Entry(page2)
page2_last_name_entry.place(x=200, y=300)

page2_register_button = Button(page2, text='Register', font=('Arial', 12), command=lambda: handle_registration())
page2_register_button.place(x=200, y=350)

page2_home = Button(page2, text='Back', font=('Arial', 12), command=lambda: show_frame(page1))
page2_home.place(x=30, y=350)

# Page 3: Client Interface
page3.config(background='lightgray')
page3_label = Label(page3, text='Welcome to Client Interface', font=('Arial', 14, 'bold'))
page3_label.place(x=50, y=150)
page3_home = Button(page3, text='Return to the main menu', font=('Arial', 12), command=lambda: show_frame(page1))
page3_home.place(x=15, y=20)


page3_contact_label = Label(page3, text='Please fill the form and our manager will contact with you')
page3_contact_label.place(x=50, y=150)
history_button = tk.Button(page3, text="History", command=lambda: show_user_history(logged_in_user_id))
history_button.pack(pady=20)

# Page 4: Admin Interface
page4.config(background='gray')
page4_label = Label(page4, text='Welcome to Admin Interface', font=('Arial', 14, 'bold'))
page4_label.place(x=50, y=150)
page4_home = Button(page4, text='Return to the main menu', font=('Arial', 12), command=lambda: show_frame(page1))
page4_home.place(x=15, y=20)

login_error_label = Label(page2, text="All fields must be completed", font=('Arial', 12), fg='red')

def show_user_id():
    if logged_in_user_id:
        user_id_label.config(text=f"Your ID is: {logged_in_user_id}")
        user_id_label.place(x=100, y=250)
    else:
        tk.messagebox.showinfo(title='Error', message="User ID Unavailable")

# Setup on Page 3
user_id_label = tk.Label(page3, font=('Arial', 12))
show_id_button = tk.Button(page3, text="Show My ID", font=('Arial', 12), command=show_user_id)
show_id_button.place(x=100, y=300)

def contact_page_setup():
    contact_frame = tk.Frame(page3)

    tk.Label(contact_frame, text='Client ID:', font=('Arial', 12)).pack(fill='x')
    client_id_entry = tk.Entry(contact_frame)
    client_id_entry.pack(fill='x')

    tk.Label(contact_frame, text='Theme:', font=('Arial', 12)).pack(fill='x')
    theme_entry = tk.Entry(contact_frame)
    theme_entry.pack(fill='x')

    tk.Label(contact_frame, text='Comment:', font=('Arial', 12)).pack(fill='x')
    comment_entry = tk.Entry(contact_frame, width=40)
    comment_entry.pack(fill='x')

    send_button = tk.Button(contact_frame, text='Send Message', font=('Arial', 12),
                            command=lambda: send_message(client_id_entry.get(), theme_entry.get(), comment_entry.get()))
    send_button.pack(pady=10)

    return contact_frame, client_id_entry, theme_entry, comment_entry

def toggle_contact_frame():
    if contact_frame.winfo_manager():
        contact_frame.pack_forget()
    else:
        contact_frame.pack(pady=20)

contact_frame, client_id_entry, theme_entry, comment_entry = contact_page_setup()

page3_contact = Button(page3, text='Contact with manager', font=('Arial', 12), command=toggle_contact_frame)
page3_contact.place(x=100, y=200)
def fetch_specializations():
    conn = database_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT DISTINCT specialization FROM employee_data")
        specializations = cursor.fetchall()
        return [spec[0] for spec in specializations]
    finally:
        cursor.close()
        conn.close()

def show_available_employee():
    specializations = fetch_specializations()
    
    if hasattr(show_available_employee, 'dropdown'):
        show_available_employee.dropdown.pack_forget()
        show_available_employee.ok_button.pack_forget()
    
    specializations.insert(0, "Specializations...")  # Add placeholder text
    
    show_available_employee.dropdown = ttk.Combobox(page3, values=specializations)
    show_available_employee.dropdown.current(0)  # Set the placeholder text as the default value
    show_available_employee.dropdown.pack(pady=10)
    
    show_available_employee.ok_button = tk.Button(page3, text="Ok", command=lambda: display_employees_by_specialization(show_available_employee.dropdown.get()))
    show_available_employee.ok_button.pack(pady=10)

def display_employees_by_specialization(specialization):
    conn = database_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT last_name, first_name FROM employee_data WHERE specialization = %s", (specialization,))
        employees = cursor.fetchall()
        
        num_employees = len(employees)
        employee_names = [f"{emp[1]} {emp[0]}" for emp in employees]
        
        detail_window = tk.Toplevel(window)
        detail_window.title(f"Employees with specialization: {specialization}")
        
        tk.Label(detail_window, text=f"Total employees: {num_employees}", font=('Arial', 12)).pack(pady=10)
        for name in employee_names:
            tk.Label(detail_window, text=name, font=('Arial', 12)).pack()
    finally:
        cursor.close()
        conn.close()
show_available_button = tk.Button(page3, text="Show available employee", command=show_available_employee)
show_available_button.pack(pady=20)
def send_message(client_id, theme, comment):
    if client_id and theme and comment:
        conn = database_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO message (client_id, theme, comment) VALUES (%s, %s, %s)", (client_id, theme, comment))
        conn.commit()
        cursor.close()
        conn.close()
        tk.messagebox.showinfo(title='Info', message="Message sent successfully")
        client_id_entry.delete(0, 'end')
        theme_entry.delete(0, 'end')
        comment_entry.delete(0, 'end')
    else:
        tk.messagebox.showinfo(title='Error', message="All fields must be filled.")

def display_messages():
    if not hasattr(display_messages, 'msg_frame'):
        display_messages.msg_frame = tk.Frame(page4)
        display_messages.msg_frame.pack(fill='both', expand=True)

        display_messages.msg_tree = ttk.Treeview(display_messages.msg_frame, columns=('message_id', 'client_id', 'theme'), show="headings", height=5)
        display_messages.msg_tree.pack(fill='both', expand=True)

        display_messages.msg_tree.heading('message_id', text="Message ID")
        display_messages.msg_tree.heading('client_id', text="Client ID")
        display_messages.msg_tree.heading('theme', text="Theme")

        display_messages.back_button = tk.Button(display_messages.msg_frame, text="Back", command=hide_messages)
        display_messages.back_button.pack(pady=10)

        display_messages.msg_tree.bind("<Double-1>", lambda event, tree=display_messages.msg_tree: on_message_select(event, tree))

    conn = database_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT message_id, client_id, theme FROM message")
        rows = cursor.fetchall()
        display_messages.msg_tree.delete(*display_messages.msg_tree.get_children())
        for row in rows:
            display_messages.msg_tree.insert("", 'end', values=row)
    finally:
        cursor.close()
        conn.close()

def hide_messages():
    if hasattr(display_messages, 'msg_frame'):
        display_messages.msg_frame.pack_forget()

def on_message_select(event, tree):
    selected_item = tree.selection()[0]
    message_id = tree.item(selected_item, "values")[0]
    show_message_detail(message_id)

def show_message_detail(message_id):
    detail_window = tk.Toplevel(window)
    detail_window.title("Message Detail")

    conn = database_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT client_id, theme, comment FROM message WHERE message_id = %s", (message_id,))
        client_id, theme, comment = cursor.fetchone()

        tk.Label(detail_window, text=f"Client ID: {client_id}", font=('Arial', 12)).pack(fill='x', padx=10, pady=2)
        tk.Label(detail_window, text=f"Theme: {theme}", font=('Arial', 12)).pack(fill='x', padx=10, pady=2)
        tk.Label(detail_window, text="Comment:", font=('Arial', 12)).pack(fill='x', padx=10, pady=2)

        comment_text = tk.Text(detail_window, height=10, width=50)
        comment_text.pack(padx=10, pady=10)
        comment_text.insert('1.0', comment)
    finally:
        cursor.close()
        conn.close()

global accept_button, reject_button
def setup_admin_interface():
    global accept_button, reject_button

    control_frame = tk.Frame(page4)
    control_frame.pack(pady=20)

    load_msg_button = tk.Button(control_frame, text="Load Messages", command=display_messages)
    load_msg_button.pack(fill='x', padx=10)

    accept_button = tk.Button(control_frame, text="Accept", font=('Arial', 12), command=lambda: accept_or_reject_application('approved'))
    reject_button = tk.Button(control_frame, text="Reject", font=('Arial', 12), command=lambda: accept_or_reject_application('rejected'))

setup_admin_interface()

tree = None
commit_button = None

def create_treeview():
    global tree
    if tree is None:
        tree = ttk.Treeview(page4, columns=(1, 2, 3), show="headings", height="5")
        tree.place(x=50, y=250)
        tree.heading(1, text="Employee ID")
        tree.heading(2, text="Name")
        tree.heading(3, text="Position")
    else:
        tree.place(x=50, y=250)

def fetch_data():
    create_treeview()
    try:
        conn = database_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id_employee, last_name, specialization FROM employee_data")
        records = cursor.fetchall()

        for i in tree.get_children():
            tree.delete(i)

        for row in records:
            tree.insert("", 'end', values=row)
        conn.close()
    except mysql.connector.Error as e:
        tk.messagebox.showinfo(title='Database Error', message="Database Error")
    except Exception as e:
        tk.messagebox.showinfo(title='Error', message="Error")

employee_form_widgets = {}

def hide_all_operations():
    if tree is not None:
        tree.place_forget()
    if app_tree is not None:
        app_tree.place_forget()
    if no_applications_label is not None:
        no_applications_label.place_forget()

    for widgets in employee_form_widgets.values():
        widgets['label'].place_forget()
        widgets['entry'].place_forget()
        widgets['entry'].delete(0, 'end')

    if commit_button is not None:
        commit_button.place_forget()
    if accept_button is not None:
        accept_button.place_forget()
    if reject_button is not None:
        reject_button.place_forget()
    if show_stats_button is not None:
        show_stats_button.place_forget()
    if history_button is not None:
        history_button.place_forget()
    

def show_employee():
    hide_all_operations()
    fetch_data()

employee_form_visible = False
employee_entries = {}

def setup_employee_form(mode, employee_data):
    global employee_form, last_name_entry, first_name_entry, specialization_entry, team_id_entry, hours_entry, vacation_date_entry, save_button, cancel_button, commit_button
    employee_form = tk.Frame(page4)
    employee_form.place(x=50, y=100)

    tk.Label(employee_form, text='Last Name:', font=('Arial', 12)).pack()
    last_name_entry = tk.Entry(employee_form)
    last_name_entry.pack()
    last_name_entry.insert(0, employee_data.get('last_name', ''))

    tk.Label(employee_form, text='First Name:', font=('Arial', 12)).pack()
    first_name_entry = tk.Entry(employee_form)
    first_name_entry.pack()
    first_name_entry.insert(0, employee_data.get('first_name', ''))

    tk.Label(employee_form, text='Specialization:', font=('Arial', 12)).pack()
    specialization_entry = tk.Entry(employee_form)
    specialization_entry.pack()
    specialization_entry.insert(0, employee_data.get('specialization', ''))

    tk.Label(employee_form, text='Team ID:', font=('Arial', 12)).pack()
    team_id_entry = tk.Entry(employee_form)
    team_id_entry.pack()
    team_id_entry.insert(0, employee_data.get('team_id', ''))

    tk.Label(employee_form, text='Number of Working Hours:', font=('Arial', 12)).pack()
    hours_entry = tk.Entry(employee_form)
    hours_entry.pack()
    hours_entry.insert(0, employee_data.get('working_hours', ''))

    tk.Label(employee_form, text='Vacation Date:', font=('Arial', 12)).pack()
    vacation_date_entry = DateEntry(employee_form, width=20, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
    
    default_date = employee_data.get('vacation_date', datetime.datetime.today().strftime('%Y-%m-%d'))
    vacation_date_entry.set_date(default_date)
    vacation_date_entry.pack()

    if mode == "modify":
        save_button = tk.Button(employee_form, text="Save", font=('Arial', 12), command=lambda: save_employee(employee_data['emp_id']))
        save_button.pack(pady=10)
        cancel_button = tk.Button(employee_form, text="Cancel", font=('Arial', 12), command=hide_employee_form)
        cancel_button.pack(pady=10)
    else:
        commit_button = tk.Button(employee_form, text="Commit", font=('Arial', 12), command=lambda: add_employee(
            last_name_entry.get(),
            first_name_entry.get(),
            specialization_entry.get(),
            team_id_entry.get(),
            hours_entry.get(),
            vacation_date_entry.get_date()
        ))
        commit_button.pack(pady=10)

def add_employee(last_name, first_name, specialization, team_id, hours, vacation_date):
    try:
        conn = database_connection()
        cursor = conn.cursor()
        query = "INSERT INTO employee_data (last_name, first_name, specialization, team_id, number_of_working_hours, vacation_date) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (last_name, first_name, specialization, team_id, hours, vacation_date))
        conn.commit()
        tk.messagebox.showinfo(title='Success', message="Employee added successfully")
    except mysql.connector.Error as e:
        tk.messagebox.showinfo(title='Database Error', message=str(e))
    finally:
        cursor.close()
        conn.close()
    hide_employee_form()

def save_employee(emp_id):
    last_name = last_name_entry.get()
    first_name = first_name_entry.get()
    specialization = specialization_entry.get()
    team_id = team_id_entry.get()
    hours = hours_entry.get()
    vacation_date = vacation_date_entry.get_date()

    try:
        conn = database_connection()
        cursor = conn.cursor()
        query = "UPDATE employee_data SET last_name=%s, first_name=%s, specialization=%s, team_id=%s, number_of_working_hours=%s, vacation_date=%s WHERE id_employee=%s"
        cursor.execute(query, (last_name, first_name, specialization, team_id, hours, vacation_date, emp_id))
        conn.commit()
        tk.messagebox.showinfo(title='Success', message="Employee details updated successfully")
    except mysql.connector.Error as e:
        tk.messagebox.showinfo(title='Database Error', message=str(e))
    finally:
        cursor.close()
        conn.close()
    hide_employee_form()

def hide_employee_form():
    global employee_form, save_button, cancel_button, commit_button
    if employee_form:
        employee_form.place_forget()
    if save_button:
        save_button.place_forget()
    if cancel_button:
        cancel_button.place_forget()
    if commit_button:
        commit_button.place_forget()

def toggle_employee_form():
    hide_all_operations()
    global employee_form_visible
    if employee_form_visible:
        hide_employee_form()
        employee_form_visible = False
    else:
        setup_employee_form(mode="add", employee_data={})
        employee_form_visible = True


employee_form_visible = False

toggle_form_button = Button(page4, text="Add Employee", font=('Arial', 12), command=toggle_employee_form)
toggle_form_button.place(x=200, y=200)

def fetch_employees():
    conn = database_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id_employee, last_name, first_name, specialization, team_id, number_of_working_hours, vacation_date FROM employee_data")
        rows = cursor.fetchall()
        if rows:
            return [{'emp_id': row[0], 'last_name': row[1], 'first_name': row[2], 'specialization': row[3], 'team_id': row[4], 'working_hours': row[5], 'vacation_date': row[6]} for row in rows]
        else:
            tk.messagebox.showinfo(title='Info', message="No employees found in the database")
            return []
    finally:
        cursor.close()
        conn.close()
def delete_employee():
    employees = fetch_employees()
    if employees:
        delete_window = tk.Toplevel(window)
        delete_window.minsize(300,100)
        delete_window.maxsize(1000, 960)
        delete_window.title("Select Employee to Delete")
        delete_label = Label(delete_window, text='Click twice on the row that you would like to delete', font=('Arial', 13))
        delete_label.pack(pady=10)
        tree = ttk.Treeview(delete_window, columns=('emp_id', 'last_name', 'first_name', 'specialization', 'team_id', 'working_hours', 'vacation_date'), show='headings')
        tree.pack(fill='both', expand=True)
        for col in tree['columns']:
            tree.heading(col, text=col.replace('_', ' ').capitalize())

        for emp in employees:
            tree.insert('', 'end', values=(emp['emp_id'], emp['last_name'], emp['first_name'], emp['specialization'], emp['team_id'], emp['working_hours'], emp['vacation_date']))

        def on_employee_select(event):
            selected_item = tree.selection()[0]
            emp_data = tree.item(selected_item, 'values')
            employee_data = {k: v for k, v in zip(['emp_id', 'last_name', 'first_name', 'specialization', 'team_id', 'working_hours', 'vacation_date'], emp_data)}
            
            confirm = tk.messagebox.askyesno(title='Confirm Deletion', message="Are you sure you want to delete this employee?")
            if confirm:
                archive_and_delete_employee(employee_data)
                tk.messagebox.showinfo(title='Success', message="Employee deleted and archived successfully")
                delete_window.destroy()

        tree.bind('<Double-1>', on_employee_select)
    else:
        tk.messagebox.showinfo(title='Info', message="No employees found in the database")

def archive_and_delete_employee(employee_data):
    try:
        conn = database_connection()
        cursor = conn.cursor()

        # Insert employee data into archive table
        archive_query = "INSERT INTO archive (id_employee, last_name, first_name, specialization, team_id, number_of_working_hours, vacation_date, employment_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(archive_query, (employee_data['emp_id'], employee_data['last_name'], employee_data['first_name'], employee_data['specialization'], employee_data['team_id'], employee_data['working_hours'], employee_data['vacation_date'], employee_data['emp_id']))

        # Delete employee data from employee_data table
        delete_query = "DELETE FROM employee_data WHERE id_employee = %s"
        cursor.execute(delete_query, (employee_data['emp_id'],))

        conn.commit()
    except mysql.connector.Error as e:
        tk.messagebox.showinfo(title='Database Error', message=str(e))
    finally:
        cursor.close()
        conn.close()

def modify_employee():
    employees = fetch_employees()
    if employees:
        modify_window = tk.Toplevel(window)
        modify_window.minsize(300,100)
        modify_window.maxsize(1000, 968)
        modify_window.title("Select Employee to Modify")
        tree = ttk.Treeview(modify_window, columns=('emp_id', 'last_name', 'first_name', 'specialization', 'team_id', 'working_hours', 'vacation_date'), show='headings')
        tree.pack(fill='both', expand=True)
        for col in tree['columns']:
            tree.heading(col, text=col.replace('_', ' ').capitalize())

        for emp in employees:
            tree.insert('', 'end', values=(emp['emp_id'], emp['last_name'], emp['first_name'], emp['specialization'], emp['team_id'], emp['working_hours'], emp['vacation_date']))

        def on_employee_select(event):
            selected_item = tree.selection()[0]
            emp_data = tree.item(selected_item, 'values')
            employee_data = {k: v for k, v in zip(['emp_id', 'last_name', 'first_name', 'specialization', 'team_id', 'working_hours', 'vacation_date'], emp_data)}
            modify_window.destroy()
            setup_employee_form(mode="modify", employee_data=employee_data)

        tree.bind('<Double-1>', on_employee_select)
    else:
        tk.messagebox.showinfo(title='Info', message="No employees found in the database")

modify_button = Button(page4, text="Modify Employee", font=('Arial', 12), command=modify_employee)
modify_button.place(x=315, y=200)

page4_employee = Button(page4, text='Show employee', font=('Arial', 12), command=show_employee)
page4_employee.place(x=80, y=200)

page4_hide_employee = Button(page4, text='←', font=('Arial', 12), command=hide_all_operations)
page4_hide_employee.place(x=50, y=200)

global app_tree, accept_button, reject_button, no_applications_label
app_tree = None
accept_button = Button(page4, text="Accept", font=('Arial', 12), command=lambda: accept_or_reject_application('approved'))
reject_button = Button(page4, text="Reject", font=('Arial', 12), command=lambda: accept_or_reject_application('rejected'))
no_applications_label = None

def accept_or_reject_application(status):
    selected_item = app_tree.selection()
    if selected_item:
        user_id = app_tree.item(selected_item[0])['values'][0]
        update_application_status(user_id, status)
    else:
        tk.messagebox.showinfo(title='Info', message="Please select an application to proceed.")

def update_application_status(user_id, status):
    try:
        conn = database_connection()
        cursor = conn.cursor()
        if status == 'approved':
            cursor.execute("UPDATE userinfo SET status = %s WHERE user_id = %s", (status, user_id))
        else:
            cursor.execute("DELETE FROM userinfo WHERE user_id = %s", (user_id,))
        conn.commit()
    except Exception as e:
        tk.messagebox.showinfo(title='Info', message=str(e))
    finally:
        cursor.close()
        conn.close()
    fetch_applications()

delete_button = Button(page4, text="Delete Employee", font=('Arial', 12), command=delete_employee)
delete_button.place(x=550, y=200)
def show_applications():
    global app_tree, accept_button, reject_button
    hide_all_operations()
    create_application_list()
    accept_button.place(x=320, y=250)
    reject_button.place(x=420, y=250)

def create_application_list():
    global app_tree
    if app_tree is None:
        app_tree = ttk.Treeview(page4, columns=('user_id', 'username', 'status'), show="headings", height="5")
        app_tree.place(x=50, y=350)
        app_tree.heading('user_id', text="User ID")
        app_tree.heading('username', text="Username")
        app_tree.heading('status', text="Status")
    fetch_applications()

def fetch_applications():
    global app_tree, no_applications_label
    try:
        conn = database_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id, username, status FROM userinfo WHERE status = 'pending'")
        records = cursor.fetchall()

        app_tree.delete(*app_tree.get_children())

        if records:
            for row in records:
                app_tree.insert("", 'end', values=row)
            app_tree.pack()
            accept_button.place(x=320, y=250)
            reject_button.place(x=420, y=250)
        else:
            if no_applications_label is None:
                no_applications_label = tk.Label(page4, text="No applications yet", font=('Arial', 12))
            no_applications_label.place(x=50, y=320)
            app_tree.pack_forget()
            accept_button.place_forget()
            reject_button.place_forget()
    finally:
        cursor.close()
        conn.close()

def display_no_applications_message():
    global no_applications_label
    if no_applications_label is None:
        no_applications_label = Label(page4, text="No applications yet", font=('Arial', 12))
    no_applications_label.place(x=50, y=320)
    app_tree.pack_forget()
    accept_button.place_forget()
    reject_button.place_forget()

applications_button = Button(page4, text="Applications", font=('Arial', 12), command=show_applications)
applications_button.place(x=450, y=200)

def calculate_sum():
    sum_window = tk.Toplevel(window)
    sum_window.title("Calculate Task Cost")

    tk.Label(sum_window, text="Hourly Rate:", font=('Arial', 12)).pack(pady=(10, 0))
    hourly_rate_entry = tk.Entry(sum_window, font=('Arial', 12))
    hourly_rate_entry.pack(pady=(0, 10))

    tk.Label(sum_window, text="Number of Working Hours:", font=('Arial', 12)).pack(pady=(10, 0))
    hours_entry = tk.Entry(sum_window, font=('Arial', 12))
    hours_entry.pack(pady=(0, 10))

    def perform_calculation():
        try:
            hourly_rate = float(hourly_rate_entry.get())
            hours = float(hours_entry.get())
            total_sum = hourly_rate * hours

            result_label.config(text=f"Total Cost: ${total_sum:.2f}")
        except ValueError:
            tk.messagebox.showinfo(title='Input Error', message="Please enter valid numbers for rate and hours")

    calculate_button = tk.Button(sum_window, text="Calculate", command=perform_calculation)
    calculate_button.pack(pady=(5, 10))

    result_label = tk.Label(sum_window, text="Total Cost: $0.00", font=('Arial', 12))
    result_label.pack(pady=(10, 10))

def insert_task(company_id2, start_date, end_date, count, sum):
    conn = database_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO tasks (company_id2, start_date, end_date, count, sum) VALUES (%s, %s, %s, %s, %s)",
                       (company_id2, start_date, end_date, int(count), float(sum)))
        conn.commit()
        return True
    except mysql.connector.Error as e:
        tk.messagebox.showinfo(title='Database Error', message=str(e))
        return False
    finally:
        cursor.close()
        conn.close()

def create_task():
    company_id2 = company_id_entry.get()
    start_date = start_date_entry.get_date()
    end_date = end_date_entry.get_date()
    count = count_entry.get()
    sum = sum_entry.get()

    if not all([company_id2, start_date, end_date, count, sum]):
        tk.messagebox.showinfo(title='Error', message="All fields must be filled")
        return

    if insert_task(company_id2, start_date, end_date, count, sum):
        tk.messagebox.showinfo(title='Success', message="Task created successfully")
        task_form.pack_forget()
    else:
        tk.messagebox.showinfo(title='Error', message="Failed to create task")

def setup_task_form():
    global task_form, company_id_entry, start_date_entry, end_date_entry, count_entry, sum_entry
    task_form = tk.Frame(page4)
    task_form.pack(pady=20, fill='x', expand=True)
    task_form.pack_forget()

    tk.Label(task_form, text='Company ID:', font=('Arial', 12)).pack(fill='x')
    company_id_entry = tk.Entry(task_form)
    company_id_entry.pack(fill='x')

    tk.Label(task_form, text='Start Date:', font=('Arial', 12)).pack(fill='x')
    start_date_entry = DateEntry(task_form, width=20, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
    start_date_entry.pack(fill='x')

    tk.Label(task_form, text='End Date:', font=('Arial', 12)).pack(fill='x')
    end_date_entry = DateEntry(task_form, width=20, background='darkblue', foreground='white', borderwidth=2, date_pattern='y-mm-dd')
    end_date_entry.pack(fill='x')

    tk.Label(task_form, text='Count:', font=('Arial', 12)).pack(fill='x')
    count_entry = tk.Entry(task_form)
    count_entry.pack(fill='x')

    tk.Label(task_form, text='Sum:', font=('Arial', 12)).pack(fill='x')
    sum_entry = tk.Entry(task_form)
    sum_entry.pack(fill='x')

    calculate_sum_button = tk.Button(task_form, text="Calculate sum", font=('Arial', 12), command=calculate_sum)
    calculate_sum_button.pack(fill='x', pady=5)

    create_task_button = tk.Button(task_form, text="Create Task", font=('Arial', 12), command=create_task)
    create_task_button.pack(fill='x', pady=5)

    back_button = tk.Button(task_form, text="Back", font=('Arial', 12), command=lambda: task_form.pack_forget())
    back_button.pack(fill='x', pady=5)

    return task_form

def show_task_form():
    hide_all_operations()
    task_form.pack(pady=20)

task_form = setup_task_form()

add_task_button = tk.Button(page4, text="Add Task", command=show_task_form)
add_task_button.pack(pady=10)

def fetch_company_statistics():
    conn = database_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
        SELECT c.company_name, IFNULL(SUM(t.sum), 0) as total_sum
        FROM company_data c
        LEFT JOIN tasks t ON c.id_company = t.company_id2
        GROUP BY c.id_company
        """)
        data = cursor.fetchall()
        return data
    except mysql.connector.Error as e:
        tk.messagebox.showinfo(title='Database Error', message="Database Error")
        return []
    finally:
        cursor.close()
        conn.close()

def hide_statistics():
    global canvas_widget
    if canvas_widget:
        canvas_widget.pack_forget()
        canvas_widget = None
    if hasattr(show_statistics, 'back_button'):
        show_statistics.back_button.pack_forget()
        del show_statistics.back_button

def show_statistics():
    global canvas_widget

    stats_window = tk.Toplevel(window)
    stats_window.title("Statistics")

    data = fetch_company_statistics()
    if data:
        company_names = [row[0] for row in data]
        sums = [float(row[1]) for row in data]
        fig, ax = plt.subplots()
        bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
        ax.bar(company_names, sums, color=bar_colors)
        ax.set_xlabel('Company Names')
        ax.set_ylabel('Sum of Tasks')
        ax.set_title('Sum of Tasks by Company')
        ax.set_xticks(range(len(company_names)))  
        ax.set_xticklabels(company_names, rotation=30, ha='right')

        if canvas_widget:
            canvas_widget.get_tk_widget().pack_forget()

        if not hasattr(show_statistics, 'back_button'):
            show_statistics.back_button = tk.Button(stats_window, text="Back", command=stats_window.destroy)
        show_statistics.back_button.pack(pady=(10, 0))

        canvas = FigureCanvasTkAgg(fig, master=stats_window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()
    else:
        tk.messagebox.showinfo(title='No Data', message="No data available to display")


show_stats_button = tk.Button(page3, text="Show Statistics", command=show_statistics)
show_stats_button.pack(pady=10)

def show_user_history(user_id):
    hide_all_operations()
    tasks = fetch_tasks_for_user(user_id)

    if tasks:
        history_window = tk.Toplevel(page3)
        history_window.title("Task History")

        for i, task in enumerate(tasks, start=1):
            tk.Label(history_window, text=f"Task {i}: {task}", font=('Arial', 12)).pack()
    else:
        tk.messagebox.showinfo(title='Info', message="The history is empty")

def fetch_tasks_for_user(user_id):
    conn = database_connection()
    cursor = conn.cursor()
    try:
        query = """
        SELECT t.* FROM tasks t
        JOIN Representative r ON t.company_id2 = r.id_company1
        WHERE r.id_client = %s
        """
        cursor.execute(query, (user_id,))
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def register():
    cnx = database_connection()
    username = page2_username_entry.get().strip()
    password = page2_password_entry.get().strip()
    company_id = page2_company_id_entry.get().strip()
    first_name = page2_first_name_entry.get().strip()
    last_name = page2_last_name_entry.get().strip()

    if not all([username, password, company_id, first_name, last_name]):
        tk.messagebox.showinfo(title='Error', message="All fields must be filled!")
        return False

    cursor = cnx.cursor()
    try:
        check_user_query = "SELECT username FROM userinfo WHERE username = %s"
        cursor.execute(check_user_query, (username,))
        if cursor.fetchone():
            tk.messagebox.showinfo(title='Error', message="Username already exists!")
            return False

        add_user_query = "INSERT INTO userinfo (username, password, role, status) VALUES (%s, %s, 'client', 'pending')"
        cursor.execute(add_user_query, (username, password))
        cursor.execute("SELECT LAST_INSERT_ID()")
        user_id = cursor.fetchone()[0]

        add_rep_query = "INSERT INTO Representative (id_client, id_company1, first_name, last_name) VALUES (%s, %s, %s, %s)"
        cursor.execute(add_rep_query, (user_id, company_id, first_name, last_name))

        cnx.commit()
        return True
    except mysql.connector.Error as e:
        tk.messagebox.showinfo(title='Error', message="Database Error")
        return False
    finally:
        cursor.close()
        cnx.close()

def handle_registration():
    if register():
        show_frame(page1)
        tk.messagebox.showinfo(title='Registration Successful', message="Your registration request has been sent. Please wait for admin approval.")
    else:
        tk.messagebox.showinfo(title='Error', message="Registration failed. Please check your details and try again")

def login():
    username = page1_entry.get()
    password = page1_entry2.get()

    if not username or not password:
        tk.messagebox.showinfo(title='Error', message="Please fill out all fields.")
        return

    conn = database_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor()
        query = ("SELECT user_id, password, role, status FROM userinfo WHERE username = %s")
        cursor.execute(query, (username,))
        user_info = cursor.fetchone()

        if user_info and password == user_info[1] and user_info[3] == 'approved':
            global logged_in_user_id
            logged_in_user_id = user_info[0]
            role = user_info[2]
            if role == 'admin':
                show_frame(page4)
            else:
                show_frame(page3)
        else:
            tk.messagebox.showinfo(title='Login Failed', message="Your account is either pending approval or you entered a wrong password.")
    except mysql.connector.Error as e:
        tk.messagebox.showinfo(title='Database Error', message=str(e))
    finally:
        cursor.close()
        conn.close()

show_frame(page1)

window.mainloop()
