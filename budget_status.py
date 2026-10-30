# Budget Status Component

def budget_status(budget, total):
    if total <= budget:
        return "Within budget"
    else:
        return "Over budget"

# Test 1: Below budget
below_budget = budget_status(16000, 15000)
print(below_budget)

# Test 2: Exactly equal to budget
equal_budget = budget_status(16000, 16000)
print(equal_budget)

# Test 3: Over budget
over_budget = budget_status(16000, 17000)
print(over_budget)

"""
Component: budget_status
Returns: "Within budget" when total <= budget, otherwise "Over budget"
Tests: below budget, exact budget, over budget
Issue: none
"""
