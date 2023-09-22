# Infrastructure as Code
### What is it? Why would I want it? Are there any alternatives?

It is a way to provision infrastructure (servers, networking etc) using code. It will help us to track changes, consistency across different environments (staging, production, etc), disaster recovery and scale the environment.

There are alternatives but still not as powerful as IaC, i.e, with ansible we can do configuration management but it doesn't cover all the aspects of infra management.


# Observability
### Please explain this term in the context of micro services. What do we want to observe? What kind of challenges do you see in a distributed environment? How can we solve them?

In micorservice ecosystem Observability means to gain insights in the behaviour and performance of micro services due to its complexity and distributed nature. In order to make a high performance distributed system we need to observer following aspects, metrics, logs, traces and configuration changes.


# Security
### Imagine you would join our team and put in charge of securing our AWS infrastructure. What are the first three things that you check, to limit the risk of a breach? Explain why.

In AWS I would like to priortize the following thing:

Enabling MFA, policy of least privilege, credentials monitoring (refresh the access token and password), data encryption at rest and in transit. Environment isolation (on VPC basis or AWS account level) is also necessary to reduce the incident blast radius.
