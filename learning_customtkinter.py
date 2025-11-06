import customtkinter as ct
from PIL import Image 
# initialisation

app = ct.CTk()
app.title("my app")
app.geometry("500x500")
# theme    
ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")
# button
"""
def b_c():
    my_label.configure(text = "HELLO WORLD")

button = ct.CTkButton(app,
                      text = "hello world",
                      command=b_c,
                      height= 150,
                      width= 200,
                      font=("New roman times",24),
                      fg_color="light blue",
                      hover_color="black",
                      corner_radius =25,
                      border_width= 5,
                      border_color= "orange")# state used to disable and normalize the animations
button.pack(padx=40, pady=40)
"""
# label
"""
my_label = ct.CTkLabel(app, text="")
my_label.pack(pady= 80)
"""

# Entry Widgets
"""
def Submit():
    my_label.configure(text=f"Hello {my_entry.get()}")
    my_entry.configure(state="disabled")

def clear():
    my_entry.delete(0,"end")
    my_entry.configure(state="normal")

my_entry = ct.CTkEntry(app,
                       placeholder_text="Enter your name:",
                       height= 100,
                       width= 500,
                       font=("New roman times",20),
                       corner_radius = 25,
                       text_color= "black",
                       placeholder_text_color="black",
                       fg_color =("green","light green"))
my_entry.pack(pady= 10)

my_label = ct.CTkLabel(app, text = "",font=("New roman times",20))
my_label.pack(pady= 20)

button = ct.CTkButton(app, text = "Submit", command = Submit,font=("New roman times",20))
button.pack(pady= 20)

clear_button = ct.CTkButton(app, text = "clear", command = clear,font=("New roman times",20))
clear_button.pack(pady= 10)
"""
# check box
"""
my_label = ct.CTkLabel(app, text = "",font=("New roman times",20))
my_label.pack(pady=10)

def game():
    if check.get() == "on":
        my_label.configure(text = "Let's play")
    else:
        my_label.configure(text = "Let's not play")
    text.set("awesome")
def clear():
    my_check.deselect()
    text.set("like to play a game")
check = ct.StringVar(value="off")
text = ct.StringVar(value="like to play a game")
my_check = ct.CTkCheckBox(app,
                          text="like to play a game",
                          variable=check,
                          onvalue = "on",
                          offvalue = "off",
                          checkbox_width=50,
                          checkbox_height=50,
                          font=("New roman times",24),
                          corner_radius=50,
                          fg_color = "green",
                          hover_color = "light blue",
                          textvariable = text)#hover=False
my_check.pack(pady=40)

my_button =ct.CTkButton(app,
                        text = "submit",
                        command = game)
my_button.pack(pady=10)

my_button2 =ct.CTkButton(app,
                        text = "clear",
                        command = clear)
my_button2.pack(pady=10)

my_toggle_button = ct.CTkButton(app,
                        text = "toggle",
                        command = my_check.toggle)
my_toggle_button.pack(pady=10)
my_select_button = ct.CTkButton(app,
                        text = "select",
                        command = my_check.select)
my_select_button.pack(pady=10)
"""
#combo box
"""
def color_picker():
        output_label.configure(text=my_combo.get(), text_color=my_combo.get())

def color_picker2():
        my_combo.set("yellow")
        output_label.configure(text=my_combo.get(), text_color=my_combo.get())

my_label = ct.CTkLabel(app, text = "pick a color", font=("New roman times",24))
my_label.pack(pady=40)

colors = ["default","red", "blue", "green"]
my_combo = ct.CTkComboBox(app,
                          values = colors,
                          height = 50,
                          width = 400,
                          font=("New roman times",18),
                          dropdown_font=("New roman times",18),
                          corner_radius=40,
                          border_width=5,
                          border_color="lightblue",
                          button_color="lightblue",
                          button_hover_color="lightgreen",
                          dropdown_hover_color="lightgreen",
                          dropdown_fg_color="lightblue",
                          dropdown_text_color="black",
                          text_color="lightblue",
                          justify="center",
                          s)#hover #state
my_combo.pack(pady=0)

my_botton = ct.CTkButton(app,
                         text="submit",
                         font=("New roman times",18),
                         command=color_picker)
my_botton.pack(pady=20)

my_botton2 = ct.CTkButton(app,
                          text="yellow",
                          font=("New roman times",18),
                          command=color_picker2)
my_botton2.pack(pady=0)

output_label = ct.CTkLabel(app,
                           text = "",
                           font=("New roman times",24))
output_label.pack(pady=40)
"""
#progress bar
"""
def clicker():
    my_progress.step()
    my_label.configure(text=int((my_progress.get())*100))

def start():
    my_progress.start()

def stop():
    my_progress.stop()

my_progress = ct.CTkProgressBar(app,
                                mode="indeterminate",
                                determinate_speed=5,
                                indeterminate_speed=.5,
                                height = 50,
                                width = 400,
                                border_width=5,
                                border_color="lightgreen",
                                fg_color="green",
                                progress_color="lightblue")#orientation
my_progress.pack(pady=20)
my_progress.set(0)


my_botton = ct.CTkButton(app,
                         text="click_me",
                         font=("New roman times",18),
                         command=clicker)
my_botton.pack(padx=10)

start_botton = ct.CTkButton(app,
                         text="start",
                         font=("New roman times",18),
                         command=start)
start_botton.pack(padx=10)

stop_botton = ct.CTkButton(app,
                         text="stop",
                         font=("New roman times",18),
                         command=stop)
stop_botton.pack(padx=10)


my_label = ct.CTkLabel(app,
                       text = "",
                       font=("New roman times",24))
my_label.pack(pady=40)
"""

