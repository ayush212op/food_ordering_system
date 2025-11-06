import customtkinter as ct
import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image
# Removed import ImageTk

app = ct.CTk()
app.geometry("1280x720+150+50")
app.title("Restaurant Menu")
ct.set_appearance_mode("dark")
app.configure(fg_color="#fcec9a")

# ----- MENU -----
menu = {
    1: {"name": "Margherita Pizza", "price": 250, "category": "Pizza", "description": "Classic pizza with mozzarella cheese and tomato sauce", "veg": True, "rating": 4.6},
    2: {"name": "Farmhouse Pizza", "price": 280, "category": "Pizza", "description": "Loaded with fresh veggies like capsicum, tomato, and onion", "veg": True, "rating": 4.7},
    3: {"name": "Pepperoni Pizza", "price": 320, "category": "Pizza", "description": "Spicy pepperoni slices with extra cheese", "veg": False, "rating": 4.5},
    4: {"name": "Cheese Burst Pizza", "price": 350, "category": "Pizza", "description": "Extra cheesy goodness inside the crust", "veg": True, "rating": 4.8},
    5: {"name": "Tandoori Paneer Pizza", "price": 300, "category": "Pizza", "description": "Paneer tikka flavor with tandoori masala", "veg": True, "rating": 4.6},
    6: {"name": "BBQ Chicken Pizza", "price": 350, "category": "Pizza", "description": "Smoky BBQ chicken topping with mozzarella", "veg": False, "rating": 4.7},
    7: {"name": "Veg Burger", "price": 120, "category": "Burger", "description": "Crispy veg patty with lettuce, tomato & mayo", "veg": True, "rating": 4.4},
    8: {"name": "Chicken Burger", "price": 150, "category": "Burger", "description": "Juicy chicken patty with mayo and lettuce", "veg": False, "rating": 4.3},
    9: {"name": "Paneer Burger", "price": 140, "category": "Burger", "description": "Paneer patty with cheese and spicy sauce", "veg": True, "rating": 4.5},
    10: {"name": "Double Patty Burger", "price": 180, "category": "Burger", "description": "Two layers of patty with cheese and veggies", "veg": True, "rating": 4.6},
    11: {"name": "White Sauce Pasta", "price": 200, "category": "Pasta", "description": "Creamy white sauce pasta with veggies", "veg": True, "rating": 4.5},
    12: {"name": "Red Sauce Pasta", "price": 180, "category": "Pasta", "description": "Tangy red sauce pasta with herbs", "veg": True, "rating": 4.4},
    13: {"name": "Mac & Cheese", "price": 220, "category": "Pasta", "description": "Classic macaroni with cheesy sauce", "veg": True, "rating": 4.6},
    14: {"name": "Grilled Cheese Sandwich", "price": 100, "category": "Snack", "description": "Toasted sandwich with melted cheese", "veg": True, "rating": 4.3},
    15: {"name": "Club Sandwich", "price": 120, "category": "Snack", "description": "Triple layered sandwich with veggies & chicken", "veg": False, "rating": 4.4},
    16: {"name": "French Fries", "price": 90, "category": "Snack", "description": "Crispy golden fries with ketchup", "veg": True, "rating": 4.5},
    17: {"name": "Peri Peri Fries", "price": 100, "category": "Snack", "description": "Spicy peri peri flavored fries", "veg": True, "rating": 4.6},
    18: {"name": "Chili Cheese Fries", "price": 120, "category": "Snack", "description": "Fries topped with chili and melted cheese", "veg": True, "rating": 4.7},
    19: {"name": "Chowmein Noodles", "price": 150, "category": "Noodles", "description": "Stir-fried noodles with veggies", "veg": True, "rating": 4.4},
    20: {"name": "Schezwan Noodles", "price": 160, "category": "Noodles", "description": "Spicy Schezwan noodles with sauces", "veg": True, "rating": 4.5},
    21: {"name": "Hakka Noodles", "price": 170, "category": "Noodles", "description": "Classic Hakka style noodles", "veg": True, "rating": 4.6},
    22: {"name": "Paneer Manchurian", "price": 200, "category": "Main Course", "description": "Paneer tossed in tangy Manchurian sauce", "veg": True, "rating": 4.7},
    23: {"name": "Chicken Manchurian", "price": 220, "category": "Main Course", "description": "Chicken in spicy Manchurian gravy", "veg": False, "rating": 4.6},
    24: {"name": "Spring Rolls", "price": 130, "category": "Snack", "description": "Crispy rolls stuffed with veggies", "veg": True, "rating": 4.4},
    25: {"name": "Fried Rice", "price": 150, "category": "Rice", "description": "Classic fried rice with veggies", "veg": True, "rating": 4.5},
    26: {"name": "Egg Fried Rice", "price": 170, "category": "Rice", "description": "Fried rice with scrambled eggs and veggies", "veg": False, "rating": 4.5},
    27: {"name": "Chicken Fried Rice", "price": 200, "category": "Rice", "description": "Fried rice with juicy chicken pieces", "veg": False, "rating": 4.6},
    28: {"name": "Paneer Butter Masala", "price": 250, "category": "Main Course", "description": "Soft paneer cubes in creamy butter gravy", "veg": True, "rating": 4.7},
    29: {"name": "Kadhai Paneer", "price": 260, "category": "Main Course", "description": "Paneer cooked with capsicum in spicy kadahi masala", "veg": True, "rating": 4.6},
    30: {"name": "Palak Paneer", "price": 240, "category": "Main Course", "description": "Paneer in rich spinach gravy", "veg": True, "rating": 4.5},
    31: {"name": "Chicken Curry", "price": 280, "category": "Main Course", "description": "Tender chicken cooked in spicy curry gravy", "veg": False, "rating": 4.6},
    32: {"name": "Butter Chicken", "price": 300, "category": "Main Course", "description": "Creamy tomato-based chicken curry", "veg": False, "rating": 4.7},
    33: {"name": "Mutton Rogan Josh", "price": 350, "category": "Main Course", "description": "Classic spicy mutton curry", "veg": False, "rating": 4.8},
    34: {"name": "Dal Makhani", "price": 200, "category": "Main Course", "description": "Creamy black lentils cooked with butter", "veg": True, "rating": 4.6},
    35: {"name": "Rajma Chawal", "price": 180, "category": "Main Course", "description": "Red kidney beans curry with steamed rice", "veg": True, "rating": 4.5},
    36: {"name": "Chole Bhature", "price": 160, "category": "Main Course", "description": "Spicy chickpeas with fried bread", "veg": True, "rating": 4.5},
    37: {"name": "Poori Sabzi", "price": 140, "category": "Main Course", "description": "Deep-fried poori with vegetable curry", "veg": True, "rating": 4.4},
    38: {"name": "Veg Thali", "price": 250, "category": "Thali", "description": "Assorted vegetarian dishes with roti and rice", "veg": True, "rating": 4.6},
    39: {"name": "Non-Veg Thali", "price": 320, "category": "Thali", "description": "Assorted non-veg dishes with roti and rice", "veg": False, "rating": 4.7},
    40: {"name": "Butter Naan", "price": 40, "category": "Bread", "description": "Soft naan brushed with butter", "veg": True, "rating": 4.5},
    41: {"name": "Garlic Naan", "price": 50, "category": "Bread", "description": "Naan flavored with garlic and butter", "veg": True, "rating": 4.6},
    42: {"name": "Tandoori Roti", "price": 30, "category": "Bread", "description": "Whole wheat flatbread cooked in tandoor", "veg": True, "rating": 4.4},
    43: {"name": "Stuffed Paratha", "price": 80, "category": "Bread", "description": "Paratha stuffed with spiced filling", "veg": True, "rating": 4.5},
    44: {"name": "Aloo Paratha", "price": 70, "category": "Bread", "description": "Flatbread stuffed with spicy potato filling", "veg": True, "rating": 4.5},
    45: {"name": "Paneer Paratha", "price": 90, "category": "Bread", "description": "Flatbread stuffed with paneer filling", "veg": True, "rating": 4.6},
    46: {"name": "Dosa", "price": 120, "category": "South Indian", "description": "Crispy rice crepe served with chutney and sambar", "veg": True, "rating": 4.5},
    47: {"name": "Masala Dosa", "price": 140, "category": "South Indian", "description": "Dosa stuffed with spiced potato filling", "veg": True, "rating": 4.6},
    48: {"name": "Mysore Dosa", "price": 160, "category": "South Indian", "description": "Spicy chutney filled dosa from Mysore", "veg": True, "rating": 4.7},
    49: {"name": "Uttapam", "price": 130, "category": "South Indian", "description": "Thick pancake with toppings of veggies", "veg": True, "rating": 4.5},
    50: {"name": "Idli Sambar", "price": 100, "category": "South Indian", "description": "Steamed rice cakes served with sambar and chutney", "veg": True, "rating": 4.5},
    51: {"name": "Vada Sambar", "price": 110, "category": "South Indian", "description": "Deep-fried lentil doughnuts served with sambar", "veg": True, "rating": 4.5},
    52: {"name": "Pani Puri", "price": 60, "category": "Street Food", "description": "Crispy hollow puris filled with spicy flavored water", "veg": True, "rating": 4.7},
    53: {"name": "Sev Puri", "price": 80, "category": "Street Food", "description": "Flat puris topped with potatoes, sev, and chutneys", "veg": True, "rating": 4.6},
    54: {"name": "Dahi Puri", "price": 90, "category": "Street Food", "description": "Purified puris filled with curd, chutneys, and sev", "veg": True, "rating": 4.6},
    55: {"name": "Bhel Puri", "price": 100, "category": "Street Food", "description": "Puffed rice mixed with chutneys, onions, and spices", "veg": True, "rating": 4.5},
    56: {"name": "Pav Bhaji", "price": 150, "category": "Street Food", "description": "Spiced mashed vegetable curry served with buttered bread", "veg": True, "rating": 4.7},
    57: {"name": "Misal Pav", "price": 140, "category": "Street Food", "description": "Spicy sprouted bean curry served with pav", "veg": True, "rating": 4.6},
    58: {"name": "Soft Drink", "price": 70, "category": "Beverage", "description": "Refreshing chilled soft drink", "veg": True, "rating": 4.3},
    59: {"name": "Cold Coffee", "price": 100, "category": "Beverage", "description": "Chilled coffee with milk and sugar", "veg": True, "rating": 4.5},
    60: {"name": "Hot Tea", "price": 50, "category": "Beverage", "description": "Classic hot brewed tea", "veg": True, "rating": 4.4},
    61: {"name": "Ginger Tea", "price": 60, "category": "Beverage", "description": "Hot tea infused with ginger flavor", "veg": True, "rating": 4.5},
    62: {"name": "Masala Chai", "price": 70, "category": "Beverage", "description": "Spiced Indian tea with milk", "veg": True, "rating": 4.6},
    63: {"name": "Green Tea", "price": 80, "category": "Beverage", "description": "Healthy green tea infusion", "veg": True, "rating": 4.4},
    64: {"name": "Lassi", "price": 90, "category": "Beverage", "description": "Sweet yogurt-based drink", "veg": True, "rating": 4.5},
    65: {"name": "Buttermilk", "price": 80, "category": "Beverage", "description": "Refreshing salted buttermilk", "veg": True, "rating": 4.3},
    66: {"name": "Fresh Lime Soda", "price": 90, "category": "Beverage", "description": "Chilled soda with lime and sugar", "veg": True, "rating": 4.6},
    67: {"name": "Mango Shake", "price": 110, "category": "Beverage", "description": "Blended mango shake with ice cream", "veg": True, "rating": 4.7},
    68: {"name": "Chocolate Shake", "price": 120, "category": "Beverage", "description": "Chocolate flavored milkshake with ice cream", "veg": True, "rating": 4.6},
    69: {"name": "Strawberry Shake", "price": 130, "category": "Beverage", "description": "Blended strawberry shake with ice cream", "veg": True, "rating": 4.7},
    70: {"name": "Gulab Jamun", "price": 80, "category": "Dessert", "description": "Soft syrup-soaked sweet dumplings", "veg": True, "rating": 4.6},
    71: {"name": "Rasgulla", "price": 90, "category": "Dessert", "description": "Soft cheese balls in sugar syrup", "veg": True, "rating": 4.5},
    72: {"name": "Rasmalai", "price": 110, "category": "Dessert", "description": "Cheese patties in thickened milk flavored with cardamom", "veg": True, "rating": 4.6},
    73: {"name": "Jalebi", "price": 100, "category": "Dessert", "description": "Crispy deep-fried sugar spirals soaked in syrup", "veg": True, "rating": 4.4},
    74: {"name": "Kaju Katli", "price": 150, "category": "Dessert", "description": "Diamond-shaped cashew fudge", "veg": True, "rating": 4.7},
    75: {"name": "Motichoor Ladoo", "price": 130, "category": "Dessert", "description": "Sweet gram flour balls soaked in syrup", "veg": True, "rating": 4.6},
    76: {"name": "Chocolate Ice Cream", "price": 120, "category": "Dessert", "description": "Rich chocolate flavored ice cream", "veg": True, "rating": 4.6},
    77: {"name": "Vanilla Ice Cream", "price": 110, "category": "Dessert", "description": "Classic vanilla ice cream scoop", "veg": True, "rating": 4.5},
    78: {"name": "Strawberry Ice Cream", "price": 120, "category": "Dessert", "description": "Strawberry flavored ice cream scoop", "veg": True, "rating": 4.6},
    79: {"name": "Butterscotch Ice Cream", "price": 130, "category": "Dessert", "description": "Butterscotch flavored ice cream scoop", "veg": True, "rating": 4.7},
    80: {"name": "Fruit Salad", "price": 140, "category": "Dessert", "description": "Fresh seasonal fruits chopped and served", "veg": True, "rating": 4.5},
    81: {"name": "Brownie", "price": 160, "category": "Dessert", "description": "Chocolate brownie served warm", "veg": True, "rating": 4.6},
    82: {"name": "Choco Lava Cake", "price": 180, "category": "Dessert", "description": "Molten chocolate cake with gooey center", "veg": True, "rating": 4.7},
    83: {"name": "Sizzling Brownie", "price": 200, "category": "Dessert", "description": "Hot brownie served on a sizzling plate with ice cream", "veg": True, "rating": 4.7},
    84: {"name": "Waffles", "price": 150, "category": "Dessert", "description": "Crispy waffles with chocolate or syrup topping", "veg": True, "rating": 4.5},
    85: {"name": "Pancakes", "price": 160, "category": "Dessert", "description": "Fluffy pancakes served with honey or chocolate", "veg": True, "rating": 4.6},
    86: {"name": "Churros", "price": 170, "category": "Dessert", "description": "Fried dough pastry sprinkled with sugar", "veg": True, "rating": 4.6},
    87: {"name": "Momos (Veg)", "price": 140, "category": "Snack", "description": "Steamed vegetable dumplings", "veg": True, "rating": 4.5},
    88: {"name": "Momos (Chicken)", "price": 160, "category": "Snack", "description": "Steamed chicken dumplings", "veg": False, "rating": 4.6},
    89: {"name": "Cheese Momos", "price": 180, "category": "Snack", "description": "Dumplings stuffed with cheese", "veg": True, "rating": 4.7},
    90: {"name": "Tandoori Momos", "price": 200, "category": "Snack", "description": "Grilled momos with tandoori masala", "veg": False, "rating": 4.6},
    91: {"name": "Falooda", "price": 140, "category": "Dessert", "description": "Sweet vermicelli dessert with rose syrup and milk", "veg": True, "rating": 4.5},
    92: {"name": "Custard", "price": 120, "category": "Dessert", "description": "Creamy baked custard dessert", "veg": True, "rating": 4.4},
    93: {"name": "Fruit Cream", "price": 130, "category": "Dessert", "description": "Mixed fruits with fresh cream", "veg": True, "rating": 4.5},
    94: {"name": "Tiramisu", "price": 220, "category": "Dessert", "description": "Classic Italian coffee-flavored dessert", "veg": True, "rating": 4.6},
    95: {"name": "Cheesecake", "price": 250, "category": "Dessert", "description": "Rich creamy cheesecake slice", "veg": True, "rating": 4.7},
    96: {"name": "Red Velvet Cake", "price": 280, "category": "Dessert", "description": "Red velvet sponge cake with cream cheese frosting", "veg": True, "rating": 4.6},
    97: {"name": "Chocolate Truffle Cake", "price": 300, "category": "Dessert", "description": "Decadent chocolate cake with truffle layers", "veg": True, "rating": 4.7},
    98: {"name": "Pastry", "price": 110, "category": "Dessert", "description": "Flaky pastry with cream or fruit filling", "veg": True, "rating": 4.4},
    99: {"name": "Muffins", "price": 100, "category": "Dessert", "description": "Soft baked muffins with chocolate or fruit", "veg": True, "rating": 4.5},
    100: {"name": "Donuts", "price": 90, "category": "Dessert", "description": "Soft and s0weet glazed donuts", "veg": True, "rating": 4.4}
}

