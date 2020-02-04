from guizero import App, PushButton, Box
from Properties import button_height, button_width, screen_width, \
screen_height, default_bg_color, image_names_off, image_names_on, \
page_button_width, page_button_height, on_text_color, off_text_color, \
strobe_text_color, back_text_color, page_text_size, strobe_images, \
mqtt_server_id, mqtt_port, mqtt_keepalive
import paho.mqtt.client as mqtt
import paho.mqtt.publish as mqtt_publish
import paho.mqtt.subscribe as mqtt_subscribe
import time








###############################################################################
###############################################################################
############################## Main App #######################################
###############################################################################
###############################################################################
    
app = \
    App(
        title="TigerV3", 
        height=str(screen_height), 
        width=str(screen_width), 
        layout="grid")
    
app.bg = default_bg_color 










###############################################################################
###############################################################################
############################## Button Boxes ###################################
###############################################################################
###############################################################################    

buttons_box_main = \
    Box(
        app, 
        layout="grid", 
        width="fill", 
        height="fill", 
        grid=[0,0])


buttons_box_1p1 = \
        Box(
            app, 
            layout="grid",
            visible=False,
            width="fill", 
            height="fill", 
            grid=[0,0])
        
buttons_box_2p1 = \
        Box(
            app, 
            layout="grid",
            visible=False,
            width="fill", 
            height="fill", 
            grid=[0,0])       

buttons_box_3p1 = \
        Box(
            app, 
            layout="grid",
            visible=False,
            width="fill", 
            height="fill", 
            grid=[0,0])
        
buttons_box_4p1 = \
        Box(
            app, 
            layout="grid",
            visible=False,
            width="fill", 
            height="fill", 
            grid=[0,0])
        
buttons_box_5p1 = \
        Box(
            app, 
            layout="grid",
            visible=False,
            width="fill", 
            height="fill", 
            grid=[0,0])
        
buttons_box_6p1 = \
        Box(
            app, 
            layout="grid",
            visible=False,
            width="fill", 
            height="fill", 
            grid=[0,0])        

###############################################################################
###############################################################################
############################# Main Page #######################################
###############################################################################
###############################################################################    

button1 = \
    PushButton(
        buttons_box_main, 
        image=image_names_off[0], 
        grid=[0,0], 
        width=button_width, 
        height=button_height,
        text="1")
button1.bg = default_bg_color

button2 = \
    PushButton(
        buttons_box_main, 
        image=image_names_off[1], 
        grid=[1,0],  
        width=button_width, 
        height=button_height,
        text="2")
button2.bg = default_bg_color

button3  = \
    PushButton(
        buttons_box_main, 
        image=image_names_off[2], 
        grid=[2,0],  
        width=button_width, 
        height=button_height,
        text="3")
button3.bg = default_bg_color

button4  = \
    PushButton(
        buttons_box_main, 
        image=image_names_off[3], 
        grid=[0,1],  
        width=button_width, 
        height=button_height,
        text="4")
button4.bg = default_bg_color

button5  = \
    PushButton(
        buttons_box_main, 
        image=image_names_off[4], 
        grid=[1,1],  
        width=button_width, 
        height=button_height,
        text="5")
button5.bg = default_bg_color

button6  = \
    PushButton(
        buttons_box_main, 
        image=image_names_off[5], 
        grid=[2,1],  
        width=button_width, 
        height=button_height,
        text="6")
button6.bg = default_bg_color

    






###############################################################################
###############################################################################
############################# Button 1 Page 1 #################################
###############################################################################
###############################################################################

button1p1b1 = \
    PushButton(
        buttons_box_1p1,
        grid=[0,0], 
        width=page_button_width, 
        height=page_button_height,
        text="ON")
button1p1b1.bg = default_bg_color
button1p1b1.text_color = on_text_color
button1p1b1.text_size = page_text_size

button1p1b2 = \
    PushButton(
        buttons_box_1p1,
        grid=[1,0],  
        width=page_button_width, 
        height=page_button_height,
        text="OFF")
button1p1b2.bg = default_bg_color
button1p1b2.text_color = off_text_color
button1p1b2.text_size = page_text_size    

