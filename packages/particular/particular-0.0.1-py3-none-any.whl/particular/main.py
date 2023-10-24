import argparse


parser = argparse.ArgumentParser(description=(
                                            f"Have fun in particular N-Body simulations."
                                            f"Brought to you by sail.black ")
                                            )
parser.add_argument('--exp_name', type=str, default='exp_1', metavar='N', help='experiment_name')
parser.add_argument('--batch_size', type=int, default=100, metavar='N',
                    help='input batch size for training (default: 128)')
parser.add_argument('--epochs', type=int, default=10000, metavar='N',
                    help='number of epochs to train (default: 10)')

args = parser.parse_args()


def main():
    
    # The idea is to implement a better Config adapter and then use the self-made cli to run it

    if args.model == 'gnn':
    



if __name__ == "__main__":
    main()


