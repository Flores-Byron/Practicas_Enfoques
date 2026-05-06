import random

# Distribuciones
p_clima = {"Soleado":0.7, "Lluvioso":0.3}
p_trafico_dado_clima = {"Soleado":{"Intenso":0.2,"Ligero":0.8},
                        "Lluvioso":{"Intenso":0.8,"Ligero":0.2}}
p_tarde_dado_trafico = {"Intenso":0.9,"Ligero":0.1}

# Muestreo directo
def muestreo_directo(n=1000):
    muestras = []
    for _ in range(n):
        clima = random.choices(["Soleado","Lluvioso"], weights=[0.7,0.3])[0]
        trafico = random.choices(["Intenso","Ligero"], 
                                 weights=[p_trafico_dado_clima[clima]["Intenso"],
                                          p_trafico_dado_clima[clima]["Ligero"]])[0]
        tarde = random.random() < p_tarde_dado_trafico[trafico]
        muestras.append((clima,trafico,tarde))
    return muestras

# Muestreo por rechazo con evidencia Clima=Lluvioso
def muestreo_rechazo(n=5000):
    muestras_validas = []
    for _ in range(n):
        clima = random.choices(["Soleado","Lluvioso"], weights=[0.7,0.3])[0]
        trafico = random.choices(["Intenso","Ligero"], 
                                 weights=[p_trafico_dado_clima[clima]["Intenso"],
                                          p_trafico_dado_clima[clima]["Ligero"]])[0]
        tarde = random.random() < p_tarde_dado_trafico[trafico]
        if clima=="Lluvioso":  # evidencia
            muestras_validas.append((clima,trafico,tarde))
    return muestras_validas

# Ejecución
directo = muestreo_directo(1000)
rechazo = muestreo_rechazo(5000)

# Estimación posterior
p_tarde_directo = sum(1 for c,t,f in directo if c=="Lluvioso" and f)/sum(1 for c,t,f in directo if c=="Lluvioso")
p_tarde_rechazo = sum(1 for c,t,f in rechazo if f)/len(rechazo)

print("Posterior con muestreo directo:", round(p_tarde_directo,3))
print("Posterior con muestreo por rechazo:", round(p_tarde_rechazo,3))
