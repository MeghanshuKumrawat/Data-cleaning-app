from tkinter import *
from tkinter import ttk, messagebox, filedialog
import imdb
from datetime import datetime
from time import strftime
from pandastable import Table
from tkPDFViewer import tkPDFViewer as pdf
import pandas as pd



class Data:
    def __init__(self, root):
        self.root = root
        self.root.title("IMDB Movie Ratings")
        self.root.geometry("1100x600")
        self.root.config(bg="black")

        self.frame_step = 0
        self.main_function()

    def main_function(self):
        self.Upload_Frame = Frame(root, bd=1, background="light blue", relief=GROOVE)
        self.Upload_Frame.place(x=0, y=0, width=1100, height=600)
        Label(self.Upload_Frame, bg="light blue", text="Upload Dataset File", font=("arial", 25, 'bold')).place(x=400, y=100)
        Label(self.Upload_Frame, bg="light blue", text="(example : .csv, .xlsx, .xls)", font=("arial", 12)).place(x=450, y=150)
        frame = Frame(self.Upload_Frame, borderwidth=4, relief="groove")
        frame.place(x=150, y=200, width=800, height=300)
        ttk.Button(self.Upload_Frame, text="next", command=self.change_frame).place(x=1000, y=500)
        
        ttk.Button(frame, text="+", command=self.upload_file).place(x=150, y=200, width=500, height=50)

        self.Cleaning_Frame = Frame(root, bd=1, relief=GROOVE)
        self.Cleaning_Frame.place(x=0, y=0, width=1100, height=600)

        Data_Frame = Frame(self.Cleaning_Frame, bd=1, relief=GROOVE)
        Data_Frame.place(x=0, y=0, width=700, height=600)
        Label(self.Cleaning_Frame, bg="light blue", text="Cleaning_Frame").place(x=10, y=0)
        ttk.Button(self.Cleaning_Frame, text="next", command=self.change_frame).place(x=1000, y=500)
        data = pd.read_excel('C:\\Users\\hp\\Downloads\\Data Science Survey.xlsx')
        sheet = Table(Data_Frame, dataframe=data)
        sheet.show()
        sheet.place(x=0, y=0, width=700, height=600)
        Label(self.Cleaning_Frame, bg="light blue", text="Feature selection", font=("arial", 20)).place(x=800, y=0)
        list_Frame = Frame(self.Cleaning_Frame)
        list_Frame.place(x=725, y=50, width=350, height=300)
        yscrollbar = Scrollbar(list_Frame)
        yscrollbar.pack(side = RIGHT, fill = Y)
        columns_var = StringVar(value=list(data.columns))
        self.listbox = Listbox(list_Frame, selectmode = "multiple", yscrollcommand = yscrollbar.set, listvariable=columns_var)
        self.listbox.pack(padx = 10, pady = 10,
          expand = YES, fill = "both")
        

        self.Algo_Selection_Frame = Frame(root)
        self.Algo_Selection_Frame.place(x=0, y=0, width=1100, height=600)
        
        ttk.Button(self.Algo_Selection_Frame, text="next", command=self.change_frame).place(x=1000, y=500)
        supervised_frame = LabelFrame(self.Algo_Selection_Frame, text="Supervised")
        supervised_frame.place(x=50, y=30, width=300, height=220)
        Label(supervised_frame, text="Regression").place(x=10, y=10)        
        Checkbutton(supervised_frame, text="Multi reg").place(x=10, y=40)
        Checkbutton(supervised_frame, text="Logistic reg").place(x=10, y=70)
        Checkbutton(supervised_frame, text="Decicion tree").place(x=10, y=100)
        Checkbutton(supervised_frame, text="Ensamble").place(x=10, y=130)

        Label(supervised_frame, text="Classification").place(x=150, y=10)
        Checkbutton(supervised_frame, text="Logistic regression").place(x=150, y=40)
        Checkbutton(supervised_frame, text="KNN").place(x=150, y=70)
        Checkbutton(supervised_frame, text="Decision tree").place(x=150, y=100)
        Checkbutton(supervised_frame, text="SVM").place(x=150, y=130)
        Checkbutton(supervised_frame, text="Ensamble").place(x=150, y=160)

        unsupervised_frame = LabelFrame(self.Algo_Selection_Frame, text="Unsupervised")
        unsupervised_frame.place(x=380, y=30, width=300, height=100)
        Checkbutton(unsupervised_frame, text="Multi reg").place(x=10, y=30)
        Checkbutton(unsupervised_frame, text="Logistic reg").place(x=150, y=30)

        deep_learning_frame = LabelFrame(self.Algo_Selection_Frame, text="Deep learning")
        deep_learning_frame.place(x=710, y=30, width=300, height=100)
        Checkbutton(deep_learning_frame, text="Multi reg").place(x=10, y=30)
        Checkbutton(deep_learning_frame, text="Logistic reg").place(x=150, y=30)


        denension_reduchon_frame = LabelFrame(self.Algo_Selection_Frame, text="Denension reduchon")
        denension_reduchon_frame.place(x=380, y=150, width=300, height=100)
        Checkbutton(denension_reduchon_frame, text="Multi reg").place(x=10, y=30)
        Checkbutton(denension_reduchon_frame, text="Logistic reg").place(x=150, y=30)
        
        aartificial_inteligence_frame = LabelFrame(self.Algo_Selection_Frame, text="Aartificial inteligence")
        aartificial_inteligence_frame.place(x=710, y=150, width=300, height=100)
        m = Checkbutton(aartificial_inteligence_frame, text="Multi reg")
        m.place(x=10, y=30)
        m.select()
        l = Checkbutton(aartificial_inteligence_frame, text="Logistic reg").place(x=150, y=30)

        separator = ttk.Separator(self.Algo_Selection_Frame, orient='horizontal')
        separator.place(relx=0, rely=0.47, relwidth=1, relheight=1)

        self.Report_Frame = Frame(root, bd=1, background="red", relief=GROOVE)
        self.Report_Frame.place(x=0, y=0, width=1100, height=600)
        Label(self.Report_Frame, bg="light blue", text="Report_Frame").place(x=10, y=0)
        ttk.Button(self.Report_Frame, text="next", command=self.change_frame).place(x=1000, y=500)

        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(self.Report_Frame, pdf_location = r"C:\\Users\\hp\\Downloads\\Python List Practice Questions.pdf")
        v2.place(x=0, y=0, width=1100, height=500)

        self.frames = {}
        self.frames[0] = self.Upload_Frame
        self.frames[1] = self.Cleaning_Frame
        self.frames[2] = self.Algo_Selection_Frame
        self.frames[3] = self.Report_Frame

        self.change_frame()
        self.listbox.bind('<<ListboxSelect>>', self.items_selected)

    def change_frame(self):
        frame = self.frames[self.frame_step]
        frame.tkraise()
        self.frame_step += 1
        
    def items_selected(self, event):
        """ handle item selected event
        """
        # get selected indices
        selected_indices = self.listbox.curselection()
        # get selected items
        selected_langs = ",".join([self.listbox.get(i) for i in selected_indices])
        msg = f'You selected: {selected_langs}'

        print(msg)

    def upload_file(self):
        file = filedialog.askopenfile()


root = Tk()
ob = Data(root)
mainloop()