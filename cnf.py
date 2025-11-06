from sympy import symbols, Function, ForAll, Exists
from sympy.logic.boolalg import Or, Not, to_cnf

# Define function symbols
Animal = Function('Animal')
Loves = Function('Loves')

# Define variables
x, y = symbols('x y')

# Build the inner logical expression: ¬∀y ¬(Animal(y) ∨ Loves(x, y))
inner_expr = Not(ForAll(y, Not(Or(Animal(y), Loves(x, y)))))

# Build the second part: ∃y Loves(y, x)
exists_expr = Exists(y, Loves(y, x))

# Full formula: ∀x [inner_expr ∨ exists_expr]
formula = ForAll(x, Or(inner_expr, exists_expr))

print("Original formula:")
print(formula)

# Note: Sympy’s `to_cnf` works for propositional logic, not full FOL.
# For demonstration, we can drop quantifiers and convert the propositional core.
propositional_core = Or(Not(Or(Animal(y), Loves(x, y))), Loves(y, x))
cnf_form = to_cnf(propositional_core, simplify=True)

print("\nApproximate propositional CNF (quantifiers ignored):")
print(cnf_form)
