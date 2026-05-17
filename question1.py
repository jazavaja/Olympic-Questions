class Wordle:
    def __init__(self,Key:str,number_of_guesses:int,guesses:list):
        self.key = list(Key)
        self.n = number_of_guesses
        self.guesses = guesses
        self.game_over = False
        for i in self.guesses:
            self.n -= 1
            if self.game_over:
                print("Game Over")
            else:
                check = self.check_length(self.key,i)


    def check_length(self,key,g):
        G = list(g)
        if len(G) == len(key):
            colors = self.check_letters(key,g)
        else:
            print("Invalid Length")
            return True
    def check_letters(self,key,g):
        G = list(g)
        colors = []
        nl = {}
        for i in key:
            if i in nl:
                nl[i] += 1
            else:
                nl[i] = 1
        for x,i in enumerate(G):
            if i == key[x]:
                nl[i] -= 1
                colors.append("G")
            elif i in key:
                if nl[i] == 0:
                    colors.append("R")
                else:
                    nl[i] -= 1
                    colors.append("Y")

            elif i not in key:
                colors.append("R")
        NG = 0
        for i in colors:
            if i == "G":
                NG += 1
        if NG == len(colors):
            self.game_over = True
        print(colors)
        # qwert
        # 2
        # qgsgw
        # qrttw
w = Wordle
# k = input()
# n = input()
# g = []
# for i in range(int(n)):
#     g.append(input())
# print(k)
# print(n)
# print(g)
w("mississippi", 7, [
    "missmissmpi",
    "ismsmsimmmm",
    "misisipi",
    "misisipipimsi",
    "mississippi",
    "icansolveit",
    "iwantmyscore"
])