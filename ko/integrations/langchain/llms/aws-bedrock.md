---
description: AWS Bedrock 대규모 언어 모델 주변의 wrapper입니다.
---

# AWS Bedrock


**AWS Bedrock LLM** node는 생성형 AI 애플리케이션을 구축하기 위한 foundation models에 대한 액세스를 제공하는 관리되는 서비스인 Amazon Bedrock과 통합됩니다. 

Flowise에서 AWS Bedrock을 사용하려면 **AWS Bedrock LLM** node를 Chatflow에 추가합니다. 

# Setup

1. Flowise에 대한 AWS 자격증명을 구성합니다.

Amazon Bedrock에서 Flowise와 사용하려는 모델에 대한 계정 액세스 권한이 있는지 확인합니다. 

2. AWS Bedrock node를 Chatflow에 추가합니다.

Flowise canvas에서 AWS Bedrock LLM node를 Chatflow로 드래그 앤 드롭합니다. 

3. AWS Bedrock inputs 구성:
<figure><img src="../../../.gitbook/assets/image (2) (5).png" alt="" width="275"><figcaption><p>AWS Bedrock Node</p></figcaption></figure>

* AWS Credential: 기존 AWS 자격증명을 선택하거나 새로 생성합니다. 관련 IAM user 또는 role은 `bedrock:InvokeModel` 및 Chatflow의 다른 필수 AWS 서비스에 대한 권한을 가져야 합니다.
* Region: Bedrock 모델이 사용 가능한 AWS region입니다.
* Model Name: conversational AI용 AWS Bedrock foundational 모델입니다.

4. Chatflow에서 AWS Bedrock node를 연결합니다.

다른 Chatflow components (예: input nodes, output nodes, memory nodes)를 추가한 후 AWS Bedrock LLM node를 적절한 components에 연결하여 Chatflow를 생성합니다.

AWS에 Flowise를 배포하는 방법에 대한 정보는 [AWS](../../../configuration/deployment/aws.md)를 참조하세요.


