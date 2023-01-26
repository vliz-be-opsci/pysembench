# pysembench


## SETTTINGS FOR PREP ACTION CRATE

### available paths:
    - ${WORKSPACE_LOCATION} => path to workspace where the action will perform its tasks
    - ${DATA_LOCATION} => path to datacrate where the action grab data for its tasks
    - ${PROFILE_LOCATION} => path to checkout of ?profile_github_connect_string

### semantic annotation:
    - ${DATA_LOCATION}/rocrate-metadata.json => will contain a triple : <./> dct:conformsTo ?profile_URI
    - ?profile_URI/ro-crate-metadata.json => will contain a triple : <./> dma:crateRepo ?profile_github_connect_string
    - ?profile_URI/ro-crate-metadata.json => will contain a triple : <./path/to/sembench.json> rdf:type dma:SemBenchConfig TODO: add SemBenchConfig to ontology dmbonassistant + note jsonld encoding via @type

### resulting outcome
    - we have a data location where we work on
    - we have a path to a config file that contains the settings for the sembench action
    - we have a path to a profile that contains the settings for the sembench action



## SETTINGS FOR SEMBANCH ACTION

### available paths:
    - ${DATA_LOCATION} => path to datacrate where the action grab data for its tasks
    - ${SEMBENCH_LOCATION} => path to sembench data context (default: folder where ${SEMBENCH_CONFIG_PATH} is located)
    - ${SEMBENCH_CONFIG_PATH} => path to sembench config file


```jsonc
[
    {
        "type":"pysubyt",
        "input": "${DATA_LOCATION}/downloads/gdoc-csv/sediment_measured.csv", /*relative to datacrate ${DATA_LOCATION} will be an env variable in action ex:downloads/gdoc-csv/sediment_measured.csv*/ 
        "output": "${DATA_LOCATION}/downloads/gdoc-csv/sediment_measured.ttl", /*relative to datacrate ${DATA_LOCATION} will be an env variable in action ex:downloads/gdoc-csv/sediment_measured.ttl*/
        "template": {
            "root": "${SEMBENCH_LOCATION}/templates",
            "name": "sediment_measured.ttl"
        }
    },
    {
        "type":"pysubyt",
        "input": "${DATA_LOCATION}/downloads/gdoc-csv/water_measured.csv", /*relative to datacrate ${DATA_LOCATION} will be an env variable in action ex:downloads/gdoc-csv/sediment_measured.csv*/ 
        "output": "${DATA_LOCATION}/downloads/gdoc-csv/water_measured.ttl", /*relative to datacrate ${DATA_LOCATION} will be an env variable in action ex:downloads/gdoc-csv/sediment_measured.ttl*/
        "template": {
            "root": "${SEMBENCH_LOCATION}/templates",
            "name": "water_measured.ttl"
        }
    }
]
```

## Suggested contents of sembench location
- ./sembench.json
- ./templates/sediment_measured.ttl
- ./templates/water_measured.ttl
- ./templates/macros/macro1.ttl
- ./templates/macros/macro2.ttl



### Future suggestions:
    - How to solve the problem of having 1500+ files to convert to ttl? => do we write a huge json file with all the settings? => have regex or globbing perhaps as extra option in pysubyt
    - Have a sembench creation tool that creates the sembench.json file based on user pref 
    - Inclusion of other sembench action types (e.g. csvW, rml.io, eye-reasoning, kg2tbl, etc.,)
    - ROCrate cleanup action
    - ROCRATE and SEMBENCH action that will add data to rocrate-meatadata.json and will delete all files in repo that are not in the rocrate-metadata.json
