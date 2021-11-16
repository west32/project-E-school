from shop.class_product import Product


# def test_add_final_grades():
#     parameters = [
#         (5, "Matematyka", None, True),
#         (5, "Historia", None, True),
#         (1, "Matematyka", GradeCalculator.normal_promotion_policy, True),
#         (2, "Matematyka", GradeCalculator.strict_promotion_policy, False),
#     ]
#
#     for params in parameters:
#         grade, subject, promotion_policy, promoted = params
#         student = Student("Bob", "Kowalski")
#         student.add_final_grade(grade,subject,promotion_policy)
#
#         if student.promoted == promoted:
#             print("OK")
#         else:
#             print(f"Błąd! Dla parametrów {params}, wynik promocji to {student.promoted} zamiast dsalms d' ")
# #
# test_add_final_grades()

# Napisz test sprawdzający poprawność wykonanej w poprzednim module metody magicznej __eq__ w klasie
# Product - czyli porównywania produktów.
#
# Dla przypomnienia, dwa produkty są sobie równe, gdy mają taką samą nazwę, taką samą kategorię
# i taką samą cenę jednostkową.
#
# Wykorzystaj tuple do przygotowania różnych zestawów parametrów danych do algorytmu testującego.

# def __eq__(self, other):
#     if self.__class__ != other.__class__:
#         return NotImplemented
#     return (self.name == other.name and
#             self.category == other.category and
#             self.prize == other.prize)


# def __str__(self):
#     return f"Product: {self.name}    |Kategoria: {self.category}     |cena: {self.prize}"

def test_eq_product():
    parameters = [
        ("woda", "jedzenie", 2, "woda", "jedzenie", 2, True),
        ("woda", "jedzenie", 2, "woda", "jedzenie", 3, False),
        ("woda", "napoje", 2, "woda", "jedzenie", 2, False),
        ("woda", "jedzenie", 4, "chleb", "jedzenie", 2, False),
        ("woda", "jedzenie", 3, "woda", "jedzenie", 3, True)
    ]

    for params in parameters:
        name, category, price, other_name, other_category, other_price, expected_result = params
        product = Product(name, category, price)
        other_product = Product(other_name, other_category, other_price)
        result = product == other_product

        if result == expected_result:
            print("OK")
        else:
            print(f" Błąd! wynik powinien byc : {result}, zamiast {expected_result}")


test_eq_product()
