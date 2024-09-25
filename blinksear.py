import numpy as np

EAR_THRESHOLD = [0.15, 0.2, 0.23, 0.25, 0.27, 0.3, 0.4]


def getEucledianDistance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


def getEAR(upper, lower):
    return (
        (getEucledianDistance(upper[5]['x'], upper[5]['y'], lower[4]['x'], lower[4]['y']) +
         getEucledianDistance(
            upper[3]['x'],
            upper[3]['y'],
            lower[2]['x'],
            lower[2]['y']
        )) / (2 * getEucledianDistance(upper[0]['x'], upper[0]['y'], upper[8]['x'], upper[8]['y']))
    )


def isBlinkByEar(rightEyeTopArc, rightEyeBottomArc, leftEyeTopArc, leftEyeBottomArc):
    rightEar = getEAR(rightEyeTopArc, rightEyeBottomArc)
    leftEar = getEAR(leftEyeTopArc, leftEyeBottomArc)
    return list(map(lambda x: rightEar < x or leftEar < x, EAR_THRESHOLD))


if __name__ == '__main__':
    # g = [{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 334.33, 'y': 217.41, 'point': 341}, {'x': 338.88, 'y': 219.75, 'point': 256}, {'x': 345.55, 'y': 222.26, 'point': 252}, {
    # 'x': 353.37, 'y': 223.18, 'point': 253}, {'x': 360.71, 'y': 222.99, 'point': 254}, {'x': 366.67, 'y': 222.05, 'point': 339}, {'x': 370.16, 'y': 219.74, 'point': 255}]
    # print(g[5]['x'])
    print(getEAR([{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 336.45, 'y': 213.25, 'point': 398}, {'x': 341.23, 'y': 211.37, 'point': 384}, {'x': 347.89, 'y': 210.66, 'point': 385}, {'x': 354.22, 'y': 210.84, 'point': 386}, {'x': 360.52, 'y': 212.02, 'point': 387}, {'x': 364.5, 'y': 213.54, 'point': 388}, {'x': 367.09, 'y': 214.62, 'point': 466}, {'x': 369.07, 'y': 215.58, 'point': 263}, {
        'x': 370.16, 'y': 219.74, 'point': 255}], [{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 334.33, 'y': 217.41, 'point': 341}, {'x': 338.88, 'y': 219.75, 'point': 256}, {'x': 345.55, 'y': 222.26, 'point': 252}, {'x': 353.37, 'y': 223.18, 'point': 253}, {'x': 360.71, 'y': 222.99, 'point': 254}, {'x': 366.67, 'y': 222.05, 'point': 339}, {'x': 370.16, 'y': 219.74, 'point': 255}]))

    print(isBlinkByEar([{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 336.45, 'y': 213.25, 'point': 398}, {'x': 341.23, 'y': 211.37, 'point': 384}, {'x': 347.89, 'y': 210.66, 'point': 385}, {'x': 354.22, 'y': 210.84, 'point': 386}, {'x': 360.52, 'y': 212.02, 'point': 387}, {'x': 364.5, 'y': 213.54, 'point': 388}, {'x': 367.09, 'y': 214.62, 'point': 466}, {'x': 369.07, 'y': 215.58, 'point': 263}, {
        'x': 370.16, 'y': 219.74, 'point': 255}], [{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 334.33, 'y': 217.41, 'point': 341}, {'x': 338.88, 'y': 219.75, 'point': 256}, {'x': 345.55, 'y': 222.26, 'point': 252}, {'x': 353.37, 'y': 223.18, 'point': 253}, {'x': 360.71, 'y': 222.99, 'point': 254}, {'x': 366.67, 'y': 222.05, 'point': 339}, {'x': 370.16, 'y': 219.74, 'point': 255}], [{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 336.45, 'y': 213.25, 'point': 398}, {'x': 341.23, 'y': 211.37, 'point': 384}, {'x': 347.89, 'y': 210.66, 'point': 385}, {'x': 354.22, 'y': 210.84, 'point': 386}, {'x': 360.52, 'y': 212.02, 'point': 387}, {'x': 364.5, 'y': 213.54, 'point': 388}, {'x': 367.09, 'y': 214.62, 'point': 466}, {'x': 369.07, 'y': 215.58, 'point': 263}, {
            'x': 370.16, 'y': 219.74, 'point': 255}], [{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 334.33, 'y': 217.41, 'point': 341}, {'x': 338.88, 'y': 219.75, 'point': 256}, {'x': 345.55, 'y': 222.26, 'point': 252}, {'x': 353.37, 'y': 223.18, 'point': 253}, {'x': 360.71, 'y': 222.99, 'point': 254}, {'x': 366.67, 'y': 222.05, 'point': 339}, {'x': 370.16, 'y': 219.74, 'point': 255}]))
