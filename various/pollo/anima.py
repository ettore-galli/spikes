import os
import sys
import time
from frames import CHICKEN_FRAMES, THE_END_SCREEN


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        sys.stdout.write("\033[H\033[J")
        sys.stdout.flush()


def animate(frames, fps=4, duration=5):
    frame_time = 1.0 / fps
    total_frames = int(duration * fps)
    has_ended = False
    try:
        for i in range(total_frames):
            clear_screen()

            current_frame = frames[i % len(frames)]
            sys.stdout.write(current_frame)
            sys.stdout.flush()

            time.sleep(frame_time)
        has_ended = True

    except KeyboardInterrupt:
        pass

    finally:
        
        clear_screen()
        sys.stdout.write(THE_END_SCREEN.replace("XXXXXXXX", "THE END!" if has_ended else "BROKEN! "))
        sys.stdout.flush()


if __name__ == "__main__":
    animate(CHICKEN_FRAMES, fps=4, duration=5)
