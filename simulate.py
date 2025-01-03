import subprocess

def run_simulations_with_restarts(num_simulations, num_requests, protocol_name, output_file):
    """
    Executa múltiplas simulações, reiniciando o kernel após cada uma.

    Args:
        num_simulations (int): Número total de simulações.
        num_requests (int): Número de requisições por simulação.
        protocol_name (str): Nome do protocolo a ser usado.
        output_file (str): Nome do arquivo CSV para salvar os resultados.
    """
    for simulation_id in range(1, num_simulations + 1):
        print(f"Running simulation {simulation_id}/{num_simulations}...")
        subprocess.run([
            "python", "run_simulations.py",  # Nome do script de simulação
            str(protocol_name),             # Protocolo
            str(num_requests),              # Número de requisições
            str(simulation_id),             # ID da simulação
            output_file                     # Arquivo de saída
        ])
        print(f"Simulation {simulation_id} completed.")

# Executar simulações com reinício do kernel
run_simulations_with_restarts(
    num_simulations=100,  # Número de simulações
    num_requests=100,     # Número de requisições por simulação
    protocol_name="Random",  # Protocolo: "BFK_BQC", "AC_BQC", ou "Random"
    output_file="simulation_results.csv"  # Arquivo de saída
)
