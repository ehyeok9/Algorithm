def solution(bandage, health, attacks):
    MAXIMUM = health
    
    healTime = bandage[0]
    secHeal = bandage[1]
    extraHeal = bandage[2]
    
    lastTime  = attacks[-1][0]
    curSuccess = 0
    attackIdx = 0
    
    for sec in range(lastTime + 1):
        # print(sec, health, curSuccess)
        if sec == attacks[attackIdx][0]:
            health -= attacks[attackIdx][1]
            curSuccess = 0
            attackIdx += 1
        else:
            health += secHeal
            curSuccess += 1
            if curSuccess == healTime:
                health += extraHeal
                curSuccess = 0
            if health > MAXIMUM: health = MAXIMUM
        
        if health <= 0: return -1
            
    return health