import pandas as pd

String = ['EUROPE', 'AFRICA', 'ASIA', 'AMERICA']
Integer = 5
Float = 1.00345237463452352

example_df = pd.DataFrame({'col_strings': String * 25,
                           'col_integers': [Integer] * 100,
                           'col_floats': [Float] * 100,
                           'col_booleans': [True, False] * 50})

print(example_df.dtypes)
print(example_df.memory_usage())

example_df['col_strings'] = example_df['col_strings'].astype('category')
example_df['col_integers'] = pd.to_numeric(example_df['col_integers'], downcast='integer')
example_df['col_floats'] = pd.to_numeric(example_df['col_floats'], downcast='float')

print(example_df.dtypes)
print(example_df.memory_usage())