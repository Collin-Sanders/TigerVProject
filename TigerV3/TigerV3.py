from guizero import App, PushButton, Box
from Properties import button_height, button_width, screen_width, \
screen_height, default_bg_color, image_names_off, image_names_on, \
page_button_width, page_button_height, on_text_color, off_text_color, \
strobe_text_color, back_text_color, page_text_size, strobe_images, \
mqtt_server_id, mqtt_port, mqtt_keepalive
import paho.mqtt.client as mqtt
import paho.mqtt.publish as mqtt_publish
import paho.mqtt.subscribe as mqtt_subscribe




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
############################### Helper Functions ##############################
###############################################################################
###############################################################################


def button_1_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("1", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("1", "OFF", "Send")
        
def button_2_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("2", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("2", "OFF", "Send")      
        
def button_3_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("3", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("3", "OFF", "Send")

def button_4_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("4", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("4", "OFF", "Send")
        
def button_5_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("5", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("5", "OFF", "Send")
        
def button_6_clicked(event_data):
    if(event_data.widget.text == "ON"):
        toggle("6", "ON", "Send")
    elif(event_data.widget.text == "OFF"):
        toggle("6", "OFF", "Send")       


 
def toggle(button_number, text, SoR):
   
    if(button_number == "1"):
        if(text == "ON"):
            button1.image = image_names_on[0]
        elif(text == "OFF"):
            button1.image = image_names_off[0]
            
    elif(button_number == "2"):
        if(text == "ON"):
            button2.image = image_names_on[1]
        elif(text == "OFF"):
            button2.image = image_names_off[1]
            
    elif(button_number == "3"): 
        if(text == "ON"):
            button3.image = image_names_on[2]
        elif(text == "OFF"):
            button3.image = image_names_off[2]
            
    elif(button_number == "4"):     
        if(text == "ON"):
            button4.image = image_names_on[3]
        elif(text == "OFF"):
            button4.image = image_names_off[3]
            
    elif(button_number == "5"):
        if(text == "ON"):
            button5.image = image_names_on[4]
        elif(text == "OFF"):
            button5.image = image_names_off[4]
            
    elif(button_number == "6"): 
        if(text == "ON"):
            button6.image = image_names_on[5]
        elif(text == "OFF"):
            button6.image = image_names_off[5]

    app.tk.update()
    
    #if(SoR == "Send"):
        #publish to mqtt
     #   mqtt_publish.single(button_number, text, hostname=mqtt_server_id)

###############################################################################
###############################################################################
############################### Button Functions ##############################
###############################################################################
###############################################################################

# Main Page Buttons
button1.when_clicked = button_1_clicked
button2.when_clicked = button_2_clicked
button3.when_clicked = button_3_clicked
button4.when_clicked = button_4_clicked
button5.when_clicked = button_5_clicked
button6.when_clicked = button_6_clicked


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


#def on_message(client, userdata, message):
#    topic = str(message.topic)
#    payload_string = str(message.payload)
#    payload = str(payload_string[2:len(payload_string)-1])
#    print(payload)
#    toggle(topic, payload, "Receive")
#mqtt_subscribe.callback(on_message, ["1", "2", "3", "4", "5", "6"], hostname=mqtt_server_id)    

