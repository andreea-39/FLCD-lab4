class ProgramInternalForm:

    def __init__(self):
        self.__content = []

    def add(self, token, pos):
        self.__content.append((token, pos))

    def __str__(self):
        result = ""
        for pair in self.__content:
            token = pair[0] if pair[0] != '\t' else '\\tab'
            result += token + "->" + str(pair[1]) + "\n"
        return result