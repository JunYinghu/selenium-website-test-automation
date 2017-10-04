from HTMLParser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):
    # handle comments
    def handle_comment(self, data):
        print "Encounted comment:", data
        pos = self.getpos()
        print "At line: ", pos[0], " Postion", pos[1]

        # def handle_startendtag(self, tag, attrs):
        #     global metacount
        #     print "Encounted a start tag- ", tag
        #     if tag == "meta":
        #         metacount += 1
        #     pos = self.getpos()
        #     if attrs.__len__ > 0:
        #         print  "\tAttributes:"
        #         for a in attrs:
        #             print "\t", a[0], "=", a[1]
        #     print "At line: ", pos[0], " Postion", pos[1]

        # def handle_endtag(self, tag):
        #     print "Encounted end tag - ", tag
        #     pos = self.getpos()
        #     print "At line: ", pos[0], " Postion", pos[1]


        # def handle_data(self, data):
        #     print "Encounted some data - ", data
        #     pos = self.getpos()
        #     print "At line: ", pos[0], " Postion", pos[1]


def main():
    parser = MyHTMLParser()
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)
        # parser.handle_comment(contents)
        print "%d meta tags encountered " % metacount


if __name__ == "__main__":
    main()
