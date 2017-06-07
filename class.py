class Bird(object):   # father class
    have_feather = True
    way_of_reproduction = 'egg'

    def move(self, dx, dy):  # define methods
        position = [0,0]
        position[0] = position[0] + dx
        position[1] = position[1] + dy
        return position


class happyBird(Bird):
    def __init__(self,more_words):  # special method _init_
        print 'We are happy birds.',more_words

summer = happyBird('happy birthday')