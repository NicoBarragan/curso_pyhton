#     dict = {}
#     for i in range(1, 101):
#         dict.update({i:i**3})
#     print(dict.values()) 
# Esto fue hecho con update
# ---------------------------
#     dict = {}
#     for i in range(1, 101):
#         if i % 3 != 0:
#             dict[i] = i**3
#     print(dict) 
# ----------------------------

    # dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # print(dict)

def run():
    dict = {i: i**2 for i in range(1, 101) if i**2 % 2 != 0}
    print(dict)

if __name__ == '__main__':
    run()