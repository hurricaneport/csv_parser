#!/bin/bash

echo "Exporting current environment"

pip freeze > requirements.txt
conda env export > environment.yml
