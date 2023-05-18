# Purple Air Data Access

## Prerequisites

### Instal PDM

Use [this guide] (https://pdm.fming.dev/latest/#recommended-installation-method) to get PDM working. 

### Set Up API Key

Add your Purple Air API key to your local Linux terminal using this command: 

```shell
export PURPLE_AIR_API_KEY='your-api-key-goes-here'
```
Chedk that your addition was sucessful using this command:

```shell
echo $PURPLE_AIR_API_KEY
```

## First Time Users

Use PDM to set up the project's dependencies and virtual environment using this command:

```shell
pdm sync
```

## Run the Code

Use PDM to execute this command: 

```shell
pdm start
```
