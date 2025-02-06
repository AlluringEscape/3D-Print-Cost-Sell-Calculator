def calculate_cost(
    material_cost, 
    material_used,
    energy_cost,
    preparation_time,
    labor_cost,
    fail_rate,
    post_processing_time,
    consumables,
    markup
):
    # Material Costs
    material_total = material_cost * material_used
    
    # Energy Costs
    energy_total = energy_cost * (preparation_time + post_processing_time)
    
    # Labor Costs
    prep_labor = labor_cost * preparation_time
    post_labor = labor_cost * post_processing_time
    total_labor = prep_labor + post_labor
    
    # Failure Costs
    fail_total = (material_total + energy_total + total_labor + consumables) * fail_rate
    
    # Totals
    subtotal = material_total + energy_total + total_labor + consumables
    total_with_markup = (subtotal + fail_total) * (1 + markup/100)
    
    return {
        "Material": material_total,
        "Energy": energy_total,
        "Preparation Labor": prep_labor,
        "Post-Processing Labor": post_labor,
        "Consumables": consumables,
        "Failure Costs": fail_total,
        "Subtotal": subtotal,
        "Markup Amount": total_with_markup - (subtotal + fail_total),
        "Total Cost": total_with_markup
    }