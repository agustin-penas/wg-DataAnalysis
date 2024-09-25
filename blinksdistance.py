import numpy as np


class BlinkDistance:
    DISTANCE_THRESHOLD = [0.15, 0.25, 0.4, 0.5, 0.6, 0.75]

    LEFT_OPEN_EYE_DISTANCE = 0
    RIGHT_OPEN_EYE_DISTANCE = 0

    def getEucledianDistance(self, x1, y1, x2, y2):
        return np.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))

    def isBlinkByDistance(self, rightEyeTopArc, rightEyeBottomArc, leftEyeTopArc, leftEyeBottomArc):
        right_distance = self.getEucledianDistance(
            rightEyeTopArc[4]['x'], rightEyeTopArc[4]['y'], rightEyeBottomArc[4]['x'], rightEyeBottomArc[4]['y'])
        left_distance = self.getEucledianDistance(
            leftEyeTopArc[5]['x'], leftEyeTopArc[5]['y'], leftEyeBottomArc[3]['x'], leftEyeBottomArc[3]['y'])

        is_blink = list(map(lambda x: right_distance < x*BlinkDistance.RIGHT_OPEN_EYE_DISTANCE or left_distance <
                            x*BlinkDistance.LEFT_OPEN_EYE_DISTANCE, BlinkDistance.DISTANCE_THRESHOLD))

        if left_distance > BlinkDistance.LEFT_OPEN_EYE_DISTANCE:
            BlinkDistance.LEFT_OPEN_EYE_DISTANCE = left_distance

        if right_distance > BlinkDistance.RIGHT_OPEN_EYE_DISTANCE:
            BlinkDistance.RIGHT_OPEN_EYE_DISTANCE = right_distance

        return is_blink


if __name__ == '__main__':
    print(BlinkDistance().isBlinkByDistance([{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 336.45, 'y': 213.25, 'point': 398}, {'x': 341.23, 'y': 211.37, 'point': 384}, {'x': 347.89, 'y': 210.66, 'point': 385}, {'x': 354.22, 'y': 210.84, 'point': 386}, {'x': 360.52, 'y': 212.02, 'point': 387}, {'x': 364.5, 'y': 213.54, 'point': 388}, {'x': 367.09, 'y': 214.62, 'point': 466}, {'x': 369.07, 'y': 215.58, 'point': 263}, {
        'x': 370.16, 'y': 219.74, 'point': 255}], [{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 334.33, 'y': 217.41, 'point': 341}, {'x': 338.88, 'y': 219.75, 'point': 256}, {'x': 345.55, 'y': 222.26, 'point': 252}, {'x': 353.37, 'y': 223.18, 'point': 253}, {'x': 360.71, 'y': 222.99, 'point': 254}, {'x': 366.67, 'y': 222.05, 'point': 339}, {'x': 370.16, 'y': 219.74, 'point': 255}], [{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 336.45, 'y': 213.25, 'point': 398}, {'x': 341.23, 'y': 211.37, 'point': 384}, {'x': 347.89, 'y': 210.66, 'point': 385}, {'x': 354.22, 'y': 210.84, 'point': 386}, {'x': 360.52, 'y': 212.02, 'point': 387}, {'x': 364.5, 'y': 213.54, 'point': 388}, {'x': 367.09, 'y': 214.62, 'point': 466}, {'x': 369.07, 'y': 215.58, 'point': 263}, {
            'x': 370.16, 'y': 219.74, 'point': 255}], [{'x': 331.49, 'y': 214.72, 'point': 463}, {'x': 334.33, 'y': 217.41, 'point': 341}, {'x': 338.88, 'y': 219.75, 'point': 256}, {'x': 345.55, 'y': 222.26, 'point': 252}, {'x': 353.37, 'y': 223.18, 'point': 253}, {'x': 360.71, 'y': 222.99, 'point': 254}, {'x': 366.67, 'y': 222.05, 'point': 339}, {'x': 370.16, 'y': 219.74, 'point': 255}]))
