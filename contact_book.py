class contact_book:
    def __init__(self):
        self.name = None
        self.address = None
        self.contact = None
        self.email = None


bookObj = contact_book()
while True:
    print("Select your input")
    print("1.Add new contact")
    print("2.Delete existing contact")
    print("3.Exit")
bookObj