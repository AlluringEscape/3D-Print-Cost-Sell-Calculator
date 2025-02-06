def calculate_cost(
    material_cost, material_used, 
    energy_cost, preparation_time, 
    labor_cost, fail_rate, 
    post_processing_time, consumables, markup
):
    material_total = material_cost * material_used
    energy_total = energy_cost * (preparation_time + post_processing_time)
    labor_total = labor_cost * (preparation_time + post_processing_time)
    fail_total = fail_rate * (material_total + energy_total + labor_total + consumables)
    base_cost = material_total + energy_total + labor_total + consumables + fail_total
    total_cost = base_cost * (1 + markup / 100)
    return total_cost