from typing import List, Dict, Tuple


class FiniteAutomata:
    states: List[str]
    alphabet: List[str]
    transitions: Dict[Tuple[str, str], List[str]]
    initialState: str
    finalStates: List[str]

    def __init__(self, states: List[str], alphabet: List[str], transitions: Dict[Tuple[str, str], List[str]],
                 initial_state: str, final_states: List[str]):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initialState = initial_state
        self.finalStates = final_states

    @staticmethod
    def readFromFile(file_name: str):
        states = []
        alphabet = []
        transitions = {}
        initialState = None
        finalStates = []

        with open(file_name, 'r') as file:
            for lineCounter, line in enumerate(file, start=1):
                line: str = line.strip()
                tokens = line.split(";")
                if tokens[0] == "states":
                    states = tokens[1:]
                elif tokens[0] == "alphabet":
                    alphabet = tokens[1:]
                elif tokens[0] == "transitions":
                    for transition in tokens[1:]:
                        transition_tokens = transition.split(",")
                        trans = (transition_tokens[0], transition_tokens[1])
                        if trans in transitions:
                            transitions[trans].append(transition_tokens[2])
                        else:
                            transitions[trans] = [transition_tokens[2]]
                elif tokens[0] == "initialState":
                    initialState = tokens[1]
                elif tokens[0] == "finalState":
                    finalStates = tokens[1:]
        return FiniteAutomata(states, alphabet, transitions, initialState, finalStates)



    def printStates(self):
        print("Set of states: ", self.states)

    def printAlphabet(self):
        print("FA alphabet: ", self.alphabet)

    def printInitialState(self):
        print("Initial state: ", self.initialState)

    def printFinalStates(self):
        print("Final states: ", self.finalStates)

    def printTransitions(self):
        print("Transitions: ")
        for transition in self.transitions.keys():
            print("delta({0}, {1}) = {2}".format(transition[0], transition[1], self.transitions[transition]))

    def isDfa(self) -> bool:
        for key in self.transitions.keys():
            if len(self.transitions[key]) > 1:
                return False
        return True

    def checkSequence(self, sequence) -> bool:
        if not self.isDfa():
            raise ArithmeticError("FiniteAutomata is not a DFA")
        currentState = self.initialState

        while sequence != "":
            transition_key = (currentState, sequence[0])

            if transition_key in self.transitions.keys():
                currentState = self.transitions[transition_key][0]
                sequence = sequence[1:]

            else:
                return False

        return currentState in self.finalStates


if __name__ == "__main__":
    print(""
          "1. Display the set of states \n"
          "2. Display the alphabet \n"
          "3. Display all the transitions \n"
          "4. Display the set of final states \n"
          "5. Check if a sequence is accepted by the FA \n"
          "0. Exit.")

    automata = FiniteAutomata.readFromFile("fa_test.in")
    menuOption = input("-> ")


    while menuOption != "0":
        if menuOption == "1":
            automata.printStates()
            menuOption = input("-> ")
        elif menuOption == "2":
            automata.printAlphabet()
            menuOption = input("-> ")
        elif menuOption == "3":
            automata.printTransitions()
            menuOption = input("-> ")
        elif menuOption == "4":
            automata.printFinalStates()
            menuOption = input("-> ")
        elif menuOption == "5":
            sequence = input("Sequence: ")
            print(sequence, automata.checkSequence(sequence))
            menuOption = input("-> ")



