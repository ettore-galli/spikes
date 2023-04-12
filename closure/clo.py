def get_signal_reader():
    idx = 0
    def signal_reader():
        nonlocal idx
        idx += 1
        return idx
        
    return signal_reader


if __name__ == '__main__':
    sr = get_signal_reader()
    print(sr())
    print(sr())
    print(sr())
    sr = get_signal_reader()
    print(sr())
    print(sr())
    print(sr())
    print(sr())
    print(sr())
    print(sr())
    sr = get_signal_reader()
    print(sr())
    print(sr())
    print(sr())