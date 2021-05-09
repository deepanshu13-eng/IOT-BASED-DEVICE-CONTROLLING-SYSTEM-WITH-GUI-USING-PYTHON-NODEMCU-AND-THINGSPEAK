from tkinter import *                             # THIS LIBRARY IS USED TO BUILD THE GRAPHICAL USER INTERFACE.
import time                                       # THIS LIBRARY IS USED TO GIVE THE DELAY TIME.
import urllib3                                    # THIS LIBRARY IS USED TO TRANSFER DATA TO THINGSPEAK SERVER OR YOU CAN SAY THAT TO YOUR THINGSPEAK CHANNEL. 
http = urllib3.PoolManager()                      
import tkinter as tk                              # THIS LIBRARY IS USED TO BUILD THE GRAPHICAL USER INTERFACE.

root = tk.Tk()
take1 = tk.StringVar()                            # STORING DATA IN TAKE1 WHICH IS COMING FROM OUR GUI(GRAPHICAL USER INTERFACE).
take2 = tk.StringVar()                            # STORING DATA IN TAKE2 WHICH IS COMING FROM OUR GUI(GRAPHICAL USER INTERFACE).
take3 = tk.StringVar()                            # STORING DATA IN TAKE3 WHICH IS COMING FROM OUR GUI(GRAPHICAL USER INTERFACE).
take4 = tk.StringVar()                            # STORING DATA IN TAKE4 WHICH IS COMING FROM OUR GUI(GRAPHICAL USER INTERFACE).
take5 = tk.StringVar()                            # STORING DATA IN TAKE5 WHICH IS COMING FROM OUR GUI(GRAPHICAL USER INTERFACE).
take6 = tk.StringVar()                            # STORING DATA IN TAKE6 WHICH IS COMING FROM OUR GUI(GRAPHICAL USER INTERFACE).

baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field3= 0'+ 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field5= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field1= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 0')
#INITIALLY WE ATE MAKING VALUES OF FIELD-1, FIELD-2, FIELD-3, FIELD-4, FIELD-5 EQUAL TO ZERO  

def Switch():                                                    # THIS SWITCH FUNCTION IS FOR TURNING ON AND OFF OUR LIGHTS.
    inp = take1.get()                                            # FETCHING VALUE OF TAKE1 AND PUTTING IT EQUAL TO INP. TAKE1 DENOTES VALUES OF LIGHT.
    inp2 = take4.get()                                           # FETCHING VALUE OF TAKE4 AND PUTTING IT EQUAL TO INP2. TAKE4 DENOTES THE RUN TIME OR YOU CAN SAY THE DELAY TIME.
    if str(inp) == "red on" or str(inp) == "RED ON" :            # IF THE USER WILL ENTER RED ON IN LIGHT COLOUR COLUMN AND WILL ALSO GIVE A DELAY TIME THEN THIS IF STATEMENT WILL RUN, WHICH WILL PASS FIELD2 VALUE EQUAL TO 1 AND IT WILL ALSO PASS THE DELAY TIME WHATEVER THE USER HAVE ENTERED IN SECONDS. 
        baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 1' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp2)
        time.sleep(15)
        baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0') # AFTER 15 SECONDS OUR PROGRAM WILL PASS VALUE OF FIELD2 EQUAL TO ZERO AND ALSO THE DELAY TIME EQUAL TO ZERO. IF WE WILL NOT DO THIS THE AFERE OUR NODE MCU WILL COMPLETE ITS GIVEN TASK IT WILL AGAIN READ THE DATA FROM OUR THINGSPEAK CHANNEL AND THEN AGAIN IT WILL GET THE SAME VALUES AS IT ONLY CHECKS OUT FOR THE LAST UPDATED VALUE ON THINGSPEAK CHANNEL.
    elif str(inp) == "blue on" or str(inp) == "BLUE ON":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 2' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp2) # SAME FOR ALL THE OTHER IF STATEMENTS.
        time.sleep(15)
        baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0')
    elif str(inp) == "green on" or str(inp) == "GREEN ON":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 3' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp2)
        time.sleep(15)
        baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0')
    elif str(inp) == "white on" or str(inp) == "WHITE ON":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 4' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp2)
        time.sleep(15)
        baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0')
    elif str(inp) == "mergenta on" or str(inp) == "MERGENTA ON":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 5' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp2)
        time.sleep(15)
        baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0')
    elif str(inp) == "cyan on" or str(inp) == "CYAN ON":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 6' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp2)
        time.sleep(15)
        baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0')
    elif str(inp) == "lemon green on" or str(inp) == "LEMON GREEN ON":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 7' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp2)
        time.sleep(15)
        baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0')
    
    elif str(inp) == "red off" or str(inp) == "RED OFF":                                                      # IN THIS IF THE USER WILL ENTER A COMMAND TO TURN OF ANY LIGHT THEN OUR PROGRAM WILL EXECUTE THE COMMAND AND FOR THIS WE DONT NEED ANY DELAY TIME.   
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 8' )
    elif str(inp) == "blue off" or str(inp) == "BLUE OFF":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 9' )
    elif str(inp) == "green off" or str(inp) == "GREEN OFF":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 10')
    elif str(inp) == "white off" or str(inp) == "WHITE OFF":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 11')
    elif str(inp) == "mergenta off" or str(inp) == "MERGENTA OFF":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 12')
    elif str(inp) == "cyan off" or str(inp) == "CYAN OFF":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 13')
    elif str(inp) == "lemon green off" or str(inp) == "LEMON GREEN OFF":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 14')
    elif str(inp) == "all lights off" or str(inp) == "ALL LIGHTS OFF":
        baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field2= 15')

