import data_fetcher

def generate_website(animals_data, animal_name):
    """
    Generates an HTML website displaying the information of the animals.
    """
    # Read the HTML template
    with open('animals_template.html', 'r') as file:
        template = file.read()

    # Generate HTML for the animals
    animals_info = ''
    for animal in animals_data:
        # Extract the necessary information
        name = animal['name']
        diet = animal['characteristics'].get('diet', 'N/A')
        locations = ', '.join(animal['locations'])
        animal_type = animal['characteristics'].get('type', 'N/A')
        skin_type = animal['characteristics'].get('skin_type', 'N/A')

        # Create a formatted string with the required details
        animal_info = f"""
            <li class="cards__item">
                <h2 class="card__title">{name}</h2>
                <p class="card__text"><strong>Diet</strong>: {diet}</p>
                <p class="card__text"><strong>Location</strong>: {locations}</p>
                <p class="card__text"><strong>Type</strong>: {animal_type}</p>
                <p class="card__text"><strong>Skin Type</strong>: {skin_type}</p>
            </li>
            """
        animals_info += animal_info

    # Replace placeholder with actual animal information
    html_content = template.replace('__REPLACE_ANIMALS_INFO__', animals_info)

    # Write the HTML content to a file
    with open('animals.html', 'w') as file:
        file.write(html_content)

def main():
    animal_name = input("Enter the name of an animal: ")
    animals_data = data_fetcher.fetch_data(animal_name)

    if animals_data:
        generate_website(animals_data, animal_name)
        print(f"Website was successfully generated to the file animals.html.")
    else:
        # Handle the case when no data is returned
        with open('animals_template.html', 'r') as file:
            template = file.read()

        html_content = template.replace('__REPLACE_ANIMALS_INFO__', f'<h2>The animal "{animal_name}" doesn\'t exist.</h2>')

        with open('animals.html', 'w') as file:
            file.write(html_content)

        print(f"The animal {animal_name} doesn't exist.")

if __name__ == "__main__":
    main()
