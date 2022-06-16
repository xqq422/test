# Define function to bin column values
def bin_values(revenue, v):
    if revenue >= v:
        val = 1
    else:
        val = 0
    return val
