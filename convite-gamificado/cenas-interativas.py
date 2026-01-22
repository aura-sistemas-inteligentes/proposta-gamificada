import streamlit as st

st.set_page_config(
    page_title="Cenas em Comum",
    page_icon="🎬",
    layout="centered"
)

if "cena" not in st.session_state:
    st.session_state.cena = 1

# CENA 1
if st.session_state.cena == 1:
    st.title("🎬 Cena 1 — Exposição de Carros")

    st.markdown("""
    Exposição de carros.

    Você de chapéu de palha e camiseta preta do evento.  
    Eu de blusa preta, short e camisa xadrez preta e vermelha amarrada na cintura.

    Entre motores, conversas soltas e olhares rápidos…  
    algo ficou registrado.
    """)

    if st.button("Continuar ▶️"):
        st.session_state.cena = 2

# CENA 2
elif st.session_state.cena == 2:
    st.title("🎬 Cena 2 — O Casamento")

    st.markdown("""
    Nosso casal de amigos, de branco.  

    Você de camisa azul claro.  
    Eu de vestido florido azul escuro.

    Outro cenário, outra vibe…  
    mas a sensação de que a conversa ainda tinha continuação.
    """)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Voltar"):
            st.session_state.cena = 1
    with col2:
        if st.button("Avançar ▶️"):
            st.session_state.cena = 3

# CENA 3
elif st.session_state.cena == 3:
    st.title("🎬 Cena 3 — Próximo Capítulo")

    escolha = st.radio(
        "Qual cena a gente grava agora?",
        [
            "☕ Café que vira horas",
            "🍻 Barzinho tranquilo",
            "🍦 Sorvete + caminhada",
            "🚗 Volta sem destino definido"
        ]
    )

    if st.button("Confirmar escolha 🎯"):
        st.session_state.escolha = escolha
        st.session_state.cena = 4

# CENA FINAL
elif st.session_state.cena == 4:
    st.title("🎬 Cena Final")

    st.success(f"Cena escolhida: {st.session_state.escolha}")

    st.markdown("""
    Dois encontros em cenários diferentes já aconteceram.  
    Agora é só levar isso do código pra vida real 😌

    **Quando a gente grava essa próxima cena?**
    """)

    if st.button("Recomeçar 🔁"):
        st.session_state.cena = 1
