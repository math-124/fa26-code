from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go


DATA_DIR = Path(__file__).resolve().parent


def plot_names():
    """Plot annual SSA birth counts for the first names in this class."""
    names = sorted(np.load(DATA_DIR / "first_names.npy", allow_pickle=False).tolist())
    births = pd.read_csv(DATA_DIR / "baby.csv", usecols=["Name", "Count", "Year"])
    births = births[births["Name"].isin(names)]
    counts = births.groupby(["Name", "Year"], as_index=False)["Count"].sum()

    years = np.arange(1880, 2023)
    fig = go.Figure()
    for name in names:
        name_counts = (
            counts[counts["Name"] == name]
            .set_index("Year")["Count"]
            .reindex(years, fill_value=0)
        )
        fig.add_trace(
            go.Scatter(
                x=years,
                y=name_counts,
                mode="lines",
                name=name,
                line=dict(color="#3d81f6", width=3),
                hovertemplate="%{x}: %{y:,} babies<extra></extra>",
                visible=(name == names[0]),
            )
        )

    buttons = [
        dict(
            label=name,
            method="update",
            args=[
                {"visible": [index == i for index in range(len(names))]},
                {"title": f"U.S. babies named {name} per year"},
            ],
        )
        for i, name in enumerate(names)
    ]

    fig.update_layout(
        updatemenus=[
            dict(buttons=buttons, x=1.02, y=1, xanchor="left", yanchor="top")
        ],
        title=f"U.S. babies named {names[0]} per year",
        plot_bgcolor="white",
        paper_bgcolor="white",
        width=850,
        height=480,
        showlegend=False,
        margin=dict(l=70, r=180, t=70, b=60),
        font=dict(family="Palatino Linotype, Palatino, serif", color="black"),
    )
    fig.update_xaxes(
        title="Year", gridcolor="#f0f0f0", showline=True, linecolor="black"
    )
    fig.update_yaxes(
        title="Number of babies", gridcolor="#f0f0f0", showline=True, linecolor="black"
    )
    fig.show()
