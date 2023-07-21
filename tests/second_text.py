# index.py
import argparse

def main():
    parser = argparse.ArgumentParser(description='My Python script with command-line arguments')
    
    # Define the command-line argument
    parser.add_argument('-param', type=int, help='An integer parameter')
    
    # Parse the command-line arguments
    args = parser.parse_args()

    # Access and use the provided argument
    if args.param:
        print('Parameter value:', args.param)
    else:
        print('No parameter provided.')

if __name__ == "__main__":
    main()
