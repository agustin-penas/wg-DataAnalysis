import datawindow as dw
import util as u


class Colors:
    def __init__(self):
        self.blinkWindow = 8
        self.equalizeStep = 5
        self.threshold = 80
        self.minCorrelation = [0.78, 0.8, 0.7,
                               0.6, 0.7, 0.65, 0.71, 0.71, 0.73, 0.68]
        self.maxCorrelation = [0.85, 0.9, 0.8,
                               0.8, 0.9, 0.85, 0.81, 0.79, 0.77, 0.82]
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
