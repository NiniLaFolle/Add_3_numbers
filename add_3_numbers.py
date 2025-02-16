import streamlit as st
import random
import time

def generate_numbers():
    """Génère trois nombres entiers aléatoires entre 1 et 100."""
    return random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)

def main():
    st.title("Jeu de Calcul Mental")

    if "questions" not in st.session_state:
        st.session_state.questions = []
        st.session_state.current_index = 0
        st.session_state.correct_answers = 0
        st.session_state.start_time = None
        st.session_state.game_active = False

    # Choix du nombre de questions
    if not st.session_state.game_active:
        num_questions = st.selectbox("Choisissez le nombre de questions :", [10, 20, 50])
        if st.button("Commencer le jeu"):
            st.session_state.questions = [generate_numbers() for _ in range(num_questions)]
            st.session_state.current_index = 0
            st.session_state.correct_answers = 0
            st.session_state.start_time = time.time()
            st.session_state.game_active = True
            st.rerun()

    if st.session_state.game_active:
        if st.session_state.current_index < len(st.session_state.questions):
            a, b, c = st.session_state.questions[st.session_state.current_index]
            st.write(f"Question {st.session_state.current_index + 1}: {a} + {b} + {c} = ?")

            user_input = st.number_input("Votre réponse :", min_value=0, step=1, format="%d", key=f"input_{st.session_state.current_index}")

            if st.button("Valider"):
                correct_sum = a + b + c
                if user_input == correct_sum:
                    st.session_state.correct_answers += 1
                    st.success("Bonne réponse !")
                else:
                    st.error(f"Mauvaise réponse ! La bonne réponse était {correct_sum}.")

                st.session_state.current_index += 1
                st.rerun()
        else:
            # Fin du jeu
            total_time = time.time() - st.session_state.start_time
            st.success(f"Fin du jeu ! Score : {st.session_state.correct_answers}/{len(st.session_state.questions)}")
            st.write(f"Temps total : {total_time:.2f} secondes")

            if st.button("Rejouer"):
                st.session_state.game_active = False
                st.session_state.questions = []
                st.rerun()

if __name__ == "__main__":
    main()