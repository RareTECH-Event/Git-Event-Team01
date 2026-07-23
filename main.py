def main():
    while True:
        print("選択してください：")
        print("1: まさき@65期")
        print("2: さえ@66期")
        print("3: しんわ@68期")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("まさきが選ばれました。")
        elif choice == "2":
            print("さえが選ばれました。")
        elif choice == "3":
            print("しんわが選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
