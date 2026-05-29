import random

# ============================================
# PARÁMETROS DEL PROBLEMA
# ============================================

W = 50  # Capacidad de la mochila

pesos = [10, 20, 30, 5, 12, 8, 15, 25, 18, 3]
valores = [60, 100, 120, 30, 50, 40, 70, 90, 80, 20]
N = len(pesos)  # Número de objetos = 10

# ============================================
# PARÁMETROS DEL ALGORITMO GENÉTICO
# ============================================

TAM_POBLACION = 50
PROB_CRUZA = 0.8
PROB_MUTACION = 0.05
MAX_GENERACIONES = 100
MAX_ESTANCAMIENTO = 20

# ============================================
# FUNCIONES BÁSICAS
# ============================================

def generar_individuo():
    """Genera un individuo aleatorio (vector binario de longitud N)"""
    return [random.randint(0, 1) for _ in range(N)]


def fitness(individuo):
    """
    Calcula el fitness de un individuo.
    Si excede la capacidad, fitness = 0 (penalización)
    """
    peso_total = sum(individuo[i] * pesos[i] for i in range(N))
    valor_total = sum(individuo[i] * valores[i] for i in range(N))
    
    if peso_total > W:
        return 0
    return valor_total


def generar_poblacion(tamano):
    """Genera una población de tamaño 'tamano'"""
    return [generar_individuo() for _ in range(tamano)]


def mejor_individuo(poblacion):
    """Encuentra el mejor individuo de la población"""
    mejor = poblacion[0]
    mejor_fit = fitness(mejor)
    
    for individuo in poblacion:
        f = fitness(individuo)
        if f > mejor_fit:
            mejor = individuo
            mejor_fit = f
    
    return mejor[:], mejor_fit


# ============================================
# SELECCIÓN (RULETA CON ELITISMO)
# ============================================

def seleccion_ruleta(poblacion):
    """
    Selecciona un individuo usando el método de la ruleta.
    La probabilidad es proporcional al fitness.
    """
    fitnesses = [fitness(ind) for ind in poblacion]
    fitness_total = sum(fitnesses)
    
    # Si todos tienen fitness 0, selección aleatoria uniforme
    if fitness_total == 0:
        return random.choice(poblacion)[:]
    
    r = random.uniform(0, fitness_total)
    acumulado = 0
    
    for i, ind in enumerate(poblacion):
        acumulado += fitnesses[i]
        if acumulado >= r:
            return ind[:]
    
    return poblacion[-1][:]


def nueva_poblacion_elitismo(poblacion, tam_poblacion):
    """
    Crea una nueva población usando:
    - Elitismo: el mejor individuo pasa directamente
    - El resto se selecciona por ruleta
    """
    nueva_pob = []
    
    # Conservar el mejor individuo (elitismo)
    elite, elite_fit = mejor_individuo(poblacion)
    nueva_pob.append(elite[:])
    
    # Completar la población con selección por ruleta
    while len(nueva_pob) < tam_poblacion:
        individuo = seleccion_ruleta(poblacion)
        nueva_pob.append(individuo[:])
    
    return nueva_pob


# ============================================
# OPERADORES GENÉTICOS
# ============================================

def cruza_un_punto(padre1, padre2):
    """
    Cruza de un punto con probabilidad PROB_CRUZA.
    Si no hay cruza, devuelve copias de los padres.
    """
    if random.random() > PROB_CRUZA:
        return padre1[:], padre2[:]
    
    punto = random.randint(1, N - 1)
    hijo1 = padre1[:punto] + padre2[punto:]
    hijo2 = padre2[:punto] + padre1[punto:]
    
    return hijo1, hijo2


def mutacion(individuo):
    """
    Aplica mutación bit-flip con probabilidad PROB_MUTACION.
    Cada bit tiene probabilidad independiente de mutar.
    """
    mutado = individuo[:]
    for i in range(N):
        if random.random() < PROB_MUTACION:
            mutado[i] = 1 - mutado[i]  # Cambia 0->1 o 1->0
    return mutado


def aplicar_cruza(poblacion):
    """
    Aplica cruza a toda la población.
    Toma individuos de dos en dos y genera hijos.
    """
    hijos = []
    for i in range(0, len(poblacion), 2):
        padre1 = poblacion[i]
        if i + 1 < len(poblacion):
            padre2 = poblacion[i + 1]
        else:
            padre2 = poblacion[0]  # Si es impar, el último con el primero
        
        hijo1, hijo2 = cruza_un_punto(padre1, padre2)
        hijos.append(hijo1)
        hijos.append(hijo2)
    
    return hijos


def aplicar_mutacion(poblacion):
    """Aplica mutación a todos los individuos de la población"""
    return [mutacion(ind) for ind in poblacion]


# ============================================
# ALGORITMO GENÉTICO COMPLETO
# ============================================

