#type: ignore 
import time 

# |(Ax(By - Cy) + Bx(Cy - Ay) + Cx(Ay - By) / 2| 

def FindArea(AX,AY,BX,BY,CX,CY):
        Area = abs((AX * (BY - CY) + BX * (CY - AY) + CX * (AY - BY)) / 2)
        return Area

while True: 
    
    try: 
        print("Type Cordinates in an X,Y Format")
        time.sleep(1)
        cordinate1 = input("Type First Cordinate: ")
        cordinate2 = input("Type Second Cordinate: ")
        cordinate3 = input("Type Third Cordinate: ")
        A = cordinate1.split(",")
        B = cordinate2.split(",")
        C = cordinate3.split(",")
        time.sleep(1)
        AX = float(A[0])
        AY = float(A[1])
        BX = float(B[0])
        BY = float(B[1])
        CX = float(C[0])
        CY = float(C[1])
        print(FindArea(AX,AY,BX,BY,CX,CY))

    except:  
        print("Somethings Wrong")





