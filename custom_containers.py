class TagCloud:
    def __init__(self):
        self.__tags = {}   #prefixing with __ makes the private

    def add(self, tag):
        self.__tags[tag] = self.__tags.get(tag.lower(), 0) + 1
    
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)
        
cloud = TagCloud()
print(cloud["Python"])
cloud.add("Python")
cloud.add("Python")
cloud.add("Python")
print(cloud.__dict__)
print(cloud._TagCloud__tags)