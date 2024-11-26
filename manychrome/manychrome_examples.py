from colorful import Colorful
from findme import FindMe
from stylish import Stylish

# From Colorful
"""Simple function to print a list with the added bonus of ability to add colors and highlights"""
heading = "Important"
stuff = ["Super", "Cool", "Stuff"]

"""Use it to print a list"""
ls = Colorful()
ls.listmepretty(stuff)

"""Print the list in color with a heading"""
c = Colorful(fg=213)
c.listmepretty(stuff, heading="Amazingly", head_style=c)

"""Print the list in color (or not) with different config
for the heading"""
h = Colorful(fg=56, bg=1, bo=True)
c = Colorful()
c.listmepretty(stuff, heading=heading, head_style=h)




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