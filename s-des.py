def encryption(text, key):    # DES encryption
    state = text     
    ciphertext = ""

    subkeys = generate_subkey(key)  
    state = initial_permutation(state)

    for i in range(2):
        state = fiestel(state, subkeys[i])

    state = inverse_permutation(state)
    ciphertext = state

    return ciphertext


def generate_subkey(key):
    P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    P8 = [6, 3, 7, 4, 8, 5, 10, 9]

    # Applying P10
    key_permuted = [key[i - 1] for i in P10]

    # LS-1
    left_shifted = key_permuted[:5]
    right_shifted = key_permuted[5:]
    left_shifted = left_shifted[1:] + left_shifted[:1]
    right_shifted = right_shifted[1:] + right_shifted[:1]

    subkey_0 = [left_shifted[i] for i in P8] + [right_shifted[i] for i in P8]

    # LS-2
    left_shifted = left_shifted[1:] + left_shifted[:1]
    right_shifted = right_shifted[1:] + right_shifted[:1]

    subkey_1 = [left_shifted[i] for i in P8] + [right_shifted[i] for i in P8]

    return subkey_0, subkey_1    


def fiestel(state, subkey):
    state_l = state[:4]
    state_r = state[4:]

    # First round function
    funstate_r = round_function(state_r, subkey)

    # XOR left side with right side
    state_l_new = [state_l[i] ^ funstate_r[i] for i in range(4)]
    state = state_r + state_l_new

    return state


def round_function(state, subkey):
    output = ""

    # E/P (Expansion permutation)
    EP = [4, 1, 2, 3, 2, 3, 4, 1]
    state_expanded = [state[i - 1] for i in EP]

    # XOR with subkey
    state_xor = [state_expanded[i] ^ subkey[i] for i in range(8)]

    # Sbox
    state_sboxed = sbox(state_xor)

    # P4
    P4 = [2, 4, 3, 1]
    output = [state_sboxed[i - 1] for i in P4]

    return output


def sbox(input):
    S0 = [
        ['01', '11', '00', '10'],
        ['00', '01', '10', '11'],
        ['11', '10', '01', '00'],
        ['10', '01', '00', '11']
    ]

    S1 = [
        ['00', '10', '11', '01'],
        ['10', '00', '01', '11'],
        ['11', '00', '01', '00'],
        ['10', '01', '00', '11']
    ]

    input_0 = int("".join(input[:4]), 2)
    input_1 = int("".join(input[4:]), 2)

    row_0 = int(input_0[0] + input_0[3], 2)
    col_0 = int(input_0[1:3], 2)
    row_1 = int(input_1[0] + input_1[3], 2)
    col_1 = int(input_1[1:3], 2)

    return [S0[row_0][col_0], S1[row_1][col_1]]


def initial_permutation(bits):
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    return [bits[i - 1] for i in IP]


def inverse_permutation(bits):
    IP_1 = [4, 1, 3, 5, 7, 2, 8, 6]
    return [bits[i - 1] for i in IP_1]
