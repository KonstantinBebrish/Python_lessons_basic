# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0)

def Rounding(floatNum, digits):

    strFloatNum = str(floatNum)
    pos = strFloatNum.find(".")
    fractionSlicePos = pos + digits + 1
    notAccurate = strFloatNum[0:fractionSlicePos]
    zeroDot = "0."
    zero = "0"
    newFraction = float(zeroDot + strFloatNum[fractionSlicePos:])

    print(f"Index of the floating point: {pos}")
    print(f"Number to round is: {floatNum}")
    print(f"Accuracy is: {digits}")
    print(f"Not Accurate number is: {notAccurate}")
    print(f"The New fraction is: {newFraction}")
            
    if newFraction >= 0.5:
        zerosAndOnes = str(1)
        zerosAndOnes = str(zero * (digits - 1) + zerosAndOnes)
        zerosAndOnes = float(zeroDot + zerosAndOnes)
    else:
        zerosAndOnes = 0
    
    accurateFloatNum = float(notAccurate) + zerosAndOnes

    return accurateFloatNum
    
print(f"Rounded number is the following: {Rounding(46.78683, 4)}")


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def LuckyTicket(number):

    sum1 = 0
    sum2 = 0
    luckySum = False
    
    numberLen = len(str(number))
    numberLst = [digit for digit in str(number)]
    
    if numberLen % 2 == 0:
        middleDigitIndex = int(numberLen / 2 - 1)
        numberLst1 = numberLst[0:middleDigitIndex + 1]
        numberLst1 = [ int(num) for num in numberLst1]
        numberLst2 = numberLst[middleDigitIndex + 1:]
        numberLst2 = [ int(num) for num in numberLst2]

        for num in numberLst1:
            sum1 += num
        for num in numberLst2:
            sum2 += num

        if sum1 == sum2:
            luckySum = True
            result = "The ticket is LUCKY!!!"
        else:
            luckySum = False
            result = "The ticket is NOT LUCKY =("
                
    else:
        middleDigitIndex = int(numberLen // 2)
        numberLst1 = numberLst[0:middleDigitIndex]
        numberLst1 = [ int(num) for num in numberLst1]
        numberLst2 = numberLst[middleDigitIndex + 1:]
        numberLst2 = [ int(num) for num in numberLst2]

        for num in numberLst1:
            sum1 += num
        for num in numberLst2:
            sum2 += num

        if sum1 == sum2:
            luckySum = True
            result = "The ticket is LUCKY!!!"
        else:
            luckySum = False
            result = "The ticket is NOT LUCKY =("
        
    return result

print(LuckyTicket(1232))
print("\n" * 3)
print(LuckyTicket(123006))
print("\n" * 3)
print(LuckyTicket(436751))
print("\n" * 3)



            


    

            


    
