# print("Welcome to ZAY-AI let us plan your adventure")
# enter = int(input("1 - start or 2 - quit: "))
# while enter == 1:
#     destination = input("Do you have a destination in mind? ").lower()
#     if destination == "yes":
#         print("Let's plan your trip")
#         transport = input("So... what mode of transport do you wwanna use. (Plane/ Train or Car) ").lower()
#         if transport == "plane":
#             class_type = input("What fare would you like?(FirstClass/Business/Economy): ").lower()
#             luggage = int(input("Enter baggage weight in KG: "))
#             if luggage >= 20 and class_type == "business" or class_type == "firstclass":
#                 print("Great you can have more baggage with thes classes")
#             elif luggage < 20 and class_type == "business" or class_type == "first":
#                 print("You can bring more if you want!")
#             else:
#                 print("Warning oh you my have too much load")
#         elif transport == "train":
#             seat_class = input("Economy or business? ").lower()
#             if seat_class == "business":
#                 print("Great, hehe,have a beautiful and comfortable trip ")
#             elif seat_class == "economy":
#                 print("Welp, there you have it, you have gotta be careful here my friend \n Although this saves more though")

#             else:
#                 print(f"We actually do not have any class called {seat_class}")

#         elif  transport == "car":
#             print("Road trips are really fun")
#             num_people = int(input("How many poeople are there? "))
#             load = int(input("How much does your luggage weigh? "))
#             if load >= 100 and num_people > 5 :
#                 print("Your luggage is really full and the passengers are more than 5, so you should pick another car")
#             else:
#                 print("You can book a cab or a mini bus")
#         else:
#             print("We do not have that transport type")
#     elif destination == "no":
#         print("I can help you choose a destination fr")
#         destination_type = input("Beach/State/Country: ").lower()
#         if destination_type == "beach":
#             print("Wanna go to any Nigerian beach?")
#             beach_type = input("Popular or local beach?: ").lower()
#             if beach_type == "popular":
#                 print("Lagos bar-beach is an amazing and famous place")
#             elif beach_type == "local":
#                 print("Well you can go to Takwa Bay Beach which is still in Lagos")
#             else:
#                 print("We do not have that option")
#         elif destination_type == "state":
#             place_of_visit = input("State to visit (Abuja/Calabar/Lagos): ").lower()
#             if place_of_visit == "abuja":
#                 print("Welcome to Abuja a place of space unlike Lagos lol")
#             elif place_of_visit == "calabar":
#                 print("Welcome to Calabar a very beautiful city of wonders, beauties and festivals")
#             elif place_of_visit =="lagos":
#                 print("Welcome to Lagos a really nice place but over crowded, also one last thing is you should watch your back so your things would not be stolen")
#             else:
#                 print("What in the world did you type really because it is not a place")
#         elif destination_type =="country":
#             countries = ["USA", "India", "Nigeria","UK","Bangladesh", "Ukraine", "Israel"]
#             pick_countries = input("Pick a country: ").lower()
#             # print(f"{country}=>")
#             count = 0
#             for country in countries:
#                 if   pick_countries==country:
#                     count+=0
#                     print(f"Welcome to the {country}")
#                 # elif country == pick_countries:
#                 #     print("Namaste welcome to india")
#                 # elif country == pick_countries:
#                 #     print("Welcome to Naija")
#                 # elif country == pick_countries:
#                 #     print("Welcome to Bangladesh")
#                 # elif country == pick_countries:
#                 #     print("Welcome to Ukraine")
#                 # elif country == pick_countries:
#                 #     print("Welcome to Israel")
#                 else:
#                     print("Not a country")
#     elif destination =="no" or destination == "I said no" or destination == "I said nooooooo" or destination =="never":
#         print("Alright then...see ya")
# print("Enjoy your trip")
    
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, LabelFrame

class AdventurePlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("ZAY-AI Adventure Planner")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.style = ttk.Style()
        self.configure_styles()
        
        self.create_welcome_frame()
        
    def configure_styles(self):
        """Configure custom styles for the application"""
        self.style.configure('TFrame', background='#f0f8ff')
        self.style.configure('TLabel', background='#f0f8ff', font=('Helvetica', 10))
        self.style.configure('Header.TLabel', font=('Helvetica', 14, 'bold'), foreground='#2c3e50')
        self.style.configure('TButton', font=('Helvetica', 10), padding=5)
        self.style.configure('Accent.TButton', background='#3498db', foreground='white')
        self.style.configure('TRadiobutton', background='#f0f8ff')
        self.style.configure('TCombobox', padding=5)
        self.style.map('Accent.TButton',
                      background=[('active', '#2980b9'), ('pressed', '#1c6ca8')])
        
    def create_welcome_frame(self):
        """Create the welcome frame with start/quit options"""
        self.clear_window()
        
        welcome_frame = ttk.Frame(self.root, padding="20")
        welcome_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(welcome_frame, 
                          text="Welcome to ZAY-AI Adventure Planner", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        desc = ttk.Label(welcome_frame, 
                        text="Let us help you plan your perfect adventure!", 
                        wraplength=400)
        desc.pack(pady=10)
        
        btn_frame = ttk.Frame(welcome_frame)
        btn_frame.pack(pady=30)
        
        start_btn = ttk.Button(btn_frame, text="Start Planning", 
                              style='Accent.TButton',
                              command=self.create_destination_frame)
        start_btn.pack(side=tk.LEFT, padx=10)
        
        quit_btn = ttk.Button(btn_frame, text="Quit", 
                             command=self.root.quit)
        quit_btn.pack(side=tk.LEFT, padx=10)
        
    def create_destination_frame(self):
        """Frame to ask if user has a destination in mind"""
        self.clear_window()
        
        dest_frame = ttk.Frame(self.root, padding="20")
        dest_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(dest_frame, 
                          text="Destination Information", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        dest_q = ttk.Label(dest_frame, 
                          text="Do you have a destination in mind?")
        dest_q.pack(pady=10)
        
        self.destination_var = tk.StringVar(value="yes")
        
        yes_btn = ttk.Radiobutton(dest_frame, text="Yes", 
                                variable=self.destination_var, 
                                value="yes")
        no_btn = ttk.Radiobutton(dest_frame, text="No", 
                                variable=self.destination_var, 
                                value="no")
        yes_btn.pack()
        no_btn.pack()
        
        btn_frame = ttk.Frame(dest_frame)
        btn_frame.pack(pady=30)
        
        next_btn = ttk.Button(btn_frame, text="Next", 
                            style='Accent.TButton',
                            command=self.process_destination)
        next_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(btn_frame, text="Back", 
                             command=self.create_welcome_frame)
        back_btn.pack(side=tk.LEFT, padx=10)
        
    def process_destination(self):
        """Process destination choice and show appropriate next screen"""
        if self.destination_var.get() == "yes":
            self.create_transport_frame()
        else:
            self.create_suggest_destination_frame()
    
    def create_transport_frame(self):
        """Frame to select transportation method"""
        self.clear_window()
        
        transport_frame = ttk.Frame(self.root, padding="20")
        transport_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(transport_frame, 
                          text="Transportation Options", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        transport_q = ttk.Label(transport_frame, 
                              text="What mode of transport would you like to use?")
        transport_q.pack(pady=10)
        
        self.transport_var = tk.StringVar()
        
        transport_options = ["Plane", "Train", "Car"]
        transport_menu = ttk.Combobox(transport_frame, 
                                    textvariable=self.transport_var,
                                    values=transport_options,
                                    state="readonly")
        transport_menu.current(0)
        transport_menu.pack(pady=10)
        
        btn_frame = ttk.Frame(transport_frame)
        btn_frame.pack(pady=30)
        
        next_btn = ttk.Button(btn_frame, text="Next", 
                            style='Accent.TButton',
                            command=self.process_transport)
        next_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(btn_frame, text="Back", 
                             command=self.create_destination_frame)
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def process_transport(self):
        """Process transport choice and show appropriate details frame"""
        transport = self.transport_var.get().lower()
        
        if transport == "plane":
            self.create_plane_details_frame()
        elif transport == "train":
            self.create_train_details_frame()
        elif transport == "car":
            self.create_car_details_frame()
        else:
            messagebox.showerror("Error", "Please select a valid transport option")
    
    def create_plane_details_frame(self):
        """Frame for plane travel details"""
        self.clear_window()
        
        plane_frame = ttk.Frame(self.root, padding="20")
        plane_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(plane_frame, 
                          text="Plane Travel Details", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        # Class selection
        class_frame = LabelFrame(plane_frame, text="Travel Class", padx=10, pady=10)
        class_frame.pack(fill=tk.X, pady=10)
        
        self.class_var = tk.StringVar(value="economy")
        
        classes = [("First Class", "firstclass"), 
                  ("Business", "business"), 
                  ("Economy", "economy")]
        
        for text, value in classes:
            ttk.Radiobutton(class_frame, text=text, 
                          variable=self.class_var, 
                          value=value).pack(anchor=tk.W)
        
        # Luggage input
        luggage_frame = ttk.Frame(plane_frame)
        luggage_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(luggage_frame, text="Baggage weight (kg):").pack(side=tk.LEFT)
        
        self.luggage_var = tk.StringVar()
        luggage_entry = ttk.Entry(luggage_frame, textvariable=self.luggage_var)
        luggage_entry.pack(side=tk.LEFT, padx=10)
        
        btn_frame = ttk.Frame(plane_frame)
        btn_frame.pack(pady=30)
        
        submit_btn = ttk.Button(btn_frame, text="Submit", 
                              style='Accent.TButton',
                              command=self.process_plane_details)
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(btn_frame, text="Back", 
                             command=self.create_transport_frame)
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def process_plane_details(self):
        """Process plane details and show results"""
        try:
            luggage = int(self.luggage_var.get())
            class_type = self.class_var.get()
            
            if luggage >= 20 and class_type in ["business", "firstclass"]:
                message = "Great! You can have more baggage with these classes."
            elif luggage < 20 and class_type in ["business", "firstclass"]:
                message = "You can bring more if you want!"
            else:
                message = "Warning: You may have too much luggage for economy class."
            
            self.show_result(message)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for luggage weight")
    
    def create_train_details_frame(self):
        """Frame for train travel details"""
        self.clear_window()
        
        train_frame = ttk.Frame(self.root, padding="20")
        train_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(train_frame, 
                          text="Train Travel Details", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        # Seat class selection
        class_frame = LabelFrame(train_frame, text="Seat Class", padx=10, pady=10)
        class_frame.pack(fill=tk.X, pady=10)
        
        self.seat_class_var = tk.StringVar(value="economy")
        
        ttk.Radiobutton(class_frame, text="Business", 
                       variable=self.seat_class_var, 
                       value="business").pack(anchor=tk.W)
        ttk.Radiobutton(class_frame, text="Economy", 
                       variable=self.seat_class_var, 
                       value="economy").pack(anchor=tk.W)
        
        btn_frame = ttk.Frame(train_frame)
        btn_frame.pack(pady=30)
        
        submit_btn = ttk.Button(btn_frame, text="Submit", 
                              style='Accent.TButton',
                              command=self.process_train_details)
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(btn_frame, text="Back", 
                             command=self.create_transport_frame)
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def process_train_details(self):
        """Process train details and show results"""
        seat_class = self.seat_class_var.get()
        
        if seat_class == "business":
            message = "Great! Have a beautiful and comfortable trip."
        else:
            message = "Economy class saves money, but be careful with your belongings."
        
        self.show_result(message)
    
    def create_car_details_frame(self):
        """Frame for car travel details"""
        self.clear_window()
        
        car_frame = ttk.Frame(self.root, padding="20")
        car_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(car_frame, 
                          text="Road Trip Details", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        # Number of people
        people_frame = ttk.Frame(car_frame)
        people_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(people_frame, text="Number of people:").pack(side=tk.LEFT)
        
        self.people_var = tk.StringVar()
        people_entry = ttk.Entry(people_frame, textvariable=self.people_var)
        people_entry.pack(side=tk.LEFT, padx=10)
        
        # Luggage weight
        luggage_frame = ttk.Frame(car_frame)
        luggage_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(luggage_frame, text="Luggage weight (kg):").pack(side=tk.LEFT)
        
        self.car_luggage_var = tk.StringVar()
        luggage_entry = ttk.Entry(luggage_frame, textvariable=self.car_luggage_var)
        luggage_entry.pack(side=tk.LEFT, padx=10)
        
        btn_frame = ttk.Frame(car_frame)
        btn_frame.pack(pady=30)
        
        submit_btn = ttk.Button(btn_frame, text="Submit", 
                              style='Accent.TButton',
                              command=self.process_car_details)
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(btn_frame, text="Back", 
                             command=self.create_transport_frame)
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def process_car_details(self):
        """Process car details and show results"""
        try:
            num_people = int(self.people_var.get())
            load = int(self.car_luggage_var.get())
            
            if load >= 100 and num_people > 5:
                message = "Your luggage is really full and the passengers are more than 5, so you should pick another car."
            else:
                message = "You can book a cab or a mini bus."
            
            self.show_result(message)
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers for people and luggage")
    
    def create_suggest_destination_frame(self):
        """Frame to suggest destinations"""
        self.clear_window()
        
        suggest_frame = ttk.Frame(self.root, padding="20")
        suggest_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(suggest_frame, 
                          text="Destination Suggestions", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        type_q = ttk.Label(suggest_frame, 
                          text="What type of destination are you interested in?")
        type_q.pack(pady=10)
        
        self.dest_type_var = tk.StringVar()
        
        types = ["Beach", "State", "Country"]
        type_menu = ttk.Combobox(suggest_frame, 
                               textvariable=self.dest_type_var,
                               values=types,
                               state="readonly")
        type_menu.current(0)
        type_menu.pack(pady=10)
        
        btn_frame = ttk.Frame(suggest_frame)
        btn_frame.pack(pady=30)
        
        next_btn = ttk.Button(btn_frame, text="Next", 
                            style='Accent.TButton',
                            command=self.process_dest_type)
        next_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(btn_frame, text="Back", 
                             command=self.create_destination_frame)
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def process_dest_type(self):
        """Process destination type and show appropriate options"""
        dest_type = self.dest_type_var.get().lower()
        
        if dest_type == "beach":
            self.create_beach_options_frame()
        elif dest_type == "state":
            self.create_state_options_frame()
        elif dest_type == "country":
            self.create_country_options_frame()
        else:
            messagebox.showerror("Error", "Please select a valid destination type")
    
    def create_beach_options_frame(self):
        """Frame for beach destination options"""
        self.clear_window()
        
        beach_frame = ttk.Frame(self.root, padding="20")
        beach_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(beach_frame, 
                          text="Beach Destination Options", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        beach_q = ttk.Label(beach_frame, 
                          text="Would you like to visit a popular or local beach?")
        beach_q.pack(pady=10)
        
        self.beach_type_var = tk.StringVar(value="popular")
        
        ttk.Radiobutton(beach_frame, text="Popular Beach", 
                       variable=self.beach_type_var, 
                       value="popular").pack(anchor=tk.W)
        ttk.Radiobutton(beach_frame, text="Local Beach", 
                       variable=self.beach_type_var, 
                       value="local").pack(anchor=tk.W)
        
        btn_frame = ttk.Frame(beach_frame)
        btn_frame.pack(pady=30)
        
        submit_btn = ttk.Button(btn_frame, text="Submit", 
                              style='Accent.TButton',
                              command=self.process_beach_choice)
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(btn_frame, text="Back", 
                             command=self.create_suggest_destination_frame)
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def process_beach_choice(self):
        """Process beach choice and show results"""
        beach_type = self.beach_type_var.get()
        
        if beach_type == "popular":
            message = "Lagos Bar Beach is an amazing and famous place."
        else:
            message = "You can go to Takwa Bay Beach which is still in Lagos."
        
        self.show_result(message)
    
    def create_state_options_frame(self):
        """Frame for state destination options"""
        self.clear_window()
        
        state_frame = ttk.Frame(self.root, padding="20")
        state_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(state_frame, 
                          text="State Destination Options", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        state_q = ttk.Label(state_frame, 
                          text="Which state would you like to visit?")
        state_q.pack(pady=10)
        
        self.state_var = tk.StringVar()
        
        states = ["Abuja", "Calabar", "Lagos"]
        state_menu = ttk.Combobox(state_frame, 
                                textvariable=self.state_var,
                                values=states,
                                state="readonly")
        state_menu.current(0)
        state_menu.pack(pady=10)
        
        btn_frame = ttk.Frame(state_frame)
        btn_frame.pack(pady=30)
        
        submit_btn = ttk.Button(btn_frame, text="Submit", 
                              style='Accent.TButton',
                              command=self.process_state_choice)
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(btn_frame, text="Back", 
                             command=self.create_suggest_destination_frame)
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def process_state_choice(self):
        """Process state choice and show results"""
        state = self.state_var.get().lower()
        
        if state == "abuja":
            message = "Welcome to Abuja, a place of space unlike Lagos lol"
        elif state == "calabar":
            message = "Welcome to Calabar, a very beautiful city of wonders, beauties and festivals"
        elif state == "lagos":
            message = "Welcome to Lagos, a really nice place but overcrowded. Watch your belongings."
        else:
            message = "Please select a valid state."
        
        self.show_result(message)
    
    def create_country_options_frame(self):
        """Frame for country destination options"""
        self.clear_window()
        
        country_frame = ttk.Frame(self.root, padding="20")
        country_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(country_frame, 
                          text="Country Destination Options", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        country_q = ttk.Label(country_frame, 
                            text="Which country would you like to visit?")
        country_q.pack(pady=10)
        
        self.country_var = tk.StringVar()
        
        countries = ["USA", "India", "Nigeria", "UK", "Bangladesh", "Ukraine", "Israel"]
        country_menu = ttk.Combobox(country_frame, 
                                   textvariable=self.country_var,
                                   values=countries,
                                   state="readonly")
        country_menu.current(0)
        country_menu.pack(pady=10)
        
        btn_frame = ttk.Frame(country_frame)
        btn_frame.pack(pady=30)
        
        submit_btn = ttk.Button(btn_frame, text="Submit", 
                              style='Accent.TButton',
                              command=self.process_country_choice)
        submit_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = ttk.Button(btn_frame, text="Back", 
                             command=self.create_suggest_destination_frame)
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def process_country_choice(self):
        """Process country choice and show results"""
        country = self.country_var.get()
        
        if country == "USA":
            message = "Welcome to the United States of America!"
        elif country == "India":
            message = "Namaste! Welcome to India"
        elif country == "Nigeria":
            message = "Welcome to Naija!"
        elif country == "UK":
            message = "Welcome to the United Kingdom"
        elif country == "Bangladesh":
            message = "Welcome to Bangladesh"
        elif country == "Ukraine":
            message = "Welcome to Ukraine"
        elif country == "Israel":
            message = "Welcome to Israel"
        else:
            message = "Please select a valid country."
        
        self.show_result(message)
    
    def show_result(self, message):
        """Show the final result with the provided message"""
        self.clear_window()
        
        result_frame = ttk.Frame(self.root, padding="20")
        result_frame.pack(expand=True, fill=tk.BOTH)
        
        header = ttk.Label(result_frame, 
                          text="Your Adventure Plan", 
                          style='Header.TLabel')
        header.pack(pady=20)
        
        # Scrolled text for the message
        output = scrolledtext.ScrolledText(result_frame, 
                                        width=60, 
                                        height=10,
                                        wrap=tk.WORD,
                                        font=('Helvetica', 10))
        output.insert(tk.INSERT, message)
        output.configure(state='disabled')
        output.pack(pady=20)
        
        btn_frame = ttk.Frame(result_frame)
        btn_frame.pack(pady=30)
        
        new_btn = ttk.Button(btn_frame, text="Plan Another Adventure", 
                           style='Accent.TButton',
                           command=self.create_welcome_frame)
        new_btn.pack(side=tk.LEFT, padx=10)
        
        quit_btn = ttk.Button(btn_frame, text="Quit", 
                            command=self.root.quit)
        quit_btn.pack(side=tk.LEFT, padx=10)
    
    def clear_window(self):
        """Clear all widgets from the root window"""
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AdventurePlanner(root)
    root.mainloop()





