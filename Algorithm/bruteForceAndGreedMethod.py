#문자열 매치
def string_matching(text, pattern) :
    n = len(text)
    m = len(pattern)

    for i in range(n) :
        j = 0
        while j < m and pattern[j] == text[i+j] :
            j = j+1
        if j == m :
            return i
    return -1

## 테스트 ##
print(string_matching("HELLO MY FRIEND", "LO"))
print(string_matching("HELLO MY FRIEND", "GF"))

##억지기법 배낭 채우기##
def Knapsack01_BF(wgt, val, W) :
    n = len(wgt)
    bestVal = 0

    for i in range(2 ** n ) :
        s = [0]*n
        for d in range(n) :
            s[d] = i%2
            i = i//2

        sumVal = 0
        sumWgt = 0
        for d in range(n) :
            if s[d] == 1:
                sumWgt += wgt[d]
                sumVal += val[d]

        if sumWgt <= W :
            if sumVal > bestVal :
                bestVal = sumVal
    return bestVal

######## 억지기법 배낭채우기 ###########
############## 테스트 #################

weight = [10,20,30,25,35]
value = [60,100,120,70,85]
print("80 무게의 배낭에서 가장 효율적으로 담으면 그 가치는 : ",Knapsack01_BF(weight, value, 80))

#탐욕 기법#
# 동전은 500, 100, 50, 10, 5, 1원이 있다고 가정

def coin_optimal(returnMoney) :
    coin = [500, 100, 50, 10, 5, 1]
    returnCoinCount = [0] * len(coin)
    for i in range(len(coin)) :
        returnCoinCount[i] = returnMoney//coin[i]
        returnMoney = returnMoney%coin[i]
        if returnMoney == 0 :
            break

    return returnCoinCount

def printCoin(coinList) :
    coin = [500, 100, 50, 10, 5, 1]
    for i in range(len(coinList)) :
        print("{", coin[i], "원 : ", coinList[i], "개}", end = " ")

## 테스트 ##

print("650원의 최적 거스름돈은 ", end = ""); printCoin(coin_optimal(650))
print()
print("866원의 최적 거스름돈은 ", end = ""); printCoin(coin_optimal(866))
print()


##분할 가능한 배낭 채우기(탐욕적 기법) ##
def KnapSackFrac(wgt, val, W) :
    bestVal = 0
    for i in range(len(wgt)) :
        if W <= 0 :
            break
        if W >= wgt[i] :
            W -= wgt[i]
            bestVal += val[i]
        else :
            fraction = W / wgt[i]
            bestVal += val[i] * fraction
            break
    return bestVal

weight = [12, 10, 8]
value = [120, 80, 60]
W = 18
print("Fractional Knapack(18) : ", KnapSackFrac(weight, value, W))


##### Exercise #####
# 미국은 25센트, 10센트, 5센트, 1센트. 거스름돈 동전 수 최소화가 탐욕적 기법으로 이루어질 수 있는가?

coinList_USA = [25,10,5,1]
coinList_USA2 = [25, 10, 1]

def change_optima_greedMethod_ver(coinList, returnMoney) :
    returnCoinCount = [0] * len(coinList)
    for i in range(len(coinList)) :
        returnCoinCount[i] = returnMoney//coinList[i]
        returnMoney = returnMoney%coinList[i]
        if returnMoney == 0 :
            break

    return returnCoinCount

def printCoin(coinNameList, coinList) :
    coin = coinNameList
    for i in range(len(coinList)) :
        print("{", coin[i], "원 : ", coinList[i], "개}", end = " ")

def change_optima_naiveMethod_ver(coinList, returnMoney) :
    returnCoinCount = [0] * len(coinList)
    optimal_return_coin_count = [999] * len(coinList)
    tempReturnMoney = returnMoney
    
    n1 = tempReturnMoney//coinList[0]

    for i in range(0, n1+1) :
        returnCoinCount[0] = i
        tempReturnMoney = tempReturnMoney - coinList[0] * i
        n2 = tempReturnMoney//coinList[1]
        for i2 in range(0, n2+1) :
            returnCoinCount[1] = i2
            if tempReturnMoney - coinList[1] >= 0 :
                tempReturnMoney = tempReturnMoney - (coinList[1] * i2)

            n3 = tempReturnMoney//coinList[2]
            
            for i3 in range(0, n3+1) :
                returnCoinCount[2] = i3
                if tempReturnMoney - coinList[2] >= 0 :
                    tempReturnMoney = tempReturnMoney - (coinList[2] * i3)

                n4 = tempReturnMoney//coinList[3]
                
                for i4 in range(0, n4+1) :
                    returnCoinCount[3] = i4
                    if tempReturnMoney - coinList[3] >= 0 :
                        tempReturnMoney = tempReturnMoney - coinList[3]

                    temp1 = 0
                    temp2 = 0
                    val = 0
                    for k in range(len(returnCoinCount)) :
                        temp1 += returnCoinCount[k]
                        temp2 += optimal_return_coin_count[k]
                        val += returnCoinCount[k] * coinList[k]

                    if temp1 < temp2 and val == returnMoney:
                        optimal_return_coin_count = returnCoinCount

                    returnCoinCount = [0] * len(coinList)
                    tempReturnMoney = returnMoney

                    print("현재 최적값은 : ", optimal_return_coin_count)

    return optimal_return_coin_count


def change_optima_naiveMethod_recursion_start(coinNameList, returnMoney) :
    endIndex = len(coinNameList)
    coinCountList = [0] * endIndex
    optimal = [0] * endIndex
    change_optima_naiveMethod_recursion(coinNameList, coinCountList, optimal, returnMoney, returnMoney, 0, endIndex-1)
    return optimal

def change_optima_naiveMethod_recursion(coinNameList, coinCountList, optimalReturnCoinCountList, returnMoney, originReturnMoney, coinIndex, endindex) :
    
    if (coinIndex == endindex) :
        #print("Bottom")
        coinCountList[coinIndex] = returnMoney
        temp1 = 0
        temp2 = 0
        val = 0
        for k in range(len(coinNameList)) :
            temp1 += coinCountList[k]
            temp2 += optimalReturnCoinCountList[k]
            val += coinCountList[k] * coinNameList[k]
        #print("현 코인 리스트 : ", coinCountList, "val :", val)
        #print(originReturnMoney, val)

        if val == originReturnMoney :
            if temp1 < temp2 or temp2 == 0 :
                for i in range(len(coinCountList)) :
                    optimalReturnCoinCountList[i] = coinCountList[i]
                #print("최적해는 : ", optimalReturnCoinCountList)      
                #return optimal
        
    else :

        n = returnMoney//coinNameList[coinIndex]

        for i in range(0, n+1) :
            newCoinCountList = coinCountList
            newCoinCountList[coinIndex] = i
            if returnMoney - coinNameList[coinIndex] >= 0 :
                result = change_optima_naiveMethod_recursion(coinNameList, newCoinCountList, optimalReturnCoinCountList, returnMoney - (coinNameList[coinIndex] * i), originReturnMoney, coinIndex+1, endindex)
            else :
                result = change_optima_naiveMethod_recursion(coinNameList, newCoinCountList, optimalReturnCoinCountList, returnMoney, originReturnMoney, coinIndex+1, endindex)

    #return result

print()
print( change_optima_greedMethod_ver(coinList_USA, 68) )
#change_optima_naiveMethod_ver(coinList_USA, 50)
print(change_optima_naiveMethod_recursion_start(coinList_USA, 68))

print(change_optima_greedMethod_ver(coinList_USA2, 30))
print(change_optima_naiveMethod_recursion_start(coinList_USA2, 30))
print()