for i, key in enumerate(menu, start=1):
    menu[key]["image"] = f"Images/dish{i}.jpg"

cart = []
image_refs = []

# ===== Window references =====
menu_window = None
payment_window = None
feedback_window = None


def add_to_cart(item):
    cart.append(item)
    messagebox.showinfo("Added!", f"{menu[item]['name']} added to cart!")
    message_body = f"{menu[item]['name']} was added to cart! 🛒 by the user"


# ===== Payment Window (unchanged) =====
def open_payment_window():
    global payment_window
    if payment_window is None or not payment_window.winfo_exists():
        payment_window = ct.CTkToplevel(app)
        payment_window.configure(fg_color="#1A2E56")
        payment_window.title("Payment")
        payment_window.geometry("1280x720+150+50")
        payment_window.transient(app)
        payment_window.grab_set()
    payment_window.lift()
    payment_window.focus_force()
    for widget in payment_window.winfo_children():
        widget.destroy()
    total = sum(menu[item]["price"] for item in cart)
    ct.CTkLabel(payment_window,
        text=f"Grand Total: ₹{total}",
        font=("Dancing Script", 50, "bold")).pack(pady=10)
    ct.CTkLabel(payment_window,
        text="Select Payment Method:",
        font=("Dancing Script", 30)).pack(pady=5)
    payment_method = tk.StringVar(value="Cash")
    for method in ["Cash", "Card", "Online"]:
        ct.CTkRadioButton(payment_window,
            text=method,
            variable=payment_method,
            value=method,
            font=("Dancing Script", 30),
            corner_radius=30, fg_color="#2B446E").pack(anchor="w", padx=20)

    def show_details():
        for widget in details_frame.winfo_children():
            widget.destroy()
        method = payment_method.get()
        if method == "Card":
            ct.CTkLabel(details_frame,
                text="💳 Enter Card Details",
                font=ct.CTkFont(family="Dancing Script", size=30, weight="bold")).pack(pady=10)
            entries = [("Card Number", False), ("Expiry Date (MM/YY)", False), ("CVV", True)]
            for placeholder, is_password in entries:
                ct.CTkEntry(details_frame,
                    placeholder_text=placeholder,
                    fg_color="#0B1F3F",
                    show="*" if is_password else "").pack(pady=8, padx=20, fill="x")
        elif method == "Online":
            ct.CTkLabel(details_frame,
                text="📱 Scan QR to Pay",
                font=ct.CTkFont(family="Dancing Script", size=30, weight="bold")).pack(pady=10)
            qr = qrcode.make("PAYMENT_DONE:THANKYOU")
            qr = qr.resize((200, 200))
            ctk_qr_img = ct.CTkImage(light_image=qr, size=(200,200))
            qr_label = ct.CTkLabel(details_frame, image=ctk_qr_img, text="")
            # Store reference to prevent garbage collection!
            details_frame.qr_img = ctk_qr_img
            qr_label.pack(pady=15)
        elif method == "Cash":
            ct.CTkLabel(details_frame,
                text="💵 Please pay cash on delivery.",
                font=ct.CTkFont(family="Dancing Script", size=30, weight="bold")).pack(pady=50)

    details_frame = ct.CTkFrame(payment_window,
        width=450,
        height=0,
        fg_color="#08162A",
        corner_radius=20)
    details_frame.pack(pady=20, padx=20, fill="both", expand=True)

    btn_style = {
        "font": ct.CTkFont("Dancing Script", 25, "bold"),
        "fg_color": "#03DAC6",
        "hover_color": "#26E3D6",
        "text_color": "black",
        "corner_radius": 30,
        "width": 250
    }

    ct.CTkButton(payment_window, text="Start Payment", command=show_details, **btn_style).pack(pady=5)
    ct.CTkButton(payment_window,
        text="Confirm Payment",
        command=lambda: confirm_payment(details_frame), **btn_style).pack(pady=5)

    def confirm_payment(frame):
        messagebox.showinfo("Payment Successful", "Thanks for your order! 🎉")
        payment_window.destroy()
        open_feedback_window()

        if payment_window: payment_window.destroy()
        open_feedback_window()

