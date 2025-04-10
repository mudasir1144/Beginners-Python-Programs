def emotions(user):
    if user.lower() == "happy":
        return "That's great to hear!"
    elif user.lower() == "sad":
        return "I am sorry to hear that you are sad , thing will get okay soon!"
    elif user.lower() == "angry":
        return "Calm Down , Take some deep breaths , easy"
    elif user.lower() == "excited":
        return "That's great to hear!"
    else:
        return("I am sorry not to understand your feelings")
    
user = input("How are you feeling today?: ")
results = emotions(user)
print(f"{results}")
