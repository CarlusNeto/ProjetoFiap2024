# Navegue até o diretório do projeto
cd projeto_data_science

# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
.\venv\Scripts\activate

# Se o comando acima falhar, tente:
# .\venv\Scripts\Activate.ps1

# Se ainda houver problemas, você pode precisar alterar a política de execução:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Seu prompt deve mudar para indicar que o ambiente virtual está ativo
# Agora, instale as dependências
pip install -r requirements.txt

# Verifique as instalações
pip list

# Para desativar o ambiente virtual quando terminar
deactivate
