# Quirk+ Guppy workshop

## How to follow along with the workshop

You can follow along with code presented in the workshop as follows.

1. Install `uv` (if you haven't already)


This can be done by following the instructions here -> https://docs.astral.sh/uv/getting-started/installation/

Here are the recommended terminal installation commands for different operating systems.

MacOS and Linux

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows

```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```


2. Install the dependencies.

Once `uv` is installed, run `uv sync` from the root of this repository.

```sh
uv sync
```

This will install all the Python packages needed to run the `demo.ipynb` example notebook.


3. Open the jupyter notebook

Now that we have installed the dependencies. We are ready to open and run the notebook. 

```sh
uv run jupyter lab
```
