# Simple Placement FAQ Chatbot (Rule-based)

def chatbot():
    print("🤖 Placement Chatbot: Hello! Ask me anything about placements.\n")
    
    while True:
        user = input("You: ").lower()

        if "job" in user or "roles" in user:
            print("Bot: Companies offer roles like Software Engineer, Data Analyst, Web Developer, etc.")

        elif "resume" in user or "cv" in user:
            print("Bot: Keep your resume to 1 page, include projects, skills, internships, and use strong action verbs.")

        elif "cgpa" in user or "percentage" in user:
            print("Bot: Most companies require a minimum CGPA of 6.0–7.0, but it varies.")

        elif "interview" in user:
            print("Bot: Prepare DSA basics, OOP concepts, your projects, HR questions, and communication skills.")

        elif "company" in user or "recruiters" in user:
            print("Bot: Common recruiters include TCS, Infosys, Wipro, Accenture, Cognizant, and many startups.")

        elif "rounds" in user or "process" in user:
            print("Bot: Typical process: Aptitude Test → Technical Interview → HR Interview.")

        elif "skills" in user:
            print("Bot: Useful skills include Python, Java, SQL, Data Structures, and Communication skills.")

        elif "bye" in user or "exit" in user:
            print("Bot: Goodbye! All the best for your placements! 😊")
            break

        else:
            print("Bot: Sorry, I don't understand. Please ask another placement-related question.")

# Run the chatbot
chatbot()
