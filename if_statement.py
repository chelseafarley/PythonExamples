greeting_option = input("Enter fr to greet in French or en to greet in English:\n")

if greeting_option == "fr":
    print("Bonjour")
elif greeting_option == "en":
    print("Hello")
else:
    print(f"Invalid option entered: {greeting_option}")