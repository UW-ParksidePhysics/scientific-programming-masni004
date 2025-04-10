import pandas as pd


def get_data():
    desired_objects = ['Mercury', 'Venus', 'Ceres']

    url = 'https://en.wikipedia.org/wiki/List_of_Solar_System_extremes'

    tables = pd.read_html(url)
    extreme_values_table = tables[5].set_index(tables[5].columns[0])
    object_names = extreme_values_table.iloc[:, 0]
    for desired_object in desired_objects:
        # Add a condition that checks for the existence of each value in the table
        # before assigning it to a variable

        minimum_temperature = extreme_values_table.loc[desired_object].iloc[5].split('K')[0]
        maximum_temperature = extreme_values_table.loc[desired_object].iloc[4].split('K')[0]
        print('The temperature range on {} is {} - {} K'.format(desired_object, minimum_temperature, maximum_temperature))

    solar_system_objects_data = []
    return solar_system_objects_data


if __name__ == '__main__':
    objects = get_data()

#### RENAME from temperature_icons.py to (your_project_short_name).py
# File structure
# 1. Commented paragraph describing project ~ 100-200 words
# 2. Module imports that are used in multiple functions
# 3. Function definitions
# 4. if __name__ == "__main__" block, which calls a primary function with a clear name 

# All code is inside function definitions for simulation solution & visualization (functional programming)
#	Each function contains a docstring compliant with PEP 257: https://www.python.org/dev/peps/pep-0257/
#	Module ends with if __name__ == "__main__" block to execute central function of the code

# Primary simulation function structure
#	1. Module imports
#		Use SciPy constants for physical constants in particular function (not globally)
#			https://docs.scipy.org/doc/scipy/reference/constants.html
#		Follow best practice order: 
#			https://docs.python.org/3/faq/programming.html#what-are-the-best-practices-for-using-import-in-a-module
# 	2. Simulation parameters
#		Each parameter named clearly and units marked in in-line comment
#		Naming of all variables should comply with PEP 8: 
#			https://www.python.org/dev/peps/pep-0008/#documentation-strings
#			(lower_case_with_underscores)
# 	3. Computed parameters (from simulation parameters)
# 	4. Function calls (use PEP 8-compliant lower_case_with_underscores) and simple calculations for:
#		data read-in
#		simulation solution 
#		visualization
