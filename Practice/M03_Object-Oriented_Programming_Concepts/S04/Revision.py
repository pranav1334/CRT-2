# Family Tree example demonstrating 5 types of inheritance in Python

class FamilyMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"{self.name} is {self.age} years old.")


# 1. Single Inheritance
class Grandparent(FamilyMember):
    def __init__(self, name, age, family_name):
        super().__init__(name, age)
        self.family_name = family_name

    def grandparent_info(self):
        print(f"{self.name} is the grandparent of the {self.family_name} family.")


# 2. Multilevel Inheritance
class Parent(Grandparent):
    def __init__(self, name, age, family_name, role):
        super().__init__(name, age, family_name)
        self.role = role

    def parent_info(self):
        print(f"{self.name} is the {self.role} of the {self.family_name} family.")


# 3. Hierarchical Inheritance
class Son(Parent):
    def __init__(self, name, age, family_name, role, hobby):
        super().__init__(name, age, family_name, role)
        self.hobby = hobby

    def show_hobby(self):
        print(f"{self.name} likes {self.hobby}.")


class Daughter(Parent):
    def __init__(self, name, age, family_name, role, hobby):
        super().__init__(name, age, family_name, role)
        self.hobby = hobby

    def show_hobby(self):
        print(f"{self.name} likes {self.hobby}.")


# 4. Multiple Inheritance
class Father:
    def __init__(self, father_name):
        self.father_name = father_name

    def father_quality(self):
        print(f"{self.father_name} teaches discipline.")


class Mother:
    def __init__(self, mother_name):
        self.mother_name = mother_name

    def mother_quality(self):
        print(f"{self.mother_name} teaches kindness.")


class Child(Father, Mother):
    def __init__(self, child_name, father_name, mother_name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.child_name = child_name

    def child_traits(self):
        print(f"{self.child_name} inherits discipline from {self.father_name} and kindness from {self.mother_name}.")


# 5. Hybrid Inheritance
class GrandChild(Child):
    def __init__(self, child_name, father_name, mother_name, generation):
        super().__init__(child_name, father_name, mother_name)
        self.generation = generation

    def grandchild_info(self):
        print(f"{self.child_name} is the {self.generation} generation of the family.")


# Demonstration
print("=== Family Tree with 5 Types of Inheritance ===")

grandparent = Grandparent("Shankar", 72, "Sharma")
grandparent.intro()
grandparent.grandparent_info()

print("\n--- Single Inheritance ---")
parent = Parent("Amit", 45, "Sharma", "father")
parent.intro()
parent.parent_info()

print("\n--- Hierarchical Inheritance ---")
son = Son("Rahul", 20, "Sharma", "son", "cricket")
daughter = Daughter("Neha", 18, "Sharma", "daughter", "music")
son.show_hobby()
daughter.show_hobby()

print("\n--- Multiple Inheritance ---")
child = Child("Riya", "Amit", "Pooja")
child.child_traits()

print("\n--- Hybrid Inheritance ---")
grandchild = GrandChild("Arya", "Amit", "Pooja", "third")
grandchild.grandchild_info()

print("\nThis family tree shows 3 generations: Grandparent -> Parent -> Child/Grandchild.")

