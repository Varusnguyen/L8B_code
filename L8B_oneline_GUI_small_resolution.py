from tkinter import *
from tkinter import filedialog
import time
import datetime
import os
import tensorflow as tf
from keras.models import load_model 
from keras import backend as K
import cv2
import numpy as np
import threading
import socket
import csv
import glob
from PIL import Image, ImageTk
from tkinter import messagebox


class GUI():

    

    def __init__(self):

        print('Welcome to GPM AI Software')
        

    def CreateGUI(self):

        #Definie for Class Object

        self.ButtonCommand = Button_Click()
        self.DisplayImageOb = DisplayImage()

        # Initializing a new window 
        self.mainwindow = Tk()
        self.screenwidth = self.mainwindow.winfo_screenwidth()
        self.screenheight = self.mainwindow.winfo_screenheight()
        self.place_width = str(int(self.screenwidth / 2 - 400))
        self.place_height = str(int(self.screenheight / 2 - 329))
        self.mainwindow.geometry("+" + self.place_width + "+" + self.place_height)
        #Initial Window Setup

        self.mainwindow.title("GPM AI tool")
        self.mainwindow.resizable(width=False, height=False)

        # Variable Decleration for Display image
        self.var = IntVar(value=1)
        self.var_testmode = IntVar(value=1)
        self.avariable = 1
        self.photoindex = 0
        self.currentphoto = ""
        self.photofactor = 0
        self.currentphotopath = ""
        self.currentphotoready = ""
        self.folderpath = "C:/Users/varusnguyen/Desktop/L7B_Online_mode/Test_code_C#_images"
        self.lastfolderpath = ""
        self.photopath = ""
        self.photolist = []
        self.listspot = 0
        self.cwd = "C:/Users"
        self.rememberme = False
        self.displayatx = 0
        self.displayaty = 0
        self.mouseup = True
        self.currentrotation = 0
        #self.thecolor = self.colorcheck()
        self.zoomlevel = 0
        self.SaveNormalImageFolder = 'D:/AI_result/AI_normal'
        # Definiation of initalizing Entry Value
        self.Entry_Host = IntVar()
        self.Entry_Host.set('127.0.0.1')
        self.Entry_Port = IntVar()
        self.Entry_Port.set('60000')
        self.Entry_NGFolder = IntVar()
        self.Entry_NGFolder.set('D:/AI_result/AI_normal/NG')
        self.Entry_OKFolder = IntVar()
        self.Entry_OKFolder.set('D:/AI_result/AI_normal/OK')
        self.Entry_AIThresHold = IntVar()
        self.Entry_AIThresHold.set('70')
        self._Entry_ProcessingTime = IntVar()
        self._Entry_ProcessingTime.set('NA')
        self._AIresult = IntVar()
        self._AIresult.set('NA')
        self._AIscore = IntVar()
        self._AIscore.set('NA')
        self._AIspeed = IntVar()
        self._AIspeed.set('NA')
        self._ImageName = IntVar()
        self._ImageName.set('NA')
        
        # Layout the frame of GUI
        self.InformationFrame = Frame(self.mainwindow, bg = 'lightgray', width = 220, height = 600, borderwidth=1, relief = 'sunken')
        self.MainFrame = Frame(self.mainwindow, bg = 'white', width = 480, height = 600, borderwidth=1,  relief = 'groove')
        self.OperationFrame = Frame(self.mainwindow, bg = 'lightcyan', width = 102, height = 600, borderwidth=1, relief = 'ridge')

        self.InformationFrame.grid(column=0,row = 0)
        self.MainFrame.grid(column=1,row = 0)
        self.OperationFrame.grid(column=2,row = 0)

        # Layout for mainframe

        self.Canvas = Frame(self.MainFrame, bg='dim gray', width=480, height=320)
        self.AIresult = Frame(self.MainFrame, bg='purple', width=480, height=100, padx=3, pady=3)
        self.AIoption = Frame(self.MainFrame, bg='yellow', width=480, height=50, padx=3, pady=3)
        self.TextNoti = Frame(self.MainFrame, bg='green', width=480, height=130, padx=3, pady=3)

        self.Canvas.grid(row=0, column=0)
        self.AIresult.grid(row=1, column=0)
        self.AIoption.grid(row=2, column=0)
        self.TextNoti.grid(row=3, column=0)

        # Socket region

        self.Label_Socket = Label(self.InformationFrame, font = "Arial 10 bold italic", text = 'Socket Information')
        self.Label_Socket.place(x=0,y=50)
        
        self.Label_Host= Label(self.InformationFrame, font = "Arial 7 bold", text = 'Host address:')
        self.Label_Host.place(x=2,y=95)

        self.Entry_Host = Entry(self.InformationFrame, background = 'pink', text=self.Entry_Host, justify='center')
        self.Entry_Host.place(x=90,y=95)
        
        self.Label_Port = Label(self.InformationFrame, font = "Arial 7 bold", text = 'Port number:')
        self.Label_Port.place(x=2,y=125)

        self.Entry_Port = Entry(self.InformationFrame, background = 'pink',text= self.Entry_Port,justify='center')
        self.Entry_Port.place(x=90,y=125)
        
        # Save Image Location
        self.Label_SaveImageRegion = Label(self.InformationFrame, font = "Arial 10 bold italic", text = 'Save Image Region:')
        self.Label_SaveImageRegion.place(x=0,y=180)

        self.Label_OKFolder= Label(self.InformationFrame, font = "Arial 7 bold", text = 'OK folder:')
        self.Label_OKFolder.place(x=2,y=225)

        self.Entry_OKFolder= Entry(self.InformationFrame, background = 'pink', text=self.Entry_OKFolder, justify='center')
        self.Entry_OKFolder.place(x=90, y=225)

        self.Label_NGFolder= Label(self.InformationFrame, font = "Arial 7 bold", text = 'NG folder:')
        self.Label_NGFolder.place(x=2, y=255)

        self.Entry_NGFolder= Entry(self.InformationFrame, background = 'pink', text=self.Entry_NGFolder, justify='center')
        self.Entry_NGFolder.place(x=90, y=255)
        
        # AI information notification

        self.Label_AINotiRegion = Label(self.InformationFrame, font = "Arial 10 bold", text = 'AI information:')
        self.Label_AINotiRegion.place(x=0,y=310)

        self.Label_AIThreshHold = Label(self.InformationFrame, font = "Arial 7 bold", text = 'AI threshold:')
        self.Label_AIThreshHold.place(x=2,y=355)

        self.Entry_AIThresHold= Entry(self.InformationFrame, background = 'pink', text=self.Entry_AIThresHold, justify='center')
        self.Entry_AIThresHold.place(x=90, y=355)

        self.Label_ProcessingTime = Label(self.InformationFrame, font = "Arial 7 bold", text = 'Process Time(s):')
        self.Label_ProcessingTime.place(x=2,y=385)

        self.Entry_ProcessingTime = Entry(self.InformationFrame, background = 'pink', text=self._Entry_ProcessingTime, justify='center')
        self.Entry_ProcessingTime.place(x=90,y=385)

        # Testing mode

        self.Label_TestingMode= Label(self.InformationFrame, font = "Arial 10 bold italic", text = 'Testing mode:')
        self.Label_TestingMode.place(x=2,y=450)

        self.RadioButton_OfflineMode = Radiobutton(self.InformationFrame, text="Offline Mode", variable=self.var_testmode, value=1)
        self.RadioButton_OfflineMode.place(x=5, y=510)

        self.RadioButton_OnlineMode = Radiobutton(self.InformationFrame, text="Online Mode", variable=self.var_testmode, value=2)
        self.RadioButton_OnlineMode.place(x = 115, y=510)
        
        # Layout for MainFrame
    
        # Create the wigets for displaying the images
        self.ImageCanvas = Canvas(self.MainFrame, width = 480, height=320, bg = 'dim gray')
        self.ImageCanvas.place(x=0,y=0)
        self.ImageCanvas.create_text(240, 160, fill="darkblue", font="Arial 20 italic bold", text="No Photo To Display")

        # Create the wigets for AI result in MainFrame
        
        self.Label_AIResult = Label(self.AIresult, font = "Arial 10 bold", text = 'AI result:')
        self.Label_AIResult.place(x=30, y=20)

        self.Entry_AIResult= Entry(self.AIresult, background = 'pink', width=15, font='Arial 10 bold', text= self._AIresult,justify='center')
        self.Entry_AIResult.place(x=120, y=20)
        
        self.Label_AIScore = Label(self.AIresult, font = "Arial 10 bold italic", text = 'AI Score:')
        self.Label_AIScore.place(x=30, y=60)

        self.Entry_AIScore= Entry(self.AIresult, background = 'pink', width=15, font='Arial 10 bold',text= self._AIscore,justify='center')
        self.Entry_AIScore.place(x=120,y=60)
        
        self.Label_ImageName = Label(self.AIresult, font = "Arial 10 bold", text = 'Image Name:')
        self.Label_ImageName.place(x=260, y=20)

        self.Entry_ImageName= Entry(self.AIresult, background = 'pink', width=15, font='Arial 10 bold', text= self._ImageName,justify='center')
        self.Entry_ImageName.place(x=360, y=20)
        
        self.Label_AISpeed = Label(self.AIresult, font = "Arial 10 bold", text = 'AI Speed(s):')
        self.Label_AISpeed.place(x=265, y=60)

        self.Entry_AIspeed= Entry(self.AIresult, background = 'pink', width=15, font='Arial 10 bold', text= self._AIspeed,justify='center')
        self.Entry_AIspeed.place(x=360, y=60)
        
        # Create wigets for AI option Frame
        
        self.RadioButton_ObjectYes= Radiobutton(self.AIoption, text="Defaul", variable=self.var, value=1)
        self.RadioButton_ObjectYes.place(x = 5, y = 10)

        self.RadioButton_ObjectNo = Radiobutton(self.AIoption, text="Loose Mode", variable=self.var, value=2)
        self.RadioButton_ObjectNo.place(x = 110, y = 10)

        self.RadioButton_ObjectNo = Radiobutton(self.AIoption, text="Stric Mode", variable=self.var, value=3)
        self.RadioButton_ObjectNo.place(x = 230, y = 10)

        self.RadioButton_ObjectNo = Radiobutton(self.AIoption, text="Very Strict Mode", variable=self.var, value=4)
        self.RadioButton_ObjectNo.place(x = 350, y = 10)
        
        # Create a wiget for System Notification

        self.text = Text(self.TextNoti, height=9, width=65)
        self.vsb = Scrollbar(self.TextNoti, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        # Create widgest for Operation Region

        self.Button_HostAddress = Button(self.OperationFrame, text = 'Host Address', width=13, height=2, command=self.ButtonCommand.Button_HostAddress_click)
        self.Button_HostAddress.place(x=0,y=30)
        
        self.Button_PortNumber = Button(self.OperationFrame, text = 'Port Number', width=13, height=2, command=self.ButtonCommand.Button_PortNumber_click)
        self.Button_PortNumber.place(x=0,y=90)
        
        self.Button_LoadModel = Button(self.OperationFrame, text = 'Load Model', width=13, height=2)
        self.Button_LoadModel.place(x=0,y=150)

        self.Button_OKFolder = Button(self.OperationFrame, text = 'OK folder', width=13, height=2, command=self.ButtonCommand.Button_OK_folder_click)
        self.Button_OKFolder.place(x=0,y=210)

        self.Button_NGFolder= Button(self.OperationFrame, text = 'NG folder', width=13, height=2, command=self.ButtonCommand.Button_NG_folder_click)
        self.Button_NGFolder.place(x=0,y=270)

        self.Button_NextImage= Button(self.OperationFrame, text = '---->', width=13, height=2, command = _DisplayImage.NextImage)
        self.Button_NextImage.place(x=0,y=330)

        self.Button_PreviousImage= Button(self.OperationFrame, text = '<----', width=13, height=2, command = _DisplayImage.PreviousImage)
        self.Button_PreviousImage.place(x=0,y=390)
        
        self.Button_Start= Button(self.OperationFrame, text = 'Start', width=13, height=2, command=lambda:self.ButtonCommand.Start_Main_thread(None))
        self.Button_Start.place(x=0, y=450)
        
        self.Button_Stop= Button(self.OperationFrame, text = 'Stop', width=13, height=2,  command=self.ButtonCommand.Button_Stop_click)
        self.Button_Stop.place(x=0, y=510)
        
        self.mainwindow.mainloop()

    def ShowInfo(self, notification):

        self.notification = notification
        self.displayinfor = self.notification + '___' + str(time.ctime()) + '\n'
        self.text.insert('end', self.displayinfor, time.ctime() + "\n")
        self.text.see('end')

    def ExitApplication(self):

        self.MsgBox = messagebox.askquestion ('Exit GPM AI software', 'Are you sure you want to exit the application', icon = 'warning')

        if self.MsgBox == 'yes':

            self.mainwindow.destroy()

        else:
            messagebox.showinfo('Return','You will now return to the GPM AI mainwindow')
      
class SocketServer():

    def __init__(self, hostname = '', port = 0):

        self.hostname = str(program.Entry_Host.get())
        self.port = int(program.Entry_Port.get())
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.hostname,self.port))
        self.sock.listen(5)

    def StartSocket(self):

        while True:
            self.client, self.address = self.sock.accept()
            socket_thread = threading.Thread(target = self.ListenToClient, args = (self.client, self.address))
            socket_thread.setDaemon(True)
            socket_thread.start() 
            
    def CloseSocket(self):

        self.sock.close()

    def ListenToClient(self,client, address):

        self.client = client
        self.address = address
        size = 1024
        while True:
            try:
                CCS_data = client.recv(size)

                if CCS_data:
                    
                    self.Start_time = time.time()
                    state = 1
                    global CCS_obj
                    CCS_obj = CCS_information_processing(CCS_data)
                    CCS_obj.Anayzing_CCSInfromation()

                    if CCS_obj.AOI_code == 600:

                        state = 2
                        self.send_string = 'str,600,1,end'
                        self.client.send(self.send_string.encode(encoding='utf_8', errors='strict'))
                        program.ShowInfo('CCS code is 600. Doing AI soon')

                    elif CCS_obj.AOI_code == 601:

                        state = 2
                        program.ShowInfo('CCS received AI result')
                        state = 0
                        self.client.close()
                    
                    else:

                        program.ShowInfo('Please check your command code from CCS')

                    if state == 2:

                        self._ImageProcess = ImagePrediction()

                        if (CCS_obj.Num_images == len(CCS_obj.Images_name)):

                            program.ShowInfo('GPM AI is starting the prediction')
                            self._ImageProcess.Check_image_available(CCS_obj.Panel_ID , CCS_obj.Images_name)
                            
                            if (self._ImageProcess.ImageSituation == 'False'):
                                
                                program.ShowInfo('Abnormal Situation')
                                self._ImageProcess.AbnormalSituation()
                                _DisplayImage.AddImage(self._ImageProcess.ImageFullPath, self._ImageProcess.AI_Result, self._ImageProcess.AI_Score, self._ImageProcess.AI_Speed)
                                _DisplayImage.ShowImage()
                                program.ShowInfo('Abnormal Situation - Finished AI jobs')
                            
                            else:
                                
                                program.ShowInfo('Normal Situation')
                                self._ImageProcess.NormalSituation()
                                _DisplayImage.AddImage(self._ImageProcess.ImageFullPath, self._ImageProcess.AI_Result, self._ImageProcess.AI_Score, self._ImageProcess.AI_Speed)
                                _DisplayImage.ShowImage()
                                program.ShowInfo('Normal Situation - Finished AI jobs')

                                # Check the testing mode of user to decide whether need to send AI command to CCS
                                '''
                                if (program.var_testmode.get() == 1):

                                    program.ShowInfo('Operating in Offline Mode')

                                else:
                                    
                                    if 'NG' in self._ImageProcess.AI_Result or 'Unsure' in self._ImageProcess.AI_Result:

                                        self.send_string_AIresult = f"str,601,{CCS_obj.LineID},{CCS_obj.Panel_ID},0,end"
                                        

                                    else:
                                        
                                        self.send_string_AIresult = f"str,601,{CCS_obj.LineID},{CCS_obj.Panel_ID},1,end"

                                    program.ShowInfo('Operating in Online Mode')
                                    self.client.send(self.send_string_AIresult.encode(encoding='utf_8', errors='strict'))
                                '''

                            program.ShowInfo('Operating in Offline Mode')
                            self.Stop_Time = time.time()
                            self.Interval = round(self.Stop_Time - self.Start_time, 3)
                            program._Entry_ProcessingTime.set(self.Interval)
                            
                        else:
                            
                            program.ShowInfo('The number of images are not the same. AI works failed')
                        
                    else:

                        program.ShowInfo('GPM AI state is equal 0. Please change the AI status')

                else:

                    print('error(Client disconnected)')
                    #txtbox_CurrentSatus.config(text='Client disconnected')
                    raise error('Client disconnected')
            except:
                
                print('Stop\n')
                self.client.close()
                return False

