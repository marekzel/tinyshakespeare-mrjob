import pandas as pd
import plotly.express as px

try:
    df = pd.read_csv('out.csv', names=['word', 'count'])
except FileNotFoundError:
    print("Error: 'out.csv' file not found.")
    exit()

df = df.dropna()
df = df[df['word'].str.len() > 1]
df['word_length'] = df['word'].str.len()

fig = px.scatter(
    df,
    x='word_length',
    y='count',
    log_y=True,
    hover_name='word',
    title='<b>Shakespeare Vocabulary: Word Length vs. Usage Frequency</b>',
    labels={'word_length': 'Word Length (Number of Characters)', 'count': 'Word Count (Log Scale)'},
    color='word_length',
    color_continuous_scale='Viridis',
    template='plotly_dark'
)

fig.update_traces(
    marker=dict(size=8, opacity=0.6, line=dict(width=0.5, color='white'))
)

fig.update_layout(
    xaxis=dict(tickmode='linear', tick0=1, dtick=1),
    coloraxis_showscale=False,
    font=dict(family="Courier New, monospace", size=14)
)

fig.show()
