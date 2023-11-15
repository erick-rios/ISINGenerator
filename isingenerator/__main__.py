import argparse
from isingenerator.create_data_simulation import CreateDataSimulation

def main() -> int:
    parser = argparse.ArgumentParser(
        "CreateDataSimulation",
        description = "Create the data simulation for the 2D Ising Model."
    )
    
    parser.add_argument('--file_name'
                        , help = "The name of the archiv CSV.")
    parser.add_argument('--steps', help = "The name of the archiv CSV.")
    parser.add_argument('--initial-step-kT', help = "The name of the archiv CSV.")
    parser.add_argument('--final-step-kT', help = "The name of the archiv CSV.")
    parser.add_argument('--delta-kT', help = "The name of the archiv CSV.")
    parser.add_argument('--dimension', help = "The name of the archiv CSV.")
    parser.add_argument('--percentage-ones', help = "The name of the archiv CSV.")
    
    args = parser.parse_args()
    
    if all(getattr(args, arg) is not None for arg in vars(args)):
        c = CreateDataSimulation(
            file_name = args.file_name,
            steps = args.steps,
            initial_step_kT = args.initial_step_kT,
            final_step_kT = args.final_step_kT,
            delta_kT = args.delta_kT,
            dimension = args.dimension,
            percentage_ones = args.percentage_ones
        )
        print(c.generate_csv_data_zero_magnetic_field())
        
        return 0
    

if __name__ = "__main__":
    exit(main())
    
    