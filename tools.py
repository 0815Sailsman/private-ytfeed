def get_all_subs():
    text = ""
    with open("subscriptions.txt") as file:
        for line in file:
            text += line
    return text
