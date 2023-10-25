# Prototype 3 FGA Project

## Setup

- Create a virtual environment: `conda create -n <env_name> python=3.10`
- Install the test package using the pip install command

## Program use

### Project initialization:

- Run `fga init` to provide user access creds and setup overall project, through responding to a series of prompts. Like shown below

```
Provide a project name default: [fga]: 
What region should your resources be provisioned in eg: eu-west-1?: 
What should we name the cluster? default: [eks-cluster]: 
What resource prefix should we use(an alphanumeric; 3-11 character limit)? default: [fga]: "provide a resource prefix"
Provide the IAM Access Key: "access key goes here"
Provide the AWS Secret key: "secret key goes here"
The fga directory already exists. Do you want to update its contents? [y/N]: y
Your project fga has been created here: /<dir-path>/fga
```

_On completion a dir path will be provided indicating where project has been setup._

cd into the dir ie: `cd <dir-path/fga>`


### Provision the FGA resources.
- run command: `fga provision` to deploy the FGA infrastructure.


### View extra commands here.
- run command: `fga --help` to see other commands