import streamlit as st
from vertexai.generative_models import GenerativeModel, Part, FinishReason, Tool
import IPython
from IPython.display import display, Markdown
import base64
import io
import vertexai
import time
from vertexai.preview.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models

# escrevendo um título na página
st.set_page_config(page_title="Meu Assistente", page_icon="/logo-assistente.png")
cols = st.columns([65, 150])
with cols[0]:
    st.image("logo-assistente.png")
with cols[1]:
    st.title("Meu Assistente")
    st.caption("(Em desenvolvimento)")
import streamlit.components.v1 as components


project_id = "{PROJECT-ID}"  #Replace with your project ID
location = "us-central1"                    #Replace with your location
model_name = "gemini-1.5-flash-001"  #Replace with model name
#model_name = "gemini-1.5-pro-001"  #Replace with model name


vertexai.init(project=project_id, location=location)
tools = [
    Tool.from_retrieval(
        retrieval=generative_models.grounding.Retrieval(
            source=generative_models.grounding.VertexAISearch(datastore="projects/{PROJECT-ID}/locations/global/collections/default_collection/dataStores/{DATA-STORE-ID}"),
            disable_attribution=False,
        )
    ),
]


model = GenerativeModel(model_name,tools=tools,)

def generate(
        pergunta: str,
        max_output_tokens: int = 8192,
        temperature: int = 0.4,
        top_p: float = 0.4,
        stream: bool = False
):

    prompt_full =  """
                  <instrucoes>
                    - Você é Mia, uma assistente da empresa Tabajara
		            - Você é uma super especialista em análise de perfis de clientes e gestão financeira
                    - Fragmente a pergunta caso ela seja complexa e colete as informações correlacionadas
 		            - Sua missão é responder detalhadamente as dúvidas de colaboradores da empresa Tabajara sobre perfis de clientes e gestão financeira
                    - Não responda perguntas que fogem da sua missão
                    - Explique o passo a passo para elaboração da resposta
		            - SEJA GENTIL E EDUCADA NAS SUAS RESPOSTAS
		            - NÃO INVENTE CONTEÚDO
		            - Formate a resposta em markdown
                  </instrucoes>

                  <pergunta>
                    {pergunta}
                  </pergunta>
                  """
    prompt=[prompt_full.format(pergunta=pergunta)]
    responses = model.generate_content(
        prompt,
        generation_config={
            "max_output_tokens": max_output_tokens,
            "temperature": temperature,
            "top_p": top_p		
        },
        safety_settings={
          generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
          generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        },
        stream=stream
    )

    return responses


with st.form('my_form'):
    text = st.text_area('Por favor, informe sua dúvida:', '')
    submitted = st.form_submit_button('Enviar')
    if submitted:
       responses = generate(pergunta=text)
       st.info(responses.text)