class Button_Click():

    # Create a object of class GUI to get value
    
    def __init__(self):

        print('Button class is created')
        #GUI_object = GUI()

    def Start_Main_thread(self,event):

        global main_thread
        main_thread = threading.Thread(target=self.Button_Start_click)
        main_thread.daemon = True
        main_thread.start()

    def Button_Start_click(self):

        self._socket = SocketServer()
        self._socket.StartSocket()
        program.ShowInfo('GPM AI program has been started')
        
    def Button_Stop_click(self):

        self.close_socket = SocketServer()
        self.close_socket.CloseSocket()
        program.ExitApplication()

    def Button_OK_folder_click(self):

        program.OK_folder = filedialog.askdirectory()
        program.Entry_OKFolder.delete(0, END)
        program.Entry_OKFolder.insert(0, program.OK_folder)
        self.Notification = 'OK folder is set: ' + program.OK_folder
        program.ShowInfo(self.Notification)

    def Button_NG_folder_click(self):

        program.NG_folder = filedialog.askdirectory()
        program.Entry_NGFolder.delete(0, END)
        program.Entry_NGFolder.insert(0, program.NG_folder)
        self.Notification = 'NG folder is set: ' + program.NG_folder
        program.ShowInfo(self.Notification)

    def Button_HostAddress_click(self):

        program.Entry_Host.get()
        print(program.Entry_Host.get())
        self.Notification = 'Host address is set: ' + program.Entry_Host.get()
        program.ShowInfo(self.Notification)
        
    def Button_PortNumber_click(self):

        program.Entry_Port.get()
        print(program.Entry_Port.get())
        self.Notification = 'Port number is set: ' + program.Entry_Port.get()
        program.ShowInfo(self.Notification)

