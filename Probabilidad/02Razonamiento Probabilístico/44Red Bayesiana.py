from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Definir estructura de la red
modelo = BayesianNetwork([('Enfermedad','Fiebre'), ('Enfermedad','DolorCabeza')])

# Definir tablas de probabilidad condicional
cpd_enfermedad = TabularCPD(variable='Enfermedad', variable_card=2, values=[[0.99],[0.01]])
cpd_fiebre = TabularCPD(variable='Fiebre', variable_card=2,
                        values=[[0.8,0.2],[0.2,0.8]],
                        evidence=['Enfermedad'], evidence_card=[2])
cpd_dolor = TabularCPD(variable='DolorCabeza', variable_card=2,
                       values=[[0.7,0.3],[0.3,0.7]],
                       evidence=['Enfermedad'], evidence_card=[2])

# Añadir CPDs al modelo
modelo.add_cpds(cpd_enfermedad, cpd_fiebre, cpd_dolor)

# Inferencia
inferencia = VariableElimination(modelo)
resultado = inferencia.query(variables=['Enfermedad'], evidence={'Fiebre':1})

print("Probabilidad de enfermedad dado fiebre:", resultado)