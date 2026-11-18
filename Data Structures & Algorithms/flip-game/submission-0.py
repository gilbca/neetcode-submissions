class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        moves = []

        for i in range(len(currentState) - 1):
          if currentState[i] == "+" and currentState[i+1] == "+":
            new_state = currentState[:i] + '--' + currentState[i+2:]
            moves.append(new_state)
        return moves
