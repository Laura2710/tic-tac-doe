import random

def display_board(board):
    """
    Affiche le plateau de jeu à l'écran.
    """
    print("\n-------------")
    for row in board:
        print("|", " | ".join(str(cell) for cell in row), "|")
        print("-------------")


def enter_move(board):
    """
    Demande à l'utilisateur de choisir une case libre et met à jour le plateau.
    """
    free_fields = make_list_of_free_fields(board)

    while True:
        try:
            move = int(input("Entrez votre coup (1-9) : ")) - 1  # Convertit l'entrée en index de 0 à 8
            row = move // 3  # Trouver la ligne
            col = move % 3   # Trouver la colonne

            if (row, col) in free_fields:
                board[row][col] = "O"
                break
            else:
                print("Case déjà prise ou invalide ! Essayez encore.")
        except ValueError:
            print("Veuillez entrer un nombre valide entre 1 et 9.")


def make_list_of_free_fields(board):
    """
    Retourne une liste des cases libres sous forme de tuples (ligne, colonne).
    """
    free_positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                free_positions.append((i, j))
    return free_positions


def victory_for(board, sign):
    """
    Vérifie si un joueur a gagné.
    """
    # Vérification des lignes et colonnes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sign:  # Ligne gagnante
            return True
        if board[0][i] == board[1][i] == board[2][i] == sign:  # Colonne gagnante
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False


def draw_move(board):
    """
    L'ordinateur joue un coup au hasard.
    """
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = "X"


# Initialisation du plateau de jeu
board = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]

# Boucle principale du jeu
display_board(board)

while True:
    enter_move(board)  # Joueur joue
    display_board(board)

    if victory_for(board, "O"):
        print("🎉 Bravo ! Vous avez gagné !")
        break

    if not make_list_of_free_fields(board):
        print("🤝 Match nul !")
        break

    draw_move(board)  # Ordinateur joue
    display_board(board)

    if victory_for(board, "X"):
        print("💻 L'ordinateur a gagné. 😢")
        break

    if not make_list_of_free_fields(board):
        print("🤝 Match nul !")
        break
