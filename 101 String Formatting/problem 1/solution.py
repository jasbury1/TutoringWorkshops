def print_stats(time, speed, fuel, x_pos, y_pos):
    # Given the following stats of a Car:
    #  - Time as an int in seconds
    #  - speed as a double in m/s
    #  - fuel as a double in L
    #  - x_pos as an int in m
    #  - y_pos as an int in m
    # Print to console a formatted string as shown in output.txt
    print("{:>10s}:{:6d} s".format("Time", time))
    print("{:>10s}:{:9.2f} m/s".format("Speed", speed))
    print("{:>10s}:{:9.2f} L".format("Fuel", fuel))
    print("{:>10s}:{:6d} m".format("X Position", x_pos))
    print("{:>10s}:{:6d} m".format("Y Position", y_pos))
    print("\n\n")


if __name__ == "__main__":
    print_stats(1, 30.8458, 1.9541, 16, -20)
    print_stats(100, 3.1, 0.31, 1, 100)