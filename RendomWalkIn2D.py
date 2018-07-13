x = [0]
y = [0]

for j in range(1000):
    step_x = random.randint(0, 1)
    if step_x == 1:
        x.append(x[j] + 1 + np.random.normal())
    else:
        x.append(x[j] - 1 + np.random.normal())

    step_y = random.randint(0, 1)
    if step_y == 1:
        y.append(y[j] + 1 + np.random.normal())
    else:
        y.append(y[j] - 1 + np.random.normal())

trace1 = go.Scatter(
    x=x,
    y=y,
    mode='markers',
    name='Random Walk',
    marker=dict(
        color=[i for i in range(len(x))],
        size=8,
        colorscale='Greens',
        showscale=True
    )
)

data = [trace1]
py.iplot(data, filename='random-walk-2d')