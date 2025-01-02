def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            
def gather_inputs():
    print("Enter Printer Details:")
    energy_cost = get_float_input("Energy cost per hour ($): ")
    labor_cost = get_float_input("Labor cost per hour ($): ")
    fail_rate = get_float_input("Failure rate (%): ") / 100

    print("\nEnter Material Details:")
    material_cost = get_float_input("Material cost per unit ($): ")
    material_used = get_float_input("Material used (units): ")

    print("\nEnter Time Details:")
    preparation_time = get_float_input("Preparation time (hours): ")
    post_processing_time = get_float_input("Post-processing time (hours): ")

    print("\nEnter Additional Costs:")
    consumables = get_float_input("Consumables cost ($): ")
    markup = get_float_input("Markup percentage (%): ")

    # Return inputs in the exact order expected by calculate_cost
    return (
        material_cost, material_used, 
        energy_cost, preparation_time, 
        labor_cost, fail_rate, 
        post_processing_time, consumables, markup
    )
