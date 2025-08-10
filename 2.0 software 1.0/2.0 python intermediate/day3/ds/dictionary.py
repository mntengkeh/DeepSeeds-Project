# declaration
# phone_book = {
#     "The Man": "1234567",
#     "Baracks": "0876543",
#     "Dungeon": "7655654"
# }


# personal contact manager

contacts = {}

def add_contact(name, phone, email):
    if name not in contacts:
        contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Added {name}")
    else:
        print(f"{name} already exists")

def update_contact(name, phone=None, email=None):
    if name in contacts:
        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        print(f"Updated {name}")
    else:
        print(f"{name} doesn't exist in contacts")

def display_contacts():
    if not contacts:
        print("Contacts is empty")
    else:
        print(contacts)

add_contact("21", 65432, "21@gmail.com")
add_contact("Okazaki", 876543, "oka@za.ki")
display_contacts()
update_contact("21", None, "2.1@gmail.com")
display_contacts()