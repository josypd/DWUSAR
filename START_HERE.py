'''
    @ GUI Implementation
    @ Class declaration of 'MainWindow'
    @ DWU Accommodation System
    @ Developers: Stafford Koki, Daniel Nelson, Louis Ronald
    @ Date: May, 2015
    @ Copyright (C) 2015
    @ DWU, Madang, Papua New Guinea.

    The 'MainWindow' class shows different screens e.g. LoginScreen, MainMenu, etc.
    based on user navigation and input. 
    
'''

#!/usr/bin/env python
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from GuiProperties import *
from MySqlAdapter import *


'''
root is defined and declared here first to allow for
control variables to be declared
'''
root = tk.Tk()





class MainWindow(tk.Frame):
    ''' declare all the control variables for text,entry widgets in gui'''
    #LoginScreen control variables (MainWindow Class in 'das_gui.py' source)
    LS_UsernameEntryCtrlVar = tk.StringVar()
    LS_PasswordEntryCtrlVar = tk.StringVar()

    #MainMenuScreen control variables (MainWindow Class in 'das_gui.py' source)
    MMS_WelcomeMsgUserTxtCtrlVar = tk.StringVar()
    MMS_WelcomeMsgSecLevelTxtCtrlVar = tk.StringVar()
    

    #StudentRecordsScreen control variables (MainWindow Class in 'das_gui.py' source)
    SAR_StudentIdEntryCtrlVar = tk.StringVar()
    SAR_FirstNameEntryCtrlVar = tk.StringVar()
    SAR_LastNameEntryCtrlVar = tk.StringVar()
    SAR_GenderEntryCtrlVar = tk.StringVar()

    SAR_DeptEntryCtrlVar = tk.StringVar()
    SAR_FacultyEntryCtrlVar = tk.StringVar()
    SAR_YearLevelEntryCtrlVar = tk.StringVar()
    SAR_DormTypeEntryCtrlVar = tk.StringVar()
    SAR_DormNameEntryCtrlVar = tk.StringVar()
    SAR_DormLocationEntryCtrlVar = tk.StringVar()
    SAR_RoomNoEntryCtrlVar = tk.StringVar()
    # note that the RoomMates text widget does not require a
    # control variable. Rather, it depends on widget-specific
    # functions that enable us to 'get' and 'set' its contents.

    #AdvancedSearchScreen control variables (MainWindow Class in 'das_gui.py' source)
    AS_StudentIdEntryCtrlVar = tk.StringVar()
    AS_FirstNameEntryCtrlVar = tk.StringVar()
    AS_LastNameEntryCtrlVar = tk.StringVar()
    AS_GenderEntryCtrlVar = tk.StringVar()

    AS_DeptEntryCtrlVar = tk.StringVar()
    AS_FacultyEntryCtrlVar = tk.StringVar()
    AS_YearLevelEntryCtrlVar = tk.StringVar()
    AS_DormTypeEntryCtrlVar = tk.StringVar()
    AS_DormNameEntryCtrlVar = tk.StringVar()
    AS_DormLocationEntryCtrlVar = tk.StringVar()
    AS_RoomNoEntryCtrlVar = tk.StringVar()


    #ReportsScreen control variables (MainWindow Class in 'das_gui.py' source)
    ''' at the moment, the 'ReportsScreen' does not have any form entry
        fields and thus, does not necessarily need control variables.
        However, if in future that control variables were needed to
        support any new form entry fields, let it be declared in this section
    '''

    #ChangePasswordScreen control variables (MainWindow Class in 'das_gui.py' source)
    CP_OldPasswordEntryCtrlVar = tk.StringVar()
    CP_NewPasswordEntryCtrlVar = tk.StringVar()

    #ReportResultsScreen control variables (MainWindow Class in 'das_gui.py' source)
    ''' I first assumed that I needed to create control variables for the following:
    RR_ReportSubtitleTtxtCtrlVar = tk.StringVar()
    RR_ReportDescriptionTxtCtrlVar = tk.StringVar()
    RR_ReportContentAreaEntryCtrlVar = tk.StringVar()

    However, it turns out that the first two are not entry fields but
    basically text label fields. Thus, they do no necessarily need
    control variables (it is also not a valid option). On the other hand,
    The content text widget does not also require a control variable since
    such feature is not supported by the widget itself. Rather, the program
    will make use of its widget-specific functions
    '''


    def __init__(self, parent):
        '''perform preliminary class configurations'''
        tk.Frame.__init__(self, parent)
        self.pack()
        self.parent = parent
        self.parent.geometry("600x700+100+30")
        self.parent.resizable(width=tk.FALSE,height=tk.FALSE)

        self.FormDefaultTtkWidgetStyle1 = ttk.Style()
        self.FormDefaultTtkWidgetStyle1.configure("TtkWidgetStyle1",foreground=FormDefaultWidgetTextColor,
                                                  background=FormDefaultWidgetColor)


    def LoginScreen(self):
        self.LS_UsernameEntryCtrlVar.set('')
        self.LS_PasswordEntryCtrlVar.set('')
        self.pack(fill=tk.BOTH,expand=tk.YES)
        self.parent.title('DWU Student Accommodation Registry - Please Login')
        self.MainCanvas = tk.Canvas(self,bg=DefaultCanvasColor)
        self.MainCanvas.pack(fill=tk.BOTH,expand=tk.YES)
        self.logo_filename = tk.PhotoImage(file="dwu_logo.png")
        self.logoImg = self.MainCanvas.create_image(300,220,image=self.logo_filename)
        self.systemTitle = self.MainCanvas.create_text(300,50,
                                                       text="\nDWU STUDENT ACCOMMODATION \n\t      REGISTRY",
                                                       fill=DefaultScreenTitleColor,
                                                       font=(DefaultScreenTitleFont,DefaultScreenTitleSize,
                                                             DefaultScreenTitleStyle),
                                                       anchor=tk.CENTER)
        self.LoginForm = tk.Frame(self.MainCanvas,bg='white')

        # LoginScreen 'Username' & 'Password' Entry Labels
        self.usernameLabel = tk.Label(self.LoginForm,text="Username: ",
                                              font=(LoginDefaultWidgetLabelFont,
                                              LoginDefaultWidgetLabelFontSize,
                                              LoginDefaultWidgetLabelFontStyle),
                                              bg=LoginDefaultWidgetLabelBackColor,
                                              fg=LoginDefaultWidgetLabelTextColor)
        self.passwordLabel = tk.Label(self.LoginForm,text="Password: ",
                                              font=(LoginDefaultWidgetLabelFont,
                                              LoginDefaultWidgetLabelFontSize,
                                              LoginDefaultWidgetLabelFontStyle),
                                              bg=LoginDefaultWidgetLabelBackColor,
                                              fg=LoginDefaultWidgetLabelTextColor)
        
        # LoginScreen 'Username' & 'Password' Entry fields
        self.usernameEntry = tk.Entry(self.LoginForm,bd=3,textvariable=MainWindow.LS_UsernameEntryCtrlVar,
                                                                font=(LoginDefaultEntryFont,
                                                                LoginDefaultEntryFontSize))
        self.passwordEntry = tk.Entry(self.LoginForm,bd=3,textvariable=MainWindow.LS_PasswordEntryCtrlVar,
                                                                font=(LoginDefaultEntryFont,
                                                                LoginDefaultEntryFontSize),show='*')

        # LoginScreen 'Login' and 'Cancel' Buttons
        self.loginButton = tk.Button(self.LoginForm,text='Login',font=(LoginDefaultEntryFont,
                                                                       LoginDefaultEntryFontSize),
                                     bg=LoginDefaultButtonColor,fg=LoginDefaultButtonTextColor,
                                     command=lambda: LS_LoginButton_onclick(self))
        self.cancelButton = tk.Button(self.LoginForm,text='Cancel',font=(LoginDefaultEntryFont,
                                                                         LoginDefaultEntryFontSize),
                                      bg=LoginDefaultButtonColor,fg=LoginDefaultButtonTextColor,
                                      command=lambda: LS_CancelButton_onclick(self))

        # geometrically position all widgets and create canvas window to hold all.
        self.usernameLabel.pack(padx=1,pady=1)
        self.usernameEntry.pack(padx=1,pady=1)
        self.passwordLabel.pack(padx=1,pady=1)
        self.passwordEntry.pack(padx=1,pady=10)
        self.loginButton.pack(side=tk.LEFT,padx=50,pady=10)
        self.cancelButton.pack(side=tk.LEFT,padx=50,pady=10)
        self.LoginWindow = self.MainCanvas.create_window(300,400,window=self.LoginForm,anchor=tk.CENTER)



    def MainMenuScreen(self):
        self.parent.title('DWU Student Accommodation Registry - Main Menu')
        self.MainCanvas = tk.Canvas(bg=DefaultCanvasColor)
        self.MainCanvas.pack(fill=tk.BOTH,expand=1)
        self.logo_filename = tk.PhotoImage(file="graphics\dwu_logo.png")
        self.logoImg = self.MainCanvas.create_image(100,100,image=self.logo_filename)
        self.systemTitle = self.MainCanvas.create_text(370,100,
                                                       text="Welcome to DWU Student\nAccommodation Registry",
                                                       fill=DefaultScreenTitleColor,
                                                       font=(DefaultScreenTitleFont,
                                                             DefaultScreenTitleSize),
                                                       anchor=tk.CENTER)
        self.systemSubTitle = self.MainCanvas.create_text(300,210,
                                                          text="MAIN MENU",
                                                          fill = DefaultScreenSub1TitleColor,
                                                          font= (DefaultScreenSub1TitleFont,
                                                                DefaultScreenSub1TitleSize,
                                                                DefaultScreenSub1TitleStyle),
                                                          anchor=tk.CENTER)
        self.userWelcomeMsg = self.MainCanvas.create_text(350,10,text=self.MMS_WelcomeMsgUserTxtCtrlVar.get(),fill='Black',font=('Tw Cen MT',12,'bold'))
        self.userSecurityLevelMsg = self.MainCanvas.create_text(470,10,text=self.MMS_WelcomeMsgSecLevelTxtCtrlVar.get(),fill='Black',
                                                                font=('Tw Cen Mt',12,'bold'))
        self.MainMenu = tk.Frame(self.MainCanvas,bg=DefaultFrameColor)

        # Main Menu Button Widgets declared here
        self.button1 = tk.Button(self.MainMenu,text='Student Accommodation Records',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=lambda: MM_StdAccRecButton_onclick(self))
        '''
        self.button2 = tk.Button(self.MainMenu,text='Advanced Search & Query',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=lambda: MM_AdvSrchButton_onclick(self))
        self.button3 = tk.Button(self.MainMenu,text='Ready-made Reports',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=lambda: MM_ReportsButton_onclick(self))
        '''
        self.button4 = tk.Button(self.MainMenu,text='Log-out',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=lambda: MM_LogOutButton_onclick(self))
        self.button5 = tk.Button(self.MainMenu,text='Exit',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=lambda: MM_ExitButton_onclick(self))        
        self.button6 = tk.Button(self.MainMenu,text='Change Password',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=lambda: MM_ChangePwdButton_onclick(self))

        # geometrically position all widgets (esp. buttons) and
        # create canvas window to accommodate them all.
        self.button6.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        self.button5.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        self.button4.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        '''
        self.button3.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        self.button2.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        '''
        self.button1.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        self.MainMenuWindow = self.MainCanvas.create_window(300,400,window=self.MainMenu,anchor=tk.CENTER)
        
    def StudentRecordsScreen(self):
        self.parent.title('DWU Student Accommodation Registry - Student Accommodation Records')
        self.MainCanvas = tk.Canvas(bg=DefaultCanvasColor)
        self.MainCanvas.pack(fill=tk.BOTH,expand=1)
        self.logo_filename = tk.PhotoImage(file="graphics\dwu_logo.png")
        self.logoImg = self.MainCanvas.create_image(100,100,image=self.logo_filename)
        self.systemTitle = self.MainCanvas.create_text(370,100,
                                                       text="Welcome to DWU Student\nAccommodation Registry",
                                                       fill=DefaultScreenTitleColor,
                                                       font=(DefaultScreenTitleFont,
                                                             DefaultScreenTitleSize),
                                                       anchor=tk.CENTER)
        self.systemSubTitle = self.MainCanvas.create_text(376,160,
                                                          text="Student Accommodation Records",
                                                          fill = DefaultScreenSub1TitleColor,
                                                          font=(DefaultScreenSub1TitleFont,
                                                                DefaultScreenSub1TitleSize,
                                                                DefaultScreenSub1TitleStyle),
                                                          anchor=tk.CENTER)
        self.EntryForm = tk.Frame(bg=DefaultFrameColor)


        # Ttk Widget Styles Local Definitions
        FormDefaultTtkWidgetStyle1 = ttk.Style()
        FormDefaultTtkWidgetStyle1.configure("TtkWidgetStyle1",foreground=FormDefaultWidgetTextColor,
                                             background=FormDefaultWidgetColor)

        # create row frames that will hold each field (widget and label pair) related
        # to a particular record
        self.row1 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row2 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row3 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row4 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row5 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row6 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row7 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row8 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row9 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row10 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row11 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row12 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        
        self.row1.pack(side=tk.TOP,anchor=tk.W)
        self.row2.pack(side=tk.TOP,anchor=tk.W)
        self.row3.pack(side=tk.TOP,anchor=tk.W)
        self.row4.pack(side=tk.TOP,anchor=tk.W)
        self.row5.pack(side=tk.TOP,anchor=tk.W)
        self.row6.pack(side=tk.TOP,anchor=tk.W)
        self.row7.pack(side=tk.TOP,anchor=tk.W)
        self.row8.pack(side=tk.TOP,anchor=tk.W)
        self.row9.pack(side=tk.TOP,anchor=tk.W)
        self.row10.pack(side=tk.TOP,anchor=tk.W)
        self.row11.pack(side=tk.TOP,anchor=tk.W)
        self.row12.pack(side=tk.TOP,anchor=tk.W)

                
        # Entry form widgets declared here along with their labels
        self.stdIdEntry = tk.Entry(self.row1,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.SAR_StudentIdEntryCtrlVar)
        self.stdFirstnameEntry = tk.Entry(self.row2,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.SAR_FirstNameEntryCtrlVar)
        self.stdLastnameEntry = tk.Entry(self.row3,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.SAR_LastNameEntryCtrlVar)
        self.stdGenderSelection = ttk.Combobox(self.row4,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.SAR_GenderEntryCtrlVar)
        
        self.stdDeptSelection = ttk.Combobox(self.row5,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.SAR_DeptEntryCtrlVar)
        self.stdFacSelection = ttk.Combobox(self.row6,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.SAR_FacultyEntryCtrlVar)
        self.stdYearLevelSelection = ttk.Combobox(self.row7,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.SAR_YearLevelEntryCtrlVar)
        self.stdDormNameSelection = ttk.Combobox(self.row8,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.SAR_DormNameEntryCtrlVar)
        self.stdRoomNoEntry = tk.Entry(self.row9,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.SAR_RoomNoEntryCtrlVar)
        self.stdRoomMatesDisplay = tk.Text(self.row10,
                                    font=(FormDefaultWidgetFont,
                                          FormDefaultWidgetFontSize),height=4,width=FormDefaultWidgetWidth)
                                           
        # set values for selection comboboxes declared above
        self.stdGenderSelection['value']=('M','F')
        rslt = db.execute("SELECT * FROM department")
        depts = []
        for dept in rslt:
            depts.append(dept[1])
        self.stdDeptSelection['value']=depts

        rslt = db.execute("SELECT * FROM faculty")
        facs = []
        for fac in rslt:
            facs.append(fac[1])
        self.stdFacSelection['value'] = facs

        rslt = db.execute("SELECT * FROM year_level")
        yearlevels = []
        for yearlevel in rslt:
            yearlevels.append(yearlevel[1])
        self.stdYearLevelSelection['value'] = yearlevels

        rslt = db.execute("SELECT * FROM dorm")
        dorms = []
        for dorm in rslt:
            dorms.append(dorm[1])
        self.stdDormNameSelection['value'] = dorms


        self.label_stdIdEntry = tk.Label(self.row1,text="Student ID     ",bg=FormDefaultLabelColor,
                                         fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdFirstnameEntry = tk.Label(self.row2,text="First Name     ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdLastnameEntry = tk.Label(self.row3,text="Last Name     ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdGenderSelection = tk.Label(self.row4,text="Gender          ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdDeptSelection = tk.Label(self.row5,text="Department   ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdFacSelection = tk.Label(self.row6,text="Faculty          ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdYearLevelSelection = tk.Label(self.row7,text="Year Level     ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdDormNameSelection = tk.Label(self.row8,text="Dorm Name   ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdRoomNoEntry = tk.Label(self.row9,text="Room No        ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdRoomMatesDisplay = tk.Label(self.row10,text="Room Mates   ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))

        
        # geometrically position all widgets (esp. entry, buttons) and
        # create canvas window to accommodate them all.

        self.label_stdIdEntry.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdFirstnameEntry.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdLastnameEntry.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdGenderSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdDeptSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdFacSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdYearLevelSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdDormNameSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdRoomNoEntry.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdRoomMatesDisplay.pack(side=tk.LEFT,anchor=tk.W)
        
        self.stdIdEntry.pack(side=tk.LEFT)
        self.stdFirstnameEntry.pack(side=tk.LEFT)
        self.stdLastnameEntry.pack(side=tk.LEFT)
        self.stdGenderSelection.pack(side=tk.LEFT)
        self.stdDeptSelection.pack(side=tk.LEFT)
        self.stdFacSelection.pack(side=tk.LEFT)
        self.stdYearLevelSelection.pack(side=tk.LEFT)
        self.stdDormNameSelection.pack(side=tk.LEFT)
        self.stdRoomNoEntry.pack(side=tk.LEFT)
        self.stdRoomMatesDisplay.pack(side=tk.LEFT)
        
        self.EntryFormWindow = self.MainCanvas.create_window(300,420,window=self.EntryForm,anchor=tk.CENTER)

        # create navigation panel at bottom of screen
        self.NavPanelBottom = tk.Frame(self.MainCanvas,bg=DefaultFrameColor,height=45,width=550)
        self.NavPanelBottom.pack(side=tk.BOTTOM,pady=7)

        # create buttons for navigation panel at bottom of screen

        
        butt_SaveChanges = tk.Button(self.NavPanelBottom,text='Save Changes',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: SR_SaveChangesButton_onclick(self))
        butt_UpdateChanges = tk.Button(self.NavPanelBottom,text='Update',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: SR_UpdateChangesButton_onclick(self))
        butt_New = tk.Button(self.NavPanelBottom,text='New',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: SR_NewButton_onclick(self))
        butt_Delete = tk.Button(self.NavPanelBottom,text='Delete',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: SR_DeleteButton_onclick(self))
        butt_Cancel = tk.Button(self.NavPanelBottom,text='Cancel',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: SR_CancelButton_onclick(self))
        butt_SearchStudent = tk.Button(self.NavPanelBottom,text='Search Student',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: SR_SearchStudent_onclick(self))

        # instantiate all the buttons on-screen
        butt_SaveChanges.pack(side=tk.LEFT)
        butt_UpdateChanges.pack(side=tk.LEFT)
        butt_New.pack(side=tk.LEFT)
        butt_Delete.pack(side=tk.LEFT)
        butt_Cancel.pack(side=tk.LEFT)
        butt_SearchStudent.pack(side=tk.LEFT)




        
    def AdvancedSearchScreen(self):
        self.parent.title('DWU Student Accommodation Registry - Advanced Search & Query')
        self.MainCanvas = tk.Canvas(bg=DefaultCanvasColor)
        self.MainCanvas.pack(fill=tk.BOTH,expand=1)
        self.logo_filename = tk.PhotoImage(file="graphics\dwu_logo.png")
        self.logoImg = self.MainCanvas.create_image(100,100,image=self.logo_filename)
        self.systemTitle = self.MainCanvas.create_text(370,100,
                                                       text="Welcome to DWU Student\nAccommodation Registry",
                                                       fill=DefaultScreenTitleColor,
                                                       font=(DefaultScreenTitleFont,
                                                             DefaultScreenTitleSize),
                                                       anchor=tk.CENTER)
        self.systemSubTitle = self.MainCanvas.create_text(340,160,
                                                          text="Advanced Search & Query",
                                                          fill = DefaultScreenSub1TitleColor,
                                                          font=(DefaultScreenSub1TitleFont,
                                                                DefaultScreenSub1TitleSize,
                                                                DefaultScreenSub1TitleStyle),
                                                          anchor=tk.CENTER)
        self.EntryForm = tk.Frame(bg=DefaultFrameColor)


        # Ttk Widget Styles Local Definitions
        FormDefaultTtkWidgetStyle1 = ttk.Style()
        FormDefaultTtkWidgetStyle1.configure("TtkWidgetStyle1",foreground=FormDefaultWidgetTextColor,
                                             background=FormDefaultWidgetColor)

        # create row frames that will hold each field (widget and label pair) related
        # to a particular record
        self.row1 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row2 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row3 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row4 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row5 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row6 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row7 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row8 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row9 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row10 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row11 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        
        self.row1.pack(side=tk.TOP,anchor=tk.W)
        self.row2.pack(side=tk.TOP,anchor=tk.W)
        self.row3.pack(side=tk.TOP,anchor=tk.W)
        self.row4.pack(side=tk.TOP,anchor=tk.W)
        self.row5.pack(side=tk.TOP,anchor=tk.W)
        self.row6.pack(side=tk.TOP,anchor=tk.W)
        self.row7.pack(side=tk.TOP,anchor=tk.W)
        self.row8.pack(side=tk.TOP,anchor=tk.W)
        self.row9.pack(side=tk.TOP,anchor=tk.W)
        self.row10.pack(side=tk.TOP,anchor=tk.W)
        self.row11.pack(side=tk.TOP,anchor=tk.W)

                
        # Entry form widgets declared here along with their labels
        self.stdIdEntry = tk.Entry(self.row1,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.AS_StudentIdEntryCtrlVar)
        self.stdFirstnameEntry = tk.Entry(self.row2,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.AS_FirstNameEntryCtrlVar)
        self.stdLastnameEntry = tk.Entry(self.row3,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.AS_LastNameEntryCtrlVar)
        self.stdGenderSelection = ttk.Combobox(self.row4,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.AS_GenderEntryCtrlVar)
        self.stdDeptSelection = ttk.Combobox(self.row5,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.AS_DeptEntryCtrlVar)
        self.stdFacSelection = ttk.Combobox(self.row6,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.AS_FacultyEntryCtrlVar)
        self.stdYearLevelSelection = ttk.Combobox(self.row7,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.AS_YearLevelEntryCtrlVar)
        self.stdDormNameSelection = ttk.Combobox(self.row8,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.AS_DormNameEntryCtrlVar)
        self.stdRoomNoEntry = tk.Entry(self.row9,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),
                                   textvariable=MainWindow.AS_RoomNoEntryCtrlVar)


        # set values for selection comboboxes declared above
        self.stdGenderSelection['value']=('M','F')
        rslt = db.execute("SELECT * FROM department")
        depts = []
        for dept in rslt:
            depts.append(dept[1])
        self.stdDeptSelection['value']=depts

        rslt = db.execute("SELECT * FROM faculty")
        facs = []
        for fac in rslt:
            facs.append(fac[1])
        self.stdFacSelection['value'] = facs

        rslt = db.execute("SELECT * FROM year_level")
        yearlevels = []
        for yearlevel in rslt:
            yearlevels.append(yearlevel[1])
        self.stdYearLevelSelection['value'] = yearlevels

        rslt = db.execute("SELECT * FROM dorm")
        dorms = []
        for dorm in rslt:
            dorms.append(dorm[1])
        self.stdDormNameSelection['value'] = dorms






        self.label_stdIdEntry = tk.Label(self.row1,text="Student ID     ",bg=FormDefaultLabelColor,
                                         fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdFirstnameEntry = tk.Label(self.row2,text="First Name     ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdLastnameEntry = tk.Label(self.row3,text="Last Name     ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdGenderSelection = tk.Label(self.row4,text="Gender          ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdDeptSelection = tk.Label(self.row5,text="Department   ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdFacSelection = tk.Label(self.row6,text="Faculty          ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdYearLevelSelection = tk.Label(self.row7,text="Year Level     ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdDormNameSelection = tk.Label(self.row8,text="Dorm Name   ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_stdRoomNoEntry = tk.Label(self.row9,text="Room No        ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))

        
        # geometrically position all widgets (esp. entry, buttons) and
        # create canvas window to accommodate them all.

        self.label_stdIdEntry.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdFirstnameEntry.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdLastnameEntry.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdGenderSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdDeptSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdFacSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdYearLevelSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdDormNameSelection.pack(side=tk.LEFT,anchor=tk.W)
        self.label_stdRoomNoEntry.pack(side=tk.LEFT,anchor=tk.W)
        
        self.stdIdEntry.pack(side=tk.LEFT)
        self.stdFirstnameEntry.pack(side=tk.LEFT)
        self.stdLastnameEntry.pack(side=tk.LEFT)
        self.stdGenderSelection.pack(side=tk.LEFT)
        self.stdDeptSelection.pack(side=tk.LEFT)
        self.stdFacSelection.pack(side=tk.LEFT)
        self.stdYearLevelSelection.pack(side=tk.LEFT)
        self.stdDormNameSelection.pack(side=tk.LEFT)
        self.stdRoomNoEntry.pack(side=tk.LEFT)
        
        self.EntryFormWindow = self.MainCanvas.create_window(300,420,window=self.EntryForm,anchor=tk.CENTER)

        # create navigation panel at bottom of screen
        self.NavPanelBottom = tk.Frame(self.MainCanvas,bg=DefaultFrameColor,height=45,width=550)
        self.NavPanelBottom.pack(side=tk.BOTTOM,pady=7)

        # create buttons for navigation panel at bottom of screen

        
        butt_Search = tk.Button(self.NavPanelBottom,text='Search',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: AS_SearchButton_onclick(self))
        butt_Cancel = tk.Button(self.NavPanelBottom,text='Cancel',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: AS_CancelButton_onclick(self))


        # instantiate all the buttons on-screen
        butt_Search.pack(side=tk.LEFT)
        butt_Cancel.pack(side=tk.LEFT)
    
    def ReportsScreen(self):
        self.parent.title('DWU Student Accommodation Registry - Ready-made Reports')
        self.MainCanvas = tk.Canvas(bg=DefaultCanvasColor)
        self.MainCanvas.pack(fill=tk.BOTH,expand=1)
        self.logo_filename = tk.PhotoImage(file="graphics\dwu_logo.png")
        self.logoImg = self.MainCanvas.create_image(100,100,image=self.logo_filename)
        self.systemTitle = self.MainCanvas.create_text(370,100,
                                                       text="Welcome to DWU Student\nAccommodation Registry",
                                                       fill=DefaultScreenTitleColor,
                                                       font=(DefaultScreenTitleFont,
                                                             DefaultScreenTitleSize),
                                                       anchor=tk.CENTER)
        self.systemSubTitle = self.MainCanvas.create_text(300,210,
                                                          text="READY-MADE REPORTS",
                                                          fill = DefaultScreenSub1TitleColor,
                                                          font=(DefaultScreenSub1TitleFont,
                                                                DefaultScreenSub1TitleSize,
                                                                DefaultScreenSub1TitleStyle),
                                                          anchor=tk.CENTER)
        self.MainMenu = tk.Frame(self.MainCanvas,bg=DefaultFrameColor)

        # Main Menu Button Widgets declared here
        self.button1 = tk.Button(self.MainMenu,text='All Female Occupants',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=RS_AllFemaleOccupantsButton_onclick)
        self.button2 = tk.Button(self.MainMenu,text='All Male Occupants',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=RS_AllMaleOccupantsButton_onclick)
        self.button3 = tk.Button(self.MainMenu,text='All Paramed-Campus Occupants',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=RS_AllParaCampusOccupantsButton_onclick)
        self.button4 = tk.Button(self.MainMenu,text='All Main-Campus Occupants',
                                 font=(MenuDefaultButtonFonts,MenuDefaultButtonFontSize),
                                 bg=MenuDefaultButtonColor,fg=MenuDefaultButtonTextColor,
                                 width=MenuDefaultButtonWidth,
                                 command=RS_AllMainCampusOccupantsButton_onclick)

        # geometrically position all widgets (esp. buttons) and
        # create canvas window to accommodate them all.
        self.button4.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        self.button3.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        self.button2.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        self.button1.pack(side=tk.BOTTOM,padx=MenuDefaultButtonPadx,pady=MenuDefaultButtonPady)
        self.MainMenuWindow = self.MainCanvas.create_window(300,400,window=self.MainMenu,anchor=tk.CENTER)
        
    def ChangePasswordScreen(self):
        CP_OldPasswordEntrySetContents('')
        CP_NewPasswordEntrySetContents('')
        self.parent.title('DWU Student Accommodation Registry - Change Password')
        self.MainCanvas = tk.Canvas(bg=DefaultCanvasColor)
        self.MainCanvas.pack(fill=tk.BOTH,expand=1)
        self.logo_filename = tk.PhotoImage(file="graphics\dwu_logo.png")
        self.logoImg = self.MainCanvas.create_image(100,100,image=self.logo_filename)
        self.systemTitle = self.MainCanvas.create_text(370,100,
                                                       text="Welcome to DWU Student\nAccommodation Registry",
                                                       fill=DefaultScreenTitleColor,
                                                       font=(DefaultScreenTitleFont,
                                                             DefaultScreenTitleSize),
                                                       anchor=tk.CENTER)
        self.systemSubTitle = self.MainCanvas.create_text(340,160,
                                                          text="CHANGE PASSWORD",
                                                          fill = DefaultScreenSub1TitleColor,
                                                          font=(DefaultScreenSub1TitleFont,
                                                                DefaultScreenSub1TitleSize,
                                                                DefaultScreenSub1TitleStyle),
                                                          anchor=tk.CENTER)
        self.EntryForm = tk.Frame(bg=DefaultFrameColor)


        # Ttk Widget Styles Local Definitions
        FormDefaultTtkWidgetStyle1 = ttk.Style()
        FormDefaultTtkWidgetStyle1.configure("TtkWidgetStyle1",foreground=FormDefaultWidgetTextColor,
                                             background=FormDefaultWidgetColor)

        # create row frames that will hold each field (widget and label pair) related
        # to a particular record
        self.row1 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        self.row2 = tk.Frame(self.EntryForm,pady=3,bg=DefaultFrameColor)
        
        self.row1.pack(side=tk.TOP,anchor=tk.W)
        self.row2.pack(side=tk.TOP,anchor=tk.W)

                
        # Entry form widgets declared here along with their labels
        self.oldPwdEntry = tk.Entry(self.row1,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),show='*',
                                    textvariable=MainWindow.CP_OldPasswordEntryCtrlVar)
        self.newPwdEntry = tk.Entry(self.row2,bg=FormDefaultWidgetColor,
                                   fg=FormDefaultWidgetTextColor,
                                   font=(FormDefaultWidgetFont,
                                         FormDefaultWidgetFontSize),show='*',
                                    textvariable=MainWindow.CP_NewPasswordEntryCtrlVar)


        self.label_oldPwdEntry = tk.Label(self.row1,text="Old Password     ",bg=FormDefaultLabelColor,
                                         fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))
        self.label_newPwdEntry = tk.Label(self.row2,text="New Password     ",bg=FormDefaultLabelColor,
                                                fg=FormDefaultLabelTextColor,
                                         font=(FormDefaultLabelFont,
                                               FormDefaultLabelFontSize))

        
        # geometrically position all widgets (esp. entry, buttons) and
        # create canvas window to accommodate them all.

        self.label_oldPwdEntry.pack(side=tk.LEFT,anchor=tk.W)
        self.label_newPwdEntry.pack(side=tk.LEFT,anchor=tk.W)
        
        self.oldPwdEntry.pack(side=tk.LEFT)
        self.newPwdEntry.pack(side=tk.LEFT)
        
        self.EntryFormWindow = self.MainCanvas.create_window(300,420,window=self.EntryForm,anchor=tk.CENTER)

        # create navigation panel at bottom of screen
        self.NavPanelBottom = tk.Frame(self.MainCanvas,bg=DefaultFrameColor,height=45,width=550)
        self.NavPanelBottom.pack(side=tk.BOTTOM,pady=7)

        # create buttons for navigation panel at bottom of screen

        
        butt_ChangePwd = tk.Button(self.NavPanelBottom,text='Change',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: CP_ChangeButton_onclick(self))
        butt_Cancel = tk.Button(self.NavPanelBottom,text='Cancel',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=lambda: CP_CancelButton_onclick(self))


        # instantiate all the buttons on-screen
        butt_ChangePwd.pack(side=tk.LEFT)
        butt_Cancel.pack(side=tk.LEFT)

    def ReportResultsScreen(self,subtitle="Unknown",description="Unknown",resultcontent="Unknown"):
        self.pack(fill=tk.BOTH,expand=tk.YES)
        self.title = "DWU Student Accommodation\nRecords Report"
        self.subtitle = subtitle
        self.description = description
        self.resultcontent = resultcontent
        self.parent.geometry("900x600+300+300")
        self.parent.title(self.title+" - "+self.subtitle)

        # create window widgets & contents and display them
        # first create main canvas
        self.MainCanvas = tk.Canvas(self,bg=DefaultCanvasColor,width=900,height=600)
        self.MainCanvas.pack(fill=tk.BOTH,expand=tk.YES)
        self.logo_filename = tk.PhotoImage(file="graphics\dwu_logo.png")
        self.logoImg = self.MainCanvas.create_image(100,100,image=self.logo_filename)
        
        self.ReportTitle = self.MainCanvas.create_text(385,100,
                                                       text=self.title,
                                                       fill=DefaultScreenTitleColor,
                                                       font=(DefaultScreenTitleFont,
                                                             DefaultScreenTitleSize),
                                                       anchor=tk.CENTER)
        self.ReportSubTitle = self.MainCanvas.create_text(450,210,
                                                          text=self.subtitle,
                                                          fill = DefaultScreenSub1TitleColor,
                                                          font=(DefaultScreenSub1TitleFont,
                                                                DefaultScreenSub1TitleSize,
                                                                DefaultScreenSub1TitleStyle),
                                                          anchor=tk.CENTER)
        self.ReportDescription = self.MainCanvas.create_text(450,245,
                                                             text=self.description,
                                                             fill=DefaultScreenDescriptionColor,
                                                             font=(DefaultScreenDescriptionFont,
                                                                   DefaultScreenDescriptionSize,
                                                                   DefaultScreenDescriptionStyle),
                                                             anchor=tk.CENTER)
        
        # create main content area with scrollbar functionality
        self.MainContentFrame = tk.Frame(bg="black")
        self.MainTextArea = tk.Text(self.MainContentFrame,height=16,width=108,bg='#ddffaa')
        
        self.MainTextAreaScrollBarY = tk.Scrollbar(self.MainContentFrame,command=self.MainTextArea.yview)
        self.MainTextArea.configure(yscrollcommand=self.MainTextAreaScrollBarY.set)
        
        self.MainTextArea.pack(side=tk.LEFT)
        self.MainTextAreaScrollBarY.pack(side=tk.RIGHT,fill=tk.Y)
        self.MainCanvas.create_window(10,400,window=self.MainContentFrame,anchor=tk.W)

        # create navigation panel at bottom of screen
        self.NavPanelBottom = tk.Frame(self.MainCanvas,bg=DefaultFrameColor,height=45,width=550)
        self.NavPanelBottom.pack(side=tk.BOTTOM,pady=3)

        # create buttons for navigation panel at bottom of screen

        
        butt_ExportToTxt = tk.Button(self.NavPanelBottom,text='Export to Txt',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=RRS_ExportToTxtButton_onclick)
        butt_ExportToPdf = tk.Button(self.NavPanelBottom,text='Export to PDF',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=RRS_ExportToPdfButton_onclick)
        butt_Cancel = tk.Button(self.NavPanelBottom,text='Cancel',
                                 font=(FormDefaultNavButt1Font,FormDefaultNavButt1FontSize),
                                 bg=FormDefaultNavButt1BackColor,fg=FormDefaultNavButt1TextColor,
                                 width=FormDefaultNavButt1Width,
                                 command=RRS_CancelButton_onclick)

        # instantiate all the buttons on-screen
        butt_ExportToTxt.pack(side=tk.LEFT)
        butt_ExportToPdf.pack(side=tk.LEFT)
        butt_Cancel.pack(side=tk.LEFT)









        
''' declare all the content manipulation functions for this gui class'''
# LoginScreen (in MainWindow Class file) Content Setter & Getter Methods
def LS_UsernameEntryGetContents(self):
    return MainWindow.LS_UsernameEntryCtrlVar.get()
def LS_PasswordEntryGetContents(self):
    return MainWindow.LS_PasswordEntryCtrlVar.get()
def LS_UsernameEntrySetContents(self,setStr):
    self.LS_UsernameEntryCtrlVar.set(setStr)
def LS_PasswordEntrySetContents(self,setStr):
    self.LS_PasswordEntryCtrlVar.set(setStr)

# MainMenuScreen (in MainWindow class file) Content Setter & Getter Methods
'''note that there are no text entry elements in the MainMenuScreen
   that will require setter and getter methods
'''



# StudentRecordsScreen (in MainWindow Class file) Content Setter & Getter Methods
def SR_StudentIdEntryGetContents(self):
    return self.SAR_StudentIdEntryCtrlVar.get()
def SR_FirstNameEntryGetContents(self):
    return self.SAR_FirstNameEntryCtrlVar.get()
def SR_LastNameEntryGetContents(self):
    return self.SAR_LastNameEntryCtrlVar.get()
def SR_GenderEntryGetContents(self):
    return self.SAR_GenderEntryCtrlVar.get()
def SR_DepartmentEntryGetContents(self):
    return self.SAR_DeptEntryCtrlVar.get()
def SR_FacultyEntryGetContents(self):
    return self.SAR_FacultyEntryCtrlVar.get()
def SR_YearLevelEntryGetContents(self):
    return self.SAR_YearLevelEntryCtrlVar.get()
def SR_DormTypeEntryGetContents(self):
    return self.SAR_DormTypeEntryCtrlVar.get()
def SR_DormNameEntryGetContents(self):
    return self.SAR_DormNameEntryCtrlVar.get()
def SR_DormLocationEntryGetContents(self):
    return self.SAR_DormLocationEntryCtrlVar.get()
def SR_RoomNoEntryGetContents(self):
    return self.SAR_RoomNoEntryCtrlVar.get()
def SR_RoomMatesEntryGetContents(self):
    return self.SAR_RoomMatesEntryCtrlVar.get()


def SR_StudentIdEntrySetContents(self,setStr):
    self.SAR_StudentIdEntryCtrlVar.set(setStr)
def SR_FirstNameEntrySetContents(self,setStr):
    self.SAR_FirstNameEntryCtrlVar.set(setStr)
def SR_LastNameEntrySetContents(self,setStr):
    self.SAR_LastNameEntryCtrlVar.set(setStr)
def SR_GenderEntrySetContents(self,setStr):
    self.SAR_GenderEntryCtrlVar.set(setStr)
def SR_DepartmentEntrySetContents(self,setStr):
    self.SAR_DeptEntryCtrlVar.set(setStr)
def SR_FacultyEntrySetContents(self,setStr):
    self.SAR_FacultyEntryCtrlVar.set(setStr)
def SR_YearLevelEntrySetContents(self,setStr):
    self.SAR_YearLevelEntryCtrlVar.set(setStr)
def SR_DormTypeEntrySetContents(self,setStr):
    self.SAR_DormTypeEntryCtrlVar.set(setStr)
def SR_DormNameEntrySetContents(self,setStr):
    self.SAR_DormNameEntryCtrlVar.set(setStr)
def SR_DormLocationEntrySetContents(self,setStr):
    self.SAR_DormLocationEntryCtrlVar.set(setStr)
def SR_RoomNoEntrySetContents(self,setStr):
    self.SAR_RoomNoEntryCtrlVar.set(setStr)
def SR_RoomMatesEntrySetContents(self,setStr):
    # does not support control variable.
    # manipulating widget content is done using
    # widget-specific functions.
    self.stdRoomMatesDisplay.delete("1.0",tk.END)
    self.stdRoomMatesDisplay.insert("1.0",setStr)
                            


# AdvancedSearchScreen (in MainWindow Class file) Content Setter & Getter Methods
def AS_StudentIdEntryGetContents(self):
    return self.AS_StudentIdEntryCtrlVar.get()
def AS_FirstNameEntryGetContents(self):
    return self.AS_FirstNameEntryCtrlVar.get()
def AS_LastNameEntryGetContents(self):
    return self.AS_LastNameEntryCtrlVar.get()
def AS_GenderEntryGetContents(self):
    return self.AS_GenderEntryCtrlVar.get()
def AS_DepartmentEntryGetContents(self):
    return self.AS_DeptEntryCtrlVar.get()
def AS_FacultyEntryGetContents(self):
    return self.AS_FacultyEntryCtrlVar.get()
def AS_YearLevelEntryGetContents(self):
    return self.AS_YearLevelEntryCtrlVar.get()
def AS_DormTypeEntryGetContents(self):
    return self.AS_DormTypeEntryCtrlVar.get()
def AS_DormNameEntryGetContents(self):
    return self.AS_DormNameEntryCtrlVar.get()
def AS_DormLocationEntryGetContents(self):
    return self.AS_DormLocationEntryCtrlVar.get()
def AS_RoomNoEntryGetContents(self):
    return self.AS_RoomNoEntryCtrlVar.get()


def AS_StudentIdEntrySetContents(self,setStr):
    self.AS_StudentIdEntryCtrlVar.set(setStr)
def AS_FirstNameEntrySetContents(self,setStr):
    self.AS_FirstNameEntryCtrlVar.set(setStr)
def AS_LastNameEntrySetContents(self,setStr):
    self.AS_LastNameEntryCtrlVar.set(setStr)
def AS_GenderEntrySetContents(self,setStr):
    self.AS_GenderEntryCtrlVar.set(setStr)
def AS_DepartmentEntrySetContents(self,setStr):
    self.AS_DeptEntryCtrlVar.set(setStr)
def AS_FacultyEntrySetContents(self,setStr):
    self.AS_FacultyEntryCtrlVar.set(setStr)
def AS_YearLevelEntrySetContents(self,setStr):
    self.AS_YearLevelEntryCtrlVar.set(setStr)
def AS_DormTypeEntrySetContents(self,setStr):
    self.AS_DormTypeEntryCtrlVar.set(setStr)
def AS_DormNameEntrySetContents(self,setStr):
    self.AS_DormNameEntryCtrlVar.set(setStr)
def AS_DormLocationEntrySetContents(self,setStr):
    self.AS_DormLocationEntryCtrlVar.set(setStr)
def AS_RoomNoEntrySetContents(self,setStr):
    self.AS_RoomNoEntryCtrlVar.set(setStr)

# ReportScreen (in MainWindow Class file) Content Setter & Getter Methods
'''note that there are no text entry elements in the ReportsScreen
   that will require setter and getter methods
'''

# ChangePasswordScreen (in MainWindow Class file) Content Setter & Getter Methods
def CP_OldPasswordEntryGetContents(self):
    return self.CP_OldPasswordEntryCtrlVar.get()
def CP_NewPasswordEntryGetContents(self):
    return self.CP_NewPasswordEntryCtrlVar.get()
def CP_OldPasswordEntrySetContents(self,setStr):
    self.CP_OldPasswordEntryCtrlVar.set(setStr)
def CP_NewPasswordEntrySetContents(self,setStr):
    self.CP_NewPasswordEntryCtrlVar.set(setStr)

# ReportResultsScreen (in MainWindow Class file) Content Setter & Getter Methods
''' note that the ReportResultScreen does not necessarily require getter and
    setter methods for its entry contents. This is because all the required
    values needed to initialize the screen are passed to the screen as parameters.
    However, there will be need for a getter method for the contents of the
    report results content text area.
'''
def RRS_ResultsContentAreaGetContents():
    '''The Result content text area does not support the
       support the use of control variables. Hence, the
       widget-specific functions will be implemented here.
    '''
    self.MainTextArea.get("1.0",tk.END)




''' declare all the content manipulation functions for this gui class'''
# LoginScreen (in MainWindow Class file) Content Setter & Getter Methods
def LS_UsernameEntryGetContents():
    return MainWindow.LS_UsernameEntryCtrlVar.get()
def LS_PasswordEntryGetContents():
    return MainWindow.LS_PasswordEntryCtrlVar.get()
def LS_UsernameEntrySetContents(setStr):
    MainWindow.LS_UsernameEntryCtrlVar.set(setStr)
def LS_PasswordEntrySetContents(setStr):
    MainWindow.LS_PasswordEntryCtrlVar.set(setStr)

# MainMenuScreen (in MainWindow class file) Content Setter & Getter Methods
'''note that there are no text entry elements in the MainMenuScreen
   that will require setter and getter methods
'''



# StudentRecordsScreen (in MainWindow Class file) Content Setter & Getter Methods
def SR_StudentIdEntryGetContents():
    return MainWindow.SAR_StudentIdEntryCtrlVar.get()
def SR_FirstNameEntryGetContents():
    return MainWindow.SAR_FirstNameEntryCtrlVar.get()
def SR_LastNameEntryGetContents():
    return MainWindow.SAR_LastNameEntryCtrlVar.get()
def SR_GenderEntryGetContents():
    return MainWindow.SAR_GenderEntryCtrlVar.get()
def SR_DepartmentEntryGetContents():
    return MainWindow.SAR_DeptEntryCtrlVar.get()
def SR_FacultyEntryGetContents():
    return MainWindow.SAR_FacultyEntryCtrlVar.get()
def SR_YearLevelEntryGetContents():
    return MainWindow.SAR_YearLevelEntryCtrlVar.get()
def SR_DormTypeEntryGetContents():
    return MainWindow.SAR_DormTypeEntryCtrlVar.get()
def SR_DormNameEntryGetContents():
    return MainWindow.SAR_DormNameEntryCtrlVar.get()
def SR_DormLocationEntryGetContents():
    return MainWindow.SAR_DormLocationEntryCtrlVar.get()
def SR_RoomNoEntryGetContents():
    return MainWindow.SAR_RoomNoEntryCtrlVar.get()
def SR_RoomMatesEntryGetContents():
    return MainWindow.SAR_RoomMatesEntryCtrlVar.get()


def SR_StudentIdEntrySetContents(setStr):
    MainWindow.SAR_StudentIdEntryCtrlVar.set(setStr)
def SR_FirstNameEntrySetContents(setStr):
    MainWindow.SAR_FirstNameEntryCtrlVar.set(setStr)
def SR_LastNameEntrySetContents(setStr):
    MainWindow.SAR_LastNameEntryCtrlVar.set(setStr)
def SR_GenderEntrySetContents(setStr):
    MainWindow.SAR_GenderEntryCtrlVar.set(setStr)
def SR_DepartmentEntrySetContents(setStr):
    MainWindow.SAR_DeptEntryCtrlVar.set(setStr)
def SR_FacultyEntrySetContents(setStr):
    MainWindow.SAR_FacultyEntryCtrlVar.set(setStr)
def SR_YearLevelEntrySetContents(setStr):
    MainWindow.SAR_YearLevelEntryCtrlVar.set(setStr)
def SR_DormTypeEntrySetContents(setStr):
    MainWindow.SAR_DormTypeEntryCtrlVar.set(setStr)
def SR_DormNameEntrySetContents(setStr):
    MainWindow.SAR_DormNameEntryCtrlVar.set(setStr)
def SR_DormLocationEntrySetContents(setStr):
    MainWindow.SAR_DormLocationEntryCtrlVar.set(setStr)
def SR_RoomNoEntrySetContents(setStr):
    MainWindow.SAR_RoomNoEntryCtrlVar.set(setStr)
def SR_RoomMatesEntrySetContents(setStr):
    # does not support control variable.
    # manipulating widget content is done using
    # widget-specific functions.
    stdRoomMatesDisplay.delete("1.0",tk.END)
    stdRoomMatesDisplay.insert("1.0",setStr)
                            


# AdvancedSearchScreen (in MainWindow Class file) Content Setter & Getter Methods
def AS_StudentIdEntryGetContents():
    return MainWindow.AS_StudentIdEntryCtrlVar.get()
def AS_FirstNameEntryGetContents():
    return MainWindow.AS_FirstNameEntryCtrlVar.get()
def AS_LastNameEntryGetContents():
    return MainWindow.AS_LastNameEntryCtrlVar.get()
def AS_GenderEntryGetContents():
    return MainWindow.AS_GenderEntryCtrlVar.get()
def AS_DepartmentEntryGetContents():
    return MainWindow.AS_DeptEntryCtrlVar.get()
def AS_FacultyEntryGetContents():
    return MainWindow.AS_FacultyEntryCtrlVar.get()
def AS_YearLevelEntryGetContents():
    return MainWindow.AS_YearLevelEntryCtrlVar.get()
def AS_DormTypeEntryGetContents():
    return MainWindow.AS_DormTypeEntryCtrlVar.get()
def AS_DormNameEntryGetContents():
    return MainWindow.AS_DormNameEntryCtrlVar.get()
def AS_DormLocationEntryGetContents():
    return MainWindow.AS_DormLocationEntryCtrlVar.get()
def AS_RoomNoEntryGetContents():
    return MainWindow.AS_RoomNoEntryCtrlVar.get()


def AS_StudentIdEntrySetContents(setStr):
    MainWindow.AS_StudentIdEntryCtrlVar.set(setStr)
def AS_FirstNameEntrySetContents(setStr):
    MainWindow.AS_FirstNameEntryCtrlVar.set(setStr)
def AS_LastNameEntrySetContents(setStr):
    MainWindow.AS_LastNameEntryCtrlVar.set(setStr)
def AS_GenderEntrySetContents(setStr):
    MainWindow.AS_GenderEntryCtrlVar.set(setStr)
def AS_DepartmentEntrySetContents(setStr):
    MainWindow.AS_DeptEntryCtrlVar.set(setStr)
def AS_FacultyEntrySetContents(setStr):
    MainWindow.AS_FacultyEntryCtrlVar.set(setStr)
def AS_YearLevelEntrySetContents(setStr):
    MainWindow.AS_YearLevelEntryCtrlVar.set(setStr)
def AS_DormTypeEntrySetContents(setStr):
    MainWindow.AS_DormTypeEntryCtrlVar.set(setStr)
def AS_DormNameEntrySetContents(setStr):
    MainWindow.AS_DormNameEntryCtrlVar.set(setStr)
def AS_DormLocationEntrySetContents(setStr):
    MainWindow.AS_DormLocationEntryCtrlVar.set(setStr)
def AS_RoomNoEntrySetContents(setStr):
    MainWindow.AS_RoomNoEntryCtrlVar.set(setStr)

# ReportScreen (in MainWindow Class file) Content Setter & Getter Methods
'''note that there are no text entry elements in the ReportsScreen
   that will require setter and getter methods
'''

# ChangePasswordScreen (in MainWindow Class file) Content Setter & Getter Methods
def CP_OldPasswordEntryGetContents():
    return MainWindow.CP_OldPasswordEntryCtrlVar.get()
def CP_NewPasswordEntryGetContents():
    return MainWindow.CP_NewPasswordEntryCtrlVar.get()
def CP_OldPasswordEntrySetContents(setStr):
    MainWindow.CP_OldPasswordEntryCtrlVar.set(setStr)
def CP_NewPasswordEntrySetContents(setStr):
    MainWindow.CP_NewPasswordEntryCtrlVar.set(setStr)

# ReportResultsScreen (in MainWindow Class file) Content Setter & Getter Methods
''' note that the ReportResultScreen does not necessarily require getter and
    setter methods for its entry contents. This is because all the required
    values needed to initialize the screen are passed to the screen as parameters.
    However, there will be need for a getter method for the contents of the
    report results content text area.
'''
def RRS_ResultsContentAreaGetContents():
    '''The Result content text area does not support the
       support the use of control variables. Hence, the
       widget-specific functions will be implemented here.
    '''
    MainTextArea.get("1.0",tk.END)

















''' define all the callback functions for all buttons in this class source file'''

dbase_config_file = open('dbase_config.txt',"r")
dbaseHost = dbase_config_file.readline()
dbaseHost = dbaseHost.replace("\n","")
dbaseHost = dbaseHost.replace("host_ip: ","")

# create database adapter to the mysql database
try:
    db = MySqlAdapter(host=dbaseHost,
                      port=3306,
                      user='mctestdb',
                      password='test',
                      db='das_db')
except:
    msgbox.showerror("Database Connection Error!","Oops! System seems to be offline and cannot connect to"
                     " data center. Please try again later.")

# LoginScreen (in MainWindow Class file) Callback functions
def LS_LoginButton_onclick(widget):
    results = db.execute("SELECT * FROM user_account")
    entered_username = LS_UsernameEntryGetContents()
    entered_password = LS_PasswordEntryGetContents()
    entered_credentials = entered_username+'+'+entered_password
    CredentialMatch = False
    credential_list = []
    for credential in results:
        c = credential[4]+'+'+credential[5]
        credential_list.append(c)
    if(entered_credentials not in credential_list):
        msgbox.showerror("Invalid Credentials","Sorry! You entered an Invalid Credential. Please try again!")
    else:
        for child in widget.parent.winfo_children():
            child.destroy()
        widget.__init__(widget.parent)
        widget.MainMenuScreen()
        
        
def LS_CancelButton_onclick(widget):
    widget.parent.destroy()


# MainMenuScreen (in MainWindow class file Callback functions
def MM_StdAccRecButton_onclick(widget):
    for child in widget.parent.winfo_children():
        child.destroy()
    widget.__init__(widget.parent)
    widget.StudentRecordsScreen()
def MM_AdvSrchButton_onclick(widget):
    for child in widget.parent.winfo_children():
        child.destroy()
    widget.__init__(widget.parent)
    widget.AdvancedSearchScreen()
def MM_ReportsButton_onclick(widget):
    for child in widget.parent.winfo_children():
        child.destroy()
    widget.__init__(widget.parent)
    widget.ReportsScreen()
def MM_LogOutButton_onclick(widget):
    for child in widget.parent.winfo_children():
        child.destroy()
    widget.__init__(widget.parent)
    widget.LoginScreen()
def MM_ExitButton_onclick(widget):
    widget.parent.destroy()
def MM_ChangePwdButton_onclick(widget):
    for child in widget.parent.winfo_children():
        child.destroy()
    widget.__init__(widget.parent)
    widget.ChangePasswordScreen()






# StudentRecordsScreen (in MainWindow Class file) Callback functions
def SR_SaveChangesButton_onclick(widget):
    stdid=SR_StudentIdEntryGetContents()
    fname=SR_FirstNameEntryGetContents()
    lname=SR_LastNameEntryGetContents()
    gender=SR_GenderEntryGetContents()
    dept=SR_DepartmentEntryGetContents()
    fac=SR_FacultyEntryGetContents()
    yearlevel=SR_YearLevelEntryGetContents()
    dormname=SR_DormNameEntryGetContents()
    roomno=SR_RoomNoEntryGetContents()

    entriesList = [stdid,fname,lname,gender,dept,fac,yearlevel,dormname,roomno]
    for entry in entriesList:
        if entry == '':
            msgbox.showerror("Empty Fields","Please enter all fields (except room-mates)")
            return
    
    
    results = db.execute("SELECT * FROM student")
    idNums = []
    for student in results:
        idNums.append(str(student[0]))
    if(stdid in idNums):
        msgbox.showerror("Student Record Exists","Oops! It appears the student has an existing record.")
        return
    else:
        try:
            stdid = int(stdid)
            deptIdNum = int(((db.execute("SELECT * FROM department WHERE DeptName LIKE '"+dept+"'"))[0])[0])
            facIdNum = int(((db.execute("SELECT * FROM faculty WHERE FacName LIKE '"+fac+"'"))[0])[0])
            yearlevelIdNum = int(((db.execute("SELECT * FROM year_level WHERE YearLevel LIKE '"+yearlevel+"'"))[0])[0])
            dormnameid = int(((db.execute("SELECT * FROM dorm WHERE DormName LIKE '"+dormname+"'"))[0])[0])
            roomno = int(roomno)
            db.execute("INSERT INTO student (StdId,Fname,Lname,Sex,DeptId,FacId,YearLevelId) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                       DataValues=(stdid,fname,lname,gender,deptIdNum,facIdNum,yearlevelIdNum))
            db.execute("INSERT INTO room_allocation (StdId,DormId,RoomNo) VALUES (%s,%s,%s)",
                       DataValues=(stdid,dormnameid,roomno))
        except:
            msgbox.showerror("Invalid Entries Detected","Oops! Please check that you have entered data of correct type")
            return
    msgbox.showinfo("Successful",fname+' '+lname+" has been successfully stored.")    


def SR_UpdateChangesButton_onclick(widget):
    stdid=SR_StudentIdEntryGetContents()
    fname=SR_FirstNameEntryGetContents()
    lname=SR_LastNameEntryGetContents()
    gender=SR_GenderEntryGetContents()
    dept=SR_DepartmentEntryGetContents()
    fac=SR_FacultyEntryGetContents()
    yearlevel=SR_YearLevelEntryGetContents()
    dormname=SR_DormNameEntryGetContents()
    roomno=SR_RoomNoEntryGetContents()

    entriesList = [stdid,fname,lname,gender,dept,fac,yearlevel,dormname,roomno]
    for entry in entriesList:
        if entry == '':
            msgbox.showerror("Empty Fields","Please enter all fields (except room-mates)")
            return
    
    try:
        stdid = int(stdid)
        deptIdNum = int(((db.execute("SELECT * FROM department WHERE DeptName LIKE '"+dept+"'"))[0])[0])
        facIdNum = int(((db.execute("SELECT * FROM faculty WHERE FacName LIKE '"+fac+"'"))[0])[0])
        yearlevelIdNum = int(((db.execute("SELECT * FROM year_level WHERE YearLevel LIKE '"+yearlevel+"'"))[0])[0])
        dormnameid = int(((db.execute("SELECT * FROM dorm WHERE DormName LIKE '"+dormname+"'"))[0])[0])
        roomno = int(roomno)
        db.execute("""UPDATE student SET StdId=%s,Fname=%s,Lname=%s,Sex=%s,DeptId=%s,FacId=%s,YearLevelId=%s WHERE StdId=%s""",DataValues=(stdid,fname,lname,gender,deptIdNum,facIdNum,yearlevelIdNum,stdid))
                   
        db.execute("""UPDATE room_allocation SET StdId=%s,DormId=%s,RoomNo=%s WHERE StdId=%s""",DataValues=(stdid,dormnameid,roomno,stdid))
    except:
        msgbox.showerror("Invalid Entries Detected","Oops! Please check that you have entered data of correct type")
        return
    msgbox.showinfo("Successful",fname+' '+lname+" has been successfully updated.")    


def SR_NewButton_onclick(widget):
    stdid=SR_StudentIdEntrySetContents('')
    fname=SR_FirstNameEntrySetContents('')
    lname=SR_LastNameEntrySetContents('')
    gender=SR_GenderEntrySetContents('')
    dept=SR_DepartmentEntrySetContents('')
    fac=SR_FacultyEntrySetContents('')
    yearlevel=SR_YearLevelEntrySetContents('')
    dormname=SR_DormNameEntrySetContents('')
    roomno=SR_RoomNoEntrySetContents('')
    widget.stdRoomMatesDisplay.delete(1.0,tk.END)
    
def SR_DeleteButton_onclick(widget):
    stdid=SR_StudentIdEntryGetContents()
    results = db.execute("SELECT * FROM student")
    idNums = []
    for student in results:
        idNums.append(str(student[0]))
    if(stdid not in idNums):
        msgbox.showerror("No Record Found","Oops! It appears the the student does not exist in the system.")
    else:
        db.execute("DELETE FROM student WHERE StdId LIKE %s",DataValues=stdid)
        db.execute("DELETE FROM room_allocation WHERE StdId LIKE %s",DataValues=stdid)
        msgbox.showinfo("Successful","Student with ID# "+stdid+" has been successfully deleted.")
        SR_NewButton_onclick(widget)
def SR_CancelButton_onclick(widget):
    for child in widget.parent.winfo_children():
        child.destroy()
    widget.__init__(widget.parent)
    widget.MainMenuScreen()

def SR_SearchStudent_onclick(widget):
    stdid=SR_StudentIdEntryGetContents()
    results = db.execute("SELECT * FROM student")
    idNums = []
    for student in results:
        idNums.append(str(student[0]))
    if(stdid not in idNums):
        msgbox.showerror("No Record Found","Oops! It appears the the student does not exist in the system.")
    else:
        results = db.execute("SELECT student.StdId,student.Fname,student.Lname,"
                             "student.Sex,student.DeptId,student.FacId,student.YearLevelId,"
                             "room_allocation.DormId,room_allocation.RoomNo FROM student, "
                             "room_allocation WHERE student.StdId LIKE "+stdid+" AND room_allocation.StdId LIKE "+stdid)
        results = results[0]
        stdid = results[0]
        fname = results[1]
        lname = results[2]
        gender = results[3]
        deptid = results[4]
        facid = results[5]
        yearlevelid = results[6]
        dormnameid = results[7] 
        roomno = results[8]

        deptname = (db.execute("SELECT DeptName FROM department WHERE DeptId LIKE "+str(deptid)))[0]
        facname = (db.execute("SELECT FacName FROM faculty WHERE FacId LIKE "+str(facid)))[0]
        yearlevel = (db.execute("SELECT YearLevel FROM year_level WHERE YearLevelId LIKE "+str(yearlevelid)))[0]
        dormname = (db.execute("SELECT DormName FROM dorm WHERE DormId LIKE "+str(dormnameid)))[0]
        deptname = deptname[0]
        facname = facname[0]
        yearlevel = yearlevel[0]
        dormname = dormname[0]

        SR_StudentIdEntrySetContents(stdid)
        SR_FirstNameEntrySetContents(fname)
        SR_LastNameEntrySetContents(lname)
        SR_GenderEntrySetContents(gender)
        SR_DepartmentEntrySetContents(deptname)
        SR_FacultyEntrySetContents(facname)
        SR_YearLevelEntrySetContents(yearlevel)
        SR_DormNameEntrySetContents(dormname)
        SR_RoomNoEntrySetContents(roomno)

        results = db.execute("SELECT StdId FROM room_allocation WHERE RoomNo LIKE "+str(roomno))
        roommatesIds = []
        roommateFullnames = []
        formattedRoommateOut = ""
        widget.stdRoomMatesDisplay.delete(1.0,tk.END)
        for ids in results:
            roommatesIds.append(ids[0])
            results = db.execute("SELECT Fname,Lname FROM student WHERE StdId LIKE "+str(ids[0]))
            results = results[0]
            fullname = results[0]+' '+results[1]
            roommateFullnames.append(fullname)
            formattedRoommateOut += str(fullname) + ' ' + 'ID# ' + str(ids[0]) + '\n'
        widget.stdRoomMatesDisplay.insert(1.0,formattedRoommateOut)





















'''continue here'''




# AdvancedSearchScreen (in MainWindow Class file) Callback functions
def AS_SearchButton_onclick(widget):
    stdid=AS_StudentIdEntryGetContents()
    fname=AS_FirstNameEntryGetContents()
    lname=AS_LastNameEntryGetContents()
    gender=AS_GenderEntryGetContents()
    dept=AS_DepartmentEntryGetContents()
    fac=AS_FacultyEntryGetContents()
    yearlevel=AS_YearLevelEntryGetContents()
    dormname=AS_DormNameEntryGetContents()
    roomno=AS_RoomNoEntryGetContents()
    
    if stdid == '':
        stdid='*'
    if fname == '':
        fname ='*'
    if lname == '':
        lname = '*'
    if gender == '':
        gender = '*'
    if dept == '':
        results = db.selectWithParameters("SELECT DeptId FROM department WHERE DeptName=%s",dept)
        print(results)
    if fac == '':
        results = db.selectWithParameters("SELECT FacId FROM faculty WHERE FacName=%s",fac)
        print(results)
    if yearlevel == '':
        results = db.selectWithParameters("SELECT YearLevelId FROM year_level WHERE YearLevel=%s",yearlevel)
        print(results)
    if dormname == '':
        results = db.selectWithParameters("SELECT DormId FROM dorm WHERE DormName=%s",dormname)
        print(results)
    if roomno == '':
        pass
    '''
    sqlcommand = "SELECT student.StdId,student.Fname,student.Lname,student.Sex,"+\
                 "student.DeptId,student.FacId,student.YearLevelId,room_allocation.DormId,"+\
                 "room_allocation.RoomNo FROM student,room_allocation "+\
                 "WHERE student.StdId = room_allocation.StdId"
                 
    result = db.execute(sqlcommand)
    for record in result:
        print(record)
    '''
    
'''
    dormid = db.execute("SELECT DormId FROM dorm WHERE DormName="+str(dormname))
    yearlevelid = db.execute("SELECT YearLevelId FROM year_level WHERE YearLevel="+str(yearlevel))
    facId = db.execute("SELECT FacId FROM faculty WHERE FacName="+str(fac))
    deptId = db.execute("SELECT DeptId FROM department WHERE DeptName="+str(dept))
    print(dormid,yearlevelid,facId,deptId)
'''
def AS_CancelButton_onclick(widget):
    for child in widget.parent.winfo_children():
        child.destroy()
    widget.__init__(widget.parent)
    widget.MainMenuScreen()



# ReportScreen (in MainWindow Class file) Callback functions
def RS_AllFemaleOccupantsButton_onclick():
    print('All Female Occupants Report Button Clicked')
def RS_AllMaleOccupantsButton_onclick():
    print('All Male Occupants Report Button Clicked')
def RS_AllParaCampusOccupantsButton_onclick():
    print('All Para Campus Occupants Report Button Clicked')
def RS_AllMainCampusOccupantsButton_onclick():
    print('All Main Campus Occupants Report Button Clicked')



# ChangePasswordScreen (in MainWindow Class file) Callback functions
def CP_ChangeButton_onclick(widget):
    oldPass = CP_OldPasswordEntryGetContents()
    newPass = CP_NewPasswordEntryGetContents()
    username = LS_UsernameEntryGetContents()
    oldcreds = (username,oldPass)
    credentials = []
    results = db.execute("SELECT Username,Password FROM user_account")
    for result in results:
        credentials.append(result)
    if(oldcreds not in credentials):
        msgbox.showerror("Wrong Password","It appears you have entered an incorrect old password.")
        return
    else:
        results = db.execute("UPDATE user_account SET Password=%s WHERE Username=%s",(newPass,username))
        msgbox.showinfo("Successful","Your password has been changed successfully."
                        "Please login with new credentials.")
    for child in widget.parent.winfo_children():
        child.destroy()
    widget.__init__(widget.parent)
    widget.LoginScreen()
        
    
    
def CP_CancelButton_onclick(widget):
    for child in widget.parent.winfo_children():
        child.destroy()
    widget.__init__(widget.parent)
    widget.MainMenuScreen()
        



# ReportResultsScreen (in MainWindow Class file) Callback functions
def RRS_ExportToTxtButton_onclick():
    print('Export To Txt Button Clicked')
def RRS_ExportToPdfButton_onclick():
    print('Export to PDF Button Clicked')
def RRS_CancelButton_onclick():
    print('Cancel Button Clicked')

mw = MainWindow(root)
mw.LoginScreen()
root.mainloop()
