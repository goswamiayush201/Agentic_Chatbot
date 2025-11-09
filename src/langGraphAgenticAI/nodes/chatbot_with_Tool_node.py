from src.langGraphAgenticAI.state.state import State

class ChatbotWithToolNode:
    """
    Chatbot Logic enhanced with tool integration.
    """
    def __init__(self,model):
        self.llm=model

    def process(self, state:State):
        """
        Processess the input state and enerates a response with tool integration."""    

        user_input=state['message'][-1] if state['message'] else ""
        llm_response=f"Tool integration for : '{user_input}"

        # Simulate tool-specific logic
        tool_response=f"Tool integration for : '{user_input}'"

        return {"message": [llm_response,tool_response]}
    

    def create_chatbot(self,tools):
        """
        Returns a chatbot node function"""

        llm_with_tools=self.llm.bind_tools(tools)
        def chatbot_node(state:State):
            """
            Chatbot logic for processing the inpt state and returning a response.
            """
            return {"messages": [llm_with_tools.invoke(state["messages"])]}
        return chatbot_node