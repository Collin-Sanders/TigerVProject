"""
Name: Tiger V2
Creator: Collin Sanders
Date: 10-3-2019
Description: 6 button gui that controls auxillary accessories on 2009 Tacoma
"""
import tkinter as tk
import smbus
import time






#bus = smbus.SMBus(0) # Rev 1 Pi
bus = smbus.SMBus(1) # Rev 2 Pi
 
DEVICE = 0x20 # Device Address (A0-A2)
IODIRA = 0x00 # Pin Register direction
IODIRB = 0x01 # Pin Register direction
OLATB = 0x15 # Register for outputs (GPB)
GPIOA = 0x12 # Register for inputs (GPA)
 
# Define GPA pin 7 as input (10000000 = 0x80)
# Binary: 0 means output, 1 means input
bus.write_byte_data(DEVICE,IODIRA,0x80)
 
# Define all GPB pins as output (00000000 = 0x00)
bus.write_byte_data(DEVICE,IODIRB,0x00)
 
# Set all 7 output bits to 0
bus.write_byte_data(DEVICE,OLATB,0)


Taster = bus.read_byte_data(DEVICE,GPIOA)



button_text = [["Fog Lights", "Light Bar", "Winch"],
               ["Air Comp","Bed Lights", "Rock Lights"]]

override_list  = [0,0,0,0,0,0]
output_list    = [0,0,0,0,0,0]
switch_state   = [0,0,0,0,0,0]
software_state = [0,0,0,0,0,0]
temp_switch_state = [int(d) for d in list('{0:06b}'.format(Taster))]
switch_state = temp_switch_state[::-1]









button_counter = 1

button_color = "black"
default_off_text_color = "red"
default_on_text_color = "green"
font = ('Helvetica',18,'bold')
border_width = 20
button_relief = tk.RIDGE


 
# Function that makes all LEDs light up.
def send():
    
        temp = output_list[::-1]    
        
        to_send = (int(''.join(map(str,temp)),2))
            
        
        bus.write_byte_data(DEVICE,OLATB,to_send)
 


def btn_color_set():
    
    for i in range (6):
        button_number = i+1
        
        if(button_number > 3):
                 row_num = 1
                 column_num = button_number - 3
        else:
                 row_num = 0
                 column_num = button_number
                 
                 
        if(output_list[i] == 1):
            frame.grid_slaves(row = row_num, column = column_num-1)[0].config(fg = "green")
        else:
            frame.grid_slaves(row = row_num, column = column_num-1)[0].config(fg = "red")
    
    
def toggle(button_number):
    for i in range(1,7):
        if(button_number == i):
            if(software_state[i-1] == 1):
                software_state[i-1] = 0
            else:
                software_state[i-1] = 1
            

       


#Create & Configure root 
root = tk.Tk()
tk.Grid.rowconfigure(root, 0, weight=1)
tk.Grid.columnconfigure(root, 0, weight=1)

#Create & Configure frame 
frame=tk.Frame(root)
root.geometry("480x320")
root.overrideredirect(True)
frame.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)

#Create a 3x2 (rows x columns) grid of buttons inside the frame
for row_index in range(2):
    tk.Grid.rowconfigure(frame, row_index, weight=1)
    for col_index in range(3):
        tk.Grid.columnconfigure(frame, col_index, weight=1)
        btn = tk.Button(frame) #create a button inside frame 
        btn.config(text=button_text[row_index-1][col_index-1],
                   bg = button_color,
                   fg = default_off_text_color,
                   relief = button_relief,
                   font = font,
                   bd = border_width,
                   wraplength = 100,
                   activebackground = "black",
                   command = lambda button_counter=button_counter:
                       toggle(button_counter))
        button_counter += 1
        btn.grid(row=row_index, column=col_index, sticky=tk.N+tk.S+tk.E+tk.W) 




def update():
    # Read status of GPIOA register
    Taster = bus.read_byte_data(DEVICE,GPIOA)
    temp_switch_state = [int(d) for d in list('{0:06b}'.format(Taster))]
    switch_state = temp_switch_state[::-1]
    change_output(software_state, switch_state, output_list)
    btn_color_set()
    send()
    root.update()


def change_output(software_state, switch_state, output_list):
    
    for i in range(6):
        if(software_state[i] and switch_state[i]):
            override_list[i] = 1
        if((software_state[i] == 0) and (switch_state[i] == 0) and override_list[i] == 1):
            override_list[i] = 0      
        
        if((switch_state[i] == 1) and (software_state[i] == 0) and (override_list[i] == 0)):
            output_list[i] = 1
            software_state[i] = 1
            
        elif((switch_state[i] == 0) and (software_state[i] == 1) and (override_list[i] == 0  )):
            output_list[i] = 1
            switch_state[i] = 1
            
        elif((switch_state[i] == 1) and (software_state[i] == 0) and (override_list[i] == 1  )):
            output_list[i] = 0
            switch_state[i] = 0

        elif((switch_state[i] == 0) and (software_state[i] == 1) and (override_list[i] == 1  )):
            output_list[i] = 0
            software_state[i] = 0
            
        
            
        if((software_state[i] == 0) and (switch_state[i] == 0)):
            output_list[i] = 0
        
        
          
            
            

while 1:
    update()
    
