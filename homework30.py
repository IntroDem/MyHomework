import threading
import time

FIELD_SIZE = 25
field = [[" " for _ in range(FIELD_SIZE)] for _ in range(FIELD_SIZE)]
field_lock = threading.Lock()


def plant_stars():
    x, y = 0, 0
    dx, dy = 1, 0
    while True:
        with field_lock:
            if field[y][x] == "@":
                break
            if field[y][x] == " ":
                field[y][x] = "*"

            next_x, next_y = x + dx, y + dy
            if (
                next_x < 0
                or next_x >= FIELD_SIZE
                or next_y < 0
                or next_y >= FIELD_SIZE
                or field[next_y][next_x] in ["*", "@"]
            ):

                dx, dy = -dy, dx

            x, y = x + dx, y + dy

        if all(cell in ["*", "@"] for row in field for cell in row):
            break

        time.sleep(0.01)


def plant_dogs():
    x, y = FIELD_SIZE - 1, FIELD_SIZE - 1
    dx, dy = -1, 0
    while True:
        with field_lock:
            if field[y][x] == "*":
                break
            if field[y][x] == " ":
                field[y][x] = "@"

            next_x, next_y = x + dx, y + dy
            if (
                next_x < 0
                or next_x >= FIELD_SIZE
                or next_y < 0
                or next_y >= FIELD_SIZE
                or field[next_y][next_x] in ["*", "@"]
            ):

                dx, dy = -dy, dx

            x, y = x + dx, y + dy

        if all(cell in ["*", "@"] for row in field for cell in row):
            break

        time.sleep(0.01)


def print_field():
    for row in field:
        print(" ".join(row))


def main():
    dog_thread = threading.Thread(target=plant_dogs)
    star_thread = threading.Thread(target=plant_stars)

    star_thread.start()
    dog_thread.start()

    star_thread.join()
    dog_thread.join()

    print_field()


if __name__ == "__main__":
    main()
