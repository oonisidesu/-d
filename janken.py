import import_junken
# randomモジュールを読み込んでください
import random

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')

retry = 0
score = 0
while(retry < 2): #2回する
    print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
    player_hand = int(input('数字で入力してください：'))

    if import_junken.validate(player_hand):
        # randintを用いて0から2までの数値を取得し、変数computer_handに代入してください
        computer_hand = random.randint(0, 2)

        if player_name == '':
            import_junken.print_hand(player_hand)
        else:
            import_junken.print_hand(player_hand, player_name)

        import_junken.print_hand(computer_hand, 'コンピューター')

        result = import_junken.judge(player_hand, computer_hand)
        print('結果は' + result + 'でした')

        if result == "勝ち":
            score += 3
            print("勝ち点" + str(score) + "が与えられました")
            retry += 1
        elif result == "負け":
            score += 0
            print("勝ち点は０です")
            retry += 1
        else:
            score += 1
            print("勝ち点" + str(score) + "が与えられました")
            retry += 1
    else:
        print('正しい数値を入力してください')
        retry += 1

    if retry == 2 and score > 0:
        print("あなたは勝ち点が" + str(score) + "点以上なので大田泰示になりました")
    elif retry == 2 and score == 0:
        print("あなたは勝ち点が" + str(score) + "点なので大田泰示にはなれませんでした")