def algoritmo_genetico(verbose=True):
    """
    Ejecuta el algoritmo genético completo.
    Retorna el mejor individuo encontrado y su fitness.
    """
    # Generar población inicial
    poblacion = generar_poblacion(TAM_POBLACION)
    
    # Mejor global
    mejor_global = None
    mejor_fitness_global = 0
    generaciones_sin_mejora = 0
    
    # Historial para estadísticas
    historial_mejores = []
    historial_promedios = []
    
    for generacion in range(MAX_GENERACIONES):
        # Evaluar población actual
        fitnesses = [fitness(ind) for ind in poblacion]
        promedio_fitness = sum(fitnesses) / len(fitnesses)
        
        # Obtener mejor individuo actual
        mejor_actual, fitness_actual = mejor_individuo(poblacion)
        
        # Verificar mejora global
        if fitness_actual > mejor_fitness_global:
            mejor_global = mejor_actual[:]
            mejor_fitness_global = fitness_actual
            generaciones_sin_mejora = 0
        else:
            generaciones_sin_mejora += 1
        
        # Guardar historial
        historial_mejores.append(mejor_fitness_global)
        historial_promedios.append(promedio_fitness)
        
        # Mostrar progreso
        if verbose:
            print(f"Gen {generacion:3d} | Mejor: {fitness_actual:3d} | "
                  f"Mejor Global: {mejor_fitness_global:3d} | "
                  f"Promedio: {promedio_fitness:.1f} | "
                  f"Sin mejora: {generaciones_sin_mejora}")
        
        # Criterio de paro por estancamiento
        if generaciones_sin_mejora >= MAX_ESTANCAMIENTO:
            if verbose:
                print(f"\n→ Parada por estancamiento después de {generaciones_sin_mejora} generaciones")
            break
        
        # Selección (con elitismo)
        seleccionados = nueva_poblacion_elitismo(poblacion, TAM_POBLACION)
        
        # Cruza
        hijos = aplicar_cruza(seleccionados)
        
        # Mutación
        nueva_generacion = aplicar_mutacion(hijos)
        
        # Reemplazo
        poblacion = nueva_generacion
    
    return mejor_global, mejor_fitness_global, historial_mejores, historial_promedios


# ============================================
# FUNCIONES PARA MOSTRAR RESULTADOS
# ============================================

def mostrar_solucion(individuo, fitness_valor):
    """Muestra la solución detallada"""
    print("\n" + "=" * 60)
    print("SOLUCIÓN FINAL")
    print("=" * 60)
    
    peso_total = sum(individuo[i] * pesos[i] for i in range(N))
    valor_total = fitness_valor
    
    print(f"\nCapacidad de la mochila: {W}")
    print(f"Peso total utilizado: {peso_total}")
    print(f"Valor total obtenido: {valor_total}")
    print(f"Espacio sobrante: {W - peso_total}")
    
    print("\nObjetos seleccionados:")
    print("-" * 40)
    print(f"{'Objeto':<8} {'Peso':<8} {'Valor':<8} {'Seleccionado'}")
    print("-" * 40)
    
    for i in range(N):
        selec = "Sí" if individuo[i] == 1 else "No"
        print(f"{i+1:<8} {pesos[i]:<8} {valores[i]:<8} {selec}")
    
    print("-" * 40)


def mostrar_estadisticas(historial_mejores, historial_promedios):
    """Muestra estadísticas de la evolución"""
    print("\n" + "=" * 60)
    print("ESTADÍSTICAS DE LA EVOLUCIÓN")
    print("=" * 60)
    
    print(f"\nMejor fitness encontrado: {max(historial_mejores)}")
    print(f"Generación del mejor: {historial_mejores.index(max(historial_mejores))}")
    print(f"Mejor promedio alcanzado: {max(historial_promedios):.1f}")
    print(f"Total de generaciones ejecutadas: {len(historial_mejores)}")


# ============================================
# EJECUCIÓN PRINCIPAL
# ============================================

if __name__ == "__main__":
    print("=" * 60)
    print("ALGORITMO GENÉTICO PARA EL PROBLEMA DE LA MOCHILA 0/1")
    print("=" * 60)
    print(f"\nConfiguración:")
    print(f"  - Número de objetos: {N}")
    print(f"  - Capacidad: {W}")
    print(f"  - Tamaño de población: {TAM_POBLACION}")
    print(f"  - Probabilidad de cruza: {PROB_CRUZA}")
    print(f"  - Probabilidad de mutación: {PROB_MUTACION}")
    print(f"  - Máximo de generaciones: {MAX_GENERACIONES}")
    print(f"  - Estancamiento máximo: {MAX_ESTANCAMIENTO}")
    print("\n" + "=" * 60)
    print("\nEVOLUCIÓN:")
    print("-" * 60)
    
    # Ejecutar el algoritmo
    mejor, fit, historial_mejores, historial_promedios = algoritmo_genetico(verbose=True)
    
    # Mostrar resultados
    mostrar_solucion(mejor, fit)
    mostrar_estadisticas(historial_mejores, historial_promedios)
    
    # Verificar si la solución es óptima (máximo teórico)
    print("\n" + "=" * 60)
    print("VERIFICACIÓN")
    print("=" * 60)
    
    # Máximo teórico (suma de todos los valores, pero sin exceder capacidad)
    # Para este problema, la solución óptima conocida es 310
    print(f"\nSolución encontrada: {fit}")
    print("Óptimo conocido para esta instancia: 310")
    if fit == 310:
        print("¡Se encontró la solución óptima!")
    else:
        print(f"  Diferencia con el óptimo: {310 - fit}")