class HashMap:
    def insert(self, key, value):
        # call resize
        self.resize()

        index = self.key_to_index(key)
        self.hashmap[index] = (key, value)

    #
    def resize(self):
        #if length of hashmap is 0, make lentgh 1 by adding a None
        if len(self.hashmap) == 0:
            self.hashmap.append(None)
            
        #get the current load
        current_load = self.current_load()

        #if less than 0.05, return
        if current_load < 0.05:
            return
        
        #store the old hashmap in a temp variable
        temp = self.hashmap

        #create a new hashmap with 10x the size
        self.hashmap = [None for i in range(len(temp) * 10)]

        #for each item in the temp variable, directly set them in the new hashmap
        for i in temp:
            if i != None:
                index = self.key_to_index(i[0])
                self.hashmap[index] = i
        
        #return the new hashmap
        return self.hashmap

    #if the length of the hashmap is 0, set the size to 1
    def current_load(self):
        if len(self.hashmap) == 0:
            return 1
        # if the current_load is greater than 0.5%, return count / len(self.hashmap)
        count = 0
        for i in self.hashmap:
            if i != None:
                count += 1
        return count / len(self.hashmap)

    
    # don't touch below this line

    def __init__(self, size):
        self.hashmap = [None for i in range(size)]

    def key_to_index(self, key):
        sum = 0
        for c in key:
            sum += ord(c)
        return sum % len(self.hashmap)

    def __repr__(self):
        final = ""
        for i, v in enumerate(self.hashmap):
            if v != None:
                final += f" - {str(v)}\n"
        return final
