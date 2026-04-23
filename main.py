def main():
    while True:
        print("選択してください：")
        print("1: taku@64期_2")
        print("2: Tomo@64期")
        print("3: 柚木62期")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("taku@64期_2が選ばれました。")
        elif choice == "2":
            print("Tomo@64期が選ばれました。")
        elif choice == "3":
            print("柚木62期が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")


if __name__ == "__main__":
    main()
