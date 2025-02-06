def calculate_cost(**kwargs):
    material_total = kwargs["material_cost"] * kwargs["material_used"]
    energy_total = kwargs["energy_cost"] * (kwargs["preparation_time"] + kwargs["post_processing_time"])
    labor_total = kwargs["labor_cost"] * (kwargs["preparation_time"] + kwargs["post_processing_time"])
    fail_total = kwargs["fail_rate"] * (material_total + energy_total + labor_total + kwargs["consumables"])
    base_cost = material_total + energy_total + labor_total + kwargs["consumables"] + fail_total
    total_cost = base_cost * (1 + kwargs["markup"] / 100)
    
    return {
        "Material": material_total,
        "Energy": energy_total,
        "Labor": labor_total,
        "Consumables": kwargs["consumables"],
        "Failure Margin": fail_total,
        "Total": total_cost
    }