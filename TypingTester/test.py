import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# List of sentences
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language.",
    "Typing speed tests are fun and challenging.",
    "Always practice coding to improve your skills."
]

# Function to calculate WPM and accuracy
def typing_speed_test():
    print(Fore.CYAN + Style.BRIGHT + "** Typing Speed Test **\n")
    print(Fore.YELLOW + "Instructions:")
    print(Fore.LIGHTGREEN_EX + "1. Type the sentence exactly as shown.")
    print(Fore.LIGHTGREEN_EX + "2. Your speed and accuracy will be measured.\n")
    
    # Choose a random sentence
    sentence = random.choice(sentences)
    print(Fore.MAGENTA + "Type the following sentence:")
    print(Fore.WHITE + f"--> {sentence}\n")
    
    # Start the timer
    input(Fore.LIGHTBLUE_EX + "Press Enter when you are ready to start...")
    start_time = time.time()
    
    # Take user input
    typed_sentence = input(Fore.LIGHTCYAN_EX + "\nStart typing: ")
    
    # End the timer
    end_time = time.time()
    
    # Calculate typing speed and accuracy
    time_taken = end_time - start_time
    words_typed = len(typed_sentence.split())
    correct_chars = sum(1 for i, j in zip(typed_sentence, sentence) if i == j)
    total_chars = len(sentence)
    
    # Words Per Minute (WPM)
    wpm = (words_typed / time_taken) * 60 if time_taken > 0 else 0
    
    # Accuracy
    accuracy = (correct_chars / total_chars) * 100
    
    # Display results
    print(Fore.LIGHTYELLOW_EX + "\n** Results **")
    print(Fore.LIGHTGREEN_EX + f"Time Taken: {time_taken:.2f} seconds")
    print(Fore.LIGHTGREEN_EX + f"Words Per Minute (WPM): {wpm:.2f}")
    print(Fore.LIGHTGREEN_EX + f"Accuracy: {accuracy:.2f}%")
    
    # Feedback based on performance
    if accuracy > 90 and wpm > 40:
        print(Fore.LIGHTBLUE_EX + "Great job! You're a fast and accurate typist! 🚀")
    elif accuracy > 70:
        print(Fore.LIGHTBLUE_EX + "Good effort! Keep practicing to improve your speed. 💪")
    else:
        print(Fore.LIGHTRED_EX + "Keep practicing! Accuracy and speed will improve over time. 🌱")

# Run the test
if __name__ == "__main__":
    typing_speed_test()
