def main():
    while True:
        print("選択してください：")
        print("1: ぶくろ")
        print("2: さえちゃ")
        print("3: 白井")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("選択肢1が選ばれました。")
        elif choice == "2":
            print("選択肢2が選ばれました。")
        elif choice == "3":
            print("選択肢3が選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