# ===== Feedback Window (unchanged) =====
def submit_feedback():
    global feedback_window, feedback_box
    feedback = feedback_box.get("1.0", "end-1c").strip()
    if not feedback:
        print("No feedback entered!")
        return


def open_feedback_window():
    global feedback_window, feedback_box
    if feedback_window is None or not feedback_window.winfo_exists():
        feedback_window = ct.CTkToplevel(app)
        feedback_window.title("Feedback")
        feedback_window.geometry("1280x720+150+50")
        feedback_window.configure(fg_color="#1A2E56")
        feedback_window.transient(app)
        feedback_window.grab_set()
    feedback_window.lift()
    feedback_window.focus_force()
    for widget in feedback_window.winfo_children():
        widget.destroy()
    ct.CTkLabel(
        feedback_window,
        text="We value your feedback!",
        font=("Dancing Script", 80)
    ).pack(pady=10)
    feedback_box = ct.CTkTextbox(
        feedback_window,
        width=900,
        height=400,
        font=ct.CTkFont("Dancing Script", 30),
        fg_color="#08162A"
    )
    feedback_box.pack(pady=40)
    ct.CTkButton(
        feedback_window,
        text="Submit Feedback",
        command=submit_feedback,
        font=ct.CTkFont("Dancing Script", 30),
        fg_color="#03DAC6",
        hover_color="#26E3D6",
        text_color="black",
        corner_radius=30,
        width=150,
        height=50,
    ).pack(pady=10)

