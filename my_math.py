def addition(a, b):
    """
    Calcule la somme de deux nombres.

    Args:
        a (int ou float): Le premier nombre.
        b (int ou float): Le deuxième nombre.

    Returns:
        int ou float: La somme de a et b.
    """
    return a + b


def soustraction(a, b):
    """
    Calcule la différence entre deux nombres.

    Args:
        a (int ou float): Le premier nombre.
        b (int ou float): Le deuxième nombre.

    Returns:
        int ou float: La différence entre a et b.

        ce ci est une amelioration
    """
    return a - b


def multiplication(a, b):
    """
    Calcule le produit de deux nombres.

    Args:
        a (int ou float): Le premier nombre.
        b (int ou float): Le deuxième nombre.

    Returns:
        int ou float: Le produit de a et b.
    """
    return a * b


def division(a, b):
    """
    Calcule le quotient de deux nombres.

    Args:
        a (int ou float): Le numérateur.
        b (int ou float): Le dénominateur.

    Returns:
        float: Le quotient de a et b.

    Raises:
        ZeroDivisionError: Si b est égal à zéro.
    """
    if b == 0:
        raise ZeroDivisionError("La division par zéro n'est pas définie.")
    return a / b


if __name__ == "__main__":
    # Exemple d'utilisation des fonctions
    nombre1 = 5
    nombre2 = 3

    resultat_addition = addition(nombre1, nombre2)
    print(f"La somme de {nombre1} et {nombre2} est {resultat_addition}.")

    resultat_soustraction = soustraction(nombre1, nombre2)
    print(f"La différence entre {nombre1} et {nombre2} est {resultat_soustraction}.")

    resultat_multiplication = multiplication(nombre1, nombre2)
    print(f"Le produit de {nombre1} et {nombre2} est {resultat_multiplication}.")

    resultat_division = division(nombre1, nombre2)
    print(f"Le quotient de {nombre1} et {nombre2} est {resultat_division}.")