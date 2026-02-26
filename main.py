def main():
    while True:
        print("選択してください：")
        print("1: daifuku")
        print("2: りゅう")
        print("3: akimo")
        print("q: MOMO")

        choice = input("> ")

        if choice == "1":
            print("選択肢1：おはよう")
        elif choice == "2":
            print("選択肢2：こんばんは！")
        elif choice == "3":
            print("選択肢3：おやすみなさい！")
        elif choice == "q":
            print("プログラムをMOMOします。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
