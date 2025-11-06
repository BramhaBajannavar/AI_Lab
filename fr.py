class ForwardChaining:
    def __init__(self):
        self.facts = set()  # Set of known facts
        self.rules = []     # List of inference rules
    
    def add_fact(self, fact):
        """Add a new fact to the set of known facts."""
        self.facts.add(fact)
        print(f"Fact added: {fact}")
    
    def add_rule(self, premises, conclusion):
        """Add a rule to the system.
        
        `premises` is a list of facts that must be true to apply the rule.
        `conclusion` is the fact that can be inferred if premises are true.
        """
        self.rules.append((premises, conclusion))
    
    def forward_chain(self):
        """Perform forward chaining to infer new facts."""
        new_inferred = True
        step = 1  # Track steps for logging

        while new_inferred:
            new_inferred = False  # No new facts inferred yet
            
            # Iterate over all rules and check if premises are satisfied
            for premises, conclusion in self.rules:
                if all(premise in self.facts for premise in premises):
                    # If all premises are in the facts, infer the conclusion
                    if conclusion not in self.facts:
                        self.facts.add(conclusion)
                        print(f"Step {step}: Inferred '{conclusion}' from premises {premises}")
                        step += 1  # Increment step
                        new_inferred = True  # Set flag to True to keep iterating
        
        print("\nFinal set of facts:")
        print(self.facts)


# Example usage:

# Create the forward chaining system
fc = ForwardChaining()

# Add some initial facts
fc.add_fact("person(Marcus)")
fc.add_fact("pompeian(Marcus)")

# Add some inference rules
# Rule 1: If pompeian(x) -> roman(x)
fc.add_rule(["pompeian(Marcus)"], "roman(Marcus)")
# Rule 2: If roman(x) -> loyal(x)
fc.add_rule(["roman(Marcus)"], "loyal(Marcus)")
fc.add_rule(["man(Marcus)"], "person(Marcus)")
# Rule 3: If person(x) -> mortal(x)
fc.add_rule(["person(Marcus)"], "mortal(Marcus)")

# Run forward chaining
fc.forward_chain()

# Check if Marcus is mortal
if "mortal(Marcus)" in fc.facts:
    print("\nYes, Marcus is mortal!")
else:
    print("\nNo, Marcus is not mortal.")
