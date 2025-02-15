import curses

def main(stdscr):
    # Configurazione iniziale
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)

    # Posizione del personaggio
    x, y = 10, 10

    while True:
        # Leggi l'input
        key = stdscr.getch()

        # Muovi il personaggio
        if key == ord('w'):
            y -= 1
        elif key == ord('s'):
            y += 1
        elif key == ord('a'):
            x -= 1
        elif key == ord('d'):
            x += 1
        elif key == ord('q'):
            break
        else:
            print(key)

        # Pulisci lo schermo e disegna il personaggio
        stdscr.clear()
        stdscr.addstr(y, x, f'[{key}]')
        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)