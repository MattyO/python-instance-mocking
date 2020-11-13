import instance

class Thing():
    def baz(self):
        ignore_me = instance.Instance()
        i = instance.Instance()
        print(i.zed())
        bar_value = i.bar()
        return  bar_value

