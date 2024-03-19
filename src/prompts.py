from langchain.prompts import PromptTemplate
import copy

template = """
    {context}

    {question}
    Answer:"""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])


def queryTemplate1():
    localPrompt = copy.copy(prompt)
    localPrompt.format(
        context="provide analysis. Focus on accuracy of the numbers. If possible write down numbered bullet points.",
        question="Give us some detailed information",
    )
    query = "Write Your query here"
    return localPrompt, query


def queryTemplate2():
    localPrompt = copy.copy(prompt)
    localPrompt.format(
        context="provide analysis. Focus on accuracy of the numbers. If possible write down numbered bullet points.",
        question="Give us some detailed information",
    )
    query = "Write Your query here"
    return localPrompt, query


def queryTemplate3():
    localPrompt = copy.copy(prompt)
    localPrompt.format(
        context="provide analysis.  Focus on accuracy of the numbers. If possible write down numbered bullet points.",
        question="Give us some detailed information",
    )
    query = "write your query here"
    return localPrompt, query




def summarizeChain():
    localPrompt = copy.copy(prompt)
    localPrompt.format(
        context="You are to read data and provide analysis. \
            Focus on accuracy of the numbers. If possible write down numbered bullet points.",
        question="Give us some detailed information",
    )
    return localPrompt
