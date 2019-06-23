class Data:

    @staticmethod
    def load_data(filename):
        file = open('data/' + str(filename))
        data = file.read().splitlines()
        return "".join(data)