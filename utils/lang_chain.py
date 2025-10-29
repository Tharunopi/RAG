from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

class chain:
    rag_query_techniques = {
        "multi_query": """You are an intelligent query refiner. Your task is to take an initial user query and generate multiple diverse but semantically relevant sub-queries that explore different possible interpretations or aspects of the user’s intent.

        Input:
        User query: {query}

        Output:
        A list of 3–7 refined queries that together capture the full meaning, context, and ambiguity of the original query.

        Guidelines:

        Maintain relevance to the original intent.

        Include possible synonyms, paraphrases, and related aspects.

        Avoid redundancy among the queries.

        Ensure clarity and completeness in each query.

        Output only the queries, and separate each query with a forward slash (/).

        Example:
        User Query: "Impacts of climate change on agriculture"
        Output:
        'How does global warming affect crop yields? / What are the effects of changing rainfall patterns on farming? / How is climate change influencing food production worldwide? / Adaptation strategies for farmers to climate change / Case studies on agriculture and climate change impacts'"""
    }
    def __init__(self, template:str="""Answer the following question from the user based on given context. If you don't know then say I don't know explicitly. Context: {context}, Question: {question}"""):
        self.template = template

    def update_template(self, new_template:str) -> bool:
        """Update the prompt template; returns True on success, False on failure."""
        try:
            self.template = new_template
            return True
        
        except Exception as e:
            print(f"chain -> update_template: {e}")
            return False
        
    def get_template_string(self) -> str | None:
        """Return the current template string, or None on error."""
        try:
            return self.template

        except Exception as e:
            print(f"chain -> get_template_string: {e}")
            return None
        
    def get_chain(self) -> object:
        """Build and return the composed chain
            PromptTemplate.from_template(template) | st.session_state["large_language_model"] | StrOutputParser().
            Requires st.session_state["large_language_model"] to be initialized; returns None on error."""
        try: 
            return PromptTemplate.from_template(self.template) | st.session_state["large_language_model"] | StrOutputParser()
        
        except Exception as e:
            print(f"chain -> get_chain: {e}")
            return None
        
    def get_chain_for_construction(self, method:str) -> object:
        """Build a chain for query construction using a predefined technique.

        Composes a chain that:
        - formats a technique-specific prompt template,
        - invokes the LLM stored in st.session_state["large_language_model"],
        - parses the string output,
        - and finally splits the result on '/' to yield a list-like output.

        Args:
            method: Key into rag_query_techniques specifying which construction
                template to use (e.g., "multi_query").

        Returns:
            The composed chain object, or None on error.
        """
        try:
            global rag_query_techniques

            template = rag_query_techniques[method]
            chain = PromptTemplate.from_template(template) | st.session_state["large_language_model"] | StrOutputParser() | (lambda x: x.split("/"))
            return chain

        except Exception as e:
            print(f"Error: get_chain_for_construction -> {e}")