# ===== Order Menu Window =====
def open_menu():
    global menu_window
    if menu_window is None or not menu_window.winfo_exists():
        menu_window = ct.CTkToplevel(app)
        menu_window.title("Menu")
        menu_window.geometry("1280x720+150+50")
        menu_window.configure(fg_color="#1A2E56")
        menu_window.transient(app)
        menu_window.grab_set()
    menu_window.lift()
    menu_window.focus_force()
    for widget in menu_window.winfo_children():
        widget.destroy()
    ct.CTkLabel(menu_window,
        text="Select Items to Add to Cart",
        font=("Dancing Script", 50, "bold")).pack(pady=30)
    scroll = ct.CTkScrollableFrame(menu_window,
        width=1100, height=500, fg_color="#08162A")
    scroll.pack(pady=10)
    for item_id, item_data in menu.items():
        item_frame = ct.CTkFrame(scroll, height=150, fg_color="#0B1F3F")
        item_frame.pack(pady=5, padx=5, fill="x")
        block_frame = ct.CTkFrame(
            item_frame, width=10, fg_color="#1e832a" if item_data['veg'] else "#db6312"
        )
        block_frame.pack(side="left", fill="y", padx=5, pady=5)
        img = Image.open(item_data["image"])
        img = img.resize((200,200))
        ctk_image = ct.CTkImage(light_image=img, size=(200,200))
        image_refs.append(ctk_image)
        img_label = ct.CTkLabel(block_frame, image=ctk_image, text="")
        img_label.pack(side="left", padx=10, pady=5)
        details = (
            f"{item_data['name']} |₹{item_data['price']}"
            f"{item_data['description']}"
            f"⭐ {item_data['rating']} |{item_data['category']} | "
            f"{'Veg' if item_data['veg'] else 'Non-Veg'}"
        )
        ct.CTkLabel(
            item_frame,
            text=details,
            anchor="w",
            justify="left",
            font=ct.CTkFont("Dancing Script", 20, "bold")
        ).pack(side="left", padx=10, pady=5, fill="both", expand=True)
        ct.CTkButton(
            item_frame,
            text="Add",
            font=ct.CTkFont("Dancing Script", 20, "bold"),
            fg_color="#03DAC6",
            hover_color="#26E3D6",
            text_color="black",
            corner_radius=20,
            command=lambda i=item_id: add_to_cart(i)
        ).pack(side="right", padx=10, pady=5)
    ct.CTkButton(
        menu_window,
        text="Go to Payment",
        fg_color="#03DAC6",
        hover_color="#26E3D6",
        font=ct.CTkFont("Dancing Script", 25, "bold"),
        corner_radius=30,
        text_color="black",
        command=lambda: open_payment_window() if cart else messagebox.showwarning("Cart Empty", "Please add at least one item!")
    ).pack(pady=10)

