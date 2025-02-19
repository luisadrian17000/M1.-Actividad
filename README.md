M1 Actividad
Descripción de la simulación
Esta simulación analiza el desempeño de agentes limpiadores (CleanAgents) en la eliminación de agentes sucios (DirtyAgents) dentro de una cuadrícula de NxM. El objetivo es evaluar la relación entre la cantidad de agentes, el tiempo de simulación y la cantidad de movimientos requeridos para completar la limpieza.
Observaciones 
1. Relación entre Cantidad de Agentes y Tiempo de Simulación (Tmax)
La cantidad de pasos necesarios para limpiar completamente la cuadrícula varía entre 5 y 31 (en el ejemplo de salida).
Cuantas menos iteraciones sean necesarias, más eficiente es el proceso de limpieza.
Un mayor número de agentes limpiadores puede reducir el tiempo total de simulación, pero también puede incrementar el número total de movimientos.
2. Impacto en la Cantidad de Movimientos Realizados
En algunas simulaciones, los agentes necesitaron más de 28 movimientos en promedio para completar la limpieza, mientras que en otras solo 4.39. Esto significa que la cantidad y distribución inicial de DirtyAgents afecta a la eficiencia de limpieza. 
3. Desempeño de los Agentes Limpiadores
La eficiencia varía en función de la cantidad de agentes y su estrategia de movimiento.
Conclusiones
Un mayor número de agentes limpiadores reduce el tiempo total de limpieza, pero su “eficiencia” depende de la distribución inicial de los agentes sucios.







Ejemplo de salida: 
Completed: 10 steps
Run time: 0:00:00.021859
Simulation finished
Simulación 1: {'success': True, 'steps_taken': 10, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 21.0}
Completed: 5 steps
Run time: 0:00:00.034151
Simulation finished
Simulación 2: {'success': True, 'steps_taken': 5, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 10.945945945945946}
Completed: 21 steps
Run time: 0:00:00.045462
Simulation finished
Simulación 3: {'success': True, 'steps_taken': 21, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 6.91764705882353}
Completed: 6 steps
Run time: 0:00:00.052403
Simulation finished
Simulación 4: {'success': True, 'steps_taken': 6, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 7.285714285714286}
Completed: 31 steps
Run time: 0:00:00.010897
Simulation finished
Simulación 5: {'success': True, 'steps_taken': 31, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 28.615384615384617}
Completed: 10 steps
Run time: 0:00:00.035709
Simulation finished
Simulación 6: {'success': True, 'steps_taken': 10, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 4.390243902439025}
Completed: 5 steps
Run time: 0:00:00.052793
Simulation finished
Simulación 7: {'success': True, 'steps_taken': 5, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 11.046511627906977}
Completed: 10 steps
Run time: 0:00:00.035084
Simulation finished
Simulación 8: {'success': True, 'steps_taken': 10, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 10.652173913043478}
Completed: 6 steps
Run time: 0:00:00.041582
Simulation finished
Simulación 9: {'success': True, 'steps_taken': 6, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 19.03448275862069}
Completed: 8 steps
Run time: 0:00:00.026546
Simulation finished
Simulación 10: {'success': True, 'steps_taken': 8, 'cleaned_percentage': 100.0, 'avg_moves_per_cleaned': 10.051282051282051}

Probabilidades de limpieza en cada corrida:
{'A': 0.8, 'B': 0.7, 'C': 0.9, 'D': 1.0}



