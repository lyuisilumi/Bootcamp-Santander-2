# 🛡️ Phishing para Captura de Senhas do Facebook  

Este repositório documenta o processo de configuração e execução de uma simulação de phishing com o objetivo de capturar credenciais do Facebook. Este material é **estritamente para fins educacionais** e para demonstrar a importância de práticas de segurança cibernética robustas.  

---

## 🚀 Ferramentas Utilizadas  

- **Kali Linux**  
- **Setoolkit (Social Engineering Toolkit)**  

---

## ⚙️ Configurando o Phishing no Kali Linux  

### 1️⃣ Acesso como Root  
Execute o comando abaixo para obter permissões de administrador: sudo su

### 2️⃣ Iniciando o Setoolkit
Inicie o Setoolkit com o seguinte comando: setoolkit

### 3️⃣ Configuração do Ataque
Siga as etapas abaixo no Setoolkit:
    Tipo de Ataque: Social-Engineering Attacks
    Vetor de Ataque: Web Site Attack Vectors
    Método de Ataque: Credential Harvester Attack Method
    Método de Ataque: Site Cloner

### 4️⃣ Obtendo o Endereço da Máquina
Identifique o endereço IP da sua máquina executando: ifconfig

### 5️⃣ URL para Clonagem
Insira a URL do site a ser clonado quando solicitado pelo Setoolkit: http://www.facebook.com

### 📊 Resultados
Após a execução do ataque, todas as credenciais capturadas serão exibidas no terminal. Este exercício destaca a vulnerabilidade de sites a ataques de phishing e reforça a necessidade de práticas de segurança como:

-Verificação de URLs.
-Uso de autenticação de dois fatores.
-Educação sobre cibersegurança para identificar sites falsos.