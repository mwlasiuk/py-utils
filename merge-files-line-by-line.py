import sys
import os
import tqdm


def main():
    if len(sys.argv) != 4:
        sys.exit(-1)

    file_path_0 = sys.argv[1]  # x y z per line
    file_path_1 = sys.argv[2]  # r g b per line
    file_path_2 = sys.argv[3]

    if not os.path.exists(file_path_0):
        sys.exit(-2)

    if not os.path.exists(file_path_1):
        sys.exit(-3)

    if os.path.exists(file_path_2):
        sys.exit(-4)

    print(f"Merging {file_path_0} and {file_path_1} to {file_path_2}")

    with open(file_path_0, "r") as file_0, open(file_path_1, "r") as file_1:
        data_0, data_1 = file_0.readlines(), file_1.readlines()

    with open(file_path_2, "w") as file_2:
        for lines in tqdm.tqdm(zip(data_0, data_1), "Merging..."):
            line_0, line_1 = lines

            line_0 = line_0.split()
            line_1 = line_1.split()

            x, y, z = line_0
            r, g, b = line_1

            file_2.write(f"{x} {y} {z} {r} {g} {b}\n")


if __name__ == "__main__":
    main()
