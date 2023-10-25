# managed-kubernetes-clusters
As prototype 3 is based on Data Governance deployed on AWS, thus here we only deploy eks.

It must be noted for eks-cluster to be deployed we need to mandatory define 6 variables explicitly 
- eks_cluster_name
- eks_vpc_name
- aws_resource_prefix
- aws_region
- project_tags
- eks_cluster_deploy (set to true if you need eks to be deployed)

