import numpy as np

def generation(line):
    for i in range(10):
        line = np.array(list(line), dtype=np.uint8)
        neighbors1 = np.roll(line, 1)
        neighbors2 = np.roll(line, 0)
        neighbors3 = np.roll(line, -1)

        for j in range(len(line)):
            if j == 0:
                if neighbors1[j] == 1 and neighbors1[j + 1] == 0 and neighbors1[j + 2] == 0 or \
                        (neighbors1[j] == 0 and neighbors1[j + 1] == 1 and neighbors1[j + 2] == 1) or \
                        (neighbors1[j] == 0 and neighbors1[j + 1] == 1 and neighbors1[j + 2] == 0) or \
                        (neighbors1[j] == 0 and neighbors1[j + 1] == 0 and neighbors1[j + 2] == 1):
                    line[j] = 1;
                else:
                    line[j] = 0;
            elif j != len(line) - 1:
                if neighbors2[j - 1] == 1 and neighbors2[j] == 0 and neighbors2[j + 1] == 0 or neighbors2[j - 1] == 0 and neighbors2[j] == 1 and neighbors2[j + 1] == 1 or neighbors2[j - 1] == 0 and neighbors2[j] == 1 and neighbors2[j + 1] == 0 or neighbors2[j - 1] == 0 and neighbors2[j] == 0 and neighbors2[j + 1] == 1:
                    line[j] = 1;
                else:
                    line[j] = 0;
            elif neighbors3[j - 2] == 1 and neighbors3[j - 1] == 0 and neighbors3[j] == 0 or neighbors3[j - 2] == 0 and neighbors3[j - 1] == 1 and neighbors3[j] == 1 or neighbors3[j - 2] == 0 and neighbors3[j - 1] == 1 and neighbors3[j] == 0 or neighbors3[j - 2] == 0 and neighbors3[j - 1] == 0 and neighbors3[j] == 1:
                line[j] = 1;
            else:
                line[j] = 0;
        line = np.array(line, dtype='<U32')
    line = ''.join(line)
    return line
print(generation('00100'))
