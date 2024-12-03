#

def display_options(options, current_index):
    print("Opciones:\n")
    for index, (id, option, help_text) in enumerate(options):
        prefix = "-> " if index == current_index else "   "
        print(f"{prefix}{id}. {option} - {help_text}")
