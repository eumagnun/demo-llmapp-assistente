Passos para execução local ou no Cloud Shell:

 - Clonar esse repo
 - Criar ambiente virtual: python -m venv venv_demo_assistente
 - Ativar ambiente virtual: source venv_demo_assistente/bin/activate
 - Instalar dependências: pip install -r requirements.txt
 - Executar app: sh run.sh

Caso queira gerar uma imagem para implantação no Cloud Run:

 - Gerar imagem: docker build -t us-central1-docker.pkg.dev/{PROJECT-ID}/demo-assistente/meu-assistente-001 .
 - Enviar imagem para o Registry:  docker push us-central1-docker.pkg.dev/{PROJECT-ID}/demo-assistente/meu-assistente-001

Diagrama:
https://drive.google.com/file/d/1ygJNa1oVLtpjKr5IYkq-qTQSKjuZVTDm/view?usp=sharing&resourcekey=0-bnd9crKzIwkHubwwBVGQLg



