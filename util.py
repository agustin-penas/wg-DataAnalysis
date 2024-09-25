

def grayscale(pixels):
    gray = []
    for x in range(0, len(pixels), 4):
        value = (pixels[x] * 0.299) + (pixels[x + 1]
                                       * 0.587) + (pixels[x + 2] * 0.114)
        gray.append(value)
    return gray


def equalizeHistogram(src, step):
    dst = []
    srcLength = len(src)
    hist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0]

    for i in range(0, srcLength, step):
        hist[src[i]] = hist[src[i]]+1

    norm = 255 * step / srcLength
    prev = 0

    for i in range(0, 256):
        h = hist[i] + prev
        h = h + prev
        prev = h
        hist[i] = h * norm

    for i in range(0, srcLength):
        dst.append(hist[src[i]])

    return dst


def threshold(data, threshold):
    return list(map(lambda x: 255 if x > threshold else 0, data))


def correlation(data1, data2):
    length = min(len(data1), len(data2))
    count = 0
    for i in range(0, length):
        if data1[i] == data2[i]:
            count += 1
    return count / max(len(data1), len(data2))
