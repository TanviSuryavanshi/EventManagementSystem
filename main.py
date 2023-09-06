from tkinter import *
import Book
import CreateEvent
import ViewTickets
import ViewEvents
import CancelTicket

top = Tk()
top.geometry('600x500')
top.title('Event Management: CopyAssignment')

Button(top, text='Book Ticket', bg='blue', fg='white', width=12, font=('Arial', 18),
       command=lambda: Book.Book()).grid(row=0, column=0, padx=25, pady=30)
Button(top, text='Create Event', bg='blue', fg='white', width=12, font=('Arial', 18),
       command=lambda: CreateEvent.CreateEvent()).grid(row=0, column=1)
Button(top, text='View Tickets', bg='blue', fg='white', width=12, font=('Arial', 18),
       command=lambda: ViewTickets.ViewTickets()).grid(row=1, pady=20, column=0)
Button(top, text='View Events', bg='blue', fg='white', width=12, font=('Arial', 18),
       command=lambda: ViewEvents.ViewEvents()).grid(row=1, column=1)
Button(top, text='Cancel Ticket', bg='blue', fg='white', width=12, font=('Arial', 18),
       command=lambda: CancelTicket.CancelTicket()).grid(row=2, pady=25, column=0)
Button(top, text='Quit App', bg='blue', fg='white', width=12, font=('Arial', 18), command=lambda: top.destroy()).grid(
    row=2, column=1)

Label(top, text=' Welcome to Event Management System ', font=('Arial', 24)).grid(row=3, column=0, columnspan=2)
top.mainloop()
