def main():
    while True:
        print("選択してください：")
        print("1: 白井")
        print("2: mojami")
        print("3: 選択肢3")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("白井が選ばれました。")
        elif choice == "2":
            print("mojamiが選ばれました。")
        elif choice == "3":
            print("mojaが選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()