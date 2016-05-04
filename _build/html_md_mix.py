import os, sys, re, urllib2
import mistune

class HtmlRenderer(mistune.Renderer):
    def __init__(self):
        return super(HtmlRenderer, self).__init__()

    def header(self, text, level, raw=None):
        def text_to_id(text):
            return text.replace(" ", "-").replace(",", "")
        return '<h%d id="%s">%s</h%d>\n' % (level, text_to_id(raw), text, level)

def gist_replace(md_parser, text):
    def replace_func(m):
        gist_id = m.group(1)
        url = urllib2.urlopen('https://gist.github.com/%s/raw' % gist_id)
        mdtext = url.read().decode("utf-8-sig")
        return md_parser.parse(mdtext)

    return re.sub('<!-- +MDGIST: *(\S+?) +-->', replace_func, text)

def main(argv):
    if len(argv) <= 1:
        return 1

    filepath = argv[1]
    with open(filepath) as f:
        content = f.read().decode("utf-8-sig")

    m = mistune.Markdown(HtmlRenderer())
    html = gist_replace(m, content)
    if len(argv) > 2:
        open(argv[2], "wb").write(html.encode("utf-8-sig"))
    else:
        print html

if __name__ == "__main__":
    main(sys.argv)