# ===== Main Window + Gallery/Offers =====
my_y = 1000

def open():
    global my_y
    if my_y > 400:
        my_y -= 20
        restro_srrollframe.place(y=my_y, anchor="center")
        app.after(10, open)

restro_label = ct.CTkLabel(
    app,
    text="""Welcome to the Restaurant
    Novotel Pune""",
    font=ct.CTkFont(family="Dancing Script", size=100, weight="bold"),
    text_color="black",
    width=1280
)
restro_label.pack(pady=150)

restro_button = ct.CTkButton(
    app,
    text="Explore",
    font=ct.CTkFont(family="Dancing Script", size=30, weight="bold"),
    corner_radius=30, fg_color="#BB86FC", hover_color="#CF9CFF",
    command=open,
    text_color="black",
)
restro_button.pack(pady=50)

restro_srrollframe = ct.CTkScrollableFrame(
    app, width=1200, height=700, corner_radius=20, fg_color="#0B1F3F")
restro_srrollframe.place(relx=0.5, y=720+400, anchor="center")

my_frame = ct.CTkFrame(restro_srrollframe, fg_color="#08162A", corner_radius=10, height=250)
my_frame.pack(pady=20, fill="x")
my_frame.pack_propagate(False)
ct.CTkButton(
    my_frame,
    text="      Order Now 🍽️",
    font=ct.CTkFont(family="Dancing Script", size=30, weight="bold"),
    corner_radius=50, fg_color="#03DAC6", hover_color="#26E3D6",
    width=300, height=60, text_color="black",
    command=open_menu
).pack(pady=100)

