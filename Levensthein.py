import numpy as np


def levenshtein(A, B):
    A_len = len(A)
    B_len = len(B)

    #Pass dimensions into np.zeros
    K = np.zeros((A_len + 1, B_len + 1))

    #Correct loop ranges for base case initialization
    for i in range(A_len + 1):
        K[i][0] = i
    for j in range(B_len + 1):
        K[0][j] = j

    for i in range(1, A_len + 1):
        for j in range(1, B_len + 1):
            # Fix 3: If characters match, cost is 0 (no addition)
            if A[i - 1] == B[j - 1]:
                cost = 0
            else:
                cost = 1

            silme = K[i - 1][j] + 1  # Deletion
            ekleme = K[i][j - 1] + 1  # Insertion
            yerDegistirme = K[i - 1][j - 1] + cost  # Substitution

            K[i][j] = min(silme, ekleme, yerDegistirme)

    # Fix 4: Return the bottom-right value of the matrix
    return int(K[A_len][B_len])


# User Input
print("1. kelimeyi girin: ")
kelime_1 = input().strip()

print("2. kelimeyi girin: ")
kelime_2 = input().strip()

# Calculate Levenshtein distance directly (Levenshtein handles different lengths naturally)
mesafe = levenshtein(kelime_1, kelime_2)

print(f"{kelime_1} ve {kelime_2} arasındaki mesafe: {mesafe}")

# Similarity calculation using the maximum length of the two words
max_len = max(len(kelime_1), len(kelime_2))
if max_len > 0:
    benzerlik_orani = (max_len - mesafe) / max_len
else:
    benzerlik_orani = 1.0

print(f"Benzerlik oranı: {benzerlik_orani:.2f}")