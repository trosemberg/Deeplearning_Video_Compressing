from random import random
def geraRandomSplitFrame(number,width,height):
    file = open("./TapEncoder/bypassdecision_frame_{}.txt".format(number),"w")
    for h in range(0,height-1,64):
        for w in range(0,width-1,64):
            string = geraRandomSplitForCU(h,w,width,height)
            file.write("CU ({:4d},{:4d}) - {}\n".format(h,w,string))
    
    file.close()
    
def geraRandomSplitForCU(pelY, pelX, width, height):

    split_D0 = getRandomSplitForCU(pelY, pelX, 0, width, height)
    string = split_D0

    if (split_D0 == '1'):
        split0_D1 = getRandomSplitForCU(pelY     , pelX     , 1, width, height)
        split1_D1 = getRandomSplitForCU(pelY     , pelX + 32, 1, width, height)
        split2_D1 = getRandomSplitForCU(pelY + 32, pelX     , 1, width, height)
        split3_D1 = getRandomSplitForCU(pelY + 32, pelX + 32, 1, width, height)

        string = string + ' '+ split0_D1+ ' ' + split1_D1 + ' '+ split2_D1 + ' ' + split3_D1
        

        if (split0_D1 == '1'):
            split0_D2 = getRandomSplitForCU(pelY     , pelX     , 2, width, height)
            split1_D2 = getRandomSplitForCU(pelY     , pelX + 16, 2, width, height)
            split2_D2 = getRandomSplitForCU(pelY + 16, pelX     , 2, width, height)
            split3_D2 = getRandomSplitForCU(pelY + 16, pelX + 16, 2, width, height)

            string = string + ' ' + split0_D2 + ' ' + split1_D2 + ' ' + split2_D2 + ' ' + split3_D2        
        
        if (split1_D1 == '1'):
            split4_D2 = getRandomSplitForCU(pelY     , pelX + 32, 2, width, height)
            split5_D2 = getRandomSplitForCU(pelY     , pelX + 48, 2, width, height)
            split6_D2 = getRandomSplitForCU(pelY + 16, pelX + 32, 2, width, height)
            split7_D2 = getRandomSplitForCU(pelY + 16, pelX + 48, 2, width, height)

            string = string + ' ' + split4_D2 + ' ' + split5_D2 + ' ' + split6_D2 + ' ' + split7_D2
        
        
        if (split2_D1 == '1'):
            split8_D2  = getRandomSplitForCU(pelY + 32, pelX     , 2, width, height)
            split9_D2  = getRandomSplitForCU(pelY + 32, pelX + 16, 2, width, height)
            split10_D2 = getRandomSplitForCU(pelY + 48, pelX     , 2, width, height)
            split11_D2 = getRandomSplitForCU(pelY + 48, pelX + 16, 2, width, height)

            string = string + ' ' + split8_D2 + ' ' + split9_D2 + ' ' + split10_D2 + ' ' + split11_D2
        
        
        if (split3_D1 == '1'):
            split12_D2  = getRandomSplitForCU(pelY + 32, pelX + 32, 2, width, height)
            split13_D2  = getRandomSplitForCU(pelY + 32, pelX + 48, 2, width, height)
            split14_D2  = getRandomSplitForCU(pelY + 48, pelX + 32, 2, width, height)
            split15_D2  = getRandomSplitForCU(pelY + 48, pelX + 48, 2, width, height)

            string = string + ' ' + split12_D2 + ' ' + split13_D2 + ' ' + split14_D2 + ' ' + split15_D2
        
    
    return string



def getRandomSplitForCU(pelY, pelX, depth, width, height):
    cuSize = 64 / (2**depth)

    if ((pelY + cuSize < height) and (pelX + cuSize < width)):
        split = str(round(random()))
    else:
        split = '1'
    return split