#Radio buttons
"""
def rad():
    if radio_var.get() == "other":
        my_label2.configure(text="bruh make a selection")
    elif radio_var.get() == "yes":
        my_label2.configure(text="Ofcourse you do like pizzas!")
    else:
        my_label2.configure(text="bruh doesn't like pizzas\n what kind of person are you\n bruh what's wrong with you")

my_label = ct.CTkLabel(app,
                      text = "you like pizza?",
                      font=("New roman times",24))
my_label.pack(pady=40)

radio_var = ct.StringVar(value="other")
my_radio1 = ct.CTkRadioButton(app,
                              text="yes i do",
                              value="yes",
                              variable=radio_var,
                              #width=20,
                              #height=20,
                              radiobutton_width=30,
                              radiobutton_height=30,
                              corner_radius=1,
                              border_width_unchecked=2,
                              border_width_checked=5,
                              border_color="lightgreen",
                              hover_color="lightblue",
                              fg_color="green",
                              text_color="red",
                              font=("New roman times",24))
#hover=False state="disabled" text_color_disabled="green"
my_radio1.pack(pady=10)

my_radio2 = ct.CTkRadioButton(app,
                              text="no i don't",
                              value="no",
                              variable=radio_var,
                              #width=20,
                              #height=20
                              radiobutton_width=30,
                              radiobutton_height=30
                              )
my_radio2.pack(pady=10)

my_button = ct.CTkButton(app,
                         text="Select",
                         command=rad)
my_button.pack(pady=10)

my_label2 = ct.CTkLabel(app,
                      text = "",
                      font=("New roman times",24))
my_label2.pack(pady=10)
"""

# Scrollable Frame
"""
my_sor_fra = ct.CTkScrollableFrame(app,
                                   width=300,
                                   height=200,
                                   label_text="Hello World",
                                   label_fg_color="lightgreen",
                                   label_text_color="black",
                                   label_font=("Helvetica",18),
                                   label_anchor="w",# w, n, ne, e, se, s, sw, w, nw, center
                                   border_width=3,
                                   border_color="green",
                                   fg_color="lightblue",
                                   scrollbar_fg_color="lightgreen",
                                   scrollbar_button_color="black",
                                   scrollbar_button_hover_color="blue",
                                   corner_radius=20) 
                                   #orientation="horizontal
my_sor_fra.pack(pady=40)

for i in range(20):
    ct.CTkButton(my_sor_fra, text="This is a button!!").pack(pady=10)
"""

# Segmented button
"""
def clicker(value):
    my_label.configure(text=f"Hello {value}")# my_seg.get()


my_values = ["John","Ayush","Manthan"]
my_seg = ct.CTkSegmentedButton(app,
                               values=my_values,
                               command=clicker,
                               width=300,
                               height=50,
                               font=("Helvetica", 18),
                               corner_radius=40,
                               border_width=5,
                               fg_color="lightgreen",
                               selected_color="black",
                               selected_hover_color="purple",
                               unselected_color="grey",
                               unselected_hover_color="lightblue",
                               dynamic_resizing=True)
                               # text_color, state, text_color_disabled
my_seg.pack(pady=40)
my_seg.set("Ayush")

my_label = ct.CTkLabel(app,
                       text="",
                       font=("Helvetica", 18))
my_label.pack(pady=20)
"""

