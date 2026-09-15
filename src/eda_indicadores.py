"""Única ayuda de tabulación del notebook 07."""

import pandas as pd


def pct_ponderado(df, var, peso="fex_c"):
    """% muestral, % ponderado y conteo válido de cada categoría."""
    sub = df[[var, peso]].dropna()
    muestral = sub[var].value_counts(normalize=True) * 100
    ponderado = sub.groupby(var, observed=True)[peso].sum() / sub[peso].sum() * 100
    return pd.DataFrame({
        "pct_muestral": muestral,
        "pct_ponderado": ponderado,
        "n_valido": sub[var].value_counts(),
    })
