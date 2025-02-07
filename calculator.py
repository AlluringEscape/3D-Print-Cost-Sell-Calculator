import random

def calculate_cost(material_cost, material_used, print_time, prep_components, post_components, consumables, energy_cost, labor_cost, fail_rate, markup):
    # Materials cost
    materials_cost = material_cost * material_used
    # Electricity cost (assume print_time in hours)
    electricity_cost = energy_cost * print_time
    # Printer depreciation (example: $0.10 per hour)
    printer_depreciation = 0.10 * print_time
    
    # Preparation costs (using labor cost per hour)
    model_preparation_cost = labor_cost * prep_components.get('model_preparation', 0)
    slicing_cost = labor_cost * prep_components.get('slicing', 0)
    material_change_cost = labor_cost * prep_components.get('material_change', 0)
    transfer_cost = labor_cost * prep_components.get('transfer', 0)
    preparation_sum = model_preparation_cost + slicing_cost + material_change_cost + transfer_cost
    
    # Post-Processing costs
    job_removal_cost = labor_cost * post_components.get('job_removal', 0)
    support_removal_cost = labor_cost * post_components.get('support_removal', 0)
    additional_work_cost = labor_cost * post_components.get('additional_work', 0)
    post_processing_sum = job_removal_cost + support_removal_cost + additional_work_cost
    
    # Additional items (set to 0 or adjust as needed)
    miscellaneous = 0
    shipping = 0
    
    # Subtotal calculation
    subtotal = (materials_cost + electricity_cost + printer_depreciation +
                preparation_sum + post_processing_sum + consumables + miscellaneous + shipping)
                
    # Failure costs and markup
    failures_cost = materials_cost * fail_rate
    markup_amount = (subtotal + failures_cost) * (markup / 100)
    # Random up amount (e.g., between 1% and 5% of subtotal)
    random_up = subtotal * random.uniform(0.01, 0.05)
    
    total_cost = subtotal + failures_cost + markup_amount + random_up
    
    return {
        "Model Preparation": model_preparation_cost,
        "Slicing": slicing_cost,
        "Material Change": material_change_cost,
        "Transfer & Start": transfer_cost,
        "Preparation Sum": preparation_sum,
        "Job Removal": job_removal_cost,
        "Support Removal": support_removal_cost,
        "Additional Work": additional_work_cost,
        "Post-Processing Sum": post_processing_sum,
        "Miscellaneous": miscellaneous,
        "Consumables": consumables,
        "Shipping": shipping,
        "Materials": materials_cost,
        "Electricity": electricity_cost,
        "Printer Depreciation": printer_depreciation,
        "Subtotal": subtotal,
        "Including Failures": failures_cost,
        "Markup": markup_amount,
        "Random Up Amount": random_up,
        "Total Cost": total_cost
    }
