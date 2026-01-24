import sys

input = sys.stdin.readline

class Bead:
    def __init__(self, y, x, direction, weight, number):
        self.y = y
        self.x = x
        self.direction = direction
        self.weight = weight
        self.number = number
    
    def __eq__(self, other):
        return isinstance(other, Bead) and self.number == other.number
    
    def getNextPos(self):
        if (self.direction == "U"):
            return (self.y - 1, self.x)
        elif (self.direction == "D"):
            return (self.y + 1, self.x)
        elif (self.direction == "R"):
            return (self.y, self.x + 1)
        elif (self.direction == "L"):
            return (self.y, self.x - 1)

    def move(self, y, x):
        self.y = y
        self.x = x
    
    def transferDirection(self):
        if (self.direction == "U"):
            self.direction = "D"
        elif (self.direction == "D"):
            self.direction = "U"
        elif (self.direction == "R"):
            self.direction = "L"
        elif (self.direction == "L"):
            self.direction = "R"
    
def simulation(beads, N, T):
    
    for t in range(T):
        
        # 구슬 움직이기
        for bead in beads:
            y, x = bead.getNextPos()
            
            # 범위를 넘어가면 방향 변경
            if (y < 0 or x < 0 or y >= N or x >= N):
                bead.transferDirection()
                continue
            
            # 한 칸 움직이기 
            bead.move(y, x)
        
        # 충돌 검사하기
        position = {}
        for bead in beads:
            pos = (bead.y, bead.x)
            position.setdefault(pos, []).append(bead)
        
        for pos, space in position.items():
            if (len(space) == 1):
                continue
            
            # 충돌이 발생
            y, x = pos
            weight = 0
            maxBead = None
            for bead in space:
                weight += bead.weight
                
                if (maxBead is None):
                    maxBead = bead
                else:
                    if (bead.number > maxBead.number):
                        maxBead = bead

            newBead = Bead(y, x, maxBead.direction, weight, maxBead.number)
            
            # 삭제 후 합쳐진 구슬 추가
            for bead in space:
                beads.remove(bead)
            beads.append(newBead)
    
    maxWeight = 0
    for bead in beads:
        maxWeight = max(maxWeight, bead.weight)
    
    # printBeads(beads)
    print(len(beads), maxWeight)

def printBeads(beads):
    for bead in beads:
        print(bead.y, bead.x, bead.direction, bead.weight, bead.number)
    print()

if __name__=="__main__":
    N, M, T = map(int, input().split())
    beads = []

    for num in range(M):
        y, x, d, w = input().split()
        beads.append(Bead(int(y) - 1, int(x) - 1, d, int(w), num))
    
    simulation(beads, N, T)