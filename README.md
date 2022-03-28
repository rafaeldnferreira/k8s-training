# Kubernetes and Helm training

## The problem statement

You work in an assigment that is creating the next revolutiary _TODO_ application.

You are the engineer maintaining these two applications: One frontend end user web application and a back end application used by the front end to process incoming requests. These two applications can be built and deployed locally via Docker using the `docker-composer.yml` provided.

This works well for development, but to ensure production scale deployment, you need to make use of [Azure Kubernetes Service](https://azure.microsoft.com/en-gb/services/kubernetes-service).


## Your tasks

Manually writing Kubernetes manifests can be tedious and error prone, so you will use Helm to better manage and package your applications.

Create the relevant [Helm](https://helm.sh/) chart under the `helm` directory to produce a compatible [Deployment]() that will achieve the following criteria:

- **Two instances** of **the front end application** are always running and **one instance** of the **back end application**;
- The front end application is public available (reachable from the internet) and the back end is **not**;
- A Load balancer will must evenly distribute the requests (round-robbin).

### Expected deliverables

- A public link where the application can be accessed;
- A tour to the created k8s manifests and rationale of each of them;
- A way to reproduce the deployment multiple times;
- If you deploy multiple instances of the back end, you will notice that the application doesn't behave as intended, can understand the problem and propose a solution to fix that? **BONUS**: can you implement that solution?

## Guidelines and resources

- Use your personal Azure subscription (not the corporate account);
- Use [AKS Quickstart](https://docs.microsoft.com/en-us/azure/aks/quickstart-helm) for sample instructions.

## Technical requirements and development environment

- You need Docker;
- You need Python3.

In your WSL environment create a `Python3` virtual environment:

```bash
$ sudo apt install python3.8-venv
$ python3 -m venv k8s-training
$ . k8s-training/bin/activate
```

Building the applications:

```bash
$ ./build.bash
```

Start the applications via:

```bash
$ docker-compose up
```

Launch a web-browser at `http://localhost:5001`,
