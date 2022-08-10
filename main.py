from cProfile import label
from cgitb import text
from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from view import *
from database import *




################# cores ###############
co0 = "#f0f3f5"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#ef5350"   # vermelha
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # sky blue


################# Janela Principal ###############

window = Tk()
window.title("pycrud")
window.geometry('1043x453')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)


################# Dividir Janela ##################
upper_frame = Frame(window, width=310, height=50, bg=co2, relief='flat')
upper_frame.grid(row=0, column=0)


lower_frame = Frame(window, width=310, height=403, bg=co1, relief='flat')
lower_frame.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)


form_frame = Frame(window, width=558, height=403, bg=co1, relief='flat')
form_frame.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)


################# Label Superior ##################
app_name = Label(upper_frame, text="Pycrud app", anchor=NW,font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_name.place(x=10, y=20)


# CLEAR FORM
def clear_data():
    e_name.delete(0, 'end')
    e_email.delete(0, 'end')
    e_phone.delete(0, 'end')
    e_bdate.delete(0, 'end')
    e_status.delete(0, 'end')
    e_details.delete(0, 'end')


    

# CRUD FUNCTIONS

global tree

# INSERT
def insert():
    name = e_name.get()
    email = e_email.get()
    phone = e_phone.get()
    bdate = e_bdate.get()
    status = e_status.get()
    details = e_details.get()

    insert_list = [name, email, phone, bdate, status, details]

    if name == '':
        messagebox.showerror('Error', 'name cannot be null!')
        
    else:
        insert_data(insert_list)
        messagebox.showinfo('Success!', 'Data was successfully saved.')

        clear_data()

    for widget in form_frame.winfo_children():
        widget.destroy()

    show_form()

# UPDATE
def update():
    try:
        treeview_data = tree.focus()
        treeview_dict = tree.item(treeview_data)

        tree_list = treeview_dict['values']

        values_id = tree_list[0]

        clear_data()

        e_name.insert(0, tree_list[1])
        e_email.insert(0, tree_list[2])
        e_phone.insert(0, tree_list[3])
        e_bdate.insert(0, tree_list[4])
        e_status.insert(0, tree_list[5])
        e_details.insert(0, tree_list[6])

        def update():
            name = e_name.get()
            email = e_email.get()
            phone = e_phone.get()
            bdate = e_bdate.get()
            status = e_status.get()
            details = e_details.get()

            update_list = [name, email, phone, bdate, status, details, values_id]

            

            if name == '':
                messagebox.showerror('Error', 'name cannot be null!')
                
            else:
                update_data(update_list)
                messagebox.showinfo('Success!', 'Data was successfully updated.')

                b_confirm.destroy()

                clear_data()



            for widget in form_frame.winfo_children():
                widget.destroy()

            show_form()

        b_confirm = Button(lower_frame,command=update, text="Confirm", width=10, bg=co2, fg=co1, font=('Ivy 7 bold'),   relief='raised', overrelief='ridge')
        b_confirm.place(x=105, y=380)

            

        show_form()

        
    except IndexError:
        messagebox.showerror('Error', 'Select a row to update.')


# DELETE
def delete():

    try:
        treeview_data = tree.focus()
        treeview_dict = tree.item(treeview_data)

        tree_list = treeview_dict['values']

        values_id = [tree_list[0]]

        delete_data(values_id)


        messagebox.showinfo('Success', 'Data was successfully deleted!')

        for widget in form_frame.winfo_children():
            widget.destroy()


        show_form()


    except IndexError:
        messagebox.showerror('Error', 'You must select a row to delete!')


    return
################# Label Inferior ##################

#Nome
label_name = Label(lower_frame, text="Name*", anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_name.place(x=10, y=10)


e_name = Entry(lower_frame, width=45, justify='left', relief='solid')
e_name.place(x=15, y=40)


# Email
label_email = Label(lower_frame, text="Email*", anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_email.place(x=10, y=70)


e_email = Entry(lower_frame, width=45, justify='left', relief='solid')
e_email.place(x=15, y=100)


# Telefone
label_phone = Label(lower_frame, text="Phone*", anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_phone.place(x=10, y=130)


e_phone = Entry(lower_frame, width=45, justify='left', relief='solid')
e_phone.place(x=15, y=160)


# Data_Nasc

label_bdate = Label(lower_frame, text="Birth Date*", anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_bdate.place(x=10, y=190)


e_bdate = DateEntry(lower_frame, width=12,background='black', foreground='grey', borderwidth=2)
e_bdate.place(x=15, y=220)


# Status
label_status = Label(lower_frame, text="Status*", anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_status.place(x=160, y=190)


e_status = Entry(lower_frame, width=20, justify='left', relief='solid')
e_status.place(x=160, y=220)


# Detalhes
label_details = Label(lower_frame, text="Details*", anchor=NW,font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
label_details.place(x=15, y=260)


e_details = Entry(lower_frame, width=45, justify='left', relief='solid')
e_details.place(x=15, y=290)



################# Botões ##################
button_insert = Button(lower_frame,command=insert, text="Insert", width=10, bg=co6, fg=co1, font=('Ivy 9 bold'),   relief='raised', overrelief='ridge')
button_insert.place(x=15, y=340)


button_update = Button(lower_frame,command=update, text="Update", width=10, bg=co2, fg=co1, font=('Ivy 9 bold'),   relief='raised', overrelief='ridge')
button_update.place(x=105, y=340)

button_delete = Button(lower_frame,command=delete, text="Delete", width=10, bg=co5, fg=co1, font=('Ivy 9 bold'),   relief='raised', overrelief='ridge')
button_delete.place(x=195, y=340)


################# CREDITOS ##################
label_details = Label(lower_frame, text="Developed by mikxingu", anchor=NW,font=('Ivy 10'), bg=co1, fg=co4, relief='flat')
label_details.place(x=15, y=380)



###############FRAME TREE #######################

def show_form():

    global tree 

    lista = read_data()
    
    tabela_head = ['ID','Name',  'Email','Phone', 'Birth Date', 'Status','Details']

    # criando a tabela
    tree = ttk.Treeview(form_frame, selectmode="extended", columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(form_frame, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar( form_frame, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    form_frame.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw","center","center"]
    h=[30,170,140,100,120,50,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)


show_form()

window.mainloop()