from playsound import playsound
print("Hello to Yoshifo, your friend to learn Japanees ")
print("Please Enter the number of the lesson you want to hear")

try:
    while True:
        print("1:lesson1       2:lesson2        3:Hiragana      Press 'q' to exit")
        print("  ")
        print("  ")
        lesson_num = input()
        if(lesson_num == "1"):
            print("Hello to lesson1 (Greatings)")
            print("Enter the word you want to hear")
            print("1:Ohayoo Gozaimaz        2:konnichiwa        3:konbanwa      4:arigatoo      5:osakini       6:sayoonara     7:sumimasen       Press 'q' to exit")
            
            while True:
                try:
                    wanted_word = input()
                    if (wanted_word == "1"):
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\ohayoo.mp3')
                    elif (wanted_word == "2"):
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\konnichiwa.mp3')
                    elif (wanted_word == "3"):
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\konbanwa.mp3')    
                    elif (wanted_word == "4"):
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\arigatoo.mp3')   
                    elif (wanted_word == "5"):
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\osakini.mp3')     
                    elif (wanted_word == "6"):
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\sayoonara.mp3')
                    elif (wanted_word == "7"):
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\sumimasen.mp3')
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\sumimasen2.mp3')
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\sumimasen3.mp3')        
                    elif(wanted_word == "q"):
                        break;

                except:
                    print("please input a valid number")  
        elif(lesson_num == "2"):
            print("Hello to lesson2")
            print("Enter the word you want to hear")
            print("1:kitte kudasai       2:wakarimashita        Press 'q' to exit")
            
            while True:
                try:
                    wanted_word = input()
                    if (wanted_word == "1"):
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\kitte_kudasai.mp3')
                    elif (wanted_word == "2"):
                        playsound(r'D:\University\Japanese langaugae\Japaneese_code\wakarimashita.mp3')        
                    elif(wanted_word == "q"):
                        break;

                except:
                    print("please input a valid number")        
        elif(lesson_num == "3"):
            playsound(r'D:\University\Japanese langaugae\Japaneese_code\hiragana.mp3')
        elif(lesson_num == "q"):
            break;            
except:
    print("please input a valid number") 
