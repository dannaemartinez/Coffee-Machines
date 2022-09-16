from premium import PMachine
from basic import CBMachine

if __name__ == '__main__':
    cBMachine = CBMachine()
    try:
        print('Can Basic Machine grind?')
        cBMachine.grindingAll()
    except:
        print('False')
    else:
        print('True')

    try:
        print('Can Basic Machine brew?')
        cBMachine.brewingAll()
    except:
        print('False')
    else:
        print('True')

    try:
        print(f'Can Basic Machine serve?')
        cBMachine.servingAll()
    except:
        print('False')
    else:
        print('True')
    
    try:
        print(f'Can Basic Machine make black coffee?')
        cBMachine.black()
    except:
         print('False')
    else:
        print('True')
        
    try:
        print('Can Basic Machine do espresso coffee?')
        cBMachine.espresso()
    except:
        print('False')
    else:
        print('True')

    try:
        print('Can Basic Machine do ice cold coffee?')
        cBMachine.icecoldcoffee()
    except:
        print('False')
    else:
        print('True')

    pmMachine = PMachine()
    try:
        print('Can Premium Machine grind?')
        pmMachine.grindingAll()
    except:
        print('False')
    else:
        print('True')

    try:
        print('Can Premium Machine brew?')
        pmMachine.brewingAll()
    except:
        print('False')
    else:
        print('True')

    try:
        print(f'Can Premium Machine serve?')
        pmMachine.servingAll()
    except:
        print('False')
    else:
        print('True')
    
    try:
        print(f'Can Premium Machine make black coffee?')
        pmMachine.black()
    except:
         print('False')
    else:
        print('True')
        
    try:
        print('Can Premium Machine do espresso coffee?')
        pmMachine.espresso()
    except:
        print('False')
    else:
        print('True')
    
    try:
        print('Can Premium Machine do ice cold coffee?')
        pmMachine.icecoldcoffee()
    except:
        print('False')
    else:
        print('True')