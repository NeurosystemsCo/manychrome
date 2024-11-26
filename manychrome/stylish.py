from colorful import Colorful

"""The intention of stylish is to provide CLI text styling also without color"""
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
