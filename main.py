def main():
    while True:
        print("選択してください：")
        print("1: 選択肢1")
        print("2: 選択肢2")
        print("3: 選択肢3")
        print("4: 選択肢4")
        print("5: 選択肢5")
        print("6: 選択肢6")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("選択肢1が選ばれました。")
        elif choice == "2":
            print("選択肢2が選ばれました。")
        elif choice == "3":
            print("選択肢3が選ばれました。")
        elif choice == "4":
            print("選択肢4が選ばれました。")
        elif choice == "5":
            print("選択肢5が選ばれました。")
        elif choice == "6":
            print("選択肢6が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")


if __name__ == "__main__":
    main()
