import streamlit as st
import time
from components.utils.model_mappings import (
    Provider,
    get_all_provider_names,
    get_models_for_provider_name,
    get_api_name_from_strings,
)

def render_authentication_fields(provider):
    """Render authentication fields based on the selected provider."""
    auth_fields = {}
    
    if provider == Provider.AWS.value:
        # AWS requires access key, secret key, session token, and region
        auth_fields["aws_access_key_id"] = st.text_input("AWS Access Key ID", type="password")
        auth_fields["aws_secret_access_key"] = st.text_input("AWS Secret Access Key", type="password")
        auth_fields["aws_session_token"] = st.text_input("AWS Session Token", type="password")
        auth_fields["aws_region"] = st.selectbox(
            "AWS Region",
            ["us-east-1", "us-east-2", "us-west-1", "us-west-2", "eu-west-1"]
        )
    elif provider == Provider.ANTHROPIC.value:
        # Anthropic requires only an API key
        auth_fields["anthropic_api_key"] = st.text_input("Anthropic API Key", type="password")
    
    # Placeholder for adding more providers in the future
    # elif provider == Provider.OPENAI.value:
    #     auth_fields["openai_api_key"] = st.text_input("OpenAI API Key", type="password")
    
    return auth_fields

def render_thinking_section(thinking_content=""):
    """Render a collapsible area for model thinking/reasoning."""
    with st.expander("Model Thinking Process", expanded=False):
        st.write(thinking_content or "Thinking process will appear here...")

def main():
    st.set_page_config(
        page_title="LLM TPS Counter",
        page_icon="=�",
        layout="wide"
    )
    
    st.title("LLM TPS Counter")
    st.write("Test the tokens per second (TPS) performance of different LLM providers and models.")
    
    # Get all available providers
    providers = get_all_provider_names()
    
    # Provider selection dropdown
    selected_provider = st.selectbox(
        "Select Provider",
        providers,
        key="provider_select"
    )
    
    # Get models for the selected provider
    models = get_models_for_provider_name(selected_provider)
    
    # Model selection dropdown
    selected_model = st.selectbox(
        "Select Model",
        models,
        key="model_select"
    )
    
    # Display the model ID for the selected provider and model
    model_id = get_api_name_from_strings(selected_provider, selected_model)
    if model_id:
        st.caption(f"Model ID: {model_id}")
    
    # Render authentication fields based on provider
    st.subheader("Authentication")
    auth_fields = render_authentication_fields(selected_provider)
    
    # User message input
    st.subheader("Test Message")
    user_message = st.text_area(
        "Enter a message to send to the LLM",
        height=150,
        placeholder="Hello, I'm testing your TPS performance. Please provide a detailed response about..."
    )
    
    # Test button with TPS calculation
    if st.button("Test LLM TPS"):
        if not user_message.strip():
            st.error("Please enter a message to test.")
            return
        
        # Check if authentication fields are filled
        auth_missing = False
        for key, value in auth_fields.items():
            if not value:
                st.error(f"Please provide {key.replace('_', ' ').title()}")
                auth_missing = True
        
        if auth_missing:
            return
        
        # Placeholder for actual LLM call implementation
        # This would be replaced with actual API calls to the selected provider
        with st.spinner("Generating response..."):
            # Create placeholder for streaming response
            thinking_placeholder = st.empty()
            response_placeholder = st.empty()
            
            # Simulate streaming response for demonstration
            full_response = ""
            thinking = "Analyzing query... Formulating response strategy... Retrieving relevant information..."
            
            # Display thinking process in the collapsible area
            with thinking_placeholder.container():
                render_thinking_section(thinking)
            
            # Simulate streaming tokens with tracking for TPS calculation
            start_time = time.time()
            token_count = 0
            
            for i in range(50):
                # Simulate token generation
                new_token = "This is a simulated response token. " if i % 5 == 0 else "More content... "
                full_response += new_token
                token_count += len(new_token.split())
                
                # Update the displayed response
                response_placeholder.markdown(full_response)
                
                # Simulate time delay between tokens
                time.sleep(0.1)
            
            end_time = time.time()
            elapsed_time = end_time - start_time
            
            # Calculate and display TPS
            if elapsed_time > 0:
                tps = token_count / elapsed_time
                st.success(f"Response complete!")
                st.metric("Tokens Per Second (TPS)", f"{tps:.2f}")
                st.metric("Total Tokens", token_count)
                st.metric("Time Elapsed", f"{elapsed_time:.2f}s")

main()