# Question 1a
x = np.arange(100)
source = pd.DataFrame({
  'x': x,
  'f(x)': x * 2
})
alt.Chart(source).mark_point().encode(
    x='x',
    y='f(x)',
    color='x'
)

# Question 1b
x = np.arange(100)
source = pd.DataFrame({
  'x': x,
  'f(x)': x * 2,
  'color_value': x % 4
})
alt.Chart(source).mark_point().encode(
    x='x',
    y='f(x)',
    color='color_value'
)

# Question 1c (bonus)
alt.Chart(source).mark_point().encode(
    x='x',
    y='f(x)',
    color=alt.condition(
        alt.FieldOneOfPredicate(field='x', oneOf=list(range(0, 100, 2))), 
        alt.value('blue'), 
        alt.value('red'))
)

# Question 2
interval = alt.selection_interval(encodings=['x'])
alt.Chart(cars).mark_circle().encode(
    x='Weight_in_lbs',
    y='Miles_per_Gallon',
    color=alt.condition(interval, 'Origin', alt.value('lightgray')),
    tooltip=['Name', 'Year']
).properties(selection=interval, height=300, width=400)
