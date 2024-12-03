# TODO Update this one as to add many colours before writing the file.
def save_favs(save_as):
    fav_fg = []
    fg_resp = input("Favourite Col#\n")
    fav_fg.append(fg_resp)
    go = ["Col: "+ str(col) + "\n" for col in fav_fg]
    with open(save_as, "a") as fi:
        fi.writelines(go)
    print("file saved: ", save_as)

keep_me = "manychrome/examples/save_my_colors.ini"
save_favs(keep_me)


def choose_color():
    for i in range(0, 256):
        print(f"\033[38;5;16;48;5;{i}m  Col: {i}  \033[0m", "", f"\033[38;5;255;48;5;{i}m  Col: {i}  \033[0m")
