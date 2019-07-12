# -*- coding: utf-8 -*-
import sys

def namahamu_generate(name="生ハム原木"):
    """生ハム原木コピペを生成する
    Args:
        name(string): 同棲することが有効なものの名前
    """
    text = "{name}が家にあると、ちょっと嫌なことがあっても「まあ家に帰れば{name}あるしな」ってなるし仕事でむかつく人に会っても「そんな口きいていいのか？私は自宅で{name}とよろしくやってる身だぞ」ってなれる。戦闘力を求められる現代社会において{name}と同棲することは有効"
    print(text.format(name=name))

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2:
        print("( ^ω^) < 同棲することが有効なものの名前を入力してください\n↓")
        name = input()
        if name == "":
            name = "生ハム原木"
        print("\n")
        namahamu_generate(name)
    else:
        for name in args[1:]:
            print("\n")
            namahamu_generate(name)
