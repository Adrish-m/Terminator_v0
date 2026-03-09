# import msvcrt as kb
# c = 1
# while c:
#     if kb.kbhit():
#         print(ord(kb.getwch()),ord(kb.getch()))
#         if kb.getwch() == "e":
#             c = 0
#             print("exit")

import key

while True:
    if key.iskeypressed():
        print(key.get_key())