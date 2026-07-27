def main():
    while True:
        print("選択してください：")
        print("1: kagaken")
        print("2: hide")
        print("3: fumifumi")
        print("4: 佐藤です！")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("kagakenが選ばれました。")
        elif choice == "2":
            print("hideが選ばれました。")
        elif choice == "3":
            print("fumifumiが選ばれました。")
        elif choice == "4":
            print("佐藤　が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
