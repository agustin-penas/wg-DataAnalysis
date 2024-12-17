import datawindow as dw
import util as u


class Colors:
    def __init__(self):
        self.blinkWindow = 8
        self.equalizeStep = 5
        self.threshold = 80
        self.minCorrelation = [0.55, 0.6, 0.61, 0.61, 0.63, 0.58]
        self.maxCorrelation = [0.75, 0.7, 0.71, 0.69, 0.67, 0.72]
        self.blinkData = dw.DataWindow(self.blinkWindow)

    def isBlinkByColors(self, left, right):
        data = self.extractBlinkData(left, right)
        self.blinkData.push(data)

        if self.blinkData.length < self.blinkWindow:
            return list(map(lambda x: False, self.minCorrelation))
        return self.isBlink()

    def extractBlinkData(self, left, right):
        return sum(left) + sum(right)

    def isBlink(self):
        medianColorData = 0
        lastFrame = self.blinkData.get(self.blinkWindow-1)
        for i in range(0, self.blinkWindow-1):
            data = self.blinkData.get(i)
            medianColorData += data
        medianColorData /= (self.blinkWindow-1)
        blink = min(medianColorData, lastFrame) / \
            max(lastFrame, medianColorData)
        isBlink = []
        for minCorr, maxCorr in zip(self.minCorrelation, self.maxCorrelation):
            isBlink.append(
                blink > minCorr and blink < maxCorr)
        return isBlink


if __name__ == '__main__':
    colors = Colors()
    print(colors.extractBlinkData([1, 2, 3], [4, 5, 6]))
