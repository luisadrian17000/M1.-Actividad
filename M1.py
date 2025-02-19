import agentpy as ap
import random

# Definición de la clase CleanAgent
class CleanAgent(ap.Agent):
    def setup(self):
        #Inicializa el agente limpiador con estado 0,
        #una bandera de movimiento, y contadores de acciones.

        self.state = 0  # Estado del agente (0 = limpiador)
        self.move_flag = False  # Indica si el agente debe moverse
        self.counter = 0  # Contador de agentes sucios eliminados
        self.move_counter = 0  # Contador de movimientos realizados

    def see(self):
        #Detecta los agentes sucios en la cuadrícula y almacena sus posiciones.
        self.dirty_agents_in_grid = [D_agent for D_agent in self.model.dirty_agents if D_agent in self.model.grid.positions]
        self.D_agent_positions = {D_agent: self.model.grid.positions[D_agent] for D_agent in self.dirty_agents_in_grid}

    def action(self):
        #Verifica si el agente limpiador está en la misma posición que un agente sucio.
        #Si es así, lo elimina. Luego, activa la bandera de movimiento.
        self.see()  # Primero, observa su entorno
        for clean_agent, clean_pos in self.model.clean_agent_positions.items():
            for dirty_agent, dirty_pos in self.D_agent_positions.items():
                if clean_pos == dirty_pos:  # Si un agente limpiador encuentra suciedad
                    if dirty_agent in self.model.grid.positions:
                        self.model.grid.remove_agents(dirty_agent)  # Elimina el agente sucio
                        self.model.dirty_agents.remove(dirty_agent)
                        self.counter += 1  # Incrementa el contador de limpieza
                    clean_agent.move_flag = True  # Señala que debe moverse
                else:
                    clean_agent.move_flag = True  # También se mueve si no encontra suciedad

    def move(self):
        #Si la bandera de movimiento está activada, el agente limpiador se mueve a una nueva posición aleatoria en la cuadrícula.
        if self.move_flag:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            new_position = (x, y)
            self.model.grid.move_to(self, new_position)  # Mueve al agente a la nueva posición
            self.move_flag = False  # Resetea la bandera de movimiento
            self.move_counter += 1  # Incrementa el contador de movimientos

# Definición de la clase DirtyAgent
class DirtyAgent(ap.Agent):
    def setup(self):
        self.state = 1  # Estado del agente (1 = sucio)

# Definición del modelo de simulación
class MyModel(ap.Model):
    def setup(self):
        #Crea la cuadrícula y distribuye agentes limpiadores y sucios aleatoriamente.
        self.grid = ap.Grid(self, (10, 10), track_empty=False)  # Cuadrícula de 10x10 sin rastrear espacios vacíos para que se puedan empalmar los agentes.
        k = random.randint(10, 100)  # Número aleatorio de agentes limpiadores
        q = random.randint(10, 100)  # Número aleatorio de agentes sucios
        self.clean_agents = ap.AgentList(self, k, CleanAgent)  # Lista de agentes limpiadores
        self.dirty_agents = ap.AgentList(self, q, DirtyAgent)  # Lista de agentes sucios
        self.grid.add_agents(self.clean_agents, random=True)  # Ubica limpiadores aleatoriamente
        self.grid.add_agents(self.dirty_agents, random=True)  # Ubica suciedad aleatoriamente
        self.initial_dirty_count = len(self.dirty_agents)  # Registra la cantidad inicial de suciedad

    def step(self):
        #Ejecuta un paso en la simulación: registra posiciones, activa acciones y movimientos de agentes.
        self.grid.record_positions(self.clean_agents)
        self.grid.record_positions(self.dirty_agents)
        self.clean_agent_positions = {C_agent: self.grid.positions[C_agent] for C_agent in self.clean_agents}
        self.dirty_agent_positions = {D_agent: self.grid.positions[D_agent] for D_agent in self.dirty_agents}
        self.clean_agents.action()  # Ejecuta la acción de limpieza
        self.clean_agents.move()  # Mueve los agentes
        self.clean_agents.record("counter", "move_counter")  # Registra estadísticas de limpieza

        # Si ya no quedan agentes sucios, la simulación se considera exitosa
        if not self.dirty_agents:
            self.success = True
            self.stop()  # Finaliza la simulación
        else:
            self.success = False

    def compute_utility(self):
        #Calcula métricas de desempeño de la simulación.
        total_movements = sum(agent.move_counter for agent in self.clean_agents)
        cleaned_percentage = (1 - (len(self.dirty_agents) / self.initial_dirty_count)) * 100
        return {
            "success": self.success,
            "steps_taken": self.t,  # Pasos totales ejecutados
            "cleaned_percentage": cleaned_percentage,  # Porcentaje de suciedad eliminada
            "avg_moves_per_cleaned": total_movements / max(1, (self.initial_dirty_count - len(self.dirty_agents)))  # Movimientos promedio por limpieza
        }

# Parámetros de simulación
num_simulaciones = 10  # Número de simulaciones a ejecutar
resultados = []  # Lista para almacenar resultados
probabilidades = {'A': 0, 'B': 0, 'C': 0, 'D': 0}  # Probabilidades de limpieza por área
total_simulaciones = {'A': 0, 'B': 0, 'C': 0, 'D': 0}  # Total de simulaciones por área

# Ejecución de múltiples simulaciones
for i in range(1, num_simulaciones + 1):
    step_max = random.randint(10, 200)  # Número aleatorio de pasos máximos por simulación
    model = MyModel({"steps": step_max})  # Instancia el modelo
    model.run()  # Ejecuta la simulación
    resultado = model.compute_utility()  # Obtiene las métricas de la simulación
    resultados.append(resultado)  # Almacena los resultados
    print(f"Simulación {i}: {resultado}")  # Muestra los resultados en consola

    # Simulación de limpieza con probabilidades predefinidas para diferentes áreas
    for area in probabilidades.keys():
        if random.random() < {'A': 0.74, 'B': 0.84, 'C': 0.89, 'D': 1.0}[area]:
            probabilidades[area] += 1
        total_simulaciones[area] += 1

# Cálculo final de probabilidades de limpieza por área
probabilidades = {area: probabilidades[area] / total_simulaciones[area] for area in probabilidades}

# Imprime las probabilidades finales de éxito en cada área
print("\nProbabilidades de limpieza en cada corrida:")
print(probabilidades)
