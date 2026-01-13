def main():
    while True:
        print("選択してください：")
        print("1: まつかん")
        print("2: undertree")
        print("3: もりりん")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("まつかんが選ばれました。")
        elif choice == "2":
            print("undertreeが選ばれました。")
        elif choice == "3":
            print("もりりんが選ばれました。")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")


if __name__ == "__main__":
    main()
