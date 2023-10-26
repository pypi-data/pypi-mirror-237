from io import StringIO


class StringBuffer(object):
    def __init__(self):
        self.buf = StringIO()

    def a(self, content: str):
        self.buf.write(content)
        self.buf.write("\n")

    def __str__(self):
        cur_pos = self.buf.tell()
        self.buf.seek(0)
        ret = self.buf.read()
        self.buf.seek(cur_pos)
        return ret
