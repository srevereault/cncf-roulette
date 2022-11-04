# cncf-roulette
A quick and dirty webapp to explore CNCF landscape

## Installation
 - Clone repo
 - Install dependencies : 

```pip install -r requirements.txt```

 - Go to the [CNCF Landscape Website](https://landscape.cncf.io/)
 - Select only projects (you can do it by opening [this link](https://landscape.cncf.io/card-mode?category=provisioning,runtime,orchestration-management,app-definition-and-development,platform,serverless,observability-and-analysis,wasm&grouping=category) directly
 - Click on the `Download as CSV` link
 - Rename the file to `cncf.csv`

## Usage
```flask run```