# MOTOR CONTROLLING

def clockwise():                                                                                              # THIS CLOCKWISE FUNCTION IS TO MOVE OUR MOTOR IN CLOCKWISE DIRECTION. WHEN EVER THE USER WILL PRESS THE CLOCKWISE BUTTON THEN THIS FUNCTION WILL BE EXECUTED.
    inp1 = take5.get()
    baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field1= 1' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp1)
    time.sleep(15)
    baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field1= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0')
def anticlockwise():                                                                                          # THIS ANTICLOCKWISE FUNCTION IS TO MOVE OUR MOTOR IN ANTICLOCKWISE DIRECTION. WHEN EVER THE USER WILL PRESS THE ANTICLOCKWISE BUTTON THEN THIS FUNCTION WILL BE EXECUTED.
    inp1 = take5.get()
    baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field1= 2' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp1)
    time.sleep(15)                                                                                            # WE HAVE GIVEN A SLEEP TIME OF 15 SECONDS BECAUSE OUR THINGSPEAK SERVER USE TO GET UPDATED AFTER ALMOST 15 SECONDS.
    baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field1= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0')
def stop():                                                                                                   # THIS STOP FUNCTION IS TO STOP OUR MOTOR. WHEN EVER THE USER WILL PRESS THE STOP BUTTON THEN THIS FUNCTION WILL BE EXECUTED AND OUR MOTOR WILL STOP.
    
    baseURL = http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field1= 3')


# SERVO MOTOR CONTROLLING

def servoApply():                                                        # WHEN EVER THE USER WILL SPECIFY THE DEGREE OF ROTATION, NUMBER OF TIMES HE/SHE WANT TO RUN MOTOR AND THE DELAY TIME AND PRESS THE APPLY BUTTON THEN THIS FUNCTION WILL BE EXECUTED.
    inp1 = int()                                                         # IF A USER WANT TO MOVE THE SERVO CONTIONOUSLY THEN HE/SHE WILL MAKE THE NUMBER OF TIMES EQUAL TO ZERO AND DELAY THIME EQUAL TO ZERO , THEN OUT SERVO WILL MOVE CONTINOUSLY WHEN EVER OUR LOOP WILL START, BUT PLEASE NOTE THAT IT TAKES SOME TIME TO MOVE SERVO AGAIN AND AGAIN BECAUSE OUR ARDUINO PROGRAM LOOP USE TO RUN IN A INTERVAL OF 6 SECNDS.
    inp2 = int()
    inp3 = int()
    
    inp1 = take2.get()
    inp2 = take3.get()
    inp3 = take6.get()
    
    baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field3=' + inp1 + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4=' + inp3 + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field5=' + inp2  )
    time.sleep(15)
    baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field3= 0'+ 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field5= 0' )
    
