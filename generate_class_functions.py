from random import choice
from string import ascii_letters

teml = [1,2,3,4,5,6,7,8,9]

class GC(object):
    def __init__(self):
        GC.gen_fn()
        pass

    def listcm(self):
        print('\n'.join([m for m in dir(self) if not m.startswith('__')]))

    def exec_all_fn(self):
        for f in [m for m in dir(self) if m.startswith('fun_')]:
            getattr(self, f)()
        print('------------------------')

    @classmethod
    def gen_fn(cls):
        for i in teml:
            def _f_gen(var):
                r = ''.join([ choice(ascii_letters) for _ in range(30) ])
                def fn(self):
                    print("I'm from : %s, Random: %s" % (var, r))
                return fn
            setattr(cls, "fun_%s" % i, _f_gen(i))


if __name__ == '__main__':

    c = GC()
    c.listcm()

    c.exec_all_fn()
    c.exec_all_fn()
    c.exec_all_fn()

    c.gen_fn()
    c.exec_all_fn()
    c.exec_all_fn()
    # for f in [m for m in dir(c) if m.startswith('fun_')]:
    #     getattr(c, f)()
