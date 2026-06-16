# Vectara

## Quickstart Tutorial

{% embed url="https://www.youtube.com/watch?v=rBqpvFcD5XY" %}

## Prerequisite

1. Register an account for [Vectara](https://vectara.com/integrations/flowise)
2. Click **Create Corpus**

<figure><img src="../../../.gitbook/assets/Vectara/1.png" alt=""><figcaption></figcaption></figure>

Name the corpus to be created and click **Create Corpus** then wait for the corpus to finish setting up.

## 설정

1. Click on the **"Access Control"** tab in the corpus view

<figure><img src="../../../.gitbook/assets/Vectara/2.png" alt=""><figcaption></figcaption></figure>

2. Click on the **"Create API Key"** button, choose a name for the API key and pick the **QueryService & IndexService** option

<figure><img src="../../../.gitbook/assets/Vectara/3.png" alt=""><figcaption></figcaption></figure>

3. Click **Create** to create the API key
4. Get your **Corpus ID, API Key, and Customer ID** by clicking the down-arrow under "copy" for your new API key:

<figure><img src="../../../.gitbook/assets/Vectara/4.png" alt=""><figcaption></figcaption></figure>

5. Back to Flowise canvas, and create your chatflow. Click **Create New** from the Credentials dropdown ane enter your Vectara credentials.

<figure><img src="../../../.gitbook/assets/Vectara/5.png" alt="" width="500"><figcaption></figcaption></figure>

6. Enjoy!

## Vectara Query 매개변수

For finer control over the Vectara query 매개변수, click on "**Additional 매개변수**" and then you can update the following 매개변수 from their default:

* Metadata Filter: Vectara supports meta-data filtering. To use [filtering](https://docs.vectara.com/docs/common-use-cases/filtering-by-metadata/filter-overview), ensure that metadata fields you want to filter by are defined in your Vectara corpus.
* "Sentences before" and "Sentences after": these control how many sentences before/after the matching text are returned as results from the Vectara retrieval engine
* Lambda: defines the behavior of [hybrid search](https://docs.vectara.com/docs/learn/hybrid-search) in Vectara
* Top-K: how many results to return from Vectara for the query
* MMR-K: number of results to use for [MMR](https://docs.vectara.com/docs/api-reference/search-apis/reranking#maximal-marginal-relevance-mmr-reranker) (max marginal relvance)

<figure><img src="../../../.gitbook/assets/Vectara/6.png" alt="" width="500"><figcaption></figcaption></figure>

## Resources

* [LangChain JS Vectara Blog Post](https://blog.langchain.dev/langchain-vectara-better-together/)
* [5 Reasons to Use Vectara's Langchain Integration Blog Post](https://vectara.com/5-reasons-to-use-vectaras-langchain-integration/)
* [Max Marginal Relevance in Vectara](https://vectara.com/blog/get-diverse-results-and-comprehensive-summaries-with-vectaras-mmr-reranker/)
* [Vectara Boomerang embedding model Blog Post](https://vectara.com/introducing-boomerang-vectaras-new-and-improved-retrieval-model/)
* [Detecting Hallucination with Vectara's HHEM](https://vectara.com/blog/cut-the-bull-detecting-hallucinations-in-large-language-models/)
