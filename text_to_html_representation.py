


def text_to_html_representation(text, hexformat=False):
     return "".join(['&#%s;'%str(hex(ord(c)))[1:] for c in text.decode('utf-8')]) if hexformat else "".join(['&#%s;'%str(ord(c)) for c in text.decode('utf-8')])
