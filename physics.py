#physics formulas calculator

calculations=['1.speed','2.force','3.density','4.weight','5.kinetic energy']
for calculation in calculations:
    print(calculation)

choice=int(input('select a a choice from 1-5: '))
if choice ==1:
    distance=float(input('enter the distance in meters: '))
    time=float(input('enter the time in seconds: '))
    print('speed = distance / time')
    print('to calculate press q:')
    while True:
     answer=(input('your answer is: '))
     if answer=='q':
         print(distance//time,'m/s')
         break


elif choice ==2:
    mass=float(input('enter the mass of the object: '))
    acceleration=float(input('enter the acceleration of the object: '))
    print('force = mass * acceleration')
    print('to calculate press q:')
    while True:
        answer = (input('your answer is: '))
        if answer == 'q':
            print(mass * acceleration, 'm/s^2',)
            break

elif choice ==3:
    mass = float(input('enter the mass of the object: '))
    volume = float(input('enter the volume of the object: '))

    print('density = mass / volume')
    print('to calculate press q:')
    while True:
        answer = (input('your answer is: '))
        if answer == 'q':
            print(mass / volume, 'kg/m^3' )
            break



elif choice ==4:
    mass = float(input('enter the mass of the object: '))
    gravity = float(input(10))
    print('weight = mass * gravity')
    print('to calculate press q:')
    while True:
        answer = (input('your answer is: '))
        if answer == 'q':
            print(mass * gravity , 'kg/m^3')
            break

elif choice ==5:
    mass = float(input('enter the mass of the object: '))
    velocity = float(input('enter the velocity of the object: '))
    print('kinetic energy = 1/2 * mass * velocity')
    print('to calculate press q:')
    while True:
        answer = (input('your answer is: '))
        if answer == 'q':
            print(0.5 * mass * velocity**2, 'Joules')
            break


else:
    print('choice error')

