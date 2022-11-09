from tkinter import *
import requests
import json
from tkinter import messagebox


def retrieve_list():
    room_list.delete(0, END)
    if token_out:
        url = 'http://localhost:8000/api/'
        headers = {'Authorization': f'Token {token_out}'}
        r = requests.get(url, headers=headers)

        out_data = json.loads(r.text)
        data = []
        for out in out_data:
            res = out.values()
            data.append(list(res))

        for k in data:

            room_list.insert(END, k)


def login():
    global token_out
    global username
    global password
    username = username_entry.get()
    password = password_entry.get()
    if username == '' or password == '':
        messagebox.showerror(
            'Required Fields', 'Username/password should not be empty')

    else:
        data = {
            "username": username,
            "password": password
        }
        try:
            response = requests.post(
                'http://localhost:8000/api-token-auth/', data=data)
            response_dict = json.loads(response.text)
            token_out = response_dict['token']

        except Exception as e:
            messagebox.showerror(
                'Login Failure', 'Username/Credentials Invalid. Please try again !!!')

        messagebox.showinfo('Login Successful')

def add_item():
    try:
        if token_out:
            if room_text.get() == '' or guest_text.get() == '' or check_in_text.get() == '' or check_out_text.get() == '':
                messagebox.showerror(
                    'Required Fields', 'Please include all fields')

            else:
                print('hi')
                end_point = 'http://localhost:8000/api/create/'
                data = {
                    "room_num": room_text.get(),
                    "guest": guest_text.get(),
                    "check_in": check_in_text.get(),
                    "check_out": check_out_text.get()
                }

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Token {token_out}"
                }
                response = requests.post(
                    end_point, json=data, headers=headers)
                print(response.content)

                room_list.delete(0, END)
                room_list.insert(END, (room_text.get(), guest_text.get(),
                                       check_in_text.get(), check_out_text.get()))
                clear_text()
                retrieve_list()

    except NameError:
        messagebox.showerror(
            'Login Failure', 'You have to Login first !!!')
    except Exception as e:
        print(e)


def remove_item():
    try:
        if token_out:
            if room_text.get() == '' or guest_text.get() == '' or check_in_text.get() == '' or check_out_text.get() == '':
                messagebox.showerror(
                    'Required Fields', 'Please include all fields')

            else:

                pk = selected_item[0]
                end_point = f'http://localhost:8000/api/{pk}/delete/'
                data = {
                    "room_num": room_text.get(),
                    "guest": guest_text.get(),
                    "check_in": check_in_text.get(),
                    "check_out": check_out_text.get()
                }

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Token {token_out}"
                }
                response = requests.delete(
                    end_point, json=data, headers=headers)
                print(response.content)

                retrieve_list()

    except NameError:
        messagebox.showerror(
            'Login Failure', 'You have to Login first !!!')
    except Exception as e:
        print(e)



def update_item():
    try:
        if token_out:
            if room_text.get() == '' or guest_text.get() == '' or check_in_text.get() == '' or check_out_text.get() == '':
                messagebox.showerror(
                    'Required Fields', 'Please include all fields')

            else:
                pk = selected_item[0]
                end_point = f'http://localhost:8000/api/{pk}/edit/'
                data = {
                    "room_num": room_text.get(),
                    "guest": guest_text.get(),
                    "check_in": check_in_text.get(),
                    "check_out": check_out_text.get()
                }

                headers = {
                    "Content-Type": "application/json",
                    "Authorization": f"Token {token_out}"
                }
                response = requests.put(
                    end_point, json=data, headers=headers)
                if response.status_code >= 200 and response.status_code <= 299:
                    print(response.content)
                else:
                    messagebox.showerror(
                        'Update Failure', f'Incorrect Format, {response.text}')

                retrieve_list()

    except NameError:
        messagebox.showerror(
            'Login Failure', 'You have to Login first !!!')
    except Exception as e:
        print(e)


def clear_text():
    room_entry.delete(0, END)
    guest_entry.delete(0, END)
    check_in_entry.delete(0, END)
    check_out_entry.delete(0, END)



def select_item(event):
    try:
        global selected_item
        index = room_list.curselection()[0]
        selected_item = room_list.get(index)

        room_entry.delete(0, END)
        room_entry.insert(END, selected_item[1])
        guest_entry.delete(0, END)
        guest_entry.insert(END, selected_item[2])
        check_in_entry.delete(0, END)
        check_in_entry.insert(END, selected_item[3])
        check_out_entry.delete(0, END)
        check_out_entry.insert(END, selected_item[4])
    except IndexError:
        pass


app = Tk()

#room
room_text = StringVar()
room_label = Label(app, text='Room No', font=('bold', 14), pady=20)
room_label.grid(row=0, column=0, sticky=W)
room_entry = Entry(app, textvariable=room_text)
room_entry.grid(row=0, column=1)

# Gues
guest_text = StringVar()
guest_label = Label(app, text='Guest', font=('bold', 14))
guest_label.grid(row=0, column=2, sticky=W)
guest_entry = Entry(app, textvariable=guest_text)
guest_entry.grid(row=0, column=3)

# Check in Date
check_in_text = StringVar()
check_in_label = Label(app, text='Check In Date', font=('bold', 14))
check_in_label.grid(row=1, column=0, sticky=W)
check_in_entry = Entry(app, textvariable=check_in_text)
check_in_entry.grid(row=1, column=1)

# Check Out Date
check_out_text = StringVar()
check_out_label = Label(app, text='Check Out Date', font=('bold', 14))
check_out_label.grid(row=1, column=2, sticky=W)
check_out_entry = Entry(app, textvariable=check_out_text)
check_out_entry.grid(row=1, column=3)

#username login
username_text = StringVar()
username_label = Label(app, text='Username', fg="blue",
                       font=('bold', 10), padx=20)
username_label.grid(row=0, column=8, sticky=W)
username_entry = Entry(app, textvariable=username_text)
username_entry.grid(row=0, column=9)

password_text = StringVar()
password_label = Label(app, text='Password', fg="blue",
                       font=('bold', 10), padx=20)
password_label.grid(row=1, column=8, sticky=W)
password_entry = Entry(app, show="*", textvariable=password_text)
password_entry.grid(row=1, column=9)

login_btn = Button(app, text='Login', fg="red", width=15, command=login)
login_btn.grid(row=2, column=9, pady=20)


# Room Details (Listbox)
room_list = Listbox(app, height=8, width=50, border=1)
room_list.grid(row=2, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)

# Set scroll to listbox
room_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=room_list.yview)

# Bind select
room_list.bind('<<ListboxSelect>>', select_item)

add_btn = Button(app, text='Add Room', width=15, command=add_item)
add_btn.grid(row=3, column=9)

remove_btn = Button(app, text='Delete Room', width=15, command=remove_item)
remove_btn.grid(row=4, column=9)

update_btn = Button(app, text='Update Room', width=15, command=update_item)
update_btn.grid(row=5, column=9)

clear_btn = Button(app, text='Clear', width=15, command=clear_text)
clear_btn.grid(row=6, column=9)

app.title("Gertion d'hotel")
app.geometry('750x350')

app.mainloop()