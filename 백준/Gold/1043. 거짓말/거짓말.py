import sys

input = sys.stdin.readline

global people, party, avoid
global visited_party, visited_person

def dfs(person, visited_person):
    for nxt_party in people[person]:
            visited_party.add(nxt_party)            
            for nxt_person in party[nxt_party]:
                # print(nxt_party, nxt_person)
                if nxt_person not in visited_person:
                    visited_person.add(nxt_person)
                    dfs(nxt_person, visited_person)



if __name__ == "__main__":
    n, m = map (int, input().split())
    avoid = list(map(int, input().split()))
    avoid = avoid[1:]
    
    people = [[] for _ in range(n+1)]
    party = [[] for _ in range(m)]
    for i in range(m):
        temp = list(map(int, input().split()))
        for j in range(1, temp[0]+1):
            people[temp[j]].append(i)
        party[i] = temp[1:]
    
    # print(people)
    # print(party)
    visited_party = set()
    for person in avoid:
        dfs(person, set())
        
    
    print(m - len(visited_party))
        
        
    
    
    