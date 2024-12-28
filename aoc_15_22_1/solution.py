from copy import deepcopy
input =  open("aoc_15_22_1\\input.txt").readlines()
bossHp = int(input[0].split()[-1])
bossDmg = int(input[1].split()[-1])
spells = {"magic_missile", "drain", "shield", "poison", "recharge"}
bestKill = None

def do_turn(spell, myHp, myAp, myMana, bhp, spentMana, activeSpells, turn):
    # dots on player turn
    global bestKill

    if bestKill != None and spentMana >= bestKill:
        return
    
    for activeSpell in activeSpells.keys():
        if activeSpell == "shield" and activeSpells["shield"] > 0:
            myAp = 7
            turns = activeSpells["shield"] - 1
            
            if turns == 0:
                myAp = 0
            
            activeSpells["shield"] = turns 
        elif activeSpell == "poison" and activeSpells["poison"] > 0:            
            bhp -= 3
            activeSpells["poison"] -= 1            
        elif activeSpell == "recharge" and activeSpells["recharge"] > 0:
            myMana += 101            
            activeSpells["recharge"] -= 1
    
    if bhp <= 0:        
        if bestKill == None or bestKill > spentMana:
            bestKill = spentMana
        return   

    
    if myMana < 53:        
        return
     
    if spell == "magic_missile":
        if myMana < 53:
            return
        else:
            myMana -= 53
            spentMana += 53
            bhp -= 4            
    elif spell == "drain":  
        if myMana < 73:
            return
        myHp += 2
        bhp -=2
        myMana -= 73
        spentMana += 73        
    elif spell == "shield":
        if myMana < 113 or activeSpells["shield"] > 0:
            return        
        myMana -= 113
        spentMana += 113
        activeSpells["shield"] = 6
    elif spell == "poison":
        if myMana < 173 or activeSpells["poison"] > 0:
            return        
        myMana -= 173
        spentMana += 173
        activeSpells["poison"] = 6
    elif spell == "recharge":
        if myMana < 229 or activeSpells["recharge"] > 0:
            return
        myMana -= 229
        spentMana += 229
        activeSpells["recharge"] = 5
    
    # boss turn
    turn +=1    
    
    for activeSpell in activeSpells.keys():
        if activeSpell == "shield" and activeSpells["shield"] > 0:
            myAp = 7
            turns = activeSpells["shield"] - 1
            
            if turns == 0:
                myAp = 0                
            
            activeSpells["shield"] = turns 
        elif activeSpell == "poison" and activeSpells["poison"] > 0:
            bhp -= 3
            activeSpells["poison"] -= 1           
        elif activeSpell == "recharge" and activeSpells["recharge"] > 0:
            myMana += 101            
            activeSpells["recharge"] -= 1

    if bhp <= 0:        
        if bestKill == None or bestKill > spentMana:
            bestKill = spentMana
        return
    
    myHp -= max(1, bossDmg - myAp)    

    if myHp <= 0:        
        return
    
    for spell in spells:
        do_turn(spell, myHp, myAp, myMana, bhp, spentMana, deepcopy(activeSpells), turn + 1)  


for spell in spells:
    activeSpells = dict()
    activeSpells["shield"] = 0
    activeSpells["poison"] = 0
    activeSpells["recharge"] = 0
    do_turn(spell, 50, 0, 500, bossHp, 0, activeSpells, 1)

print(bestKill)
