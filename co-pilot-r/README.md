# MoveApps R SDK

## Build

```
docker build -t co-pilot-r-sdk .
```

## Run

You can simulate the app lifecycle on MoveApps by running the image locally.

### Prepare local machine

```
export LOCAL_SHARE_DIR=/tmp/co-pilot-r-share
export SAMPLE_INPUT=input2_geese.rds
mkdir $LOCAL_SHARE_DIR
cp sample-data/$SAMPLE_INPUT $LOCAL_SHARE_DIR
```

### Run the MoveApps App locally

> :warning: Make sure docker can access `$LOCAL_SHARE_DIR` (Docker Desktop: Settings > Resources > File Sharing)

Provide input data and app configuration during runtime and start the app:

```
docker run -v $LOCAL_SHARE_DIR:/tmp -e SOURCE_FILE=/tmp/$SAMPLE_INPUT -e OUTPUT_FILE=/tmp/output.rds -e CONFIGURATION='{"year":2014}' co-pilot-r-sdk
```

### Expected Result

`ls $LOCAL_SHARE_DIR` should listen the generated output file `output.rds` (and in this case also `hello_world.pdf`).
