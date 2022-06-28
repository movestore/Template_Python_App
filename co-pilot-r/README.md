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
mkdir $LOCAL_SHARE_DIR
cp sample-data/input.rds $LOCAL_SHARE_DIR
```

### Run the MoveApps App

!> Make sure docker can access `$LOCAL_SHARE_DIR` (Docker Desktop: Settings > Resources > File Sharing)

```
docker run -v $LOCAL_SHARE_DIR:/tmp co-pilot-r-sdk
```

### Expected Result

`ls $LOCAL_SHARE_DIR` should listen the generated output file `output.rds`.