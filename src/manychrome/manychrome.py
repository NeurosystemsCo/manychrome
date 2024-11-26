from dataclasses import dataclass

class ColorfulConfig:
    def __init__(self, *, default):
        self._default = default

    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, obj, type):
        if obj is None:
            return self._default

        return getattr(obj, self._name, self._default)

    def __set__(self, obj, value):
        setattr(obj, self._name, (value))



@dataclass
class Colorful:
    fg: ColorfulConfig = ColorfulConfig(default=0)
    bg: ColorfulConfig = ColorfulConfig(default=0)
    bo: ColorfulConfig = ColorfulConfig(default=False)
    ft: ColorfulConfig = ColorfulConfig(default=False)
    it: ColorfulConfig = ColorfulConfig(default=False)
    ul: ColorfulConfig = ColorfulConfig(default=False)
    st: ColorfulConfig = ColorfulConfig(default=False)
    sh: ColorfulConfig = ColorfulConfig(default=False)
    wx: ColorfulConfig = ColorfulConfig(default='')


    def write(self, words):
        styling = []
        fg = []
        bg = []
        styles = [(self.it, 3), (self.bo, 1), (self.ul, 4), (self.st, 9), (self.sh, 7)]
        colours = [(self.fg, self.bg)]
        for key, value in styles:
            if key:
                s = f"\033[{value};5m"
                styling.append(s)

        for key, value in colours:
            if key:
                f = f"\033[38;5;{key}m"
                fg.append(f)
            if value:
                v = f"\033[48;5;{value}m"
                bg.append(v)
        z = "\033[0m"

        s1 = styling + fg + bg
        styled_text = "".join(s1) + words + z
        print(styled_text)

    def styleme(self, words):
        styling = []
        fg = []
        bg = []
        styles = [(self.it, 3), (self.bo, 1), (self.ul, 4), (self.st, 9), (self.sh, 7)]
        colours = [(self.fg, self.bg)]
        for key, value in styles:
            if key:
                s = f"\033[{value};5m"
                styling.append(s)

        for key, value in colours:
            if key:
                f = f"\033[38;5;{key}m"
                fg.append(f)
            if value:
                v = f"\033[48;5;{value}m"
                bg.append(v)
        z = "\033[0m"

        s1 = styling + fg + bg
        styled_text = "".join(s1) + words + z
        return(styled_text)

# TODO Update this one as to add many colours before writing the file.
def save_favs(save_as):
    fav_fg = []
    fg_resp = input("Favourite Col#\n")
    fav_fg.append(fg_resp)
    go = ["Col: "+ str(col) + "\n" for col in fav_fg]
    with open(save_as, "a") as fi:
        fi.writelines(go)
    print("file saved: ", save_as)

file = "manychrome/examples/save_my_colors.ini"
# save_favs(file)


def choose_color():
    for i in range(0, 256):
        print(f"\033[38;5;16;48;5;{i}m  Col: {i}  \033[0m", "", f"\033[38;5;255;48;5;{i}m  Col: {i}  \033[0m")



class Stylish(dict, Colorful):
    def __missing__(self, key):
        return str(key)

    def findme(self, doc):
        for key, value in self.items():
            v = Colorful()
            v = self.styleme(value)
            self.update({key: v})
        print(doc.format_map(self))

    def italics(self, txt):
        v = Colorful()
        v.it = True
        v.fg = self.fg
        print(v.styleme(txt))

    def highlight(self, txt):
        v = Colorful()
        v.fg = self.fg
        v.bg = self.bg
        print(v.styleme(txt))

    def underline(self, txt):
        v = Colorful()
        v.ul = True
        v.fg = self.fg
        print(v.styleme(txt))

    def strikethrough(self, txt):
        v = Colorful()
        v.st = True
        v.fg = self.fg
        print(v.styleme(txt))

    def bold(self, txt):
        v = Colorful()
        v.bo = True
        v.fg = self.fg
        print(v.styleme(txt))

    def swap(self, txt):
        # This one is not quite working
        v = Colorful()
        v.sh = True
        v.fg = self.fg
        v.bg = self.bg
        print(v.styleme(txt))

