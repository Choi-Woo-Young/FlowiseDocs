---
description: AWS Bedrock 대규모 언어 모델 래퍼.
---

# AWS Bedrock


**AWS Bedrock LLM** 노드는 Amazon Bedrock과 통합되며, 생성형 AI 애플리케이션 구축을 위한 기초 모델에 대한 접근을 제공하는 관리형 서비스입니다.

Flowise에서 AWS Bedrock을 사용하려면 Chatflow에 **AWS Bedrock LLM** 노드를 추가하세요.

# 설정

1. Flowise용 AWS 자격증명 구성.

Amazon Bedrock에서 Flowise에서 사용하려는 모델에 대한 계정 접근 권한이 있는지 확인하세요.

2. Chatflow에 AWS Bedrock 노드 추가.

Flowise Canvas에서 AWS Bedrock LLM 노드를 드래그하여 Chatflow에 놓으세요.

3. AWS Bedrock 입력 구성:
<figure><img src="../../../.gitbook/assets/image (2) (5).png" alt="" width="275"><figcaption><p>AWS Bedrock 노드</p></figcaption></figure>

* AWS Credential: 기존 AWS 자격증명을 선택하거나 새로운 자격증명을 생성하세요. 관련 IAM 사용자 또는 역할은 `bedrock:InvokeModel` 및 Chatflow의 기타 필요한 AWS 서비스에 대한 권한을 가져야 합니다.
* Region: Bedrock 모델을 사용할 수 있는 AWS 리전.
* Model Name: 대화형 AI용 AWS Bedrock 기초 모델.

4. Chatflow에서 AWS Bedrock 노드 연결.

다른 Chatflow 컴포넌트(입력 노드, 출력 노드, 메모리 노드 등)를 추가한 후, AWS Bedrock LLM 노드를 적절한 컴포넌트에 연결하여 Chatflow를 생성하세요.

AWS에 Flowise 배포에 대한 정보는 [AWS](../../../configuration/deployment/aws.md)를 참조하세요.


