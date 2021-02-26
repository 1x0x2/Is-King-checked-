import sys
def main():
    def check_rock(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy, list1):
        rook_move_Ox = [-1,1,0,0]
        rook_move_Oy = [0,0,1,-1]
        
        for i in range(0,4):
            Ox = posision_Ox
            Oy = posision_Oy
            while Ox >= 97 and Ox <= 104 and Oy >= 1 and Oy <= 8:
                Ox += rook_move_Ox[i]
                Oy += rook_move_Oy[i]
                if Ox == wking_posision_Ox and Oy == wking_posision_Oy:
                    return 1
                list2 = []
                list2.append(Ox)
                list2.append(Oy)
                if list1.count(list2) > 0:
                    break
        return 0
        
    def check_bishop(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy, list1):
        rook_move_Ox = [-1,1,1,-1]
        rook_move_Oy = [1,-1,1,-1]
        
        for i in range(0,4):
            Ox = posision_Ox
            Oy = posision_Oy
            while Ox >= 97 and Ox <= 104 and Oy >= 1 and Oy <= 8:
                Ox += rook_move_Ox[i]
                Oy += rook_move_Oy[i]
                if Ox == wking_posision_Ox and Oy == wking_posision_Oy:
                    return 1
                list2 = []
                list2.append(Ox)
                list2.append(Oy)
                if list1.count(list2) > 0:
                    break
        return 0
    
    def check_knight(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy, list1):
        rook_move_Ox = [2,2,-2,-2,1,-1,1,-1]
        rook_move_Oy = [1,-1,1,-1,2,2,-2,-2]
        
        for i in range(0,8):
            Ox = posision_Ox
            Oy = posision_Oy
            Ox += rook_move_Ox[i]
            Oy += rook_move_Oy[i]
            if Ox == wking_posision_Ox and Oy == wking_posision_Oy:
                return 1
        return 0
        
    def check_pawn(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy, status, list1):
        pawn_move_Ox = [-1,1]
        pawn_move_Oy = [1,1]
        
        for i in range(0,2):
            if status == 1:
                Ox = posision_Ox
                Oy = posision_Oy
                Ox += pawn_move_Ox[i]
                Oy += pawn_move_Oy[i]
                if Ox == wking_posision_Ox and Oy == wking_posision_Oy:
                    return 1
            if status == -1:
                Ox = posision_Ox
                Oy = posision_Oy
                Ox -= pawn_move_Ox[i]
                Oy -= pawn_move_Oy[i]
                if Ox == wking_posision_Ox and Oy == wking_posision_Oy:
                    return 1
        return 0
    
    def checkmate(str1):
        str1 = str1.split('+')
    
        wking_posision_Ox = 0
        wking_posision_Oy = 0
        bking_posision_Ox = 0
        bking_posision_Ox = 0
    
        list1 = []
        for ele in str1:
            list2 = []
            list2.append(ord(ele[4]))
            list2.append(int(ele[5], 10))
            list1.append(list2)
        
        for ele in str1:
            if ele.find('w,k,') == 0:
                wking_posision_Ox = ord(ele[4])
                wking_posision_Oy = int(ele[5], 10)
            elif ele.find('b,k,') == 0:
                bking_posision_Ox = ord(ele[4])
                bking_posision_Oy = int(ele[5], 10)
    
        posision_Ox = 0
        posision_Oy = 0
        
        for ele in str1:
            if ele.find('w,q,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if (check_rock(posision_Ox, posision_Oy, bking_posision_Ox, bking_posision_Oy, list1)) or (check_bishop(posision_Ox, posision_Oy, bking_posision_Ox, bking_posision_Oy, list1)):
                    return True
            elif ele.find('b,q,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if (check_rock(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy, list1)) or (check_bishop(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy, list1)):
                    return True
                    
            elif ele.find('w,r,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if check_rock(posision_Ox, posision_Oy, bking_posision_Ox, bking_posision_Oy, list1):
                    return True
            elif ele.find('b,r,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if check_rock(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy, list1):
                    return True
                    
            elif ele.find('w,b,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if check_bishop(posision_Ox, posision_Oy, bking_posision_Ox, bking_posision_Oy, list1):
                    return True
            elif ele.find('b,b,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if check_bishop(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy, list1):
                    return True
            
            elif ele.find('w,n,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if check_knight(posision_Ox, posision_Oy, bking_posision_Ox, bking_posision_Oy, list1):
                    return True
            elif ele.find('b,n,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if check_knight(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy, list1):
                    return True
                    
            elif ele.find('w,p,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if check_pawn(posision_Ox, posision_Oy, bking_posision_Ox, bking_posision_Oy,1, list1):
                    return True
            elif ele.find('b,p,') == 0:
                posision_Ox = ord(ele[4])
                posision_Oy = int(ele[5], 10)
                if check_pawn(posision_Ox, posision_Oy, wking_posision_Ox, wking_posision_Oy,-1, list1):
                    return True
        return False
        
    res = []
    chess_matches = raw_input()
    chess_matches = chess_matches.split(' ')
    for chess_match in chess_matches:
        res.append(checkmate(chess_match))
    print(res)

main()