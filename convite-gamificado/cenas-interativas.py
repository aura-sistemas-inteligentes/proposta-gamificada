import streamlit as st
import urllib.parse

st.set_page_config(
    page_title="Cenas em Comum",
    page_icon="🎬",
    layout="centered"
)

# Configuração - COLOQUE SEU NÚMERO AQUI (com código do país, sem + ou espaços)
# Exemplo: "5511999999999" para Brasil
MEU_WHATSAPP = "5564984207232"  # ⚠️ ALTERE AQUI!

if "cena" not in st.session_state:
    st.session_state.cena = 1

# CENA 1
if st.session_state.cena == 1:
    st.title("🎬 Cena 1 — Exposição de Carros Antigos")

    st.markdown("""
    Uma tarde de sol forte, carros reluzentes, pessoas circulando.
    
    Você de chapéu de palha e camiseta do evento, explicando detalhes técnicos.  
    Eu de blusa preta, short e camisa xadrez amarrada na cintura, fingindo entender de motores.

    Entre conversas aleatórias e risadas despretensiosas…  
    **um olhar que durou mais que o necessário.**
    
    E a chuva caiu como se não ouvesse amanhã.            

    Algo ali já dizia: "a gente se vê de novo".
    """)

    if st.button("Continuar ▶️", use_container_width=True):
        st.session_state.cena = 2
        st.rerun()

# CENA 2
elif st.session_state.cena == 2:
    st.title("🎬 Cena 2 — O Casamento")

    st.markdown("""
    Algumas semana depois. Um casamento, nossos amigos de branco, felicidade no ar.
    
    Você de camisa azul claro, elegante sem esforço.  
    Eu de vestido florido azul escuro, tentando não tropeçar no próprio pé.

    A música tocava, as pessoas conversavam, mas quando nossos olhos se cruzaram de novo…  
    **foi como se o universo dissesse: "tá vendo? Eu avisei".**
    
    Conversamos, rimos, e ficou aquela sensação:  
    *"Por que a gente não faz isso mais vezes? Por que não estender?"*
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Voltar", use_container_width=True):
            st.session_state.cena = 1
            st.rerun()
    with col2:
        if st.button("Avançar ▶️", use_container_width=True):
            st.session_state.cena = 3
            st.rerun()

# CENA 3
elif st.session_state.cena == 3:
    st.title("🎬 Cena 3 — Próximo Capítulo")

    st.markdown("""
    Duas cenas já aconteceram. Dois encontros que pareciam casuais.
    
    Agora, que tal a gente escrever a próxima cena **de propósito**?
    """)

    escolha = st.radio(
        "**Qual cena a gente grava agora?**",
        [
            "☕ Café que vira horas — aquele papo que não tem hora pra acabar",
            "🍻 Barzinho com petiscos — cerveja gelada e conversa boa",
            "🍦 Sorvete + caminhada — andar sem rumo, só curtindo a companhia",
            "🚗 Volta sem destino — música boa, janela aberta, pra onde der",
            "🎬 Você escolhe — me surpreende!"
        ]
    )

    st.markdown("---")
    
    #horario = st.radio(
     #   "**Qual horário combina mais com você?**",
      #  [
       #     "☀️ Manhã (9h-12h) — começar o dia bem",
        #    "🌤️ Tarde (14h-17h) — aquele break no meio do dia",
         #   "🌅 Fim de tarde (17h-19h) — pegar o pôr do sol",
          #  "🌙 Noite (19h-22h) — quando o dia acalma"
       # ]
    #)
    if st.button("Confirmar escolha 🎯", use_container_width=True):
        st.session_state.escolha = escolha
       # st.session_state.horario = horario
        st.session_state.cena = 4
        st.rerun()

# CENA FINAL
elif st.session_state.cena == 4:
    st.title("🎬 Cena Final — Seu Momento")

    st.success("✨ Escolhas registradas!")

    st.markdown(f"""
    **Cena escolhida:** {st.session_state.escolha}  
    """)
# **Horário preferido:** {st.session_state.horario}
    st.markdown("---")

    st.markdown("""
    Dois encontros em cenários diferentes já aconteceram.  
    Agora é só levar isso do código pra vida real 😌

    """)

   # nome = st.text_input("Digite seu nome:", placeholder="Ex: João")

    if nome:
        st.markdown("---")
        st.markdown("### 💬 Pronto para enviar sua resposta?")
        
        # Monta a mensagem do WhatsApp
        mensagem = f"""Oi Michelle! 😊

Acabei de completar as cenas do convite!


Que tal {st.session_state.escolha}

Bora marcar? 🎬"""
        
        # Codifica a mensagem para URL
        mensagem_encoded = urllib.parse.quote(mensagem)
        
        # Cria o link do WhatsApp
        whatsapp_link = f"https://wa.me/{MEU_WHATSAPP}?text={mensagem_encoded}"
        
        # Botão que abre o WhatsApp
        st.markdown(f"""
        <a href="{whatsapp_link}" target="_blank">
            <button style="
                background-color: #25D366;
                color: white;
                padding: 15px 32px;
                text-align: center;
                font-size: 18px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                width: 100%;
                font-weight: bold;
            ">
                📱 Enviar resposta pelo WhatsApp
            </button>
        </a>
        """, unsafe_allow_html=True )
        
        st.markdown("")
        
        if st.button("🔁 Recomeçar", use_container_width=True):
            st.session_state.cena = 1
            st.session_state.clear()
            st.rerun()