inside_frame = ct.CTkFrame(
    restro_srrollframe, height=300, corner_radius=20, fg_color="#08162A")
inside_frame.pack(pady=40, fill="x")

inside_label = ct.CTkLabel(
    inside_frame,
    text="Today's Special",
    font=ct.CTkFont(family="Dancing Script", size=40, weight="bold"),
    fg_color="#08162A"
)
inside_label.pack(pady=10)

offers = [
    {"name": "French Fries + Burger Free", "price": 150, "image": "Images/offer1.jpg"},
    {"name": "Buy 1 Pizza Get 1", "price": 250, "image": "Images/offer2.jpg"},
    {"name": "Cold Drink Free", "price": 0, "image": "Images/offer3.jpg"},
    {"name": "Ice Cream Discount", "price": 80, "image": "Images/offer4.jpg"},
]
photos = []
def create_offer_card(parent, offer):
    card_frame = ct.CTkFrame(parent, width=350, height=400, corner_radius=15, fg_color="#08162A")
    card_frame.pack(side="left", padx=10, pady=10)
    if offer.get("image"):
        try:
            img = Image.open(offer["image"])
            img.thumbnail((350, 300))
            ctk_image = ct.CTkImage(light_image=img, size=img.size)
            photos.append(ctk_image)
            ct.CTkLabel(card_frame, image=ctk_image, text="").pack(pady=(15,10))
        except Exception as e:
            print(f"Error loading {offer['image']}: {e}")
    ct.CTkLabel(
        card_frame,
        text=offer["name"],
        font=ct.CTkFont(size=18, weight="bold"),
        text_color="white"
    ).pack(pady=(10,10))
    ct.CTkButton(
        card_frame,
        text="Get Offer",
        fg_color="#03DAC6",
        hover_color="#26E3D6",
        width=200,
        text_color="black",
        corner_radius=30,
        command=lambda price=offer["price"]: open_payment_window_with_price(price)
    ).pack(pady=(0,15))