class FindMe(dict, Colorful):
    def __missing__(self, key):
        return str(key)

    def showme(self, doc):  # Could name to makemepop
        for key, value in self.items():
            v = Colorful()
            v = self.styleme(value)
            self.update({key: v})
        print(doc.format_map(self))

    def reverseme(self, words):
        pass

    def mirrorme(self, words):
        bg = dict(bg="fg")
        print(f"abc {bg["bg"]} def")

    def listme(self, list, heading=False):
        v = [str(item) for item in list]
        if not heading:
            print(f"{"\n".join(v)}")
        else:
            print(f"\33[48;5;{self.fg}m{heading}\033[0m\n{"\n".join(v)}")

    def listmepretty(self, list, heading=False, head_style=False):
        v = [self.styleme(str(item)) for item in list]
        h = head_style.styleme(str(heading))
        if not heading:
            print(f"{"\n".join(v)}")
        else:
            print(f"{h}\033[0m\n{"\n".join(v)}")
            # print(f"\33[48;5;{head_style.bg}m{h}\033[0m\n{"\n".join(v)}")

    def but_why(self, doc):
        """
        a = "Get text"
        b = "Get list of why words from db"
        c = "Find the words in the doc"
        cd = "Split the sentences where the words are present and store this list"
        d = "wrap only the words in the doc so to be able to display the whole text with the sentences"
        e = "return the list with only the sentences, and second, return the text where the words have been highlighted (to be able to check the sentences in the full context)."
        """

        why_words = ["why", "because", "which means", "therefore"]
        r = [doc.partition(why) for why in why_words]
        print(r)

    def but_what(self, doc):
        what_words = ["list of", "what", "essentially"]
        print(what_words)


    def but_how(self, list, doc):
        how_words = ["how", "you do", "first take"]
        print(how_words)



v = FindMe()
v.mirrorme("Ohreally?")
v.listme(["here", "we", "have", "dogs", "cats", 1, 4, "teddy"])
j = Colorful(fg=209, it=True)
li = ["here", "we", "have", "dogs", "cats", 1, 4, "teddy"]
bob = [j.styleme(str(item)) for item in li]
v.listme(bob)

m = FindMe()
m.fg = 24

mm = FindMe()
mm.fg = 199
mm.bg=57
mm.bo = True
m.listmepretty(li, heading=" SOME LIST ", head_style=mm)



document = "Once upon a time there was a {noun} who really wanted to {desire}. Everybody knew it would take {verb} and {stuff}..."
doc2 = "Some other stuff here {text} and there is also a {doc}, and {someone} said they really wanted to go outside."

# Could name this "LookMeUp or FindMe or WhereAmI or PopMeOut"
wrap = Stylish(
    noun=" doggo ",
    desire=" jump around ",
    verb=" a joyous attitude ",
    stuff=" heaps of time "
)
wrap.fg = 123
wrap.bg = 129
wrap.it = True
wrap.findme(document)

styled = FindMe(
    text="Named",
    doc="Excellent Book",
    someone="Unnamed"
)
styled.fg = 201
styled.it = True
styled.bo = True
styled.showme(doc2)

s = Colorful(bg=69, it=True)
s.write("This is a colorful highlighted message.")

c = Colorful(fg=195, it=True, bo=True)
c.write("Here is an example that has other colors.")



# TODO >> need to organise the modules because right now the classes Colorful and Stylish seems to overlap, so need some structure later when I write more functions with these. Use colorful for colour, stylish for style. But then the FindMe should be elsewhere...

# Example Code
heading = " DOGGOS "
dogs = ["Max", "Bobby", "Dracula", "Leopold"]
d = FindMe()
c = Colorful(fg=204, it=True)
h = Colorful(fg=195, bg=204, bo=True)
heading = h.styleme(heading)
d.listme([c.styleme(dog) for dog in dogs], heading=heading)

nn = FindMe()
nn.fg=47
nn.bg=96
nn.listmepretty(dogs, heading=heading, head_style=h)
