# Quirk+ Guppy workshop

## How to follow along with the workshop

You can follow along with code presented in the workshop as follows.

1. Install `uv` (if you haven't already)


This can be done by following the instructions here -> https://docs.astral.sh/uv/getting-started/installation/

If you would rather install the dependencies manually... See (3.)


Here are the recommended terminal installation commands for different operating systems. These are copied from uv docs page linked above.

MacOS and Linux

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


2. Clone this repository.

Clone this github repository onto your local machine.

```sh
git clone git@github.com:Quantinuum/Quirk_Guppy_workshop.git
```


3. Install the dependencies.

Once `uv` is installed, run `uv sync` from the root of this repository.

```sh
uv sync
```

This will install all the Python packages needed to run the `demo.ipynb` example notebook.

If you would rather install the dependencies manually... Install the following packages with pip.

```
guppylang[pytket]>=0.21.8
ipykernel>=7.2.0
jupyterlab>=4.5.3
matplotlib>=3.10.8
```


4. Open the jupyter notebook

Now that we have installed the dependencies. We are ready to open and run the notebook. 

```sh
uv run jupyter lab
```