button1p1b3  = \
    PushButton(
        buttons_box_1p1, 
        grid=[2,0],  
        width=page_button_width, 
        height=page_button_height,
        text="STROBE")
button1p1b3.bg = default_bg_color
button1p1b3.text_color = strobe_text_color
button1p1b3.text_size = page_text_size

button1p1b4  = \
    PushButton(
        buttons_box_1p1, 
        grid=[0,1],  
        width=page_button_width, 
        height=page_button_height,
        text="BACK")
button1p1b4.bg = default_bg_color
button1p1b4.text_color = back_text_color
button1p1b4.text_size = page_text_size

button1p1b5  = \
    PushButton(
        buttons_box_1p1,
        grid=[1,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button1p1b5.bg = default_bg_color
button1p1b5.text_size = page_text_size

button1p1b6  = \
    PushButton(
        buttons_box_1p1, 
        grid=[2,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button1p1b6.bg = default_bg_color
button1p1b6.text_size = page_text_size


###############################################################################
###############################################################################
############################# Button 2 Page 1 #################################
###############################################################################
###############################################################################

button2p1b1 = \
    PushButton(
        buttons_box_2p1,
        grid=[0,0], 
        width=page_button_width, 
        height=page_button_height,
        text="ON")
button2p1b1.bg = default_bg_color
button2p1b1.text_color = on_text_color
button2p1b1.text_size = page_text_size

button2p1b2 = \
    PushButton(
        buttons_box_2p1,
        grid=[1,0],  
        width=page_button_width, 
        height=page_button_height,
        text="OFF")
button2p1b2.bg = default_bg_color
button2p1b2.text_color = off_text_color
button2p1b2.text_size = page_text_size    

button2p1b3  = \
    PushButton(
        buttons_box_2p1, 
        grid=[2,0],  
        width=page_button_width, 
        height=page_button_height,
        text="STROBE")
button2p1b3.bg = default_bg_color
button2p1b3.text_color = strobe_text_color
button2p1b3.text_size = page_text_size

button2p1b4  = \
    PushButton(
        buttons_box_2p1, 
        grid=[0,1],  
        width=page_button_width, 
        height=page_button_height,
        text="BACK")
button2p1b4.bg = default_bg_color
button2p1b4.text_color = back_text_color
button2p1b4.text_size = page_text_size

button2p1b5  = \
    PushButton(
        buttons_box_2p1,
        grid=[1,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button2p1b5.bg = default_bg_color
button2p1b5.text_size = page_text_size

button2p1b6  = \
    PushButton(
        buttons_box_2p1, 
        grid=[2,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button2p1b6.bg = default_bg_color
button2p1b6.text_size = page_text_size




###############################################################################
###############################################################################
############################# Button 3 Page 1 #################################
###############################################################################
###############################################################################

button3p1b1 = \
    PushButton(
        buttons_box_3p1,
        grid=[0,0], 
        width=page_button_width, 
        height=page_button_height,
        text="ON")
button3p1b1.bg = default_bg_color
button3p1b1.text_color = on_text_color
button3p1b1.text_size = page_text_size

button3p1b2 = \
    PushButton(
        buttons_box_3p1,
        grid=[1,0],  
        width=page_button_width, 
        height=page_button_height,
        text="OFF")
button3p1b2.bg = default_bg_color
button3p1b2.text_color = off_text_color
button3p1b2.text_size = page_text_size    

button3p1b3  = \
    PushButton(
        buttons_box_3p1, 
        grid=[2,0],  
        width=page_button_width, 
        height=page_button_height,
        text="STROBE")
button3p1b3.bg = default_bg_color
button3p1b3.text_color = strobe_text_color
button3p1b3.text_size = page_text_size

button3p1b4  = \
    PushButton(
        buttons_box_3p1, 
        grid=[0,1],  
        width=page_button_width, 
        height=page_button_height,
        text="BACK")
button3p1b4.bg = default_bg_color
button3p1b4.text_color = back_text_color
button3p1b4.text_size = page_text_size

button3p1b5  = \
    PushButton(
        buttons_box_3p1,
        grid=[1,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button3p1b5.bg = default_bg_color
button3p1b5.text_size = page_text_size

button3p1b6  = \
    PushButton(
        buttons_box_3p1, 
        grid=[2,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button3p1b6.bg = default_bg_color
button3p1b6.text_size = page_text_size


###############################################################################
###############################################################################
############################# Button 4 Page 1 #################################
###############################################################################
###############################################################################

button4p1b1 = \
    PushButton(
        buttons_box_4p1,
        grid=[0,0], 
        width=page_button_width, 
        height=page_button_height,
        text="ON")
button4p1b1.bg = default_bg_color
button4p1b1.text_color = on_text_color
button4p1b1.text_size = page_text_size

button4p1b2 = \
    PushButton(
        buttons_box_4p1,
        grid=[1,0],  
        width=page_button_width, 
        height=page_button_height,
        text="OFF")
button4p1b2.bg = default_bg_color
button4p1b2.text_color = off_text_color
button4p1b2.text_size = page_text_size    

button4p1b3  = \
    PushButton(
        buttons_box_4p1, 
        grid=[2,0],  
        width=page_button_width, 
        height=page_button_height,
        text="STROBE")
button4p1b3.bg = default_bg_color
button4p1b3.text_color = strobe_text_color
button4p1b3.text_size = page_text_size

button4p1b4  = \
    PushButton(
        buttons_box_4p1, 
        grid=[0,1],  
        width=page_button_width, 
        height=page_button_height,
        text="BACK")
button4p1b4.bg = default_bg_color
button4p1b4.text_color = back_text_color
button4p1b4.text_size = page_text_size

button4p1b5  = \
    PushButton(
        buttons_box_4p1,
        grid=[1,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button4p1b5.bg = default_bg_color
button4p1b5.text_size = page_text_size

button4p1b6  = \
    PushButton(
        buttons_box_4p1, 
        grid=[2,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button4p1b6.bg = default_bg_color
button4p1b6.text_size = page_text_size





###############################################################################
###############################################################################
############################# Button 5 Page 1 #################################
###############################################################################
###############################################################################

button5p1b1 = \
    PushButton(
        buttons_box_5p1,
        grid=[0,0], 
        width=page_button_width, 
        height=page_button_height,
        text="ON")
button5p1b1.bg = default_bg_color
button5p1b1.text_color = on_text_color
button5p1b1.text_size = page_text_size

button5p1b2 = \
    PushButton(
        buttons_box_5p1,
        grid=[1,0],  
        width=page_button_width, 
        height=page_button_height,
        text="OFF")
button5p1b2.bg = default_bg_color
button5p1b2.text_color = off_text_color
button5p1b2.text_size = page_text_size    

button5p1b3  = \
    PushButton(
        buttons_box_5p1, 
        grid=[2,0],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button5p1b3.bg = default_bg_color
button5p1b3.text_size = page_text_size

button5p1b4  = \
    PushButton(
        buttons_box_5p1, 
        grid=[0,1],  
        width=page_button_width, 
        height=page_button_height,
        text="BACK")
button5p1b4.bg = default_bg_color
button5p1b4.text_color = back_text_color
button5p1b4.text_size = page_text_size

button5p1b5  = \
    PushButton(
        buttons_box_5p1,
        grid=[1,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button5p1b5.bg = default_bg_color
button5p1b5.text_size = page_text_size

button5p1b6  = \
    PushButton(
        buttons_box_5p1, 
        grid=[2,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button5p1b6.bg = default_bg_color
button5p1b6.text_size = page_text_size




###############################################################################
###############################################################################
############################# Button 6 Page 1 #################################
###############################################################################
###############################################################################

button6p1b1 = \
    PushButton(
        buttons_box_6p1,
        grid=[0,0], 
        width=page_button_width, 
        height=page_button_height,
        text="ON")
button6p1b1.bg = default_bg_color
button6p1b1.text_color = on_text_color
button6p1b1.text_size = page_text_size

button6p1b2 = \
    PushButton(
        buttons_box_6p1,
        grid=[1,0],  
        width=page_button_width, 
        height=page_button_height,
        text="OFF")
button6p1b2.bg = default_bg_color
button6p1b2.text_color = off_text_color
button6p1b2.text_size = page_text_size    

button6p1b3  = \
    PushButton(
        buttons_box_6p1, 
        grid=[2,0],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button6p1b3.bg = default_bg_color
button6p1b3.text_size = page_text_size

button6p1b4  = \
    PushButton(
        buttons_box_6p1, 
        grid=[0,1],  
        width=page_button_width, 
        height=page_button_height,
        text="BACK")
button6p1b4.bg = default_bg_color
button6p1b4.text_color = back_text_color
button6p1b4.text_size = page_text_size

button6p1b5  = \
    PushButton(
        buttons_box_6p1,
        grid=[1,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button6p1b5.bg = default_bg_color
button6p1b5.text_size = page_text_size

button6p1b6  = \
    PushButton(
        buttons_box_6p1, 
        grid=[2,1],  
        width=page_button_width, 
        height=page_button_height,
        text="")
button6p1b6.bg = default_bg_color
button6p1b6.text_size = page_text_size






###############################################################################
###############################################################################
############################### Helper Functions ##############################
###############################################################################
###############################################################################

def main_button_clicked(event_data):
    
    if(event_data.widget.text == "1"):
        buttons_box_main.hide()
        buttons_box_1p1.show()
    elif(event_data.widget.text == "2"):
        buttons_box_main.hide()
        buttons_box_2p1.show()
    elif(event_data.widget.text == "3"):
        buttons_box_main.hide()
        buttons_box_3p1.show()
    elif(event_data.widget.text == "4"):
        buttons_box_main.hide()
        buttons_box_4p1.show()
    elif(event_data.widget.text == "5"):
        buttons_box_main.hide()
        buttons_box_5p1.show()
    elif(event_data.widget.text == "6"):
        buttons_box_main.hide()
        buttons_box_6p1.show()    



def sub_1_button_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("1", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("1", "OFF", "Send")
    elif(event_data.widget.text == "STROBE"):
        toggle("1", "STROBE", "Send")    
    elif(event_data.widget.text == "BACK"):
        buttons_box_1p1.hide()
        buttons_box_main.show()
        
def sub_2_button_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("2", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("2", "OFF", "Send")
    elif(event_data.widget.text == "STROBE"):
        toggle("2", "STROBE", "Send")    
    elif(event_data.widget.text == "BACK"):
        buttons_box_2p1.hide()
        buttons_box_main.show()        
        
def sub_3_button_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("3", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("3", "OFF", "Send")
    elif(event_data.widget.text == "STROBE"):
        toggle("3", "STROBE", "Send")    
    elif(event_data.widget.text == "BACK"):
        buttons_box_3p1.hide()
        buttons_box_main.show()

def sub_4_button_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("4", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("4", "OFF", "Send")
    elif(event_data.widget.text == "STROBE"):
        toggle("4", "STROBE", "Send")    
    elif(event_data.widget.text == "BACK"):
        buttons_box_4p1.hide()
        buttons_box_main.show()
        
def sub_5_button_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("5", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("5", "OFF", "Send")
    elif(event_data.widget.text == "STROBE"):
        toggle("5", "STROBE", "Send")    
    elif(event_data.widget.text == "BACK"):
        buttons_box_5p1.hide()
        buttons_box_main.show()
        
def sub_6_button_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("6", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("6", "OFF", "Send")
    elif(event_data.widget.text == "STROBE"):
        toggle("6", "STROBE", "Send")    
    elif(event_data.widget.text == "BACK"):
        buttons_box_6p1.hide()
        buttons_box_main.show()        











def toggle(button_number, text, SoR):
   
    if(button_number == "1"):
        if(text == "STROBE"): 
            button1.image = strobe_images[0]
        elif(text == "ON"):
            button1.image = image_names_on[0]
        elif(text == "OFF"):
            button1.image = image_names_off[0]
            
    elif(button_number == "2"):
        if(text == "STROBE"): 
            button2.image = strobe_images[1]
        elif(text == "ON"):
            button2.image = image_names_on[1]
        elif(text == "OFF"):
            button2.image = image_names_off[1]
            
    elif(button_number == "3"):
        if(text == "STROBE"): 
            button3.image = strobe_images[2]  
        elif(text == "ON"):
            button3.image = image_names_on[2]
        elif(text == "OFF"):
            button3.image = image_names_off[2]
            
    elif(button_number == "4"):
        if(text == "STROBE"): 
            button4.image = strobe_images[3]     
        elif(text == "ON"):
            button4.image = image_names_on[3]
        elif(text == "OFF"):
            button4.image = image_names_off[3]
            
    elif(button_number == "5"):
        if(text == "STROBE"): 
            button5.image = strobe_images[4] 
        elif(text == "ON"):
            button5.image = image_names_on[4]
        elif(text == "OFF"):
            button5.image = image_names_off[4]
            
    elif(button_number == "6"):    
        if(text == "STROBE"): 
            button6.image = strobe_images[5] 
        elif(text == "ON"):
            button6.image = image_names_on[5]
        elif(text == "OFF"):
            button6.image = image_names_off[5]

    app.tk.update()
    
    if(SoR == "Send"):
        #publish to mqtt
        mqtt_publish.single(button_number, text, hostname=mqtt_server_id)

###############################################################################
###############################################################################
############################### Button Functions ##############################
###############################################################################
###############################################################################

# Main Page Buttons
button1.when_clicked = main_button_clicked
button2.when_clicked = main_button_clicked
button3.when_clicked = main_button_clicked
button4.when_clicked = main_button_clicked
button5.when_clicked = main_button_clicked
button6.when_clicked = main_button_clicked


# Button 1 Page 1 Buttons
button1p1b1.when_clicked = sub_1_button_clicked
button1p1b2.when_clicked = sub_1_button_clicked
button1p1b3.when_clicked = sub_1_button_clicked
button1p1b4.when_clicked = sub_1_button_clicked
button1p1b5.when_clicked = sub_1_button_clicked
button1p1b6.when_clicked = sub_1_button_clicked

# Button 2 Page 1 Buttons
button2p1b1.when_clicked = sub_2_button_clicked
button2p1b2.when_clicked = sub_2_button_clicked
button2p1b3.when_clicked = sub_2_button_clicked
button2p1b4.when_clicked = sub_2_button_clicked
button2p1b5.when_clicked = sub_2_button_clicked
button2p1b6.when_clicked = sub_2_button_clicked

# Button 3 Page 1 Buttons
button3p1b1.when_clicked = sub_3_button_clicked
button3p1b2.when_clicked = sub_3_button_clicked
button3p1b3.when_clicked = sub_3_button_clicked
button3p1b4.when_clicked = sub_3_button_clicked
button3p1b5.when_clicked = sub_3_button_clicked
button3p1b6.when_clicked = sub_3_button_clicked

# Button 4 Page 1 Buttons
button4p1b1.when_clicked = sub_4_button_clicked
button4p1b2.when_clicked = sub_4_button_clicked
button4p1b3.when_clicked = sub_4_button_clicked
button4p1b4.when_clicked = sub_4_button_clicked
button4p1b5.when_clicked = sub_4_button_clicked
button4p1b6.when_clicked = sub_4_button_clicked

# Button 5 Page 1 Buttons
button5p1b1.when_clicked = sub_5_button_clicked
button5p1b2.when_clicked = sub_5_button_clicked
button5p1b3.when_clicked = sub_5_button_clicked
button5p1b4.when_clicked = sub_5_button_clicked
button5p1b5.when_clicked = sub_5_button_clicked
button5p1b6.when_clicked = sub_5_button_clicked

# Button 6 Page 1 Buttons
button6p1b1.when_clicked = sub_6_button_clicked
button6p1b2.when_clicked = sub_6_button_clicked
button6p1b3.when_clicked = sub_6_button_clicked
button6p1b4.when_clicked = sub_6_button_clicked
button6p1b5.when_clicked = sub_6_button_clicked
button6p1b6.when_clicked = sub_6_button_clicked








###############################################################################
###############################################################################
############################### Show the Application ##########################
###############################################################################
###############################################################################

app.set_full_screen()
app.tk.update()


###############################################################################
###############################################################################
############################## MQTT Subscribe ##########################
###############################################################################
###############################################################################


def on_message(client, userdata, message):
    topic = str(message.topic)
    payload_string = str(message.payload)
    payload = str(payload_string[2:len(payload_string)-1])
    print(payload)
    toggle(topic, payload, "Receive")
mqtt_subscribe.callback(on_message, ["1", "2", "3", "4", "5", "6"], hostname=mqtt_server_id)    

