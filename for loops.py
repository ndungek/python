# read the number of test cases
T = int(input().strip())

# loop over the test cases
for _ in range(T):
    # read a line of input
    S = input().strip()

    # initialize two string variables to store even and odd characters
    even_chars = ""
    odd_chars = ""

    # loop through the string and append even and odd characters to respective variables
    for i in range(len(S)):
        if i % 2 == 0:
            even_chars += S[i]
        else:
            odd_chars += S[i]

    # print the even and odd characters with a space in between
    print(even_chars, odd_chars)