# Slider
"""
def sliding(value):
    my_label.configure(text=int(value))

my_slider = ct.CTkSlider(app,
                         from_=0,
                         to=100,
                         command=sliding,
                         orientation="horizontal",
                         number_of_steps=10,
                         width=400,
                         height=50,
                         #border_width=20
                         fg_color="lightblue",
                         progress_color="lightgreen",
                         button_color="purple",
                         #button_hover_color="purple",
                         # state = disabled
                         hover=False)
my_slider.pack(pady=20)
my_slider.set(0)
my_label = ct.CTkLabel(app,
                       text=my_slider.get(),
                       font=("Helvetica", 18))
my_label.pack(pady=20)
"""
# Switch widget
"""
def switcher():
    my_label.configure(text=switch_var.get())
def clicker():
    my_switch.toggle()
switch_var = ct.StringVar(value="off")
my_switch = ct.CTkSwitch(app,
                         text="Switch",
                         command=switcher,
                         variable=switch_var,
                         onvalue="on",
                         offvalue="off",
                         #width=200,
                         #height=25,
                         switch_width=50,
                         switch_height=25,
                         #corner_radius=10
                         border_color="green",
                         border_width=5,
                         fg_color="red",
                         progress_color="blue",
                         button_color="lightgreen",
                         button_hover_color="purple",
                         font=("Helvetica", 18),
                         text_color="violet")
                        #state 
my_switch.pack(padx=80,pady=40)

my_label = ct.CTkLabel(app,
                       text="",
                       font=("Helvetica", 18))
my_label.pack(pady=20)

my_button = ct.CTkButton(app,
                         text="toggle",
                         command=clicker)
my_button.pack(pady=10)
"""

# Tab view
"""
def clicker():
    my_button.configure(text="You clicked me")


my_tab = ct.CTkTabview(app,
                       width=1280,
                       height=720,
                       corner_radius=10,
                       fg_color="silver",
                       segmented_button_fg_color="lightgreen",
                       segmented_button_selected_color="blue",
                       segmented_button_selected_hover_color="purple",
                       segmented_button_unselected_hover_color="green",
                       segmented_button_unselected_color="yellow",
                       command=clicker,
                       anchor="w")
                        # text_color, state
my_tab.pack(pady=10)

tab_1 = my_tab.add("tab 1")
tab_2 = my_tab.add("tab 2")

my_button = ct.CTkButton(tab_1,
                         text="toggle")
my_button.pack(pady=10)
"""

# text box
"""
thing = ''

def delete():
    my_textBox.delete(0.0,'end')
def copy():
    global thing
    thing = my_textBox.get(0.0,'end')
def paste():
    if thing:
        my_textBox.insert('end',thing)
    else:
        my_textBox.insert('end', "there is nothing to paste")

my_textBox = ct.CTkTextbox(app,
                           width=600,
                           height=300,
                           corner_radius=25,
                           border_width=10,
                           border_color="lightblue",
                           border_spacing=20,
                           fg_color="silver",
                           text_color="black",
                           font=("helvetica",30),
                           wrap="word",# default, word, none, char
                           scrollbar_button_color="lightblue",
                           scrollbar_button_hover_color="lightgreen") # activate_scrollbars = True/False
my_textBox.pack(pady=10)

my_frame = ct.CTkFrame(app)
my_frame.pack(pady=10)

del_bun = ct.CTkButton(my_frame,
                       text="delete button",
                       command=delete)

copy_bun = ct.CTkButton(my_frame,
                       text="copy button",
                       command=copy)

paste_bun = ct.CTkButton(my_frame,
                       text="paste button",
                       command=paste)

del_bun.grid(row=0, column=0 ,padx=10)
copy_bun.grid(row=0, column=1 ,padx=10)
paste_bun.grid(row=0, column=2 ,padx=10)
"""

# Input popup box also known as input dialog box
"""
def input():
    dialog = ct.CTkInputDialog(text = "what is your name",
                               title = "hello there",
                               fg_color="lightblue",
                               button_fg_color="lightgreen",
                               button_hover_color="purple",
                               button_text_color="black",
                               entry_fg_color="green",
                               entry_border_color="black",
                               entry_text_color="black")
    thing = dialog.get_input()
    if thing:
        my_label.configure(text=f"your name is {thing}")
    else:
        my_label.configure(text="bruh type something")
my_button = ct.CTkButton(app,
                         text="Click Me",
                         command=input)
my_button.pack(pady=40)

my_label = ct.CTkLabel(app,
                       text='')
my_label.pack(pady=10)
"""

