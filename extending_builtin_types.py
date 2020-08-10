class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.lower())
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append Called " , self)
        super().append(object)


list = TrackableList("Python")
list.append("1")
