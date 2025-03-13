import sys

input = sys.stdin.readline


class Pocketmon:

    def __init__(self, name, number) -> None:
        self.name = name
        self.number = number

    # def __str__(self) -> str:
    #     return self.name

    def __call__(self):
        print(self.name)


def main():
    n, m = map(int, (input().split(" ")))
    i = 1
    pocketdict = {}
    pocktlist = [""]
    for _ in range(n):
        pmname = input().strip()
        pocketdict[pmname] = i
        pocktlist.append(pmname)
        i += 1

    for _ in range(m):
        q = input().strip()
        try:
            q = int(q)
            print(pocktlist[q])
        except ValueError:
            print(pocketdict[q])


if __name__ == "__main__":
    main()
