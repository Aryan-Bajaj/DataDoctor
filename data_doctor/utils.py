import chardet


def detect_encoding(data):
    detector = chardet.UniversalDetector()
    for row in data:
        detector.feed(row)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']