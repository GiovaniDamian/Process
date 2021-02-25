def Sem_Fale(eo, ed, min):


    total = 0
    vm = 0
    if eo == 1:
        if ed == 2:
            total += (min*1.9)
            vm += 1.9
        if ed == 3:
            total += (min*1.7)
            vm += 1.7
        if ed == 4:
            total += (min*0.9)
            vm += 0.9
    if eo == 2:
        total += (min*2.9)
        vm += 2.9
    if eo == 3:
        total += (min*2.7)
        vm += 2.7
    if eo == 4:
        total += (min*1.9)
        vm += 1.9
    return(f'{total:.2f}', vm)