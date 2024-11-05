def mood_response(mood):
    mood = mood.lower()
    if mood == "happy":
        return "That's great to hear!"

    elif mood == "sad":
        return "I'm sorry to hear that. I hope your day gets better."
    
    elif mood == "excited":
        return "I'm thrilled to hear that! Keep up the great work!"

    elif mood == "angry":
        return "It's okay to feel angry. Take a deep breath and try to relax."

    elif mood == "anxious":
        return "I understand that feeling. It's important to take care of yourself."

    elif mood == "relaxed":
        return "That's wonderful! Enjoy your calmness."

    else:
        return "I'm not sure what you're feeling. Can you tell me more?"