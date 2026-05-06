from pgmpy.models import BayesianNetwork

# Definir estructura
modelo = BayesianNetwork([
    ('Genetica','Enfermedad'),
    ('Enfermedad','Fiebre'),
    ('Enfermedad','DolorCabeza'),
    ('Virus','Fiebre')
])

# Obtener el Manto de Markov de "Enfermedad"
manto = modelo.get_markov_blanket('Enfermedad')
print("Manto de Markov de Enfermedad:", manto)
