import datawindow as dw
import util as u


class Correlation:
    def __init__(self):
        self.blinkWindow = 8
        self.equalizeStep = 5
        self.threshold = 80
        self.minCorrelation = [0.78, 0.8, 0.7, 0.6, 0.6, 0.7]
        self.maxCorrelation = [0.85, 0.9, 0.8, 0.7, 0.8, 0.9]
        self.blinkData = dw.DataWindow(self.blinkWindow)

    def isBlinkByCorrelation(self, left, right):
        data = self.extractBlinkData(right)
        self.blinkData.push(data)

        if self.blinkData.length < self.blinkWindow:
            return list(map(lambda x: False, self.minCorrelation))
        return self.isBlink()

    def extractBlinkData(self, eye):
        grayscaled = u.grayscale(eye)
        equalized = u.equalizeHistogram(grayscaled, self.equalizeStep)
        return u.threshold(equalized, self.threshold)

    def isBlink(self):
        correlation = 0
        for i in range(0, self.blinkWindow):
            data = self.blinkData.get(i)
            nextData = self.blinkData.get(i+1)
            correlation += u.correlation(data, nextData)
        correlation /= self.blinkWindow
        isBlink = []
        for minCorr, maxCorr in zip(self.minCorrelation, self.maxCorrelation):
            isBlink.append(
                correlation > minCorr and correlation < maxCorr)
        return isBlink
