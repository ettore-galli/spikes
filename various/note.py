if __name__ == "__main__":
    semi = 2 ** (1 / 12)

    note = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    freq = [444 * semi**i for i in range(12)]

    for freqnote in list(zip(note, freq)):
        print(freqnote)
