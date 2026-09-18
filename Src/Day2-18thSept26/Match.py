browser_name = input("Enter the browser name:")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("The browser is Firefox")
    case "chrome":
        print("The browser is Chrome")
    case _:
        print("The browser is not found")