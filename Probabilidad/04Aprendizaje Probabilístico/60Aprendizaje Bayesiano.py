# Probabilidades a priori
p_spam = 0.4
p_no_spam = 0.6

# Verosimilitudes (probabilidad de ver la palabra "oferta")
p_oferta_dado_spam = 0.8
p_oferta_dado_no_spam = 0.2

# Evidencia: aparece la palabra "oferta"
p_oferta = p_spam*p_oferta_dado_spam + p_no_spam*p_oferta_dado_no_spam

# Posterior
p_spam_dado_oferta = (p_oferta_dado_spam*p_spam) / p_oferta
p_no_spam_dado_oferta = (p_oferta_dado_no_spam*p_no_spam) / p_oferta

print("Probabilidad Spam dado 'oferta':", round(p_spam_dado_oferta,3))
print("Probabilidad No Spam dado 'oferta':", round(p_no_spam_dado_oferta,3))
