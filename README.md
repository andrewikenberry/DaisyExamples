![](https://github.com/electro-smith/daisyexamples/blob/master/resources/assets/banner.png)

**This repo contains example programs for the [Daisy Embedded Audio Platform.](https://www.electro-smith.com/daisy)** 

If you are just getting started with Daisy, check out our [Getting Started Wiki page!](https://github.com/electro-smith/DaisyWiki/wiki)

Examples are organized by hardware platform.

Included as well are:
- Both libraries as git submodules
- Scripts for rebuildling the libraries as well as all examples
- cube/ folder with .ioc files and example projects that use STM32CubeMX generated code via the STM32 HAL.

## Getting Started

There are a few ways to clone and initialize the repo (with its submodules).

You can do either of the following:

```
git clone --recursive https://github.com/electro-smith/DaisyExamples
```

or 

```
git clone https://github.com/electro-smith/DaisyExamples
git submodule update --init
```

## Updating the Submodules

To pull everything for the repo and submodules:

```
git pull --recurse-submodules
```

to only pull changes for the submodules:

```
git submodule update --remote
```

Alternatively, you can simply run git commands from within the submodule and they will be treated as if you were in that repository instead of Daisy_Examples

## Testing Changes to the Libraries

As the libraries' submodules are tracked to origin-master by default, there are a few ways to go about this.

1. You can checkout a branch from within the repo as normal, and test and work on the library as you would.
2. Each example has conditional setters in their Makefile for variables: `DAISYSP_DIR` and `LIBDAISY_DIR`. These can be set externally to a destination of the users choice.
