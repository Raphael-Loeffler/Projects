from time import sleep

def countdown(t: int) -> None:
    if t >= 0:
        while t:
            mins, secs = divmod(t, 60)
            time_elapsed: str = f"{mins:02d}:{secs:02d}"
            print(time_elapsed, end='\r')
            sleep(1)
            t -= 1
        print("Time is up!")
    else:
        print("No negative numbers are accepted")

if __name__ == "__main__":
    t = int(input("Time (seconds): "))
    countdown(t)