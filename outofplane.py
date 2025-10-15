
THRESHOLD = [0.15, 0.2, 0.25, 0.27, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.57, 0.6, 0.63, 0.65, 0.7, 0.75]


def isOutOfPlane(importantKeypoints):
    noseX = importantKeypoints['noseX']
    noseY = importantKeypoints['noseY']
    topY = importantKeypoints['topY']
    bottomY = importantKeypoints['bottomY']
    leftEarX = importantKeypoints['leftEarX']
    rightearX = importantKeypoints['rightearX']

    distanceToTop = noseY - topY
    distanceToBottom = bottomY - noseY

    distanceToLeft = leftEarX - noseX
    distanceToRight = noseX - rightearX
    # return [distanceToBottom, distanceToTop, distanceToLeft, distanceToRight]
    return list(map(lambda x: evaluate_distances(distanceToLeft, distanceToRight, distanceToTop, distanceToBottom, x), THRESHOLD))


def evaluate_distances(left, right, top, bottom, x):
    return left < (x*right) or right < (x*left) or top < (x*bottom) or bottom < (x*top)
