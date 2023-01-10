#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    size = 0
    statuscd = {}

    while True:
        try:
            counter = 0
            for line in sys.stdin:
                line = line.split()

                size += int(line[8])
                if statuscd.get(line[7], -1) == -1:
                    statuscd[line[7]] = 1
                else:
                    statuscd[line[7]] += 1

                if counter == 10:
                    break
                counter += 1

        except KeyboardInterrupt:
            exit()
        finally:
            print("File size: {}".format(size))
            for key in sorted(statuscd):
                print("{}: {}".format(key, statuscd[key]))