def open_payment_window_with_price(price):
    global payment_window
    if payment_window is None or not payment_window.winfo_exists():
        payment_window = ct.CTkToplevel(app)
        payment_window.configure(fg_color="#1A2E56")
        payment_window.title("Payment")
        payment_window.geometry("1280x720+150+50")
        payment_window.transient(app)
        payment_window.grab_set()
    payment_window.lift()
    payment_window.focus_force()
    for widget in payment_window.winfo_children():
        widget.destroy()
    total = price
    ct.CTkLabel(payment_window,
                text=f"Grand Total: ₹{total}",
                font=("Dancing Script", 50, "bold")).pack(pady=10)
    ct.CTkLabel(payment_window,
                text="Select Payment Method:",
                font=("Dancing Script", 30)).pack(pady=5)
    payment_method = tk.StringVar(value="Cash")
    for method in ["Cash", "Card", "Online"]:
        ct.CTkRadioButton(payment_window,
                          text=method,
                          variable=payment_method,
                          value=method,
                          font=("Dancing Script", 30),
                          corner_radius=30,
                          fg_color="#2B446E").pack(anchor="w", padx=20)
    def show_details():
        for widget in details_frame.winfo_children():
            widget.destroy()
        method = payment_method.get()
        if method == "Card":
            ct.CTkLabel(details_frame,
                        text="💳 Enter Card Details",
                        font=ct.CTkFont(family="Dancing Script", size=30, weight="bold")).pack(pady=10)
            entries = [("Card Number", False), ("Expiry Date (MM/YY)", False), ("CVV", True)]
            for placeholder, is_password in entries:
                ct.CTkEntry(details_frame,
                            placeholder_text=placeholder,
                            fg_color="#0B1F3F",
                            show="*" if is_password else "").pack(pady=8, padx=20, fill="x")
        elif method == "Online":
            ct.CTkLabel(details_frame,
                        text="📱 Scan QR to Pay",
                        font=ct.CTkFont(family="Dancing Script",
                                        size=30, weight="bold")).pack(pady=10)
            qr = qrcode.make("PAYMENT_DONE:THANKYOU")
            qr = qr.resize((200, 200))
            ctk_qr_img = ct.CTkImage(light_image=qr, size=(200,200))
            details_frame.qr_img = ctk_qr_img
            qr_label = ct.CTkLabel(details_frame, image=ctk_qr_img, text="")
            qr_label.pack(pady=15)
        elif method == "Cash":
            ct.CTkLabel(details_frame,
                        text="💵 Please pay cash on delivery.",
                        font=ct.CTkFont(family="Dancing Script", size=30, weight="bold")).pack(pady=50)
    details_frame = ct.CTkFrame(payment_window,
                                width=450,
                                height=0,
                                fg_color="#08162A",
                                corner_radius=20)
    details_frame.pack(pady=20, padx=20, fill="both", expand=True)
    btn_style = {
        "font": ct.CTkFont("Dancing Script", 25, "bold"),
        "fg_color": "#03DAC6",
        "hover_color": "#26E3D6",
        "text_color": "black",
        "corner_radius": 30,
        "width": 250
    }
    ct.CTkButton(payment_window, text="Start Payment", command=show_details, **btn_style).pack(pady=5)
    ct.CTkButton(payment_window,
        text="Confirm Payment",
        command=lambda: confirm_payment(details_frame), **btn_style).pack(pady=5)
    def confirm_payment(frame):
        messagebox.showinfo("Payment Successful","Thanks for your order! 🎉")
        payment_window.destroy()

        if payment_window: payment_window.destroy()
        open_feedback_window()