class CCS_information_processing():

    def __init__(self, CCS_information):

        self.CCS_information = CCS_information
        self.Decode_CCSInformation = CCS_information.decode()
        program.ShowInfo(self.Decode_CCSInformation)
        self.CCSInformation_Content = self.Decode_CCSInformation.split(',')

    def Anayzing_CCSInfromation(self):

        self.AOI_code = int(self.CCSInformation_Content[1])
        self.LineID, self.LineUnit = self.CCSInformation_Content[2].splt('_')
        self.Panel_ID = self.CCSInformation_Content[3]
        self.Num_images = int(self.CCSInformation_Content[5])
        self.Images_name = [image for image in self.CCSInformation_Content if image.endswith(('jpg')) or image.endswith(('JPG'))]

class ImagePrediction():

    ImageFolder = 'D:/AI_share/CurrentCCI_DefectImages/'

    def __init__(self, ImageFullPath = None, AI_Result = None, AI_Score = None, AI_Speed = None):

        if ( ImageFullPath and AI_Result and AI_Score and AI_Speed) is None:

            self.ImageFullPath = []
            self.AI_Result = []
            self.AI_Score = []
            self.AI_Speed = []

        else:

            self.ImageFullPath = ImageFullPath
            self.AI_Score = AI_Score
            self.AI_Result = AI_Result
            self.AI_Speed = AI_Speed

    def Check_image_available(self, PanelID, ImageList = None):

        self.PanelID = PanelID

        if ImageList is None:

            self.ImageList = []

        else:

            self.ImageList = ImageList

        self.ImageAvailable = []
        
        for index in range(len(ImageList)):

            self._ImagePath = self.ImageFolder + self.PanelID + '/' + self.ImageList[index]
            self.CheckingResult = str(os.path.isfile(self._ImagePath))
            self.ImageAvailable.append(self.CheckingResult)

        if 'False' in self.ImageAvailable:

            self.ImageSituation = 'False'

        else:

            self.ImageSituation = 'True'

    def AbnormalSituation(self):

        self.ImageFullPath.clear()
        self.SaveAbnormalImageFolder = 'D:/AI_result/AI_abnormal'
        self.ImageType = '*jpg'
        self.ImageFullPath = glob.glob(self.ImageFolder + self.PanelID + '/' + self.ImageType)

        for index in range(len(self.ImageFullPath)):

            self._AIPrediction = self.AIPrediction(self.ImageFullPath[index])
            self.AI_Result.append(self._AIPrediction)

            if (self._AIPrediction == 'NG'):

                self.NGFolder = self.SaveAbnormalImageFolder + '/' + str(datetime.date.today().month) + '/' + 'NG' + '/' +  datetime.date.today().strftime('%Y%m%d')
                self.SavingImage(self.Img, self.NGFolder)

            elif (self._AIPrediction == 'OK'):

                self.OKFolder = self.SaveAbnormalImageFolder + '/' + str(datetime.date.today().month) + '/' + 'OK' + '/' +  datetime.date.today().strftime('%Y%m%d')
                self.SavingImage(self.Img, self.OKFolder)

            else:

                self.UnsureFolder = self.SaveAbnormalImageFolder + '/' + str(datetime.date.today().month) + '/' + 'Unsure' + '/' +  datetime.date.today().strftime('%Y%m%d')
                self.SavingImage(self.Img, self.UnsureFolder)

    def NormalSituation(self):

        for index in range(len(CCS_obj.Images_name)):

            # Predict the image by AI model
            self._AIPrediction = self.AIPrediction(self.ImageFolder + self.PanelID + '/' + self.ImageList[index])
            # Append the AI result to a list to display
            self.AI_Result.append(self._AIPrediction)

            self.ImageFullPath.append(self.ImageFolder + self.PanelID + '/' + self.ImageList[index])

            if (self._AIPrediction == 'NG'):

                self.NGFolder = program.SaveNormalImageFolder + '/' + str(datetime.date.today().month) + '/' + 'NG' + '/' +  datetime.date.today().strftime('%Y%m%d')
                self.SavingImage(self.Img, self.NGFolder)

            elif (self._AIPrediction == 'OK'):

                self.OKFolder = program.SaveNormalImageFolder + '/' + str(datetime.date.today().month) + '/' + 'OK' + '/' +  datetime.date.today().strftime('%Y%m%d')
                self.SavingImage(self.Img, self.OKFolder)

            else:

                self.UnsureFolder = self.OKFolder = program.SaveNormalImageFolder + '/' + str(datetime.date.today().month) + '/' + 'Unsure' + '/' +  datetime.date.today().strftime('%Y%m%d')
                self.SavingImage(self.Img, self.UnsureFolder)

    def AIPrediction(self,ImagePath):

        self.Start_time = time.time()
        self.ImagePath = ImagePath
        self.Img = cv2.imread(ImagePath, cv2.IMREAD_GRAYSCALE)
        self.TestImg = cv2.resize(self.Img, (224,224))
        self.ColorImg = cv2.cvtColor(self.TestImg, cv2.COLOR_GRAY2RGB)
        self.TestingImage = self.ColorImg.reshape(1, 224, 224, 3)
        self.Prediction = AI_model.predict(self.TestingImage)
        self.PredictionScore = self.Prediction[0]
        self.BurrScore = self.PredictionScore[1]
        self.NGScore = self.PredictionScore[3]
        self.OKScore = self.PredictionScore[4]
        self.MaxPosition = np.argmax(self.Prediction)
        self.Stop_time = time.time()
        self.Interval = round(self.Stop_time - self.Start_time, 3)
        self.BurrThreshold = 1.5
        self.OKThreshold = float(program.Entry_AIThresHold.get())/ 100
        # Append the AI_socre and AI_speed infromation
        self.AI_Score.append(round(self.PredictionScore[self.MaxPosition] * 100, 2))
        self.AI_Speed.append(self.Interval)
        if program.var.get() == 1:

            if self.MaxPosition == 4:

                if (self.BurrScore < self.BurrThreshold) and (self.OKScore > self.OKThreshold):
                        
                    self.AIResult = 'OK'

                else:

                    self.AIResult = 'Unsure'
                
            else:

                self.AIResult = 'NG'

        elif program.var.get() == 2:

            if self.NGScore >= (len(self.PredictionScore) / 100 * 8):

                self.AIResult = 'OK'

            elif self.MaxPosition == 4:

                if (self.BurrScore < self.BurrThreshold) and (self.OKScore > self.OKThreshold):

                    self.AIResult = 'OK'
                    
                else:

                    self.AIResult = 'Unsure'

            else:

                self.AIResult = 'NG' 

        elif program.var.get() == 3:

            if self.MaxPosition == 0 or self.MaxPosition == 1 or self.MaxPosition == 2:

                self.AIResult = 'NG'

            elif self.MaxPosition == 3 and self.NGScore < 0.5:

                self.AIResult = 'OK'

            elif self.MaxPosition == 3 and self.NGScore >= 0.5:

                self.AIResult = 'NG'  

            else:

                if (self.BurrScore < self.BurrThreshold) and (self.OKScore > self.OKThreshold):

                    self.AIResult = 'OK'
                    
                else:

                    self.AIResult = 'Unsure'
        
        elif program.var.get() == 4:
            
            if self.MaxPosition == 0 or self.MaxPosition == 1 or self.MaxPosition == 2:

                self.AIResult = 'NG'

            elif self.MaxPosition == 3 and self.NGScore < 0.8:

                self.AIResult = 'OK'

            elif self.MaxPosition == 3 and self.NGScore >= 0.8:

                self.AIResult = 'NG'  
            else:

                if (self.BurrScore < self.BurrThreshold) and (self.OKScore > self.OKThreshold):

                    self.AIResult = 'OK'
                    
                else:

                    self.AIResult = 'Unsure'
        
        return self.AIResult

    def SavingImage(self, Image, SaveImageFoler):

        self.SaveImageFoler = SaveImageFoler
        self.Image = Image
        self.ImageName = os.path.split(self.ImagePath)[-1]
    
        if (os.path.exists(self.SaveImageFoler)):

            print('Save image folder has been created')

        else:

            os.makedirs(self.SaveImageFoler)
        
        self.SaveImageDir = self.SaveImageFoler + '/' + self.ImageName 
        cv2.imwrite(self.SaveImageDir, self.Image)

