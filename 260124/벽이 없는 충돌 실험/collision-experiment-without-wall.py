import sys

input = sys.stdin.readline

class Bead:
    def __init__(self, x, y, weight, direction, number):
        self.x = x
        self.y = y
        self.weight = weight
        self.direction = direction
        self.number = number
    
    def __eq__(self, other):
        return isinstance(other, Bead) and self.number == other.number
    
    def move(self):
        if (self.direction == "U"):
            self.y += 1
        elif (self.direction == "D"):
            self.y -= 1
        elif (self.direction == "R"):
            self.x += 1
        elif (self.direction == "L"):
            self.x -= 1
    
    def isOutOfBoard(self):
        if (self.x < 0 or self.y < 0 or self.x > 4000 or self.y > 4000):
            return True
        return False

def simulation(beads):
    answer = -1
    time = 0

    while(beads):
        time += 1
        # 구슬을 0.5초(1칸)씩 움직이기
        for bead in beads:
            bead.move()
        
        position = {}
        # 현재 위치들을 map에 저장
        for bead in beads:
            pos = (bead.x, bead.y)
            position.setdefault(pos, []).append(bead)
        
        # 충돌이 발생한지 검증
        for pos, arr in position.items():
            if (len(arr) == 1): continue
            # 엉향력이 큰 순서대로 정렬
            arr.sort(key = lambda x: (-x.weight, -x.number))
            
            for i in range(1, len(arr)):
                beads.remove(arr[i])

            # 충돌한 시간 설정
            answer = time
        
        temp = []
        # 영역을 넘어가면 구슬은 사라진다
        for bead in beads:
            if (bead.isOutOfBoard()):
                temp.append(bead)
        
        for bead in temp:
            beads.remove(bead)
    
    print(answer)
            


if __name__=="__main__":
    T = int(input())
    
    for t in range(T):
        N = int(input())
        beads = []
        for n in range(1, N + 1):
            x, y, w, d = input().split()
            x = (int(x) + 1000) * 2
            y = (int(y) + 1000) * 2
            beads.append(Bead(x, y, int(w), d, n))
        
        simulation(beads)
            
            

        
