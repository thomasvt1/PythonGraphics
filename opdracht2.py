import math


def RGBtoCMY(R, G, B):
    C = 1 - R
    M = 1 - G
    Y = 1 - B
    return [C, M, Y]


def CMYtoRGB(C, M, Y, K):
    R = (1 - C) * (1 - K)
    G = (1 - M) * (1 - K)
    B = (1 - Y) * (1 - K)
    return [R, G, B]


def RGBtoHSL(R, G, B):
    minimum = min(R, G, B)
    maximum = max(R, G, B)

    L = (minimum + maximum) / 2
    if minimum == maximum:
        S = 0
    else:
        if L < 0.5:
            S = (maximum - minimum) / (maximum + minimum)
        else:
            S = (maximum - minimum) / (2.0 - maximum - minimum)

    if R == G and G == B:
        H = 0
    else:
        if maximum == R:
            H = (G - B) / (maximum - minimum)
        elif maximum == G:
            H = 2.0 + (B - R) / (maximum - minimum)
        elif maximum == B:
            H = 4.0 + (R - G) / (maximum - minimum)
    H *= 60
    if H < 0:
        H += 360

    return [H, S, L]


def HSLtoRGB(H, S, L):
    if S == 0:
        R = 0.4
        G = 0.4
        B = 0.4
    else:
        if L < 0.5:
            temp1 = L * (1.0 + S)
        else:
            temp1 = L + S - (L * S)

        temp2 = (2 * L) - temp1
        H /= 360
        tempR = calc_correction(H + 0.333)
        tempG = calc_correction(H)
        tempB = calc_correction(H - 0.333)

        R = temp_to_final(tempR, temp1, temp2)
        G = temp_to_final(tempG, temp1, temp2)
        B = temp_to_final(tempB, temp1, temp2)

    return [R, G, B]


# Corrects numbers which are above 1 or below 0
def calc_correction(correctable):
    while correctable<0 or correctable>1:
        if correctable>1:
            correctable-=1
        elif correctable<0:
            correctable+=1
    return correctable


# Converts the temparary collors to the actual numbers
def temp_to_final(tempCol, temp1, temp2):
    if (6 * tempCol) < 1:
        col = temp2 + ((temp1 - temp2) * 6 * tempCol)
    elif (2 * tempCol) < 1:
        col = temp1
    elif (3 * tempCol) < 2:
        col = temp2 + ((temp1 - temp2) * (0.666 - tempCol) * 6)
    else:
        col = temp2

    return col


# calculates new color from the 2 overlay colors
def calc_transparency(R1, G1, B1, alpha, R2, G2, B2):
    R3 = math.ceil(R1 * alpha) + math.ceil(R2 * (1 - alpha))
    G3 = math.ceil(G1 * alpha) + math.ceil(G2 * (1 - alpha))
    B3 = math.ceil(B1 * alpha) + math.ceil(B2 * (1 - alpha))
    return [R3, G3, B3]


print(RGBtoHSL(24, 98, 118))
#print (CMYtoRGB(1, 0.5, 0, 0.7))
#print (RGBtoCMY(1, 0, 1))