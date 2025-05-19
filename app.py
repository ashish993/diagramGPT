import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import AzureChatOpenAI
from code_editor import code_editor

# Page setting
st.set_page_config(layout="wide")

# Azure OpenAI Configuration with error handling
try:
    azure_endpoint = st.secrets["AZURE_OPENAI_ENDPOINT"]
    azure_api_key = st.secrets["AZURE_OPENAI_API_KEY"]
    deployment_name = st.secrets["AZURE_OPENAI_DEPLOYMENT"]
    model_name = st.secrets["AZURE_OPENAI_MODEL_NAME"]
    api_version = "2025-01-01-preview"  # Using the specified API version
    
    # Initialize Azure OpenAI with LangChain
    llm = AzureChatOpenAI(
        azure_deployment=deployment_name,
        openai_api_version=api_version,
        azure_endpoint=azure_endpoint,
        api_key=azure_api_key,
        model_name=model_name,  # Explicitly set model name for token counting
        temperature=0,
        max_retries=3,  # Add retry logic for reliability
        request_timeout=30  # Add timeout for better error handling
    )
except Exception as e:
    st.error(f"Error initializing Azure OpenAI: {str(e)}")
    st.stop()

# ============== LANGCHAIN CONFIG SECTION ========================
output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a solution architecture expert with over 15 years of experience working with both AWS and Azure cloud services. You excel at creating detailed architecture diagrams using advanced visualization techniques including clusters, directional flows, and edge styling."),
    ("user", '''
# CHARACTER
You have the following skills {{SKILLS}}, and your answer should adhere to the constraints {{CONSTRAINTS}}. Based on the following user input, choose the corresponding {{SKILLS}} and process it. Keep your answer as simple as possible.
User input: {user_request}

# SKILLS
## SKILL 1: Converting the user's workflow into a Diagram
Steps:
- Detect if the user is asking about Azure or AWS based on their input
- Map components in the workflow to corresponding components in the appropriate cloud provider's stack
- Organize related components into clusters when appropriate
- Use appropriate node connections (>>, <<, -) to show data flow direction
- Use edges with labels and styling where needed to clarify relationships
- Focus on creating clear and visually appealing diagrams
Response Format:
- The response must follow the TYPE1 format

## SKILL 2: Finding and advising a solution based on the user's needs
Steps:
- Detect if the user is asking about Azure or AWS based on their input
- Think step-by-step to provide the best solution using the appropriate cloud provider's services
- Group related services into logical clusters
- Show data flow between services using appropriate directional operators
- Use edge styling to indicate different types of connections (e.g., sync vs async)
- Focus on the final result, don't need to show immediate thinking steps
Response Format:
- The response must follow the TYPE2 format.

## SKILL 3: Show how to use specific cloud services
Steps:
- Show the best practices of the service along with a useful sample workflow
- Use clusters to group related components
- Use edge labels to describe interactions between services
Response Format:
- The response must follow the TYPE2 format.

# CONSTRAINTS

## CONSTRAINT 1: Responses in TYPE1 format
- Your response contains only the Python code

## CONSTRAINT 2: Responses in TYPE2 format
- Short explanation and conclusion with the Python code at the bottom.

## CONSTRAINT 3: Diagram creation method
- Use the Python diagram library to create the code
- Choose imports based on the cloud provider (diagrams.aws.* for AWS, diagrams.azure.* for Azure)
- Always import needed components directly from their modules
- Make use of Cluster class to group related components
- Use appropriate flow operators:
  * >> for left to right flow
  * << for right to left flow
  * - for undirected connections
- Use Edge class with labels and styling where appropriate
- Support diagram direction options (TB, BT, LR, RL)
- Group similar nodes into lists for cleaner connections
- To avoid errors related to incorrect class imports, refer to:
  - For AWS services: {aws_knowledge}
  - For Azure services: {azure_knowledge}
- The generated code should only create the diagram, do not include any Streamlit display code.

EXAMPLE
```python
from diagrams import Cluster, Diagram, Edge
from diagrams.azure.compute import AppServices  # or diagrams.aws.compute.EC2 for AWS
from diagrams.azure.database import SQLDatabases  # or diagrams.aws.database.RDS for AWS
from diagrams.azure.network import LoadBalancers

# Create the diagram using `diagrams` lib
with Diagram("Web Application", show=False, filename="diagram_temp"):
    lb = LoadBalancers("Load Balancer")
    
    with Cluster("Application Tier"):
        apps = [
            AppServices("App 1"),
            AppServices("App 2"),
            AppServices("App 3")
        ]
    
    with Cluster("Database Tier"):
        primary = SQLDatabases("Primary")
        replica = SQLDatabases("Replica")
        primary - Edge(color="brown", style="dashed") - replica

    lb >> apps >> primary
```

'''
    )])