# New top level windows
"""
def new():
    new_window = ct.CTkToplevel(app,
                                fg_color="white")
    new_window.title("this is a new window")
    new_window.geometry("400x200")
    #new_window.resizable(False,False)# width, height 
    def close():
        new_window.destroy()
        new_window.update()
    close_window = ct.CTkButton(new_window,
                            text="close button",
                            command=close)
    close_window.pack(pady=20)

my_button = ct.CTkButton(app,
                         text="open new window",
                         command=new)
my_button.pack(pady=40)
"""

# Custom font widget
"""
def change():
    my_font.configure(underline=False,
                      overstrike=False,
                      size=200,
                      slant="italic")


my_font = ct.CTkFont(family="JetsBrain",
                     size=100,
                     weight="bold",
                     slant="roman",
                     underline=True,
                     overstrike=True)
#weight = bold, normal, slant = italic, roman
my_label = ct.CTkLabel(app,
                       text="this is a text",
                       font=my_font)
my_label.pack(pady=40)

my_button = ct.CTkButton(app,
                         text="change the font",
                         command=change)
my_button.pack(pady=40)
"""

# Images


# Option Menu
"""
def tog():
    my_label.configure(text = my_option_menu.get(),
                       text_color = my_option_menu.get())
def clicker(choice):
    my_label.configure(text = choice,
                       text_color = choice)
my_option_menu = ct.CTkOptionMenu(app,
                                  values=["red","blue","green"],
                                  height=50,
                                  width=200,
	                          font=("Helvetica", 18),
	                          fg_color="white",
	                          dropdown_font=("Helvetica", 18),
	                          corner_radius=50,
                                  button_color="red",
	                          button_hover_color="green",
	                          dropdown_hover_color="green",
	                          dropdown_fg_color="blue",
	                          dropdown_text_color="orange",
	                          text_color="red",
	                          hover=True,
	                          anchor="center", # n-s-e-w-center
	                          state="normal",
	                          text_color_disabled="black",
	                          dynamic_resizing=False, )
                                  #command=clicker)
my_option_menu.pack(pady=0)
my_label = ct.CTkLabel(app,
                       text="",
                       font=("Helvetica",20))
my_label.pack(pady=40)

my_button = ct.CTkButton(app,
                         text="pick a color",
                         command=tog)
my_button.pack(pady=10)
"""

# Switching Between Light and Dark Mode
"""
def theme(choice):
    ct.set_default_color_theme(choice)

mode = "dark"
def change():
    global mode
    if mode == "dark":
        ct.set_appearance_mode("light")
        mode = "light"
        my_text.delete("0.0","end")
        my_text.insert("0.0","this is light mode..")
    else:
        ct.set_appearance_mode("dark")
        mode = "dark"
        my_text.delete("0.0","end")
        my_text.insert("0.0","this is dark mode..")
my_text = ct.CTkTextbox(app,
                        width=400,
                        height=200)
my_text.pack(pady=10)

my_button = ct.CTkButton(app,
                         text="change theme",
                         command=change)
my_button.pack(pady=10)

my_option = ct.CTkOptionMenu(app,
                             values=["green","blue","dark-blue"],
                             command=theme)
my_option.pack(pady=10)

"""
# scaling
"""
ct.deactivate_automatic_dpi_awareness()

ct.set_window_scaling(1.0)
ct.set_widget_scaling(1.0)
"""

# Object Oriented
"""
class App(ct.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("my app")
        self.geometry("500x500")

        self.my_text = ct.CTkTextbox(self,
                                width=400,
                                height=350)
        self.my_text.pack(pady=40)

        self.my_button = ct.CTkButton(self,
                                 text="clear box",
                                 command=self.clear)
        self.my_button.pack(pady=10)
        
    def clear(self):
        self.my_text.delete('0.0','end')
        
        
app = App()
"""

# Widget Animation
global my_y
my_y = 500/2 + 400
def up():
    global my_y
    my_y -= 20
    if my_y >= 200:
        my_text.place(x=500/2,y=my_y,anchor='center')
        app.after(5,up)
    
def down():
    global my_y
    my_y += 20
    if my_y <= 700:
        my_text.place(x=500/2,y=my_y,anchor='center')
        app.after(5,down)

my_frame = ct.CTkFrame(app)
my_frame.pack(pady=20)

up_button = ct.CTkButton(my_frame,
                         text="Up",
                         command=up)
up_button.grid(row=0, column=0, padx=10, pady=10)

down_button = ct.CTkButton(my_frame,
                           text="Down",
                           command=down)
down_button.grid(row=0, column=1, padx=10, pady=10)

my_text = ct.CTkFrame(app,
                        width=400,
                        height=200)
my_text.place(x=500/2,y=my_y,anchor='center')

app.mainloop()
