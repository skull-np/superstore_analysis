from dash import Dash, html, dcc
import pandas as pd
import plotly.express as px

# Load data 
df = pd.read_csv('data/Superstore.csv', encoding='latin-1')

# Pre-compute the four findings
profit_by_subcategory = df.groupby('Sub-Category')['Profit'].sum().reset_index().sort_values('Profit')
regional_profit = df.groupby('Region')['Profit'].sum().reset_index().sort_values('Profit')
regional_sales = df.groupby('Region')['Sales'].sum().reset_index().sort_values('Sales')
region_category = df.groupby(['Region', 'Category'])['Profit'].sum().reset_index().sort_values('Profit')

fig1 = px.scatter(df, x='Discount', y='Profit', title='Discount vs Profit')
fig2 = px.bar(regional_profit, x='Region', y='Profit', title='Profit by Region')
fig3 = px.bar(regional_sales, x='Region', y='Sales', title='Sales by Region')
fig4 = px.bar(profit_by_subcategory, x='Sub-Category', y='Profit', title='Profit by Sub-Category')

# Making it transparent
for fig in [fig1, fig2, fig3, fig4]:
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='#ffffff'
    )

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Superstore Sales Dashboard"),
    html.P("Discount & Profitability Analysis"),
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    dcc.Graph(figure=fig4),
])

if __name__ == '__main__':
    app.run(debug=True)

