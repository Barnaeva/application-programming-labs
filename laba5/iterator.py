import os


class MyIterator:
    def __init__(self, name_dir:str):
        data=[]
        for name in os.listdir(name_dir):
            data.append(os.path.join(name_dir,name))
        limit=len(data)
        self.data=data
        self.limit = limit
        self.counter = 0


    def __iter__(self):
        return self


    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.data[self.counter-1]
        else:
            raise StopIteration