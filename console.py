import random
import time
import os
import json
from datetime import datetime

class womenQuiz:
    def __init__(self):
        self.score = 0
        self.total_questions = 0
        self.categories = ["History", "Technology", "Leadership"]
        self.user_name = ""
        self.quiz_history = []
        self.streak = 0
        self.longest_streak = 0
        self.questions = {
            "History": [
                {
                    "question": "Who was the first woman to win a Nobel Prize?",
                    "options": ["Marie Curie", "Rosa Parks", "Florence Nightingale", "Amelia Earhart"],
                    "correct_answer": "Marie Curie",
                    "fun_fact": "Marie Curie was the first person ever to win Nobel Prizes in two different scientific fields."
                },
                {
                    "question": "Which woman was known as the 'Moses of her people' for leading dozens of enslaved people to freedom via the Underground Railroad?",
                    "options": ["Sojourner Truth", "Harriet Tubman", "Rosa Parks", "Ida B. Wells"],
                    "correct_answer": "Harriet Tubman",
                    "fun_fact": "Harriet Tubman conducted approximately 13 missions and helped free more than 70 enslaved people."
                },
                {
                    "question": "Who was the first female Prime Minister of the United Kingdom?",
                    "options": ["Queen Elizabeth II", "Margaret Thatcher", "Theresa May", "Angela Merkel"],
                    "correct_answer": "Margaret Thatcher",
                    "fun_fact": "Margaret Thatcher served as Prime Minister for 11 years from 1979 to 1990, the longest tenure of any British PM in the 20th century."
                },
                {
                    "question": "Which woman wrote 'Frankenstein'?",
                    "options": ["Jane Austen", "Emily Dickinson", "Mary Shelley", "Virginia Woolf"],
                    "correct_answer": "Mary Shelley",
                    "fun_fact": "Mary Shelley wrote 'Frankenstein' when she was only 18 years old."
                },
                {
                    "question": "Who was the first female astronaut in space?",
                    "options": ["Sally Ride", "Valentina Tereshkova", "Mae Jemison", "Christa McAuliffe"],
                    "correct_answer": "Valentina Tereshkova",
                    "fun_fact": "Valentina Tereshkova completed 48 orbits of Earth during her three-day mission in 1963."
                },
            ],
            "Technology": [
                {
                    "question": "Who is considered the first computer programmer?",
                    "options": ["Grace Hopper", "Ada Lovelace", "Katherine Johnson", "Hedy Lamarr"],
                    "correct_answer": "Ada Lovelace",
                    "fun_fact": "Ada Lovelace wrote an algorithm for Charles Babbage's Analytical Engine in the 1840s, long before modern computers existed."
                },
                {
                    "question": "Which woman coined the term 'software engineering' and developed the first compiler?",
                    "options": ["Grace Hopper", "Ada Lovelace", "Margaret Hamilton", "Radia Perlman"],
                    "correct_answer": "Grace Hopper",
                    "fun_fact": "Grace Hopper also found the first computer 'bug' - an actual moth stuck in a relay."
                },
                {
                    "question": "Who led the team that developed the algorithm for the first image of a black hole?",
                    "options": ["Katie Bouman", "Mae Jemison", "Jocelyn Bell Burnell", "Ellen Ochoa"],
                    "correct_answer": "Katie Bouman",
                    "fun_fact": "Katie Bouman's algorithm helped capture the first-ever image of a black hole, announced in 2019."
                },
                {
                    "question": "Which actress co-invented a frequency hopping technology that became a precursor to Wi-Fi, GPS, and Bluetooth?",
                    "options": ["Audrey Hepburn", "Marilyn Monroe", "Hedy Lamarr", "Elizabeth Taylor"],
                    "correct_answer": "Hedy Lamarr",
                    "fun_fact": "Hedy Lamarr was a Hollywood star who developed this technology during World War II to prevent radio-guided torpedoes from being jammed."
                },
                {
                    "question": "Who was the NASA mathematician whose calculations were critical to the success of the first U.S. crewed spaceflights?",
                    "options": ["Katherine Johnson", "Dorothy Vaughan", "Mary Jackson", "Annie Easley"],
                    "correct_answer": "Katherine Johnson",
                    "fun_fact": "Katherine Johnson's calculations were so trusted that astronaut John Glenn requested that she verify the computer's orbital calculations before his flight."
                },
            ],
            "Leadership": [
                {
                    "question": "Who founded the Girls Who Code organization to close the gender gap in technology?",
                    "options": ["Sheryl Sandberg", "Reshma Saujani", "Melinda Gates", "Susan Wojcicki"],
                    "correct_answer": "Reshma Saujani",
                    "fun_fact": "Girls Who Code has reached over 300,000 girls in all 50 U.S. states since its founding in 2012."
                },
                {
                    "question": "Which woman served as Chairperson of the Indian Space Research Organisation (ISRO) and led India's first interplanetary mission?",
                    "options": ["Kalpana Chawla", "Sunita Williams", "Ritu Karidhal", "Tessy Thomas"],
                    "correct_answer": "Tessy Thomas",
                    "fun_fact": "Tessy Thomas is known as the 'Missile Woman of India' for her contributions to ballistic missile technology."
                },
                {
                    "question": "Who was the first female CEO of a Fortune 500 company?",
                    "options": ["Indra Nooyi", "Katharine Graham", "Carly Fiorina", "Mary Barra"],
                    "correct_answer": "Katharine Graham",
                    "fun_fact": "Katharine Graham became CEO of The Washington Post Company in 1972 and led the paper during the Watergate scandal."
                },
                {
                    "question": "Which activist became the youngest Nobel Prize laureate for her work on female education?",
                    "options": ["Greta Thunberg", "Malala Yousafzai", "Emma González", "Wangari Maathai"],
                    "correct_answer": "Malala Yousafzai",
                    "fun_fact": "Malala was only 17 when she won the Nobel Peace Prize in 2014."
                },
                {
                    "question": "Who founded The Body Shop and pioneered ethical consumerism?",
                    "options": ["Anita Roddick", "Oprah Winfrey", "Arianna Huffington", "Martha Stewart"],
                    "correct_answer": "Anita Roddick",
                    "fun_fact": "Anita Roddick was one of the first to prohibit the use of ingredients tested on animals and to promote fair trade with developing countries."
                },
            ]
        }
        self.achievements = {
            "First Quiz": False,
            "Perfect Round": False,
            "History Buff": False,
            "Tech Pioneer": False,
            "Leader at Heart": False,
            "Streak Master": False,
            "Quiz Champion": False
        }
        self.load_data()
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_welcome(self):
        self.clear_screen()
        print("=" * 60)
        print("  INSPIRATIONAL WOMEN IN HISTORY, TECHNOLOGY & LEADERSHIP  ")
        print("=" * 60)
        print("\nWelcome to the Quiz that celebrates remarkable women who")
        print("have changed the world through their contributions!")
        
        if not self.user_name:
            print("\nWhat is your name?")
            self.user_name = input("> ").strip()
            if not self.user_name:
                self.user_name = "Learner"
            self.save_data()
        
        print(f"\nWelcome, {self.user_name}!")
        
        if self.achievements["First Quiz"]:
            print("\nYou've unlocked achievements:")
            for achievement, unlocked in self.achievements.items():
                if unlocked:
                    print(f"- {achievement}")
        
        print("\nPress Enter to continue...")
        input()
    
    def display_menu(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print(f"                MAIN MENU - {self.user_name}                ")
        print("=" * 60)
        print("\n1. Take a quiz on Women in History")
        print("2. Take a quiz on Women in Technology")
        print("3. Take a quiz on Women in Leadership")
        print("4. Take a random quiz across all categories")
        print("5. View your current score")
        print("6. View quiz history")
        print("7. View achievements")
        print("8. Timed challenge mode")
        print("9. Reset progress")
        print("10. Exit")
        print("\n" + "=" * 60)
    
    def get_menu_choice(self):
        while True:
            try:
                choice = int(input("\nEnter your choice (1-10): "))
                if 1 <= choice <= 10:
                    return choice
                else:
                    print("Invalid choice. Please enter a number between 1 and 10.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def check_achievements(self, category=None, score=0, total=0):
        if not self.achievements["First Quiz"]:
            self.achievements["First Quiz"] = True
            print("\n🏆 Achievement unlocked: First Quiz!")
        
        if score == total and total >= 5:
            if not self.achievements["Perfect Round"]:
                self.achievements["Perfect Round"] = True
                print("\n🏆 Achievement unlocked: Perfect Round!")
        
        if category == "History" and score >= 4:
            if not self.achievements["History Buff"]:
                self.achievements["History Buff"] = True
                print("\n🏆 Achievement unlocked: History Buff!")
        
        if category == "Technology" and score >= 4:
            if not self.achievements["Tech Pioneer"]:
                self.achievements["Tech Pioneer"] = True
                print("\n🏆 Achievement unlocked: Tech Pioneer!")
        
        if category == "Leadership" and score >= 4:
            if not self.achievements["Leader at Heart"]:
                self.achievements["Leader at Heart"] = True
                print("\n🏆 Achievement unlocked: Leader at Heart!")
        
        if self.streak >= 5:
            if not self.achievements["Streak Master"]:
                self.achievements["Streak Master"] = True
                print("\n🏆 Achievement unlocked: Streak Master!")
        
        if self.score >= 25:
            if not self.achievements["Quiz Champion"]:
                self.achievements["Quiz Champion"] = True
                print("\n🏆 Achievement unlocked: Quiz Champion!")
        
        self.save_data()
    
    def take_quiz(self, category=None, timed_mode=False):
        self.clear_screen()
        
        if category:
            print(f"\n=== Quiz on Women in {category} ===\n")
            questions = self.questions[category].copy()
        else:
            print("\n=== Random Quiz Across All Categories ===\n")
            questions = []
            for cat in self.categories:
                questions.extend(self.questions[cat])
            random.shuffle(questions)
            questions = questions[:5]
        
        random.shuffle(questions)
        
        round_score = 0
        round_total = len(questions)
        correct_streak = 0
        
        if timed_mode:
            print("TIMED MODE: You have 60 seconds to answer all questions!")
            print("Press Enter to start the timer...")
            input()
            start_time = time.time()
            time_limit = 60
        
        for i, q in enumerate(questions, 1):
            if timed_mode:
                elapsed_time = time.time() - start_time
                remaining_time = time_limit - elapsed_time
                
                if remaining_time <= 0:
                    print("\n⏰ TIME'S UP! ⏰")
                    break
                
                print(f"\nTime remaining: {remaining_time:.1f} seconds")
            
            print(f"Question {i}/{round_total}:")
            print(f"\n{q['question']}\n")
            
            for j, option in enumerate(q['options'], 1):
                print(f"{j}. {option}")
            
            while True:
                try:
                    if timed_mode and time.time() - start_time >= time_limit:
                        print("\n⏰ TIME'S UP! ⏰")
                        answer = 0
                        break
                    
                    answer = int(input("\nYour answer (1-4): "))
                    if 1 <= answer <= 4:
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and 4.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
            
            if timed_mode and answer == 0:
                break
            
            selected_answer = q['options'][answer-1]
            self.total_questions += 1
            
            if selected_answer == q['correct_answer']:
                self.score += 1
                round_score += 1
                self.streak += 1
                correct_streak += 1
                if self.streak > self.longest_streak:
                    self.longest_streak = self.streak
                print("\n✓ Correct! Well done!")
                if correct_streak >= 3:
                    print(f"🔥 {correct_streak} correct answers in a row!")
            else:
                self.streak = 0
                correct_streak = 0
                print(f"\n✗ Incorrect. The correct answer is: {q['correct_answer']}")
            
            print(f"\nFun Fact: {q['fun_fact']}")
            print("\n" + "-" * 60)
            
            if not timed_mode:
                input("\nPress Enter to continue...")
            
            if i < round_total and not timed_mode:
                self.clear_screen()
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.quiz_history.append({
            "date": timestamp,
            "category": category if category else "Random",
            "score": round_score,
            "total": round_total,
            "percentage": (round_score / round_total) * 100 if round_total > 0 else 0,
            "timed_mode": timed_mode
        })
        
        self.check_achievements(category, round_score, round_total)
        self.save_data()
        
        self.clear_screen()
        print("\n" + "=" * 60)
        print("                  QUIZ RESULTS                  ")
        print("=" * 60)
        print(f"\nYou scored {round_score} out of {round_total} in this round!")
        
        if timed_mode:
            elapsed_time = min(time.time() - start_time, time_limit)
            print(f"Time taken: {elapsed_time:.1f} seconds")
        
        print(f"Your overall score is {self.score} out of {self.total_questions}.")
        
        percentage = (self.score / self.total_questions) * 100 if self.total_questions > 0 else 0
        print(f"Overall accuracy: {percentage:.1f}%")
        print(f"Current streak: {self.streak}")
        print(f"Longest streak: {self.longest_streak}")
        
        print("\n" + "=" * 60)
        input("\nPress Enter to return to the main menu...")
    
    def view_score(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print("                  YOUR SCORE                  ")
        print("=" * 60)
        
        if self.total_questions == 0:
            print("\nYou haven't taken any quizzes yet!")
        else:
            print(f"\nYour current score is {self.score} out of {self.total_questions}.")
            percentage = (self.score / self.total_questions) * 100
            print(f"Accuracy: {percentage:.1f}%")
            print(f"Current streak: {self.streak}")
            print(f"Longest streak: {self.longest_streak}")
            
            if percentage >= 90:
                print("\nOutstanding! You're an expert on inspirational women!")
            elif percentage >= 70:
                print("\nGreat job! You know a lot about these pioneering women!")
            elif percentage >= 50:
                print("\nGood effort! Keep learning about these amazing women!")
            else:
                print("\nThere's still more to learn about these remarkable women!")
        
        print("\n" + "=" * 60)
        input("\nPress Enter to return to the main menu...")
    
    def view_history(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print("                 QUIZ HISTORY                 ")
        print("=" * 60)
        
        if not self.quiz_history:
            print("\nYou haven't taken any quizzes yet!")
        else:
            print("\n" + "-" * 78)
            print(f"{'Date':<20} {'Category':<10} {'Score':<10} {'Percentage':<12} {'Mode':<10}")
            print("-" * 78)
            
            for entry in self.quiz_history:
                mode = "Timed" if entry["timed_mode"] else "Normal"
                print(f"{entry['date']:<20} {entry['category']:<10} {entry['score']}/{entry['total']:<8} {entry['percentage']:.1f}%{' ':<7} {mode:<10}")
            
            print("-" * 78)
        
        print("\n" + "=" * 60)
        input("\nPress Enter to return to the main menu...")
    
    def view_achievements(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print("               YOUR ACHIEVEMENTS               ")
        print("=" * 60 + "\n")
        
        achievement_descriptions = {
            "First Quiz": "Complete your first quiz",
            "Perfect Round": "Get all questions correct in a round of 5 or more questions",
            "History Buff": "Get at least 4 correct in a History quiz",
            "Tech Pioneer": "Get at least 4 correct in a Technology quiz",
            "Leader at Heart": "Get at least 4 correct in a Leadership quiz",
            "Streak Master": "Get a streak of 5 or more correct answers",
            "Quiz Champion": "Reach a total score of 25 correct answers"
        }
        
        for achievement, unlocked in self.achievements.items():
            status = "🏆 UNLOCKED" if unlocked else "🔒 LOCKED"
            print(f"{status} - {achievement}: {achievement_descriptions[achievement]}")
        
        print("\n" + "=" * 60)
        input("\nPress Enter to return to the main menu...")
    
    def reset_progress(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print("               RESET PROGRESS                ")
        print("=" * 60 + "\n")
        
        print("Are you sure you want to reset all your progress?")
        print("This will delete your score, quiz history, and achievements.")
        print("This action cannot be undone!")
        
        choice = input("\nType 'RESET' to confirm: ")
        
        if choice == "RESET":
            self.score = 0
            self.total_questions = 0
            self.streak = 0
            self.longest_streak = 0
            self.quiz_history = []
            for key in self.achievements:
                self.achievements[key] = False
            
            self.save_data()
            
            print("\nProgress has been reset successfully.")
        else:
            print("\nReset cancelled.")
        
        input("\nPress Enter to return to the main menu...")
    
    def save_data(self):
        data = {
            "user_name": self.user_name,
            "score": self.score,
            "total_questions": self.total_questions,
            "streak": self.streak,
            "longest_streak": self.longest_streak,
            "quiz_history": self.quiz_history,
            "achievements": self.achievements
        }
        
        try:
            with open("quiz_data.json", "w") as f:
                json.dump(data, f)
        except:
            pass
    
    def load_data(self):
        try:
            with open("quiz_data.json", "r") as f:
                data = json.load(f)
                self.user_name = data.get("user_name", "")
                self.score = data.get("score", 0)
                self.total_questions = data.get("total_questions", 0)
                self.streak = data.get("streak", 0)
                self.longest_streak = data.get("longest_streak", 0)
                self.quiz_history = data.get("quiz_history", [])
                self.achievements = data.get("achievements", self.achievements)
        except:
            pass
    
    def exit_application(self):
        self.clear_screen()
        print("\n" + "=" * 60)
        print("                   GOODBYE!                   ")
        print("=" * 60)
        
        if self.total_questions > 0:
            print(f"\nFinal Score: {self.score} out of {self.total_questions}")
            percentage = (self.score / self.total_questions) * 100
            print(f"Final Accuracy: {percentage:.1f}%")
        
        print(f"\nThank you for playing, {self.user_name}!")
        print("Keep learning about inspirational women throughout history!")
        print("\n" + "=" * 60)
        time.sleep(2)
        exit()
    
    def run(self):
        self.display_welcome()
        
        while True:
            self.display_menu()
            choice = self.get_menu_choice()
            
            if choice == 1:
                self.take_quiz("History")
            elif choice == 2:
                self.take_quiz("Technology")
            elif choice == 3:
                self.take_quiz("Leadership")
            elif choice == 4:
                self.take_quiz()
            elif choice == 5:
                self.view_score()
            elif choice == 6:
                self.view_history()
            elif choice == 7:
                self.view_achievements()
            elif choice == 8:
                self.take_quiz(timed_mode=True)
            elif choice == 9:
                self.reset_progress()
            elif choice == 10:
                self.exit_application()


if __name__ == "__main__":
    quiz_app = womenQuiz()
    quiz_app.run()