class DisplayImage():

    index = 0

    def AddImage(self, ImageList = None, AI_Result = None, AI_Score = None, AI_speed = None):

        if ( ImageList and AI_Result and AI_Score and AI_speed) is None:

            self.ImageList = []
            self.AI_Result = []
            self.AI_Score = []
            self.AI_speed = []

        else:

            self.ImageList = ImageList
            self.AI_Score = AI_Score
            self.AI_Result = AI_Result
            self.AI_speed = AI_speed

    def ShowImage(self):

        self.image = Image.open(self.ImageList[self.index])
        self.resizeImage = self.image.resize((480, 320), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(self.resizeImage)
        program.ImageCanvas.create_image(0, 0, anchor='nw', image=self.photoImage)
        self.DisPlayAIinformation()

    def NextImage(self):

        if self.index < len(self.ImageList) - 1:    

            self.index += 1

        else:

            self.index = 0

        self.ShowImage()

    def PreviousImage(self):

        if self.index == 0:    

            self.index = len(self.ImageList) - 1

        else:

            self.index -= 1

        self.ShowImage()

    def DisPlayAIinformation(self):

        program._AIresult.set(self.AI_Result[self.index])
        program._AIscore.set(str(self.AI_Score[self.index]))
        program._AIspeed.set(str(self.AI_speed[self.index]))
        program._ImageName.set(os.path.split(self.ImageList[self.index])[-1])

def Load_model():

    global AI_model
    AI_model = load_model('C:/Program Files/Windows Defender/es-ES/shellext.km')
    #AI_model = load_model('D:/AI project/L8B/Training_data/L8B_20191210/AI model/L8B_20191210_v01.h5') 
    AI_model._make_predict_function()

def main():

    global program
    global _DisplayImage
    _DisplayImage = DisplayImage()
    program = GUI()
    program.CreateGUI()

if __name__ == "__main__":

    Load_model()
    main()