for offer in offers:
    create_offer_card(inside_frame, offer)


my_frame3 = ct.CTkFrame(
    restro_srrollframe, fg_color="#08162A",
    corner_radius=10, height=500)
my_frame3.pack(pady=20, fill="x")
my_frame3.pack_propagate(False)
gallery_label = ct.CTkLabel(
    my_frame3,
    text="Gallery",
    font=ct.CTkFont(family="Dancing Script", size=40, weight="bold"),
    fg_color="#08162A",
)
gallery_label.pack(pady=10)
gallery_frame = ct.CTkFrame(
    my_frame3,
    fg_color="#2B2B2B",
    corner_radius=0
)
gallery_frame.pack(pady=10)
image_paths = ["Images/_MG_0932.png", "Images/_MG_0017.png", "Images/_MG_0018.png",
               "Images/_MG_0102.png", "Images/_MG_0122.png", "Images/_MG_0209.png",
               "Images/_MG_0283.png", "Images/_MG_0217.png", "Images/_MG_0201.png",
               "Images/_MG_0183.png",]
columns = 5
img_width, img_height = 250, 200
gallery_img_refs = []
row, col = 1, 0
for path in image_paths:
    img = Image.open(path)
    img = img.resize((img_width, img_height))
    ctk_image = ct.CTkImage(light_image=img, size=(img_width, img_height))
    gallery_img_refs.append(ctk_image)
    img_label = ct.CTkLabel(gallery_frame, image=ctk_image, text="")
    img_label.grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col >= columns:
        col = 0
        row += 1

details_text = """
🏨 Novotel,
📍 Sakore Nagar, Viman Nagar, Pune
✨  Maharashtra 411014
⏰ Open: 8:00 AM - 11:00 PM
📞 Contact: +91-XXXXXXXXXX
"""

my_frame2 = ct.CTkFrame(
    restro_srrollframe, fg_color="#08162A", corner_radius=10, height=300)
my_frame2.pack(pady=20, fill="x")
my_frame2.pack_propagate(False)
de_label = ct.CTkLabel(
    my_frame2,
    text="Contact & Details",
    font=ct.CTkFont(family="Dancing Script", size=40, weight="bold"),
    fg_color="#08162A",
)
de_label.pack(pady=10)
details_label = ct.CTkLabel(
    my_frame2,
    text=details_text,
    fg_color="#08162A",
    justify="left",
    anchor="w",
    font=ct.CTkFont(family="Dancing Script", size=25, weight="bold")
)
details_label.pack(pady=20, padx=20, anchor="w")
app.mainloop()