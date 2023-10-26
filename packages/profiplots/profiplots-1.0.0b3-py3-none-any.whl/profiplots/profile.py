"""
This module contains implementation of profiles. Profiles is a combination of styles made for a specific purpose. For example profile `exploration` was made to allow quick data exploration.
"""


from profiplots.style import _modifier


def exploration() -> dict:
    """Profile whose purpose is to be used for exploratory analysis.

    Returns
    -------
    dict
        Matplotlib rc settings.

    Examples
    -------

    ```{python}
    import seaborn.objects as so
    import seaborn as sns
    import profiplots as pf

    data = sns.load_dataset("titanic")
    pf.set_theme(name="default")

    (
        so.Plot(data=data, x="age", y="fare")
        .theme(pf.profile.exploration())
        .add(so.Dots())
    )
    ```

    """
    return (
        _modifier.grid(x=True, y=True)
        | _modifier.spines(left=False, right=False, top=False, bottom=False)
        | _modifier.ticks(x=True, y=True)
    )


def publish() -> dict:
    """Use this profile for final visualizations that we want to publish. It has a very clean look.

    Returns
    -------
    dict
        Matplotlib rc settings.

    Examples
    -------

    ```{python}
    import seaborn.objects as so
    import seaborn as sns
    import profiplots as pf

    data = sns.load_dataset("titanic")
    pf.set_theme(name="default")

    (
        so.Plot(data=data, x="age", y="fare")
        .theme(pf.profile.publish())
        .add(so.Dots())
    )
    ```

    """
    return (
        _modifier.grid(x=False, y=False)
        | _modifier.spines(left=True, bottom=True, right=False, top=False)
        | _modifier.ticks(x=True, y=True)
    )
