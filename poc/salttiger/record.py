class Record(dict):
    def __setattr__(self, name, value):
        # print(f'name = {name}')
        self[name] = value

    def __getattr__(self, name):
        return self[name]

    def __delattr__(self, name):
        del self[name]

    def __dir__(self):
        return list(self) + list(type(self))
