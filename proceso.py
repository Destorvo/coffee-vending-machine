# from automata.fa.dfa import DFA
# class ProcesoAutomata:
#     def __init__(self, entrada):
#         self.entrada = entrada

#     def validarCadena(self):
#         dfa = DFA(
#             states={'q0', 'q1', 'q2', 'q3', 'q4'},
#             input_symbols={'h','o','l','a'},
#             transitions={
#                 'q0': {'h': 'q1', 'o': 'q0', 'l': 'q0', 'a': 'q0'},
#                 'q1': {'h': 'q0', 'o': 'q2', 'l': 'q0', 'a': 'q0'},
#                 'q2': {'h': 'q1', 'o': 'q0', 'l': 'q3', 'a': 'q0'},
#                 'q3': {'h': 'q1', 'o': 'q0', 'l': 'q0', 'a': 'q4'},
#                 'q4': {'h': 'q0', 'o': 'q0', 'l': 'q0', 'a': 'q4'}
#             },
#             initial_state='q0',
#             final_states={'q4'}
#         )
#         try:
#             if dfa.accepts_input(self.entrada):
#                     print('Accepted')
#             else:
#                     print('Rejected')
#         except KeyboardInterrupt:
#             print('XD')
            
        

