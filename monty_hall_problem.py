import random

botWins = 0
plays = int(input('How many plays should there be?:  '))

def main():
    doors = ['Door One', 'Door Two', 'Door Three']
    chosen = random.randint(0,2)
    winningDoor = doors[chosen]
    chosen = random.randint(0,2)
    botsChoice = doors[chosen]
    hostsReveal = HostOpensDoor(winningDoor, botsChoice, doors)
    botsChoice = BotChangesMind(botsChoice, hostsReveal, doors)
    if botsChoice == winningDoor:
        return 1
    else:
        return 0
    
def HostOpensDoor(winningDoor, botsChoice, doors):
    candidates = []
    for door in doors:
        possibleCandidate = door
        if possibleCandidate != winningDoor and possibleCandidate != botsChoice:
            candidates.append(door)
    lastIndex = (len(candidates) - 1)
    hostsReveal = random.randint(0,lastIndex)
    return candidates[hostsReveal]

def BotChangesMind(botsChoice, hostsReveal, doors):
    for door in doors:
        if door != botsChoice and door != hostsReveal:
            return door

for play in range(plays):
    botWins += main()

winPercentage = (botWins / plays) * 100
print('Bot win percentage is', winPercentage)
print()
input('Enter to close.')