# Load cloud service knowledge
loader_aws = TextLoader('aws.knowledge')
aws_knowledge = loader_aws.load()[0].page_content

loader_azure = TextLoader('azure.knowledge')
azure_knowledge = loader_azure.load()[0].page_content

chain = prompt | llm | output_parser

# ============== MANAGE SESSION STATE ========================
if "current_code" not in st.session_state:
    st.session_state.current_code = None
if "response" not in st.session_state:
    st.session_state.response = None


# ============== MAIN FUNCTIONS ========================
# @st.cache_data
def invoke(user_request):
    """Call chatgpt to process user input, store the response in cache memory"""
    response = chain.invoke({"aws_knowledge": aws_knowledge, "azure_knowledge": azure_knowledge, "user_request": user_request})
    return response

def extract_main_content(text):
    """Extract the main content from the given text"""
    # print(f"DEBUG:RESPONSE:{text}")
    code_start = text.find("```python")

    if code_start != -1:
        main_content = text[0:code_start].strip()
        if len(main_content) == 0:
            return None
        else:
            return main_content
    else:
        return text

def extract_diagram_code(text):
    """Extract the diagram code from the given text"""
    print(f"DEBUG:RESPONSE:{text}")
    code_start = text.find("```python")

    if code_start != -1:
        code_end = text.find("```", code_start + 1)

        if code_start != -1 and code_end != -1:
            code_to_execute = text[code_start + len("```python"):code_end].strip()
            return code_to_execute
        else:
            st.write("There is no Python code in DIAGRAM part.")
    else:
        st.write("There is no DIAGRAM part")
    return None

# ============== MAIN PAGE SECTION ========================
btn_settings_editor_btns = [{
    "name": "Generate Diagram",
    "feather": "RefreshCw",
    "primary": True,
    "alwaysOn": True,
    "hasText": True,
    "showWithIcon": True,
    "commands": ["submit"],
    "style": {"top": "0rem", "right": "0.4rem"}
  }]

def main_page():
    st.header("👨‍💻 Chat with Diagram Agent")
    user_request = st.text_area(label="What is your Problem Statement?",
                                value="Mobile application -> DNS ->  Load Balancer -> 3 web services -> 2 Database servers ")

    clicked = st.button(" Generate Code!", type="primary")
    if clicked:
        with st.spinner("I'm thinking...wait a minute!"):
            response = invoke(user_request)
            st.session_state.response = response
            st.session_state.current_code = extract_diagram_code(response)

    code = st.session_state.current_code
    if code is not None:
        try:
            # Remove any st.image calls from the generated code
            code = code.replace('st.image("diagram_temp.png")', '').replace("st.image('diagram_temp.png')", '')
            
            # Execute the code silently to generate the diagram
            exec(code)
            
            # Display the diagram
            st.image("diagram_temp.png")
        except Exception as e:
            st.error(f"Error generating diagram: {str(e)}")


if __name__ == '__main__':
    main_page()
