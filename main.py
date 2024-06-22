from playsound import playsound


def main_menu():
    print("Hello to Yoshifo, your friend to learn Japanese")
    print("Please enter the number of the lesson you want to hear")
    print("1: Lesson 1 (Greetings)       2: Lesson 2       3: Hiragana       Press 'q' to exit")
    print("")


def lesson1_menu():
    print("Hello to Lesson 1 (Greetings)")
    print("Enter the word you want to hear")
    print("1: Ohayoo Gozaimasu       2: Konnichiwa       3: Konbanwa")
    print("4: Arigatoo              5: Osakini          6: Sayoonara")
    print("7: Sumimasen             Press 'q' to exit")


def lesson2_menu():
    print("Hello to Lesson 2")
    print("Enter the word you want to hear")
    print("1: Kitte Kudasai       2: Wakarimashita       Press 'q' to exit")


def play_lesson1_word(word_num):
    audio_files = {
        "1": './Audios/ohayoo.mp3',
        "2": './Audios/konnichiwa.mp3',
        "3": './Audios/konbanwa.mp3',
        "4": './Audios/arigatoo.mp3',
        "5": './Audios/osakini.mp3',
        "6": './Audios/sayoonara.mp3',
        "7": ['./Audios/sumimasen.mp3', './Audios/sumimasen2.mp3', './Audios/sumimasen3.mp3']
    }
    if word_num in audio_files:
        if isinstance(audio_files[word_num], list):
            for audio in audio_files[word_num]:
                playsound(audio)
        else:
            playsound(audio_files[word_num])


def play_lesson2_word(word_num):
    audio_files = {
        "1": './Audios/kitte_kudasai.mp3',
        "2": './Audios/wakarimashita.mp3'
    }
    if word_num in audio_files:
        playsound(audio_files[word_num])


def main():
    while True:
        main_menu()
        lesson_num = input().strip()

        if lesson_num == "1":
            while True:
                lesson1_menu()
                word_num = input().strip()
                if word_num == "q":
                    break
                else:
                    play_lesson1_word(word_num)
        elif lesson_num == "2":
            while True:
                lesson2_menu()
                word_num = input().strip()
                if word_num == "q":
                    break
                else:
                    play_lesson2_word(word_num)
        elif lesson_num == "3":
            playsound('./Audios/hiragana.mp3')
        elif lesson_num == "q":
            break
        else:
            print("Please input a valid number")


if __name__ == "__main__":
    main()
