# trestle-devops-demo
Simple example of using trestle to complete release management for devops.


## Overall workflow
The conceptual workflow is designed to operate as closely as possible to a standard
devops process

- `develop` is a 'trunk' branch on which core development is maintained
- `main` is a release branch on which the current active version of the code is setup
  - Releases are automated on merges
  - Semantic releases can be used to govern the repository 
  - Semantic release at the file management layer is an open issue: https://github.com/IBM/compliance-trestle/issues/323

To keep things simple the expectation is that users have run trestle assemble beflreo a release themselves. The CICD merely 
check that this has occured.

## Repository setup:
### Recommended branch protection


### DevOps automation


### )RE
