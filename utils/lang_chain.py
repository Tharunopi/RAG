from langchain_core.prompts import PromptTemplate
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

class chain:
    """
    Wrapper for constructing a prompt→model→string LCEL chain using langchain_core and Streamlit.

    Args:
        template: Initial prompt template string with {context} and {question} placeholders.

    Attributes:
        template: The current prompt template.

    Methods:
        update_template(new_template): Update the prompt template; returns True on success, False on failure.
        get_template_string(): Return the current template string, or None on error.
        get_chain(): Build and return the composed chain
            PromptTemplate.from_template(template) | st.session_state["large_language_model"] | StrOutputParser().
            Requires st.session_state["large_language_model"] to be initialized; returns None on error.
"""
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
        
    def get_chain(self) -> PromptTemplate:
        """Build and return the composed chain
            PromptTemplate.from_template(template) | st.session_state["large_language_model"] | StrOutputParser().
            Requires st.session_state["large_language_model"] to be initialized; returns None on error."""
        try: 
            return PromptTemplate.from_template(self.template) | st.session_state["large_language_model"] | StrOutputParser()
        
        except Exception as e:
            print(f"chain -> get_chain: {e}")
            return None