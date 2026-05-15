import plotly.graph_objects as go
import plotly.express as px
import numpy as np


def volatility_smile_chart(df):

    fig = px.line(
        df,
        x="strike",
        y="implied_vol",
        markers=True,
        title="Implied Volatility Smile"
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis_title="Strike",
        yaxis_title="Implied Volatility"
    )

    return fig


def calibration_chart(strikes, market_vols, model_vols):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=strikes,
            y=market_vols,
            mode='lines+markers',
            name='Market Volatility'
        )
    )

    fig.add_trace(
        go.Scatter(
            x=strikes,
            y=model_vols,
            mode='lines+markers',
            name='SABR Model Volatility'
        )
    )

    fig.update_layout(
        template="plotly_dark",
        title="Market vs SABR Calibration",
        xaxis_title="Strike",
        yaxis_title="Volatility"
    )

    return fig


def surface_plot(X, Y, Z):

    fig = go.Figure(
        data=[
            go.Surface(
                x=X,
                y=Y,
                z=Z
            )
        ]
    )

    fig.update_layout(
        template="plotly_dark",
        title="3D Volatility Surface",
        scene=dict(
            xaxis_title="Strike",
            yaxis_title="Expiry",
            zaxis_title="Volatility"
        ),
        height=700
    )

    return fig


def heatmap_plot(Z):

    fig = px.imshow(
        Z,
        aspect="auto",
        color_continuous_scale="Viridis",
        title="Volatility Heatmap"
    )

    fig.update_layout(template="plotly_dark")

    return fig
