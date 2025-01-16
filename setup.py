from setuptools import find_packages, setup
from typing import List

# Define the required dependencies
def get_requirements() -> List[str]:
    """
    This function reads the 'requirements.txt' file and returns a list of dependencies.
    
    Returns:
        List[str]: A list of requirements extracted from 'requirements.txt'.
    """
    # Initialize an empty list to store requirements
    requirement_list: List[str] = []
    
    try:
        # Open and read the 'requirements.txt' file
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                # Strip whitespace and handle specific cases
                requirement = line.strip()
                if requirement and requirement != "-e .":  # Ignore empty lines and '-e .' entries
                    requirement_list.append(requirement)
    except FileNotFoundError:
        # Handle the case where 'requirements.txt' is missing
        print("requirements.txt not found")
    
    return requirement_list

setup(
    name = "Network Security",
    version = "0.0.1",
    author = "Acheampong Stephen",
    author_email = "acheampongstephen392024@gmail.com",
    description = "A package for network security analysis and monitoring",
    packages = find_packages(),
    install_requires = get_requirements()
)
