from itertools import product

# Define propositional variables
variables = ['P', 'Q', 'R']

# Define formulas in KB
def implies(a, b):
    return (not a) or b

def KB(P, Q, R):
    # Q → P
    s1 = implies(Q, P)
    # P → ¬Q
    s2 = implies(P, not Q)
    # Q ∨ R
    s3 = Q or R
    return s1, s2, s3

# Queries
def query_R(P, Q, R):
    return R

def query_R_implies_P(P, Q, R):
    return implies(R, P)

def query_Q_implies_R(P, Q, R):
    return implies(Q, R)

# Print table header
print(f"{'P':^3} {'Q':^3} {'R':^3} {'Q→P':^5} {'P→¬Q':^6} {'Q∨R':^5} {'KB True?':^8} {'R':^3} {'R→P':^5} {'Q→R':^5}")

models_true = []
for P, Q, R in product([False, True], repeat=3):
    s1, s2, s3 = KB(P, Q, R)
    kb_true = s1 and s2 and s3

    if kb_true:
        models_true.append((P, Q, R))

    print(f"{int(P):^3} {int(Q):^3} {int(R):^3} {int(s1):^5} {int(s2):^6} {int(s3):^5} {int(kb_true):^8} "
          f"{int(query_R(P,Q,R)):^3} {int(query_R_implies_P(P,Q,R)):^5} {int(query_Q_implies_R(P,Q,R)):^5}")

# Determine entailments
def entails(query_fn):
    for P, Q, R in models_true:
        if not query_fn(P, Q, R):
            return False
    return True

print("\nKB True in Models:")
for m in models_true:
    print(f"P={m[0]}, Q={m[1]}, R={m[2]}")

print("\nEntailment Results:")
print(f"KB ⊨ R?           {'Yes' if entails(query_R) else 'No'}")
print(f"KB ⊨ (R → P)?      {'Yes' if entails(query_R_implies_P) else 'No'}")
print(f"KB ⊨ (Q → R)?      {'Yes' if entails(query_Q_implies_R) else 'No'}")
