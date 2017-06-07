class superList(list):  # list is a built-in class
    def __sub__(self, b): # re-define substrate -
        a = self[:]
        b = b[:]
        while len(b) > 0:
            element_b = b.pop()
            if element_b in a:
                a.remove(element_b)
        return a

print superList([1,2,3]) - superList([3,4])