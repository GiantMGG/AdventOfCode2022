class HelferWichtel():
    def __init__(self) -> None:
        return

    def getPuzzleInput(self,Tuernummer:str) -> list[str]:
        if not Tuernummer:
            raise Exception('Kein gültiger String als Türnummer angegeben')
        pathToInput = './Input/'
        pathToFile = 'day' + Tuernummer +'.txt'
        try:
            with open(pathToInput + pathToFile) as file:
                lines = file.readlines()
        except EnvironmentError:
            raise Exception('Datei mit diesem Namen existiert nicht')
        return lines
        