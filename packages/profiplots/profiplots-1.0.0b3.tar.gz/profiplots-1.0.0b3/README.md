# profiplots

Make Matplotlib and Seaborn plots with Profinit theme!

- Documentation: https://datascience.profinitservices.cz/sablony/profiplots/.

## Install

Now we can install the package with the following command:

```sh
python -m pip install profiplots
```

## Usage

Now we can start using this package!

First we import `profiplots` package and call `set_theme`.

```python
import profiplots as pf

pf.set_theme(name="default")
```

Then we can start using `seaborn` or `matplotlib` plotting as usually. But instead of the default design, we will now have the **enhanced** Profinit theme.


```python
import seaborn as sns
import seaborn.objects as so

# load dataset from seaborn
dataset = sns.load_dataset("titanic")[["sex", "survived"]]

# write out the plot
(
    so.Plot(data=dataset, x="survived", y="sex")
    .add(so.Bar(alpha=1), so.Agg(), legend=False)
    .label(title="Female passengers survived much more frequently", x="Survival Rate", y="Sex")
)
```