def servoStop():                                                            # IN CONTINOUS ROTATION MODE WHEN EVER A USER WANTS TO STOP THE SERVO MOTOR THEN HE/SHE HAS TO JUST PRESS THE STOP BUTTON AND THIS FUNCTION WILL BE EXECUTED.
    baseURL =  http.request('POST','https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field3= 0'+ 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field4= 0' + 'https://api.thingspeak.com/update?api_key=LNHX8YF2SUQ50UMW&field5= 0' )

if __name__ == '__main__':                            # THIS IS OUR MAIN PART OF THE PROGRAM BECAUSE HERE WE ARE MAKING OUR GRAPHICAL USER INTERFACE WHICH CONTAIN'S TEXT, LANEL'S AND BUTTON'S WHICH HELP'S US TO TAKE INPUT FROM THE USER

    root.title("IOT SYSTEM CONTROLLING")              # WHEN THE USER WILL PRESS A BUTTON OR A USER WILL ENTER THE VALUES THEN OUR GRAPHICAL USER INTERFACE WILL TAKE THESE VALUES AND WILL CHECK IN THE PROGRAM THAT WHAT IT HAS TO DO WITH THESE VALUES AND THEN ACCORDING TO THE TASK IT HAS TO PERFORM IT USE TO SEND ALL THE VALUES TO THE FUNCTION RELATED TO IT.  
    root.geometry("1000x1000")

                           
    root.configure(bg = 'yellow')
    
    
    tk.Label(root, text = "****** ",font = ('Ink free',20,'bold'),fg = "yellow",bg = "yellow").grid( row= 1,column = 0, sticky ='w') 
    tk.Label(root, text = "IOT BASED SYSTEM CONTROLLING ",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 2,column = 1, sticky ='w')
    tk.Label(root, text = "****** ",font = ('Ink free',10,'bold'),fg = "yellow",bg = "yellow").grid( row= 3,column = 0, sticky ='w')  
    tk.Label(root, text = "          Light Controlling ",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 4,column = 1, sticky ='w') 
    
     
    tk.Label(root, text = "Colour Name : ",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 5,column = 0, sticky ='w')
    name = tk.Entry(root,textvariable = take1, font=('calibre',20,'normal'), width = 30).grid( row= 5,column = 1,sticky ='w' )
    
    tk.Label(root, text = "Run Time : ",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 6,column = 0, sticky ='w')
    name1 = tk.Entry(root,textvariable = take4, font=('calibre',20,'normal'), width = 30).grid( row= 6,column = 1,sticky ='w' )
    
    sub_btn= tk.Button(root,text = 'APPLY', command = Switch, font=('calibre',20,'normal')).grid( row= 7,column = 0,sticky ='w' )
    tk.Label(root, text = "****** ",font = ('Ink free',20,'bold'),fg = "yellow",bg = "yellow").grid( row= 8,column = 0, sticky ='w')
    

    tk.Label(root, text = "            Motor Control ",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 9,column = 1, sticky ='w') 
    button1 = tk.Button(root,text = 'CLOCKWISE', command = clockwise, font =('Ink free',20,'bold'), bg='#fc0303', fg='#ffffff',state=ACTIVE, activebackground='#fc0303', activeforeground = '#ffffff').grid( row= 10,column = 0,sticky ='w' )
    button2 = tk.Button(root,text = 'STOP', command = stop, font =('Ink free',20,'bold'), bg='#fc0303', fg='#ffffff',state=ACTIVE, activebackground='#fc0303', activeforeground = '#ffffff').grid( row= 11,column = 0,sticky ='w' )
    button3 = tk.Button(root,text = 'ANTICLOCKWISE', command = anticlockwise, font =('Ink free',20,'bold'), bg='#fc0303', fg='#ffffff',state=ACTIVE, activebackground='#fc0303', activeforeground = '#ffffff').grid( row= 12,column = 0,sticky ='w' )
    tk.Label(root, text = "Run Time : ",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 13,column = 0, sticky ='w')
    name1 = tk.Entry(root,textvariable = take5, font=('calibre',20,'normal'), width = 30).grid( row= 13,column = 1,sticky ='w' )
    tk.Label(root, text = "*****",font = ('Ink free',20,'bold'),fg = "yellow",bg = "yellow").grid( row= 14,column = 0, sticky ='w')
    
    
    tk.Label(root, text = "             Servo Control",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 15,column = 1, sticky ='w')
    tk.Label(root, text = "Enter Angle in Degree : ",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 16,column = 0, sticky ='w')
    name1 = tk.Entry(root,textvariable = take2, font=('calibre',20,'normal'), width = 30).grid( row= 16,column = 1,sticky ='w' )
    tk.Label(root, text = "Number of Times : ",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 17,column = 0, sticky ='w')
    name1 = tk.Entry(root,textvariable = take3, font=('calibre',20,'normal'), width = 30).grid( row= 17,column = 1,sticky ='w' )
    tk.Label(root, text = "Run Time : ",font = ('Ink free',20,'bold'),fg = "red",bg = "yellow").grid( row= 18,column = 0, sticky ='w')
    name1 = tk.Entry(root,textvariable = take6, font=('calibre',20,'normal'), width = 30).grid( row= 18,column = 1,sticky ='w' )
    
    sub_btn = tk.Button(root,text = 'APPLY', command = servoApply, font=('calibre',20,'normal')).grid( row= 19,column = 0,sticky ='w' )
    button3 = tk.Button(root,text = 'Servo Stop', command = servoStop, font =('Ink free',20,'bold'), bg='#fc0303', fg='#ffffff',state=ACTIVE, activebackground='#fc0303', activeforeground = '#ffffff').grid( row= 20,column = 0,sticky ='w' )

root.mainloop()