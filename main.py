import json

def create_quiz():
    quiz = []
    print("Quiz erstellen. Geben Sie 'exit' ein, um zu beenden.")
    while True:
        question = input("Frage: ")
        if question.lower() == 'exit':
            break
        answer = input("Antwort: ")
        quiz.append({"question": question, "answer": answer})
    filename = input("Dateiname zum Speichern (z.B. quiz.json): ")
    with open(filename, "w") as f:
        json.dump(quiz, f)
    print(f"Quiz wurde in {filename} gespeichert.")

def play_quiz():
    filename = input("Dateiname des Quizzes (z.B. quiz.json): ")
    try:
        with open(filename, "r") as f:
            quiz = json.load(f)
        print("Quiz starten!")
        score = 0
        for item in quiz:
            print(item["question"])
            user_answer = input("Ihre Antwort: ")
            if user_answer.lower() == item["answer"].lower():
                print("Richtig!")
                score += 1
            else:
                print(f"Falsch! Die richtige Antwort ist: {item['answer']}")
        print(f"Quiz beendet! Ihr Punktestand: {score}/{len(quiz)}")
    except FileNotFoundError:
        print(f"Datei {filename} nicht gefunden.")

def main():
    while True:
        print("\n1. Quiz erstellen")
        print("2. Quiz spielen")
        print("3. Beenden")
        choice = input("Wählen Sie eine Option: ")
        if choice == "1":
            create_quiz()
        elif choice == "2":
            play_quiz()
        elif choice == "3":
            print("Programm beendet.")
            break
        else:
            print("Ungültige Eingabe. Bitte erneut versuchen.")

if __name__ == "__main__":
    main()
