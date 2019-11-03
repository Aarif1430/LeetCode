class Singleton(object):
    _instance = None
    __iterator = 1

    def __new__(cls):
        print('++++++++++++++++++++++++++++++++++++++++++')
        if not cls._instance:
            Singleton.__iterator = Singleton.__iterator + 4
            cls._instance = super(Singleton, cls).__new__(cls)

    def getIncrementedValue(cls):

        if Singleton.__iterator is not 0:
            print('######################')
            Singleton.__new__(cls)
            Singleton._instance = None
        return Singleton.__iterator


if __name__ == '__main__':
    for i in range(60):
        # s1 = Singleton()
        print(Singleton.getIncrementedValue(Singleton))
