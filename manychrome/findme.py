from colorful import Colorful

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
