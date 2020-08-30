import clases

persona = clases.persona()
persona.setNombre("Marcos")
persona.setApellidos("Rivera")
persona.setAltura("180 cm")
persona.setEdad("19 Años")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}")
print(persona.hablar())

print("-----------------------------")

informatico = clases.Informatico()
informatico.setNombre("Victor")
informatico.setApellidos("Robles")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)

print("-----------------------------")

tecnico = clases.TecnicoRedes()
tecnico.setNombre("Paco")
print(tecnico.auditarRedes, tecnico.getNombre(), tecnico.getLenguajes())